# coding=utf-8
# 6.00.2x Problem Set 2: Simulating robots

import math
import random
import ps2_visualize
import pylab

# For Python 2.7:
from ps2_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, you are not using 
# Python 2.7 and using most likely Python 2.6:


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1, 定义房间类
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.room = {(w, h): False for w in range(width) for h in range(height)}
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x, y = math.floor(pos.getX()), math.floor(pos.getY())
        self.room[(x, y)] = True


    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.room.get((m, n), False)

    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.height * self.width

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        count = 0
        for clened in self.room.values():
            if clened:
                count += 1
        return count

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x, y = random.randrange(self.width), random.randrange(self.height)
        return Position(x, y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x, y = math.floor(pos.getX()), math.floor(pos.getY())
        if (x, y) in self.room.keys():
            return True
        return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self._room = room
        self._pos = self._room.getRandomPosition()
        self._room.cleanTileAtPosition(self._pos)
        self._speed = speed
        self._direction = random.randrange(1, 360)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self._pos
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self._direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        if self._room.isPositionInRoom(position):
            self._pos = position


    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        if 0 <= direction < 360:
            self._direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        raise NotImplementedError  # don't change this!


# 普通机器人，打扫打扫，碰壁了就改变方向
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        while True:
            new_postion = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self._speed)
            if self._room.isPositionInRoom(new_postion):
                self.setRobotPosition(new_postion)
                self._room.cleanTileAtPosition(new_postion)
                break
            else:
                self.setRobotDirection(random.randrange(1, 360))


#  Uncomment this line to see your implementation of StandardRobot in action!
#  testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def simulation_trial(robots, min_coverage, room):
    # anim = ps2_visualize.RobotVisualization(len(robots), room.width, room.height, 0.01)
    converage = 0
    time_steps = 0
    while converage < min_coverage:
        for robot in robots:
            robot.updatePositionAndClean()
        # anim.update(room, robots)
        num = room.getNumTiles()
        clean_num = room.getNumCleanedTiles()
        converage = clean_num/float(num)
        time_steps += 1
    # anim.done()
    return time_steps

# 模拟n个机器人在n次事件中打扫房间（给定min_coverage，表示清洁率）的平均步长
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    time_steps = 0
    for i in range(num_trials):
        room = RectangularRoom(width, height)
        robots = [robot_type(room, speed) for robot in range(num_robots)]
        time_steps += simulation_trial(robots, min_coverage, room)
    return time_steps / float(num_trials)

# Uncomment this line to see how much your simulation takes on average
# print runSimulation(1, 1.0, 5, 5, 1, 10, StandardRobot)
# print runSimulation(1, 1.0, 20, 20, 1, 30, StandardRobot)
# print runSimulation(3, 1.0, 20, 20, 1, 30, StandardRobot)
# ps2_visualize.RobotVisualization(num_robots, width, height)


# 随机移动机器人，每次移动后，随机改变方向
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        while True:
            new_postion = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self._speed)
            if self._room.isPositionInRoom(new_postion):
                self.setRobotPosition(new_postion)
                self._room.cleanTileAtPosition(new_postion)
                self.setRobotDirection(random.randrange(1, 360))
                break
            else:
                self.setRobotDirection(random.randrange(1, 360))


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 3)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

# showPlot1("Time It Takes 1 - 10 Robots To Clean 80% Of A Room", "Number of Robots", "Time-steps")

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

showPlot2("a", "Aspect Ratio", "Time-steps")

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#


# if __name__ == '__main__':
#     r = RectangularRoom(3, 4)
#     pos = Position(1, 2)
#     robot = Robot(r, 100)
#     print robot.getRobotPosition()
#     sr = StandardRobot(r, 10)
#     # sr.updatePositionAndClean()


