import numpy as np

def random_genotype(dims):
    """Generate random genotype with standard normal distributed weight values.
    """
    return np.random.standard_normal(dims)
