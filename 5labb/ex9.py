import re

def test(pattern, sub, testData, testNumber, expectedResult):
    result = re.sub(pattern, sub, testData)
    print(result)

    if result == expectedResult:
        print(testNumber + " is passed!")
    else:
        print(testNumber + " is not passed!")


pattern = r"(\w)([A-Z])"
sub = r"\1 \2"

test(pattern, sub, "LongStringWithBlahBlah", "test1", "Long String With Blah Blah")
test(pattern, sub, " MySuperTest IAmRobot", "test2", " My Super Test I Am Robot")
test(pattern, sub, "WatchLecture FromTeams ", "test3", "Watch Lecture From Teams ")



