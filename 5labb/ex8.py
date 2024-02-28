import re

def test(pattern, testData):
    obj = re.split(pattern, testData)
    result = ""
    for x in obj:
        if x != "":
            result += x
    
    print(result)
    
pattern = "[A-Z]"

test(pattern, "JsaySgoodSbye")
test(pattern, "HAHAHAlowwwwJKJK")
test(pattern, "12OPPO111")
