from collections import namedtuple
from operator import attrgetter as attr
import copy
import numpy as np
import random

import beerworld
import ea_gtype
import neuron

Generation = namedtuple('Generation', 'best_weights board timesteps')

class Candidate(object):
    def __init__(self, timesteps, weights=None):
        if weights is not None:
            self.weights = weights
        else:
            self.weights = ea_gtype.random_genotype()
        self.fitness = 0
        self.timesteps = timesteps

    def calculate_fitness(self, beer):
        score = 0
        nn = neuron.Neural_net(self.weights)
        for _ in range(self.timesteps):
            stim = beer.sensor_cells()
            output = nn.act_on_input(stim)
            object_type  = beer.modify_on_action(output)

            if object_type == "S":
                score += 2
            elif object_type == "B":
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

    def crossover(self, other):
        point = random.randrange(len(self.weights))
        if random.randint(0,1):
            return Candidate(self.timesteps, np.concatenate([self.weights[:point],other.weights[point:]]))
        else:
            return Candidate(self.timesteps, np.concatenate([other.weights[:point],self.weights[point:]]))

class Population(object):
    def __init__(self, candidate, size, timesteps, max_generations, probability, num_elites, run_type):
        self.candidate = candidate
        self.size = size
        self.timesteps = timesteps
        self.max_generations = max_generations
        self.population = self.initialize_population()
        self.probability = probability
        self.num_elites = num_elites
        self.run_type = run_type
        self.beer = beerworld.Beer()

    def initialize_candidate(self):
        return self.candidate(self.timesteps)

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
        board = self.beer.board

        for candidate in population:
            candidate.calculate_fitness(self.beer)

        for i in range(self.max_generations):
            adults = self.adult_selection(population)
            parents = self.fitness_proportionate_selection(population)
            children = self.reproduction(parents)
            elites = self.elitism(population)

            fitness_sum = 0
            for child in children:
                child.mutate(self.probability)
                child.calculate_fitness(self.beer)
                fitness_sum += child.fitness
            print fitness_sum

            population = elites + self.best_candidates(adults, children)

            yield Generation(elites[0].weights, self.beer.board, 60)

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

    def sigma_scaling_selection(self, population):
        fitnesses = map(attr('fitness'), population)
        mu = np.mean(fitnesses)
        sigma = np.std(fitnesses)
        mu_sum = np.sum((fitnesses - mu)/(2*sigma) + 1)

        new_population =  []
        for i in range(len(population)):
            current_counter = 0
            candidate_random_number = random.random() * mu_sum

            for _ in range(1):
                parents = []
                for candidate in population:
                    current_counter += (1 + (candidate.fitness - mu) / (2 * sigma))
                    if current_counter >=  candidate_random_number:
                        parents.append(candidate)
                        break
                new_population.append(parents[0].crossover(parents[1]))

        return population

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

def run(run_type):
    size = 40
    max_generations = 100
    timesteps = 600
    probability = 0.01
    num_elites = 2
    population = Population(Candidate, size, timesteps, max_generations, probability, num_elites, run_type)
    for generation in population.evolve():
        yield generation

if __name__ == '__main__':
    run()
