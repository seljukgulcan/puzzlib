import libunittest
import unittest

testList = [libunittest.TestGrid]
testLoad = unittest.TestLoader()
 
caseList = []
for testCase in testList:
    testSuite = testLoad.loadTestsFromTestCase(testCase)
    caseList.append(testSuite)
 
suite = unittest.TestSuite(caseList)

runner = unittest.TextTestRunner()
runner.run(suite)