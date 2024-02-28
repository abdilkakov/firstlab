import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern, testData) == expectedResult:
        print(testNumber + " is passed!")
    elif re.search(pattern, testData) != None:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")
        
        
pattern = r"[A-Z][a-z]+"

test(pattern, "Beee", "test1", True)
test(pattern, "ddZZZZiii", "test2", True)
test(pattern, "VILLAIN", "test3", False)
test(pattern, "45FF_aaaa", "test4", False)
test(pattern, "&(*God)", "test5", True)      