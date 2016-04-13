from collections import namedtuple
import pprint
import numpy as np

input_count = 6
hidden_count = 2
output_count = 2

dot = np.dot
cat = np.concatenate
one = np.array([1.0])

NetParameters = namedtuple('NetParameters', 'weight gain mass bias')

def random():
    weight = 0
    gain = np.random.uniform(1.0, 5.0, [hidden_count + output_count])
    mass = np.random.uniform(1.0, 2.0, [hidden_count + output_count])
    bias = np.random.uniform(-10.0, 0.0, [hidden_count + output_count, 1])
    dims = (hidden_count + output_count, input_count + hidden_count + output_count)
    weight = np.random.uniform(-5.0, 5.0, [dims[0], dims[1] -1])
    weight[0:2, 8:10] = 0
    weight[2:5, 0:5] = 0
    parameters = NetParameters(weight, gain, mass, bias)

    return parameters

def make_CTRNN(output_count=2):
    class CTRNN(object):
        def __init__ (self, parameters):
            self.weight = parameters.weight
            self.bias = parameters.bias
            self.gain = parameters.gain
            self.mass = parameters.mass
            self.state = np.zeros(self.weight.shape[0])
            self.output = np.zeros(self.weight.shape[0])

        def act_on_input(self, inputs):
            w = cat([self.weight, self.bias], axis=1)
            s = cat((inputs, self.output, one))
            stimulus = dot(w, s)

            # change
            self.state += (stimulus - self.state) / self.mass

            # output with gain and sigmoid
            self.output = (1.0 / (1.0 + np.exp(-self.state * self.gain)))

            return self.output[:output_count]

    return CTRNN
random()
