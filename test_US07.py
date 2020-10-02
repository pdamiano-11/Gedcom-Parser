import unittest
import US07

# ----------------------------------- Test Cases for Use Case 41 -----------------------------------
class usecase01_test(unittest.TestCase):
    def test1(self):
            self.assertEqual(US07.usecase07("testFiles/test1.ged"),"All ages are less than 150")

    def test2(self):
            self.assertEqual(US07.usecase07("testFiles/test2.ged"),"All ages are less than 150")

    def test3(self):
            self.assertEqual(US07.usecase07("testFiles/test3.ged"),"All ages are less than 150")

    def test4(self):
            self.assertEqual(US07.usecase07("testFiles/test4.ged"),"At least one individual lived to be over 150")

    def test5(self):
            self.assertEqual(US07.usecase07("testFiles/test5.ged"),"At least one individual lived to be over 150")

if __name__ == '__main__':
    unittest.main()