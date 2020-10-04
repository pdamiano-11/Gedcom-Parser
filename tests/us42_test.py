import unittest
import sys
import os
sys.path.append(os.path.abspath('../src/userstories'))
#imports us41 correctly as class
from us42 import us42
 
# ----------------------------------- Test Cases for Use Case 42 -----------------------------------
class us42_test(unittest.TestCase):
    def test1(self):
        val = "30 FEB 2020"
        val2 = "invalid"
        self.assertEqual(us42(val),val2)

    def test2(self):
            val = "01 JAN 2020"
            val2 = "01 JAN 2020"
            self.assertEqual(us42(val),val2)

    def test3(self):
            val = "YIKES 2020"
            val2 = "invalid"
            self.assertEqual(us42(val),val2)
    
    def test4(self):
            val = ""
            val2 = "invalid"
            self.assertEqual(us42(val),val2)
    
    def test5(self):
            val = "pleasedon'tBreAkmyCode"
            val2 = "invalid"
            self.assertEqual(us42(val),val2)

#unittest.main()
