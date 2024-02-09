class Shape:
    def __init__(self):
        self.area = 0

class Rectangle(Shape):
    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def getParameters(self):
        self.width = int(input("width: "))
        self.length = int(input("lenght: "))

    def printArea(self):
        self.area = self.width * self.length
        return self.area

a = Rectangle(0,0)
a.getParameters()
print("Area is equal:", a.printArea())