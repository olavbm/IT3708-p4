import numpy as np

input_count = 6
hidden_count = 0
output_count = 3

def random_genotype():
    """Generate random genotype with standard normal distributed weight values.
    """
    dims = (hidden_count + output_count
           ,input_count + hidden_count + output_count)
    return np.random.standard_normal(dims)
