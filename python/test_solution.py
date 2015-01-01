import random
import unittest
from solution import solution

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

class TestSolution(unittest.TestCase):

    def test_solution_1000(self):
        self.assertEqual(233168,solution(1000))

    def test_solution_0(self):
        self.assertEqual(0,solution(0))

    def test_solution_10(self):
        self.assertEqual(23,solution(10))

if __name__ == '__main__':
    unittest.main()