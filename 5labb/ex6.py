import re

def test(pattern, sub, testData, testNumber, expectedResult):
    result = re.sub(pattern, sub, testData)
    print(result)
    
    if result == expectedResult:
        print(testNumber + " is passed!")
    else:
        print(testNumber + " is not passed!")
        
pattern = r"[\s,\.]"
sub = r":"

test(pattern, sub, "He love bacon, cakes, animals, and math.", "test1", "He:love:bacon::cakes::animals::and:math:")
test(pattern, sub, " monkey,turtle,coala", "test2", ":monkey:turtle:coala")
test(pattern, sub, "+8777.561.8989 ", "test3", "+8777:561:8989:")

