def solve(numheads, numlegs):
    rabbits=(numlegs-(2*numheads))/2
    chickens=numheads-rabbits
    print(chickens, rabbits)

numheads=35
numlegs=94
solve(numheads, numlegs)