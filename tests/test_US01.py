import unittest
import sys
import os
sys.path.append(os.path.abspath('../src/userstories'))
import US01

# ----------------------------------- Test Cases for Use Case 41 -----------------------------------
class usecase01_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(US01.usecase01("testFiles/test1.ged"),'All dates are before today')

    def test2(self):
            self.assertEqual(US01.usecase01("testFiles/test2.ged"),'All dates are before today')

    def test3(self):
            self.assertEqual(US01.usecase01("testFiles/test3.ged"),'All dates are before today')

    def test4(self):
            self.assertEqual(US01.usecase01("testFiles/test4.ged"),"There is at least one date later than the current date")

    def test5(self):
            self.assertEqual(US01.usecase01("testFiles/test5.ged"),"There is at least one date later than the current date")

if __name__ == '__main__':
    unittest.main()