import time, math

def root(num, delay):
    time.sleep(delay / 1000)
    return math.sqrt(num)

mainRoot = float(input())
msec = float(input())

print(f"Square root of {mainRoot} after {msec} miliseconds is {root(mainRoot, msec)}")