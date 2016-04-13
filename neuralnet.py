import numpy as np

dot = np.dot
cat = np.concatenate
bias = np.array([1.0])

def make_CTRNN(output_count=2):
    class CTRNN(object):
        def __init__ (self, weight, gain, mass):
            self.weight = weight
            self.gain = gain
            self.mass = mass
            self.state = np.zeros(weight.shape[0])
            self.output = np.zeros(weight.shape[0])

        def act_on_input(self, inputs):

            stimulus = dot(self.weight, cat((inputs, self.output, bias)))

            # change
            self.state += (stimulus - self.state) / self.mass

            # output with gain and sigmoid
            self.output = (1.0 / (1.0 + np.exp(-self.state * self.gain)))

            return self.outputs[:output_count]

    return CTRNN
