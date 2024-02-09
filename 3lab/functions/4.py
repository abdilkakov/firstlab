import math
def razdelitelstrok(stroka):
    res = []
    t = ""
    for i in stroka:
        t+=i
        if i==" ":
            res.append(int(t))
            t = ""
    res.append(int(t))
    return res

def is_prime(s):
    if s==2:
        return True
    if s==1:
        return False
    if s%2==0:
        return False
    n =int(math.sqrt(s))
    for i in range(3,n+1):
        if s%i==0:
            return False
    return True
def filter_prime(str_nums):
    nums =razdelitelstrok(str_nums)
    res = []
    for i in nums:
        if is_prime(i):
            res.append(i)
    return res

s=input()
print(filter_prime(s))