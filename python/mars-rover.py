
import math


class Rover(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.ang = 0
        self.direction = direction
        self.rad = {"E": 0, "N": math.pi/2, "W": math.pi, "S": 3*math.pi/2}
        self.card = {0: "E", math.pi/2: "N", math.pi: "W", 3*math.pi/2: "S"}
        self.updateAngleFromDirection()
        return

    def updatePos(self, cmd):
        if cmd == "L":
            self.ang += math.pi/2
            self.updateDirectionFromAngle()
        if cmd == "R":
            self.ang -= math.pi/2
            self.updateDirectionFromAngle()
        if cmd == "M":
            self.x = round(self.x + math.cos(self.ang))
            self.y = round(self.y + math.sin(self.ang))
        self.updateAngleFromDirection()
        return self

    def updateAngleFromDirection(self):
        self.ang = self.rad[self.direction]
        return self

    def updateDirectionFromAngle(self):
        self.direction = self.card[(self.ang) % (2*math.pi)]
        return self

    def printState(self):
        print(self.x)
        print(self.y)
        print(math.degrees(self.ang))
        print(self.direction)


Rv = Rover(0, 0, "S")
Rv.printState()
Rv.updatePos("L")
Rv.updatePos("M")
Rv.printState()
