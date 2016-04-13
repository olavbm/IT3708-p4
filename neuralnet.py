from collections import namedtuple
import pprint
import numpy as np

input_count = 6
hidden_count = 2
output_count = 2

dot = np.dot
cat = np.concatenate
bias = np.array([1.0])

Net_parameters = namedtuple('Net_parameters', 'weight gain mass')

def random():
    weight = 0
    gain = np.random.uniform(1.0, 5.0, [hidden_count + output_count])
    mass = np.random.uniform(1.0, 2.0, [hidden_count + output_count])
    bias = np.random.uniform(-10.0, 0.0, [hidden_count + output_count, 1])
    dims = (hidden_count + output_count, input_count + hidden_count + output_count)
    weight = np.random.uniform(-5.0, 5.0, [dims[0], dims[1] -1])
    weight = cat([weight, bias], axis=1)
    weight[0:2, 8:10] = 0
    weight[2:5, 0:5] = 0
    parameters = Net_parameters(weight, gain, mass)

    return parameters

def make_CTRNN(output_count=2):
    class CTRNN(object):
        def __init__ (self, parameters):
            self.weight = parameters.weight
            self.gain = parameters.weight
            self.mass = parameters.mass
            self.state = np.zeros(self.weight.shape[0])
            self.output = np.zeros(self.weight.shape[0])

        def act_on_input(self, inputs):

            stimulus = dot(self.weight, cat((inputs, self.output, bias)))

            # change
            self.state += (stimulus - self.state) / self.mass

            # output with gain and sigmoid
            self.output = (1.0 / (1.0 + np.exp(-self.state * self.gain)))

            return self.outputs[:output_count]

    return CTRNN
random()
