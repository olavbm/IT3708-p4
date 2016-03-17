import numpy as np

iter_limit = 100
input_count = 6

class Neural_net(object):
    def __init__ (self, weights):
        self.weights = weights
        hidden_count = weights.shape[0]
        self.syn = np.zeros(hidden_count)

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def act_on_input(self, inputs):
        syn = self.syn
        dot = np.dot
        cat = np.concatenate
        for x in range(iter_limit):
            syn = sigmoid(dot(weights, cat((inputs, syn))))
        self.syn = syn
        return syn[:3]
