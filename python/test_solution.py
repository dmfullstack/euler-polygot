import random
import unittest
from solution import solution

class TestSolution(unittest.TestCase):

    def test_solution_1000(self):
        self.assertEqual(233168,solution(1000))

    def test_solution_0(self):
        self.assertEqual(0,solution(0))

    def test_solution_10(self):
        self.assertEqual(23,solution(10))

if __name__ == '__main__':
    unittest.main()