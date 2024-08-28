from kast import kachuaAST
import sys
import random
from z3 import *
sys.path.insert(0, "KachuaCore/interfaces/")
from interfaces.fuzzerInterface import *
sys.path.insert(0, '../KachuaCore/')

# Each input is of this type.
#class InputObject():
#    def __init__(self, data):
#        self.id = str(uuid.uuid4())
#        self.data = data
#        # Flag to check if ever picked
#        # for mutation or not.
#        self.pickedOnce = False
        
class CustomCoverageMetric(CoverageMetricBase):
    # Statements covered is used for
    # coverage information.
    def __init__(self):
        super().__init__()

    # TODO : Implement this
    def compareCoverage(self, curr_metric, total_metric):
        # must compare curr_metric and total_metric
        # True if Improved Coverage else False
        curr_metric_set = set(curr_metric)
        total_metric_set = set(total_metric)
        # Check if there is an element in curr_metric_set that is not in total_metric_set
        return any(elem not in total_metric_set for elem in curr_metric_set)

    # TODO : Implement this
    def updateTotalCoverage(self, curr_metric, total_metric):
        # Compute the total_metric coverage and return it (list)
        # this changes if new coverage is seen for a
        # given input.
        curr_metric_set = set(curr_metric)
        total_metric_set = set(total_metric)
        # Find the elements in curr_metric_set that are not in total_metric_set
        missing_elements = curr_metric_set - total_metric_set
        # Add the missing elements to total_metric
        total_metric.extend(missing_elements)
        return total_metric

class CustomMutator(MutatorBase):
    def __init__(self):
        pass

    # TODO : Implement this
    def mutate(self, input_data, coverageInfo, irList):
        # Mutate the input data and return it
        # coverageInfo is of type CoverageMetricBase
        # Don't mutate coverageInfo
        # irList : List of IR Statments (Don't Modify)
        # input_data.data -> type dict() with {key : variable(str), value : int}
        # must return input_data after mutation.

        def count_bits(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count
        
        def reverse_number(number):
            # Handle the sign of the number
            sign = -1 if number < 0 else 1
            number = abs(number)  # Take the absolute value for reversal 
            # Convert the number to a string
            num_str = str(number)
            # Reverse the string
            reversed_str = num_str[::-1]
            # Convert the reversed string back to an integer and apply the sign
            reversed_num = sign * int(reversed_str)
            return reversed_num

        def mutation_1(input_data):
            for i in (input_data.data.keys()):
                random_integer = random.randint(-1000, 1000)
                input_data.data[i] = input_data.data[i]*random_integer

        def mutation_2(input_data):
            random_integer = random.randint(-1000, 1000)
            for i in (input_data.data.keys()):
                input_data.data[i] ^= random_integer;

        def mutation_3(input_data):
            for i in(input_data.data.keys()):
                input_data.data[i] = 0;   

        def mutation_4(input_data):
            for i in(input_data.data.keys()):
                input_data.data[i] = reverse_number(input_data.data[i]);
        
        def mutation_5(input_data):
            for i in(input_data.data.keys()):
                num = random.randint(-1000,1000);
                input_data.data[i] = num;
        
        def mutation_6(input_data):
            for i in(input_data.data.keys()):
                input_data.data[i] = -input_data.data[i];
        
        def mutation_7(input_data):
            cnt = 1
            for i in(input_data.data.keys()):
                num = random.randint(-1000,1000);
                if(cnt==1):
                    input_data.data[i] = input_data.data[i]&num;
                    cnt = 0;
                else:
                    input_data.data[i] = input_data.data[i]|num;
                    cnt = 1;
                

        funcNum = random.randint(1,7);
        if(funcNum==1):
            mutation_1(input_data);
        elif(funcNum==2):
            mutation_2(input_data);
        elif(funcNum==3):
            mutation_3(input_data);
        elif(funcNum==4):
            mutation_4(input_data);
        elif(funcNum==5):
            mutation_5(input_data);
        elif(funcNum==6):
            mutation_6(input_data);
        else:
            mutation_7(input_data);

        return input_data


# Reuse code and imports from
# earlier submissions (if any).
