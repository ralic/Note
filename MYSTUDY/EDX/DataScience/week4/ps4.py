# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """
    virsues_total_population = [0 for i in range(300)]
    virsues_resist_population = [0 for i in range(300)]
    timestep = range(1, 301)
    patient_resist = ["guttagonol"]
    for trial in range(numTrials):
        virsues = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses)]
        patient = TreatedPatient(virsues, maxPop)
        for first_timestep in range(150):
            virsues_total_population[first_timestep] += patient.update()
            virsues_resist_population[first_timestep] += patient.getResistPop(patient_resist)
        patient.addPrescription("guttagonol")
        for second_timestep in range(150, 300):
            virsues_total_population[second_timestep] += patient.update()
            virsues_resist_population[second_timestep] += patient.getResistPop(patient.getPrescriptions())
    virsues_total_population = map(lambda x: x / float(numTrials), virsues_total_population)
    virsues_resist_population = map(lambda x: x / float(numTrials), virsues_resist_population)
    pylab.plot(virsues_total_population, timestep)
    pylab.plot(virsues_resist_population, timestep)
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("time step")
    pylab.ylabel("# viruses")
    pylab.legend()
    pylab.show()

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
    for index, one_time in enumerate(time):
        virsues_total_population = [0 for i in range(one_time + 150)]
        timestep = range(1, one_time + 150 + 1)
        patient_resist = ["guttagonol"]
        for trial in range(numTrials):
            virsues = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses)]
            patient = TreatedPatient(virsues, maxPop)
            for first_timestep in range(one_time):
                virsues_total_population[first_timestep] += patient.update()
            patient.addPrescription("guttagonol")
            for second_timestep in range(one_time, one_time + 150):
                virsues_total_population[second_timestep] += patient.update()
            virsues_total_population = map(lambda x: x / float(numTrials), virsues_total_population)
        pylab.title("ResistantVirus simulation")
        pylab.xlabel("total virus")
        pylab.ylabel("trials ->" + str(one_time))
        pylab.ylim(1, 450)
        pylab.hist(virsues_total_population)
    pylab.show()
simulationDelayedTreatment(10)

#
# PROBLEM 2
#
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
    # TODO
