import re

def test(pattern, testData, testNumber, expectedResult):
    x = re.findall(pattern, testData)
    result = '_'.join(x).lower()
    print(result)

    if result == expectedResult:
        print(testNumber + " is passed!")
    else:
        print(testNumber + " is not passed!")


pattern = r"[A-Z][a-z]*"

test(pattern, "CamelCase", "test1", "camel_case")
test(pattern, "Study00SmartNot  Hard", "test2", "study_smart_not_hard")
test(pattern, "_    Blue__Lock", "test3", "blue_lock")
