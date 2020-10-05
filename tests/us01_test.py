import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
import us01

# ----------------------------------- Test Cases for Use Case 41 -----------------------------------
class usecase01_test(unittest.TestCase):
    def test1(self):
        self.assertEqual(us01.usecase01("seeds/test8.ged"),'All dates are before today')

    def test2(self):
            self.assertEqual(us01.usecase01("seeds/test9.ged"),'All dates are before today')

    def test3(self):
            self.assertEqual(us01.usecase01("seeds/test10.ged"),'All dates are before today')

    def test4(self):
            self.assertEqual(us01.usecase01("seeds/test11.ged"),"There is at least one date later than the current date")

    def test5(self):
            self.assertEqual(us01.usecase01("seeds/test12.ged"),"There is at least one date later than the current date")

if __name__ == '__main__':
    unittest.main()
