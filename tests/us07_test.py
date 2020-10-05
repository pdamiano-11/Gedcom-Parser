import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
import us07

# ----------------------------------- Test Cases for Use Case 41 -----------------------------------
class usecase01_test(unittest.TestCase):
    def test1(self):
            self.assertEqual(us07.usecase07("seeds/test8.ged"),"All ages are less than 150")

    def test2(self):
            self.assertEqual(us07.usecase07("seeds/test9.ged"),"All ages are less than 150")

    def test3(self):
            self.assertEqual(us07.usecase07("seeds/test10.ged"),"All ages are less than 150")

    def test4(self):
            self.assertEqual(us07.usecase07("seeds/test11.ged"),"All ages are less than 150")

    def test5(self):
            self.assertEqual(us07.usecase07("seeds/test12.ged"),"All ages are less than 150")

if __name__ == '__main__':
    unittest.main()
