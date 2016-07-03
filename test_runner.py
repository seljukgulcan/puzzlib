from libunittest import *
from unittest import *

testList = [TestGrid, TestMazePuzzle]
testLoad = unittest.TestLoader()
 
caseList = []
for testCase in testList:
    testSuite = testLoad.loadTestsFromTestCase(testCase)
    caseList.append(testSuite)
 
def start_test():
	suite = unittest.TestSuite(caseList)

	runner = unittest.TextTestRunner()
	runner.run(suite)

if __name__ == '__main__':
	start_test()