import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern, testData) == expectedResult:
        print(testNumber + " is passed!")
    elif re.search(pattern, testData) != None:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")
        
        
pattern = r"[a-z]+[_][a-z]+"

test(pattern, "stat-123", "test1", False)
test(pattern, "__learn_python", "test2", True)
test(pattern, "hello _world", "test3", False)
test(pattern, "average_score", "test4", True)
test(pattern, "adventure__time", "test5", False)      

