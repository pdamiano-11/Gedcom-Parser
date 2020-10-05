import unittest
import datetime
import sys
import os
sys.path.append(os.path.abspath('../src/userstories'))
import sys
# sys.path.append("c:\\Users\\Stevens User\\555_Team_4\\Team-4-Code\\seeds")
os.chdir("c:\\Users\\Stevens User\\555_Team_4\\Team-4-Code\\seeds")
from us30 import listLivingMarried

class Inneo_Tests_HW4(unittest.TestCase):
    def test1(self):
        filename = "seed.ged" 
        ret = ['John Smith', 'Susan Jones', 'Frank Jones', 'Emily Michaels', 'Bernard Smith', 'Theresa Kelly', 'Kevin Brown', 'Diane Brown']
        self.assertEqual(listLivingMarried(filename),ret)

    def test2(self):
        filename = "test1.ged" 
        ret = ['Sam Smith', 'Rick Smith', 'Hannah Smith', 'Alexa Smith']
        self.assertEqual(listLivingMarried(filename),ret)


    def test3(self):
        filename = "test2.ged" 
        ret = ['James Smith', 'Jen Smith', 'Claire Smith', 'Cody Smith', 'Rachel Smith', 'Rick Smith']
        self.assertEqual(listLivingMarried(filename),ret)

    def test4(self):
        filename = "test3.ged" 
        ret = ['Sam Smith', 'Rick Smith', 'Hannah Smith']
        self.assertEqual(listLivingMarried(filename),ret)
    
    def test5(self):
        filename = "test4.ged" 
        ret = ['Joseph Jones', 'Cassidy Smith', 'Betty Jefferson', 'Maria Hamilton']
        self.assertEqual(listLivingMarried(filename),ret)

if __name__ == '__main__':
        unittest.main() 
