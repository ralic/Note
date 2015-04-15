# coding=utf-8
# 6.00.2x Problem Set 4
import math

import numpy
import random
import pylab
from ps3b import ResistantVirus, TreatedPatient

import math
def mean(alist):
    return sum(alist) / float(len(alist))


def stddev(alist):
    n = len(alist)
    list_mean = mean(alist)
    sd = math.sqrt(sum([(num - list_mean) ** 2 for num in alist]) / float(n))
    return sd


# 变异系数= 标准差 /  均值
def cv(alist):
    sd = stddev(alist)
    means = mean(alist)
    return sd / means

#
# PROBLEM 1
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials, start_times):
    average = []
    for trial in range(numTrials):
        virsues = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses)]
        patient = TreatedPatient(virsues, maxPop)
        for first_timestep in range(start_times):
            patient.update()
        patient.addPrescription("guttagonol")
        for second_timestep in range(start_times, start_times+150):
            patient.update()
        average.append(patient.getTotalPop())
    return average

def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    time = [300, 150, 75, 0]
    result = simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                                  mutProb, numTrials, 0)
    f = filter(lambda x: x <= 50, result)
    print f, len(f)
    print result
    print len(f)/float(len(result))

    # for index, t in enumerate(time):
    #     popu = simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
    #                               mutProb, numTrials, t)
    #     pylab.subplot(220+index+1)
    #     pylab.hist(popu, bins=numTrials)
    #     pylab.title("simulation")
    #     pylab.xlabel("Populations")
    #     pylab.ylabel("numTrails")
    #     pylab.legend()
    # pylab.show()

#
# simulationDelayedTreatment(100)
#
# PROBLEM 2

def simulationWithDrug2(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials, start_times):
    average = []
    for trial in range(numTrials):
        virsues = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses)]
        patient = TreatedPatient(virsues, maxPop)
        for first_timestep in range(150):
            patient.update()
        patient.addPrescription("guttagonol")
        for second_timestep in range(start_times):
            patient.update()
        patient.addPrescription("grimpex")
        for third_timestep in range(150):
            patient.update()
        average.append(patient.getTotalPop())
    return average

def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    time = [300, 150, 75, 0]
    result = simulationWithDrug2(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                                  mutProb, numTrials, 300)
    f = filter(lambda x: x <= 50, result)
    print f, len(f)
    print result, len(result)
    print len(f)/float(len(result))
    print cv(result)

# 2.16773301573, 1.13, 0.4

simulationTwoDrugsDelayedTreatment(100)
