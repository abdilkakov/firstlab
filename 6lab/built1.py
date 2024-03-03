import functools

ourList = map(int, list(input().split()))
print(functools.reduce(lambda x, y: x * y, ourList))