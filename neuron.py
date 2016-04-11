import numpy as np
from time import sleep

iter_limit = 100

def sigmoid(x):
    return 1/(1+np.exp(-x))

def tanh(x):
    return np.tanh(x)

def runes_to_stim(runes):
    food = [rune == 'F' for rune in runes]
    poison = [rune == 'P' for rune in runes]
    return np.array(food + poison, dtype='float64')

def output_to_rulf(output):
    if max(output) < 0.3:
        return 'U'

    return 'RLF'[np.where(output == max(output))[0][0]]

class Neural_net(object):
    def __init__ (self, weights):
        self.weights = weights
        self.syn = np.zeros(weights.shape[0])

    def act_on_input(self, inputs):
        inputs = runes_to_stim(inputs)
        syn = self.syn
        dot = np.dot
        cat = np.concatenate
        weights = self.weights
        for x in range(iter_limit):
            syn = sigmoid(dot(weights, cat((inputs, syn))))
        self.syn = syn
        return output_to_rulf(syn[:3])
