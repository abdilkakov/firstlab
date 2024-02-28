import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern, testData) == expectedResult:
        print(testNumber + " is passed!")
    elif re.search(pattern, testData) != None:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")
        
        
pattern = r"a[b]{2,3}"

test(pattern, "123ab45", "test1", False)
test(pattern, "abbb45as", "test2", True)
test(pattern, "*-]a452", "test3", False)
test(pattern, "123abb&^", "test4", True)
test(pattern, "aboooo452", "test5", False)