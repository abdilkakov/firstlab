from math import *


class Point:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def getData(self):
        self.x1 = int(input("x1: "))
        self.y1 = int(input("y1: "))
        self.x2 = int(input("x2: "))
        self.y2 = int(input("y2: "))

    def showCoordinates(self):
        return self.x1, self.y1, self.x2, self.y2

    def changeCoordinates(self):
        self.x1 = int(input("x1: "))
        self.y1 = int(input("y1: "))
        self.x2 = int(input("x2: "))
        self.y2 = int(input("y2: "))

    def distCoordinates(self):
        return sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)


a = Point()
a.getData()
print("Coordinata: {}".format(a.showCoordinates()))
a.changeCoordinates()
print("New coordinata {}".format(a.showCoordinates()))
print("Distation: {}".format(a.distCoordinates()))