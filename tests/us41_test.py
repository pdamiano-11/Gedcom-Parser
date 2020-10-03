import unittest
import sys
sys.path.append("/Users/tringapps/Desktop/Team_4_Code/src/UserStories")
#imports us41 correctly as class
from us41 import us41
 
# ----------------------------------- Test Cases for Use Case 41 -----------------------------------
class us41_test(unittest.TestCase):
    def test1(self):
        val = "SEPT 2020"
        val2 = "01 SEPT 2020"
        self.assertEqual(us41(val),val2)

    def test2(self):
            val = "2020"
            val2 = "01 JAN 2020"
            self.assertEqual(us41(val),val2)

    def test3(self):
            val = "26 SEPT 2020"
            val2 = "26 SEPT 2020"
            self.assertEqual(us41(val),val2)

    def test4(self):
            val = "26 SEPT 2020 20"
            val2 = "invalid"
            self.assertEqual(us41(val),val2)

    def test5(self):
            val = "26 SEPT OK 2020"
            val2 = "invalid"
            self.assertEqual(us41(val),val2)

#unittest.main()