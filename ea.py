
class Candidate(object):
    def __init__(self, gType):
        '''
        Create a new Candidate with 'gType'(possibly a matrix of floats).
        If there is a float in two indices, there is a connection between the nodes.
        '''
        self.gType = gType
        self.weights = [[]]

    # Fitness evaluation function.
    # Somehow needs to pass board to the ann it represents.
    def calculateFitness(self):
        pass

    def mutate(self, probability):
        pass

    def crossover(self, other):
        pass

class Population(object):
    def __init__(self):
        pass

    def generateCandidate():
        pass

    def generatePopulation(self, size):
        pass

    # Main evolution loop.
    def evolve():
        pass
