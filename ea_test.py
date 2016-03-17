import unittest
import ea

class TestEA(unittest.TestCase):
    def testInitializePopulation(self):
        population = ea.Population(ea.Candidate, 10, 20)
        print population
    def testFitnessProportionateSelection(self):
        population = ea.Population(ea.Candidate, 10, 20)

if __name__ == '__main__':
    unittest.main()
