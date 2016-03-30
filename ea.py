import random

class Candidate(object):
    def __init__(self, gType):
        '''
        Create a new Candidate with 'gType'(possibly a matrix of floats).
        If there is a float in two indices, there is a connection between the nodes.
        '''
        self.gType = gType
        self.weights = [[]]
        self.fitness = 0

    '''
    Fitness evaluation function.  
    Somehow needs to pass board to the ann for action-response.
    '''
    # TODO: Communicate with board and ann.
    def calculate_fitness(self):
        pass

    # given a probability p, in p occurences, change the weight up or down slightly
    def mutate(self, probability):
        for y in range(len(self.weights)):
            for x in range(len(y)):
                if random.random() <= probability:
                    # mutation is done by moving the weight slightly up or
                    # down. Might want to bound this.
                    self.weights[y][x] += random.uniform(-1, 1) * 0.001

    # Simple crossover, prone to division-errors
    def crossover(self, other):
        point = len(self.weights/2)
        self.weights = self.weights[:point] + other.weights[point:]

class Population(object):
    def __init__(self, candidate, size, max_generations, probability, num_elites):
        self.candidate = candidate
        self.size = size
        self.max_generations = max_generations
        self.population = self.initialize_population()
        self.probability = probability
        self.num_elites = num_elites

    '''
    This needs some fixing. How do we initialize the ann, and with what
    kind of matrix? Should it just take care of that itself? But what with
    the gType then?
    '''
    def initialize_candidate(self):
        gType = "test"
        return self.candidate(gType)

    '''
    Initializes the population.
    Uses the candidate provided when initializing the population.
    '''
    def initialize_population(self):
        population = []
        for i in range(self.size):
            population.append(self.initialize_candidate())

        return population

    # TODO: Decision on what parent-selection-function to be used.
    def evolve():
        population = self.population
        for candidate in population:
            candidate.calculate_fitness()
        for i in range(self.max_generations):
            adults = self.adult_selection(population)
            parents = self.fitness_proportionate_selection(population)
            children = self.reproduction(parents)
            elites = self.elitism(population)

            for child in children:
                child.mutate(self.probability)
                child.calculate_fitness()

            population = elites + self.best_candidates(adults, children)

        return population

    # TODO: Implement how many adults we want to keep
    def adult_selection(population):
        return []

    '''
    Sum all fitnesses up to a number, a.
    For each candidate, sum the fitnesses.
        Pick a number between 0 and a.
        If sumFitness > a, you have your candidate.
    '''
    def fitness_proportionate_selection(self, population):
        fitness_sum = 0
        for candidate in population:
            fitness_sum += candidates.fitness

        new_population =  []
        for i in range(len(population)):
            current_counter = 0
            candidate_random_number = random.random() * fitness_sum

            for candidate in population:
                if current_counter >=  candidate_random_number:
                    new_population.append(candidate)
                    break
                else:
                    current_counter += candidate.fitness

        return population

    # Returns a reproduciton of two completely random parents in the population
    def reproduction(self):
        parent1 = self.population[int(random.random() * self.size - 1)]
        parent2 = self.population[int(random.random() * self.size - 1)]
        child = parent1.crossover(parent2)

        return child

    # Returning the best candidates of adults and children
    def best_candidates(adults, children):
        return sorted(adults + children, key=lambda c: c.fitness, reverse=True)[:self.size - self.num_elites]

    # Keep the best n candidates in each generation
    def elitism(self, population):
        return sorted(population, key=lambda c: c.fitness, reverse=True)[:self.num_elites]

def run():
    # It is possible to have many different candidates here.
    class Example_candidate(Candidate):
        # A specialized mutate-function for this exact problem and candidate.
        def mutate(probability):
            pass

    size = 100
    max_generations = 100
    population = Population(Example_candidate, size, max_generations)
    result = population.evolve()
