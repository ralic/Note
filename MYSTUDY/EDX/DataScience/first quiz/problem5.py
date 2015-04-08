# coding=utf-8
import random
import pylab

def samplequiz():
    """
    使用蒙特卡罗方法模拟出学生最终成绩在70-75之间的概率。两次期中考试的成绩分别站25%的权重，期末考试占50%的权重
    考试分数（皆为整数）服从均匀分布
    """
    trail = 0
    for num in range(10000):
        first_midterm = random.randint(50, 80)
        second_midterm = random.randint(60, 90)
        final_exam = random.randint(55, 95)
        score = first_midterm * 0.25 + second_midterm * 0.25 + final_exam * 0.5
        if 70 <= score <= 75:
            trail += 1
    return trail / float(10000)


def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of
    the three exams, then calculates the final score and
    appends it to a list of scores.

    Returns: A list of numTrials scores.
    """
    scroes = []
    for num in range(numTrials):
        first_midterm = random.randint(50, 80)
        second_midterm = random.randint(60, 90)
        final_exam = random.randint(55, 95)
        score = first_midterm * 0.25 + second_midterm * 0.25 + final_exam * 0.5
        scroes.append(score)
    return scroes


# 绘制10000次模拟成绩分布的直方图
def plotQuizzes():
    scorelist = generateScores(9575)
    pylab.hist(scorelist, bins=7)
    pylab.xlabel("Final Score")
    pylab.ylabel("Number of Trials")
    pylab.title("Distribution of Scores")
    pylab.show()


if __name__ == '__main__':
    plotQuizzes()