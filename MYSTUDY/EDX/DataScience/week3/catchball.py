import random


def noReplacementSimulation(numTrials):
    """
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    """
    same = 0
    for i in range(numTrials):
        balls = ["red", "red", "red", "green", "green", "green"]
        first_ball = random.choice(balls)
        balls.remove(first_ball)
        second_ball = random.choice(balls)
        balls.remove(second_ball)
        third_ball = random.choice(balls)
        if first_ball == second_ball == third_ball:
            same += 1
    return same/float(numTrials)

print noReplacementSimulation(1000)
