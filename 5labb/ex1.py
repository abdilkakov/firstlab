import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern, testData) == expectedResult:
        print(testNumber + " is passed!")
    elif re.search(pattern, testData) != None:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")
        
        
pattern = r"ab*"

test(pattern, "123ab45", "test1", True)
test(pattern, "123abbb45as", "test2", True)
test(pattern, "123452", "test3", False)
test(pattern, "%&^%&^", "test4", False)
test(pattern, "a452", "test5", True)    
    