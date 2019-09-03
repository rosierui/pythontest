import unittest
import math
import factorial_v1
from test import test_support

class FactorialTest(unittest.TestCase):
    def setUp(self):
        print("setup")

    def tearDown(self):
        print("cleanup")

    def test_positives(self):
        for x in range(0,10+1):
            act = math.factorial( x )
            val = factorial_v1.fact( x )
            print("%d! = %g == %g"%(x,val,act))
            self.assertAlmostEqual( act, val, 1e-1 )

    def test_negative(self):
        passed = False
        try:
            factorial_v1.fact( -3 )
        except Exception as e:
            print(dir(e))
            print(type(e))
            print(e)
            msg = str(e)
            passed = True and (msg.find("Cannot calculate")>= 0 )
        self.assertTrue( passed )

        ## alternate way
        with self.assertRaises( Exception ) as cm:
            factorial_v1.fact(-3)

if __name__ == "__main__":
    test_support.run_unittest(FactorialTest)
