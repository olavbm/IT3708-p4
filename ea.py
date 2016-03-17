import random

class Candidate(object):
    def __init__(self, gType):
        '''
        Create a new Candidate with 'gType'(possibly a matrix of floats).
        If there is a float in two indices, there is a connection between the nodes.
        '''
        self.gType = gType
        self.weights = [[]]

    '''
    Fitness evaluation function.  
    Somehow needs to pass board to the ann for action-response.
    '''
    def calculatefitness(self):
        pass

    def mutate(self, probability):
        pass

    def crossover(self, other):
        pass

class Population(object):
    def __init__(self, candidate, size, maxGenerations):
        self.candidate = candidate
        self.size = size
        self.maxGenerations = maxGenerations
        self.population = self.initializePopulation(self.size)

    '''
    This needs some fixing. How do we initialize the ann, and with what
    kind of matrix? Should it just take care of that itself? But what with
    the gType then?
    '''
    def initializeCandidate(self):
        gType = "hei"
        return self.candidate(gType)

    '''
    Initializes the population.
    Uses the candidate provided when initializing the population.
    '''
    def initializePopulation(self, size):
        population = []
        for i in range(size):
            population.append(self.initializeCandidate())

        return population

    '''
    Main evolution loop.
    Decision on what parent-selection-function to be used needs to be done.
    '''
    def evolve():
        for i in range(self.maxGenerations):
            generation = generateGeneration()

    '''
    Sum all fitnesses up to a number, a.
    For each candidate, sum the fitnesses.
        Pick a number between 0 and a.
        If sumFitness > a, you have your candidate.
    '''
    def fitnessProportionateSelection(self):
        fitnessSum = 0
        for candidate in self.population:
            fitnessSum += candidates.fitness

        population =  []
        for i in range(self.size):
            currentCounter = 0
            candidateRandomNumber = random.random() * fitnessSum

            for candidate in self.population:
                if currentCounter >=  candidateRandomNumber:
                    population.append(candidate)
                    break
                else:
                    currentCounter += candidate.fitness

        return population

    def generateGeneration(self):
        generation = []
        for i in range(self.size):
            generation.append(self.reproduction())

        return generation

    def reproduction(self):
        rand1 = int(random.random() * self.size -1)
        rand2 = int(random.random() * self.size -1)
        parent1 = self.population[rand1]
        parent2 = self.population[rand2]
        child = parent1.crossover(parent2)
        child.mutate()

        return child

def run():
    # It is possible to have many different candidates here.
    def exempleCandidate(Candidate):
        # A specialized mutate-function for this exact problem and candidate.
        def mutate(probability):
            pass

    size = 100
    maxGenerations = 100
    population = Population(exempleCandidate, size, maxGenerations)
    result = population.evolve()
