Test case directory:

assignment_3_231110007\Chiron-Framework-1.0.4\ChironCore


Commands to follow for different test cases:

First navigate to Submission folder: 

Testcase 1 : ./chiron.py --SBFL ./testFolder/test1/testcase1.tl --buggy ./testFolder/test1/testcase1_buggy.tl -vars '[":x", ":y", ":z"]' --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True

Testcase 2 : ./chiron.py --SBFL ./testFolder/test2/testcase2.tl --buggy ./testFolder/test2/testcase2_buggy.tl -vars '[":x", ":y"]' --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True

Testcase 3 : ./chiron.py --SBFL ./testFolder/test3/testcase3.tl --buggy ./testFolder/test3/testcase3_buggy.tl -vars '[":x"]' --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True
Testcase 4 : ./chiron.py --SBFL ./testFolder/test4/testcase4.tl --buggy ./testFolder/test4/testcase4_buggy.tl -vars '[":x", ":y"]' --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True

Testcase 5 : ./chiron.py --SBFL ./testFolder/test5/testcase5.tl --buggy ./testFolder/test5/testcase5_buggy.tl -vars '[":x", ":y", ":z"]' --timeout 10 --ntests 20 --popsize 100 --cxpb 1.0 --mutpb 1.0 --ngen 100 --verbose True