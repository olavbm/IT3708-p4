import copy
import random
import neuron
import flatland
import ea_gtype
import numpy as np

class Candidate(object):
    def __init__(self, weights, timesteps):
        '''
        Create a new Candidate with 'gType'(possibly a matrix of floats).
        If there is a float in two indices, there is a connection between the nodes.
        '''
        self.weights = weights
        self.fitness = 0
        self.timesteps = timesteps

    '''
    Fitness evaluation function.  
    Somehow needs to pass board to the ann for action-response.
    '''
    # TODO: Communicate with board and ann.
    def calculate_fitness(self, board):
        score = 0
        nn = neuron.Neural_net(self.weights)
        for _ in range(self.timesteps):
            stim = flatland.sensor_cells(board)
            output = nn.act_on_input(stim)
            board, rune = flatland.modify_on_action(board, output)

            if rune == "F":
                score += 2
            elif rune == "P":
                score -= 3
        self.fitness = score

    # given a probability p, in p occurences, change the weight up or down slightly
    def mutate(self, probability):
        for y in range(len(self.weights)):
            for x in range(len(self.weights[y])):
                if random.random() <= probability:
                    # mutation is done by moving the weight slightly up or
                    # down. Might want to bound this.
                    self.weights[y][x] += random.uniform(-1, 1) * 0.001

    # Simple crossover, prone to division-errors
    def crossover(self, other):
        point = len(self.weights/2)
        self.weights = np.concatenate([self.weights[:point],other.weights[point:]])

        return Candidate(self.weights, self.timesteps)


class Population(object):
    def __init__(self, candidate, size, timesteps, max_generations, probability, num_elites, weight_dimensions):
        self.candidate = candidate
        self.size = size
        self.timesteps = timesteps
        self.weight_dimensions = weight_dimensions
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
        return self.candidate(ea_gtype.random_genotype(self.weight_dimensions), self.timesteps)

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
    def evolve(self):
        population = self.population
        board = flatland.create_board(10, 0.3, 0.3)
        for candidate in population:
            board_copy = copy.deepcopy(board)
            candidate.calculate_fitness(board_copy)
        for i in range(self.max_generations):
            adults = self.adult_selection(population)
            parents = self.fitness_proportionate_selection(population)
            children = self.reproduction(parents)
            elites = self.elitism(population)

            for child in children:
                board_copy = copy.deepcopy(board)
                child.mutate(self.probability)
                child.calculate_fitness(board_copy)


            population = elites + self.best_candidates(adults, children)

        return population

    # TODO: Implement how many adults we want to keep
    def adult_selection(self, population):
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
            fitness_sum += candidate.fitness

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
    def reproduction(self, parents):
        new_population = []
        for i in range(self.size):
            new_population.append(parents[i].crossover(parents[int(random.random() * self.size - 1)]))
        return new_population

    # Returning the best candidates of adults and children
    def best_candidates(self, adults, children):
        return sorted(adults + children, key=lambda c: c.fitness, reverse=True)[:self.size - self.num_elites]

    # Keep the best n candidates in each generation
    def elitism(self, population):
        return sorted(population, key=lambda c: c.fitness, reverse=True)[:self.num_elites]

def run():
    size = 100
    max_generations = 100
    timesteps = 60
    probability = 0.0000000001
    num_elites = 2
    weight_dimensions = [10, 10]
    population = Population(Candidate, size, timesteps, max_generations, probability, num_elites, weight_dimensions)
    result = population.evolve()

if __name__ == '__main__':
    run()
