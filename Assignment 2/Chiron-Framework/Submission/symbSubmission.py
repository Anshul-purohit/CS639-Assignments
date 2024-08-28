from z3 import *
import argparse
import json
import sys

sys.path.insert(0, '../KachuaCore/')

from sExecutionInterface import *
import z3solver as zs
from irgen import *
from interpreter import *
import ast

def example(s):
    # To add symbolic variable x to solver
    s.addSymbVar('x')
    s.addSymbVar('y')
    # To add constraint in form of string
    s.addConstraint('x==5+y')
    s.addConstraint('And(x==y,x>5)')
    # s.addConstraint('Implies(x==4,y==x+8')
    # To access solvers directly use s.s.<function of z3>()
    print("constraints added till now",s.s.assertions())
    # To assign z=x+y
    s.addAssignment('z','x+y')
    # To get any variable assigned
    print("variable assignment of z =",s.getVar('z'))

def checkEq(args,ir):

    solver = zs.z3Solver()

    unknown = open("../Submission/testData1_1.json", "r+")
    testData_2 = json.loads(unknown.read())
    unknown.close()
    
    known = open("../Submission/testData1_2.json", "r+")
    testData_1 = json.loads(known.read())
    known.close()
    
    for data_1 in testData_1.keys():
        for data_2 in testData_2.keys():
            if testData_1[data_1]['params'] == testData_2[data_2]['params']:
                params = testData_1[data_1]['params'].replace("'", "\"")
                
                symbEnc_1 = testData_1[data_1]['symbEnc'].replace("'", "\"")
                symbEnc_2 = testData_2[data_2]['symbEnc'].replace("'", "\"")
                
                expression_1 = eval(symbEnc_1)
                expression_2 = eval(symbEnc_2)
                parameter_1 = eval(params)

                for data in parameter_1.keys():
                    solver.addSymbVar('{}'.format(data))

                for data in parameter_1.keys():
                    solver.addConstraint("{} == {}".format(expression_1[data], expression_2[data]))

    answer = solver.s.check()
    
    if str(answer)=="sat":
        print("Programs are symbolically equivalent, and the constraints are :",solver.s.model())
    else:
        print("Programs are not symbolically equivalent")


    

    # file1.close()
    # s = zs.z3Solver()
    # testData = convertTestData(testData)
    # print(testData)
    # output = args.output
    # example(s)
    # TODO: write code to check equivalence

if __name__ == '__main__':
    cmdparser = argparse.ArgumentParser(
        description='symbSubmission for assignment Program Synthesis using Symbolic Execution')
    cmdparser.add_argument('progfl')
    cmdparser.add_argument(
        '-b', '--bin', action='store_true', help='load binary IR')
    cmdparser.add_argument(
        '-e', '--output', default=list(), type=ast.literal_eval,
                               help="pass variables to kachua program in python dictionary format")
    args = cmdparser.parse_args()
    ir = loadIR(args.progfl)
    checkEq(args,ir)
    exit()
