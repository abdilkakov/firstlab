class twoMethods:
    def __init__(self):
        self.string=""
    def getString(self):
        self.string=input()
    def printString(self):
        print(self.string.upper())

x = twoMethods()
x.getString()
x.printString()