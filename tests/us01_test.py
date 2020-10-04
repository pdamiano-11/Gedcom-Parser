import unittest
import datetime
import sys
import os
sys.path.append(os.path.abspath('../src/userstories'))
from us01 import us01

class us01_test(unittest.TestCase):
    def test1(self):
        val = datetime.datetime(2020, 9, 25)
        self.assertEqual(us01(val), 'This date is valid')

    def test2(self):
        val = datetime.datetime(1999, 12, 29)
        self.assertEqual(us01(val), 'This date is valid')

    def test3(self):
        val = datetime.datetime(1800, 3, 15)
        self.assertEqual(us01(val), 'This date is valid')

    def test4(self):
        val = datetime.datetime(2021, 9, 26)
        self.assertEqual(us01(val), 'This date is after current date.')

    def test5(self):
        val = datetime.datetime(3000, 9, 26)
        self.assertEqual(us01(val), 'This date is after current date.')
