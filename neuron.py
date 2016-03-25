import numpy as np
import pprint

iter_limit = 100
input_count = 6
hidden_count = 0
output_count = 3

class Neural_net(object):
    def __init__ (self, weights):
        self.weights = weights
        self.hidden_count = weights.shape[0]
        self.syn = np.ones(self.hidden_count)

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def act_on_input(self, inputs):
        syn = self.syn
        dot = np.dot
        cat = np.concatenate
        sigmoid = self.sigmoid
        syn = sigmoid(dot(inputs, self.weights))
        for i in range(len(self.weights)):
            syn = sigmoid(dot(self.weights[i], syn))
        self.syn = syn
        return syn
