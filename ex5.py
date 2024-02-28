import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern, testData) == expectedResult:
        print(testNumber + " is passed!")
    elif re.search(pattern, testData) != None:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")
        
        
pattern = r"a.*b$"

test(pattern, "12a%^&*  b", "test1", True)
test(pattern, "@@@a_  _+bm", "test2", False)
test(pattern, "``;::a}{89ahjhjhjb", "test3", True)
test(pattern, "qAzzzzz  b", "test4", False)
test(pattern, "Sak89    ./|pob", "test5", True)     
