from itertools import permutations

def ppermutations(s):
    perm = permutations(s)
    for x in perm:
        print(''.join(x))

s=input()
ppermutations(s)
