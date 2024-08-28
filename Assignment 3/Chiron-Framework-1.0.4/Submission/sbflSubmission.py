#!/usr/bin/env python3

import argparse
import sys
import numpy as np
import math


sys.path.insert(0, "../ChironCore/")
from irhandler import *
from ChironAST.builder import astGenPass
import csv
from collections import Counter


def fitnessScore(IndividualObject):
    """
    Parameters
    ----------
    IndividualObject : Individual (definition of this class is in ChironCore/sbfl.py)
        This is a object of class Individual. The Object has 3 elements
        1. IndividualObject.individual : activity matrix.
                                    type : list, row implies a test
                                    and element of rows are components.
        2. IndividualObject.fitness : fitness of activity matix.
                                    type : float
        3. Indivisual.fitness_valid : a flag used by Genetic Algorithm.
                                    type : boolean
    Returns
    -------
    fitness_score : flaot
        returns the fitness-score of the activity matrix.
        Note : No need to set/change fitness and fitness_valid attributes.
    """
    # Design the fitness function
    fitness_score = 0
    activity_mat = np.array(IndividualObject.individual, dtype="int")
    activity_mat = activity_mat[:, : activity_mat.shape[1] - 1]
    # Use 'activity_mat' to compute fitness of it.
    # ToDo : Write your code here to compute fitness of test-suite

    total_sum = np.sum(activity_mat)
    num_values = activity_mat.size

    # print(activity_mat)

    # print(fitness_score)
    # print(num_values)

    density = total_sum/num_values

    # print(density)

    # Get the total number of columns
    total_columns = activity_mat.shape[1]

    # Get the number of unique columns
    unique_columns = np.unique(activity_mat, axis=1).shape[1]

    # Calculate the ratio of unique columns to total columns
    uniqueness = unique_columns / total_columns

    # print(total_columns)
    # print(unique_columns)
    # print(uniqueness)

    # Count the occurrences of each row in the activity matrix
    activity_counts = Counter(tuple(row) for row in activity_mat)

    # Calculate the sum of (count * (count - 1)) for each unique activity
    similarity_sum = sum(count * (count - 1) for count in activity_counts.values())

    diversity = 1  # Your existing diversity calculation




    # Calculate the similarity index formula
    if len(activity_mat) != 1:
        diversity = 1 - similarity_sum / (len(activity_mat) * (len(activity_mat) - 1))

    density_change = 1 - abs(1-2*density)

    fitness_score = -1*(density_change*uniqueness*diversity)
    # print("fitness score  ----------   ",fitness_score)
    
    # print("-----")

    return fitness_score


# This class takes a spectrum and generates ranks of each components.
# finish implementation of this class.
class SpectrumBugs:
    def __init__(self, spectrum):
        self.spectrum = np.array(spectrum, dtype="int")
        self.comps = self.spectrum.shape[1] - 1
        self.tests = self.spectrum.shape[0]
        self.activity_mat = self.spectrum[:, : self.comps]
        self.errorVec = self.spectrum[:, -1]

    def getActivity(self, comp_index):
        """
        get activity of component 'comp_index'
        Parameters
        ----------
        comp_index : int
        """

        return self.activity_mat[:, comp_index]

    def suspiciousness(self, comp_index):
        """
        Parameters
        ----------
        comp_index : int
            component number/index of which you want to compute how suspicious
            the component is. assumption: if a program has 3 components then
            they are denoted as c0,c1,c2 i.e 0,1,2
        Returns
        -------
        sus_score : float
            suspiciousness value/score of component 'comp_index'
        """
        sus_score = 0
        # ToDo : implement the suspiciousness score function.

        # column_data = [row[comp_index] for row in self.activity_mat]

        column_data = []

        # Iterate through rows to extract the data for a specific component index
        for row in self.activity_mat:
            component_value = row[comp_index]
            column_data.append(component_value)
            
        # print(column_data)

        c_f = 0
        c_p = 0
        n_f = 0
        n_p = 0

        for i in range(0,len(self.errorVec)):
            if(self.errorVec[i]==0 and column_data[i]==0):
                n_p = n_p + 1
            if(self.errorVec[i]==0 and column_data[i]==1):
                c_p = c_p + 1
            if(self.errorVec[i]==1 and column_data[i]==0):
                n_f = n_f + 1
            if(self.errorVec[i]==1 and column_data[i]==1):
                c_f = c_f + 1

        divisor = math.sqrt((c_f + n_f) * (c_f + c_p))
        if divisor:
            sus_score = c_f / divisor
        else:
            sus_score = 0    

        return sus_score

    def getRankList(self):
        """
        find ranks of each components according to their suspeciousness score.

        Returns
        -------
        rankList : list
            ranList will contain data in this format:
                suppose c1,c2,c3,c4 are components and their ranks are
                1,2,3,4 then rankList will be :
                    [[c1,1],
                     [c2,2],
                     [c3,3],
                     [c4,4]]
        """
        rankList = []
        # ToDo : implement rankList

        ranklist2 = []

        for i in range(len(self.activity_mat[0])):
            component_name = 'c' + str(i + 1)
            component_suspiciousness = self.suspiciousness(i)
            entry = [component_name, component_suspiciousness]
            ranklist2.append(entry)
        
        rankList = sorted(ranklist2,key=lambda x:x[1],reverse=True)
        print("Rank List : ",rankList)

        # rank = 1

        # for i in range(0,len(rankList)):
        #     if (i > 0 and rankList[i][1] != rankList[i - 1][1]):
        #         rank = rank + 1
        #     rankList[i][1] = rank


        customRankList = rankList
        my_custom_rank = 1
        highest_rank = customRankList[0][1]

        for idx in range(0, len(customRankList)):
            if highest_rank != customRankList[idx][1]:
                my_custom_rank += 1
                highest_rank = customRankList[idx][1]
            customRankList[idx][1] = my_custom_rank

        
        # print(self.activity_mat)
        # print("Rank List: ", rankList)

        return rankList


# do not modify this function.
def computeRanks(spectrum, outfilename):
    """
    Parameters
    ----------
    spectrum : list
        spectrum
    outfilename : str
        components and their ranks.
    """
    S = SpectrumBugs(spectrum)
    rankList = S.getRankList()
    with open(outfilename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(rankList)
