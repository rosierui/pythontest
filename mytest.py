import unittest
from test import support

class MyTestCase7(unittest.TestCase):
     # Only use setUp() and tearDown() if necessary

    def setUp(self):
        #... code to execute in preparation for tests ...
        pass

    def tearDown(self):
        #... code to execute to clean up after tests ...
        pass

    def test_feature_one(self):
        # Test feature one.
        print("...MyTestCase7::test_feature_one...")

    def test_feature_two(self):
        # Test feature two.
        print("...MyTestCase7::test_feature_two...")

    def test_feature_7(self):
        # Test feature two.
        print("...MyTestCase7::test_feature_7...")


class MyTestCase8(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        #... code to execute in preparation for tests ...
        pass

    def tearDown(self):
        #... code to execute to clean up after tests ...
        pass

    def test_feature_one(self):
        # Test feature one.
        print("...MyTestCase8::test_feature_one...")

    def test_feature_two(self):
        # Test feature two.
        print("...MyTestCase8::test_feature_two...")

    def test_feature_3(self):
        # Test feature one.
        print("...MyTestCase8::test_feature_3...")

    def test_feature_4(self):
        # Test feature two.
        print("...MyTestCase8::test_feature_4...")




#if __name__ == '__main__':
#    unittest.main()
