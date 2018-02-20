#!/usr/bin/env python3
"""
Test the function
"""
import unittest
import time
from func import func, generate_random

class TestFunc(unittest.TestCase):
    """
    Run the test to see when you are done improving the code.
    When you first run the test don't be discourage by
    the long execution times.
    Small improvements to the code can have big impact.
    Once b,c and d are OK uncomment e and f and run them to check.
    """

    def setUp(self):
        """ Setup each test. Create all lists. """
        self.static = [22, 34, -31, 50, -30, 18, -40, 26, -34, 21, 23, 27, -5, 37, 49, -38, 2, 46, 24, -5]
        self.generated_500 = generate_random(500, 24)
        self.generated_1000 = generate_random(1000, 24)
        self.generated_1200 = generate_random(1200, 24)
        self.generated_5000 = generate_random(5000, 24)
        self.generated_15000 = generate_random(15000, 24)


    def test_a_func_working(self):
        """ Test the functionality on pre-defined list."""
        self.assertEqual(func(self.static), 201)

    def test_b_func_time_500(self):
        """ Test speed of func on random list with 500 elements """
        start = time.time()
        res = func(self.generated_500)
        end = time.time() - start
        print(end)
        self.assertEqual(res, 1336)
        self.assertTrue(end < 1)

    def test_c_func_time_1000(self):
        """ Test speed of func on random list with 1000 elements """
        start = time.time()
        res = func(self.generated_1000)
        end = time.time() - start
        print(end)
        self.assertEqual(res, 1336)
        self.assertTrue(end < 1.5)


    def test_d_func_time_1200(self):
        """ Test speed of func on random list with 1200 elements"""
        start = time.time()
        res = func(self.generated_1200)
        end = time.time() - start
        print(end)
        self.assertEqual(res, 1398)
        self.assertTrue(end < 2)


    # def test_e_func_time_5000(self):
    #     """ Test so func works on random list with 5000 elements"""
    #     start = time.time()
    #     res = func(self.generated_5000)
    #     end = time.time() - start
    #     print(end)
    #     self.assertTrue(end < 5)
    #     self.assertEqual(res, 7348)
    # 
    # 
    # def test_f_func_time_15000(self):
    #     """ Test so func works on random list with 15000 elements"""
    #     start = time.time()
    #     res = func(self.generated_15000)
    #     end= time.time() - start
    #     print(end)
    #     self.assertTrue(end < 30)
    #     self.assertEqual(res, 7582)




if __name__ == '__main__':
    unittest.main(verbosity=2)
