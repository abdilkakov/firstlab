def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
"""
def spy_game(nums):    
    zero_1, zero_2 ,seven = False, False, False
    for i in nums:
        if i ==0:
            if zero_1:
                zero_2 = True
            else:
                zero_1 = True
        if zero_1 and zero_2 and i == 7:
            seven  = True
        if zero_1 and zero_2 and seven:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))