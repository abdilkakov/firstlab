import os

path = os.getcwd()
def checkIt(path):
    if os.access(path, mode=os.EX_OK):
        return os.listdir(path)
    else:
        return False
    
print(checkIt(path))