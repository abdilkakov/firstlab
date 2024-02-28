import re

def test(pattern, testData, testNumber, expectedResult):
    listOfObj = re.split(pattern, testData)

    result = ""
    for x in listOfObj:
        result += x.capitalize()
    print(result)
    
    if result == expectedResult:
        print(testNumber + " is passed!")
    else:
        print(testNumber + " is not passed!")


pattern = r"[_]+"

test(pattern, "this_is_snake_case", "test1", "ThisIsSnakeCase")
test(pattern, "he110____wor1d", "test2", "He110Wor1d")
test(pattern, "_let_him8_cook%_", "test3", "LetHim8Cook%")


# this_is_snake_case
# ThisIsCamelCase
