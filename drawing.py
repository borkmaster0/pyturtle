from turtle import *

def line(x: float, y: float, x1: float, y1: float):
    return [[x, y], [x1, y1]]

def point(x: float, y: float):
    return [x, y]

def moveUp(self, steps: float):
    self.setheading(90)
    self.forward(steps)
    
def moveDown(self, steps: float):
    self.setheading(270)
    self.forward(steps)

def moveLeft(self, steps: float):
    self.setheading(180)
    self.forward(steps)

def moveRight(self, steps: float):
    self.setheading(0)
    self.forward(steps)

def drawPolygon(self, obj: list, dotSize: int):
    self.penup()
    self.goto(obj[0])
    for item in obj:
        self.pendown()
        self.goto(item)
        self.dot(dotSize)
    self.pendown()
    self.goto(obj[0])
    self.dot(dotSize)

def objectAssemble(type: str, pointList: list, drawList: list=[]):
    a = []
    if type == '2D':
        for item in pointList:
            a.append(item)
        return a
    else:
        if len(pointList) != len(drawList):
            TypeError('Unequal length')
        
        if type == '3D':
            for i in range(0, len(pointList)):
                a.append(pointList[i].append(list(drawList[i])))
            return a
        ValueError('Unknown type')

def 