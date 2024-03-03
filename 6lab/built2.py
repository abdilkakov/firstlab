outString = 'iLiKeAnimE' #Example

Upper = sum(map(lambda x: x.isupper(), outString))
Lower = sum(map(lambda x: x.islower(), outString))

print(f"upper: {Upper}, lower: {Lower}")