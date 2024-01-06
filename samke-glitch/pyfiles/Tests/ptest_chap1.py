#!/usr/bin/env python3

import unittest

def sumOne(a, b):
    return a + b
class sumTest(unittest.TestCase):
    def setUp(self):
        print("SETUP is Called...")
        # Arrange
        self.a = 10
        self.b = 20

    def tearDown(self):
        print("TEARDOWN is called")
    def testSumOne(self):
        print("TEST-- 1 Called...")
        # Act
        result = sumOne(self.a, self.b)

        # Assert
        self.assertEqual(result, self.a + self.b)

    def testSumOne1(self):
        print("Test -- 3 Called...")
        # Act
        result = sumOne(self.b, self.a)

        # Assert
        self.assertEqual(result, self.a + self.b)


if __name__== "__main__":
    unittest.main()
