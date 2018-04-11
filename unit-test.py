import unittest

from Zadatak1 import Robot, Grid

class TestRobotMethods(unittest.TestCase):
    
    def test_placing(self):
        robot = Robot()
        #robot.placeRobot(0, 0, 'NORTH')
        self.assertEqual(robot.face,  None)
        robot.placeRobot(2, 3, 'NORTH')
        self.assertEqual(robot.x, 2)
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.face, 'NORTH')

    def test_rotation(self):
        robot.placeRobot(0, 0,'NORTH')
        self.assertEqual(robot.rotate('RIGHT'), 'EAST')

        robot.rotate('LEFT')
        self.assertEqual(robot.rotate('LEFT'), 'WEST')
        self.assertEqual(robot.rotate('RIGHT'), 'NORTH')

    def test_movement(self):
        robot.placeRobot(0, 0, 'NORTH')
        self.assertEqual(robot.move(), (0,1))

        robot.rotate('RIGHT')
        self.assertEqual(robot.move(), (1,1))

    def test_bounds(self):
        #Donji lijevi kut
        robot.placeRobot(0,0, 'SOUTH')
        self.assertEqual(robot.move(), (0,0))

        robot.rotate('RIGHT')
        self.assertEqual(robot.move(), (0,0))

        #Desni gornji kut
        robot.placeRobot(5,5, 'NORTH')
        self.assertEqual(robot.move(), (5,5))

        robot.rotate('RIGHT')
        self.assertEqual(robot.move(), (5,5))

robot = Robot()

if __name__ == '__main__':
    unittest.main()