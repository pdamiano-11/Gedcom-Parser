import unittest
import datetime
import sys
import os
sys.path.append(os.path.abspath('../src/userstories'))
import sys
# sys.path.append("c:\\Users\\Stevens User\\555_Team_4\\Team-4-Code\\seeds")
os.chdir("c:\\Users\\Stevens User\\555_Team_4\\Team-4-Code\\seeds")
from us13 import siblingsAgeGap

class US_13_TEST(unittest.TestCase):
    def test1(self):
        filename = "seed.ged" 
        ret = "All siblings are valid"
        self.assertEqual(siblingsAgeGap(filename),ret)

    def test2(self):
        filename = "test1.ged" 
        ret = "All siblings are valid"
        self.assertEqual(siblingsAgeGap(filename),ret)


    def test3(self):
        filename = "test2.ged" 
        ret = "All siblings are valid"
        self.assertEqual(siblingsAgeGap(filename),ret)

    def test4(self):
        filename = "test5.ged" 
        ret = "All siblings are valid"
        self.assertEqual(siblingsAgeGap(filename),ret)
    
    def test5(self):
        filename = "test4.ged" 
        ret = "Individuals  I14  and  I15  are invalid.\n Individuals  I15  and  I14  are invalid."
        self.assertEqual(siblingsAgeGap(filename),ret)

if __name__ == '__main__':
        unittest.main() 
