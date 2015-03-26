# coding=utf-8
# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics
from ps3b_precompiled_27 import *
import random
import pylab


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. 当病毒没有复制的时候触发该异常
    """


class SimpleVirus(object):

    """
    普通病毒
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: 最高复制几率 (a float between 0-1)
        clearProb: 最高清除几率（即病毒销毁） (a float between 0-1).
        """
        self._maxBirthProb = maxBirthProb
        self._clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self._maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self._clearProb

    def doesClear(self):
        """
        判断是否清除该病毒
        Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        clear_prob = random.random()
        # 最大清除概率小于当前生成的概率，则不清除
        if clear_prob >= self.getClearProb():
            return False
        return True

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. 病毒复制几率计算公式：
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        reproduce_prob = random.random()
        # 所计算的复制几率小于当前概率，则不进行复制
        if reproduce_prob >= self.getMaxBirthProb() * (1 - popDensity):
            raise NoChildException
        else:
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())


class Patient(object):
    """
    表示普通病人，病人没有服药，且其体内病毒种群没有抗药性
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: 携带的病毒列表

        maxPop: 携带病毒最大数
        """

        self.viruses = viruses
        self._maxpop = maxPop


    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self._maxpop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.getViruses())


    def update(self):
        """
        每一个时间步进行一次update，更新病人携带病毒种群的状态
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - 确定病毒的生存状态，更新当前携带病毒的种群
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - 计算当前病毒种群密度
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - 根据种群密度进行复制
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    
        - 返回update之后的病人携带病毒的总数
        returns: The total virus population at the end of the update (an
        integer)
        """

        alive_virus = []
        repro_virus = []
        for virus in self.getViruses():
            if virus.doesClear():
                continue
            alive_virus.append(virus)
        popDensity = len(alive_virus) / float(self.getMaxPop())
        for virus in alive_virus:
            repro_virus.append(virus)
            if len(repro_virus) >= self.getMaxPop():
                break
            try:
                repro_virus.append(virus.reproduce(popDensity))
            except NoChildException:
                pass
        self.viruses = repro_virus
        return len(repro_virus)


def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """

    for trial in range(numTrials):
        timestep = []
        average_virus_size = []
        viruses = [SimpleVirus(maxBirthProb, clearProb) for i in range(numViruses)]
        patient = Patient(viruses, maxPop)
        for chance in range(300):
            timestep.append(chance)
            average_virus_size.append(float(patient.update()))
    pylab.plot(timestep, average_virus_size)
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend()
    pylab.show()



class ResistantVirus(SimpleVirus):
    """
    具有抗药性的病毒
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
            Initialize a ResistantVirus instance, saves all parameters as attributes
            of the instance.

            maxBirthProb: Maximum reproduction probability (a float between 0-1)

            clearProb: Maximum clearance probability (a float between 0-1).

            resistances: 病毒的抗药性字典.
            --A dictionary of drug names (strings) mapping to the state
            of this virus particle's resistance (either True or False) to each drug.
            e.g. {'guttagonol':False, 'srinol':False}, means that this virus
            particle is resistant to neither guttagonol nor srinol.

            mutProb: 病毒后代失去或获得抗药性的概率
            Mutation probability for this virus particle (a float). This is
            the probability of the offspring acquiring or losing resistance to a drug.
            """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self._resistance = resistances
        self._mutporb = mutProb




    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self._resistance

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self._mutporb

    def isResistantTo(self, drug):
        """
        获得病毒对某种药物是否具有抗药性
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        resist = self.getResistances().get(drug, False)
        return resist




    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        当且仅当病毒对所给定的药物都具有抗药性才进行复制

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.
        -- 复制阶段，遍历病毒的抗药性列表，对于True的药物，其复制给子类的概率为：1-mutprob
        对于False的药物，其复制给子类的概率：mutprob
        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        active = True
        for drug in activeDrugs:
            if self.isResistantTo(drug):
                continue
            else:
                active = False
                break
        if not active:
            raise NoChildException

        reproduce_prob = random.random()
        if reproduce_prob >= self.getMaxBirthProb() * (1 - popDensity):
            raise NoChildException
        else:
            new_resist = {}
            for drugname, resist in self.getResistances().items():
                chance = random.random()
                if resist:
                    new_resist[drugname] = True if chance < 1 - self.getMutProb() else False
                else:
                    new_resist[drugname] = True if chance < self.getMutProb() else False
            return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(), new_resist, self.getMutProb())



class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        Patient.__init__(self, viruses, maxPop)
        self._drugs = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self._drugs:
            self._drugs.append(newDrug)




    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self._drugs



    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resist_viruses = []
        for virus in self.getViruses():
            canresist = True
            for resist_drug in drugResist:
                if virus.isResistantTo(resist_drug):
                    continue
                else:
                    canresist = False
                    break
            if canresist:
                resist_viruses.append(virus)
        return len(resist_viruses)





    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        alive_virus = []
        repro_virus = []
        drugs = self.getPrescriptions()
        for virus in self.getViruses():
            if virus.doesClear():
                continue
            alive_virus.append(virus)
        popDensity = len(alive_virus) / float(self.getMaxPop())
        for virus in alive_virus:
            repro_virus.append(virus)
            if len(repro_virus) >= self.getMaxPop():
                break
            for drug in drugs:
                if not virus.isResistantTo(drug):
                    break
            try:
                repro_virus.append(virus.reproduce(popDensity, drugs))
            except NoChildException:
                pass
        self.viruses = repro_virus
        return len(repro_virus)



if __name__ == '__main__':
    virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
    virus2 = ResistantVirus(1.0, 0.0, {"drug1": False}, 0.0)
    patient = TreatedPatient([virus1, virus2], 1000000)
    patient.addPrescription("drug1")



#
# PROBLEM 5
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

    # TODO


