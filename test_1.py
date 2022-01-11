import unittest
from test import support

class MyTestCase2(unittest.TestCase):
     # Only use setUp() and tearDown() if necessary

    def setUp(self):
        #... code to execute in preparation for tests ...
        pass

    def tearDown(self):
        #... code to execute to clean up after tests ...
        pass

    def test_feature_one(self):
        # Test feature one.
        print("...MyTestCase2::test_feature_one...")

    def test_feature_two(self):
        # Test feature two.
        print("...MyTestCase2::test_feature_two...")

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        #... code to execute in preparation for tests ...
        pass

    def tearDown(self):
        #... code to execute to clean up after tests ...
        pass

    def test_feature_one(self):
        # Test feature one.
        print("...MyTestCase1::test_feature_one...")

    def test_feature_two(self):
        # Test feature two.
        print("...MyTestCase1::test_feature_two...")



#if __name__ == '__main__':
#    unittest.main()
