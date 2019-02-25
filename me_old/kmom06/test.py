#!/usr/bin/env python3
"""
Test the max_subset_sum functions
"""
import unittest
import time
import max_sub_sum as mss

class Testsub_sum(unittest.TestCase):
    """ Submodule for unittests, derives from unittest.TestCase """

    def setUp(self):
        self.static = [3, -4, 6, 1, 1, -2, 2, 3]
        self.generated_1000 = mss.generate_random(1000, 24)
        self.generated_1500 = mss.generate_random(1500, 24)
        self.generated_5000 = mss.generate_random(5000, 24)
        self.generated_15000 = mss.generate_random(15000, 24)

    def test_a_sum1_working(self):
        """ Test so sum1 works on pre-defined list """
        self.assertEqual(mss.max_sub_sum1(self.static), 11)
    
    # def test_b_sum1_time_1000(self):
    #     """ Test so sum1 works on random list with 1000 elements """
    #     s = time.time()
    #     mss.max_sub_sum1(self.generated_1000)
    #     e = time.time() - s
    #     print(e)
    #     self.assertTrue(e>7)
    # 
    # def test_c_sum1_time_1500(self):
    #     """ Test so sum1 works on random list with 1500 elements"""
    #     s = time.time()
    #     mss.max_sub_sum1(self.generated_1500)
    #     e = time.time() - s
    #     print(e)
    #     self.assertTrue(e>200)

    def test_d_sum2_working(self):
        """Test so sum2 works on pre-defined list"""
        self.assertEqual(mss.max_sub_sum2(self.static), 11)
        
    def test_e_sum2_time_1000(self):
        """ Test so sum2 works on random list with 1000 elements"""
        s = time.time()
        mss.max_sub_sum2(self.generated_1000)
        e = time.time() - s
        print(e)
        self.assertTrue(e<0.5)

    def test_f_sum2_time_1500(self):
        """ Test so sum2 works on random list with 1500 elements"""
        s = time.time()
        mss.max_sub_sum2(self.generated_1500)
        e = time.time() - s
        print(e)
        self.assertTrue(e<0.1)

    def test_g_sum2_time_5000(self):
        """ Test so sum2 works on random list with 5000 elements"""
        s = time.time()
        mss.max_sub_sum2(self.generated_5000)
        e = time.time() - s
        print(e)
        self.assertTrue(e<1)
        
    def test_h_sum3_working(self):
        """Test so sum3 works on pre-defined list"""
        self.assertEqual(mss.max_sub_sum2(self.static), 11)
        
    def test_i_sum3_time_1000(self):
        """ Test so sum3 works on random list with 1000 elements"""
        s = time.time()
        mss.max_sub_sum3(self.generated_1000)
        e = time.time() - s
        print(e)
        self.assertTrue(e<0.0005)

    def test_j_sum3_time_1500(self):
        """ Test so sum3 works on random list with 1500 elements"""
        s = time.time()
        mss.max_sub_sum3(self.generated_1500)
        e = time.time() - s
        print(e)
        self.assertTrue(e<0.005)

    def test_k_sum3_time_5000(self):
        """ Test so sum3 works on random list with 5000 elements"""
        s = time.time()
        mss.max_sub_sum3(self.generated_5000)
        e = time.time() - s
        print(e)
        pass
        self.assertTrue(e<0.0008 or e == 0.0)

    def test_l_sum_max_working(self):
        """Test so sum_max works on pre-defined list"""
        self.assertEqual(mss.max_sub_sum_max(self.static), 11)
        
    def test_m_sum_max_time_1000(self):
        """ Test so sum max works on random list with 1000 elements"""
        s = time.time()
        mss.max_sub_sum_max(self.generated_1000)
        e = time.time() - s
        print(e)
        self.assertTrue(e<0.0005 or e == 0.0)

    def test_n_sum_max_time_1500(self):
        """ Test so sum max works on random list with 1500 elements"""
        s = time.time()
        mss.max_sub_sum_max(self.generated_1500)
        e = time.time() - s
        print(e)
        self.assertTrue(e<0.005)
        
    def test_o_sum_max_time_5000(self):
        """ Test so sum max works on random list with 5000 elements"""
        s = time.time()
        mss.max_sub_sum_max(self.generated_5000)
        e = time.time() - s
        print(e)
        self.assertTrue(e<0.05)



    def test_p_sum2_time_15000(self):
        """ Test so sum2 works on random list with 15000 elements"""
        s = time.time()
        mss.max_sub_sum2(self.generated_15000)
        e = time.time() - s
        print(e)
        self.assertTrue(e<10)

    def test_q_sum3_time_15000(self):
        """ Test so sum max works on random list with 15000 elements"""
        s = time.time()
        mss.max_sub_sum3(self.generated_15000)
        e = time.time() - s
        print(e)
        self.assertTrue(e<0.05)

    def test_r_sum_max_time_15000(self):
        """ Test so sum max works on random list with 15000 elements"""
        s = time.time()
        mss.max_sub_sum_max(self.generated_15000)
        e = time.time() - s
        print(e)
        self.assertTrue(e<0.05)


if __name__ == '__main__':
    unittest.main(verbosity=2)