import math


class Rover(object):
    def __init__(self, x, y, grid_x, grid_y, direction):
        self.x = x
        self.y = y
        self.grid_x = grid_x
        self.grid_y = grid_y
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
        if self.x >= self.grid_x:
            self.x = self.grid_x
        if self.y >= self.grid_y:
            self.y = self.grid_y
        if self.x <= 0:
            self.x = 0
        if self.y <= 0:
            self.y = 0
        self.updateAngleFromDirection()
        return self

    def updateAngleFromDirection(self):
        self.ang = self.rad[self.direction]
        return self

    def updateDirectionFromAngle(self):
        self.direction = self.card[(self.ang) % (2*math.pi)]
        return self

    def chainCmds(self, cmds):
        for char in cmds:
            self.updatePos(char)
        return (self.x, self.y, self.direction)


# initial position is 0,0 on grid size 5 by 5, rover is facing north
print(Rover(0, 0, 5, 5, "N").chainCmds("MML"))
