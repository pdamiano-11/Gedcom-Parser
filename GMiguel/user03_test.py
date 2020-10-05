import unittest
import pandas as pd
import Project02
import user03
import sys
sys.path.append("C:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\seeds")

class TestUser03(unittest.TestCase):
    #all deaths are after birth
    def test1(self):
        s = ""
        self.assertTrue(user03.user03("seeds/test6.ged"))

