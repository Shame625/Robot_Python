commands = "PLACE, MOVE, LEFT, RIGHT, REPORT"
faces = {'NORTH' : 0, 'EAST' : 1, 'SOUTH' : 2, 'WEST' : 3 }

class Grid:
    x = 5
    y = 5


class Robot:
    def __init__(self):
        self.face = None
        self.x = None
        self.y = None

    def placeRobot(self, x, y, face):
        if isFaceLegit(face) and isMoveLegit(x,y):
            self.x = x
            self.y = y
            self.face = face

    def move(self):
        if(self.face == None):
            return
        
        x,y = getDir(self.face)
        if(isMoveLegit(self.x + x, self.y + y)):
            self.x += x
            self.y += y
        return (self.x, self.y)

    def rotate(self, side):
        if(self.face != None):
            self.face = getNewRotation(side, self.face)
        return self.face

    def report(self):
        print('Output:{0},{1},{2}'.format(self.x, self.y, self.face))


            
def isFaceLegit(face):
    return face in faces

def isMoveLegit(x, y):
    if (x < 0 or x > Grid.x) or (y < 0 or y > Grid.y):
        return False
    return True

def getDir(face):
    if isFaceLegit(face):
        if face == 'NORTH':
            return (0, 1)
        elif face == 'SOUTH':
            return (0, -1)
        elif face == 'WEST':
            return (-1, 0)
        elif face == 'EAST':
            return (1, 0)
    return (0, 0)

def getNewRotation(side, currentFace):
    if side == 'LEFT':
        x = faces[currentFace] - 1
        if(x < 0):
            x = 3
        return (list(faces.keys())[list(faces.values()).index(x)])

    elif side == 'RIGHT':
        x = faces[currentFace] + 1
        if x > 3:
            x = 0
        return (list(faces.keys())[list(faces.values()).index(x)])


def commandParser(x, robot):
    temp = x.split(' ')

    for x in range (len(temp)):
        if temp[x] in commands:
            if temp[x] == 'PLACE':
                if (x + 1) < len(temp):
                    args = temp[x + 1].split(',')
                    robot.placeRobot(int(args[0]), int(args[1]), args[2])
                    x+=1

            elif temp[x] == 'MOVE':
                robot.move()

            elif temp[x] == 'LEFT':
                robot.rotate('LEFT')

            elif temp[x] == 'RIGHT':
                robot.rotate('RIGHT')

            elif temp[x] == 'REPORT':
                robot.report()
                

robot = Robot() 

while True:
    x = input("Input:")
    commandParser(x, robot)