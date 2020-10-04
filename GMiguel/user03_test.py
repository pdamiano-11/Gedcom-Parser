import unittest
import pandas as pd
import Project02
import user03

class TestUser03(unittest.TestCase):
    #tests that all deaths are after birth
def
'''
if "BIRT" in lst:
            i = lst.index("BIRT")
            date_b = pd.to_datetime('-'.join(lst[i+3:i+6]))
            individuals.Birthday[idx] = date_b.strftime("%b-%d-%Y")
        
        if "DEAT" in lst:
            i = lst.index("DEAT")
            date_d = pd.to_datetime('-'.join(lst[i+4:i+7]))
            individuals.Dead[idx] = date_d.strftime("%b-%d-%Y")
            individuals.Age[idx] = int((date_d - date_b).days/365)
            individuals.Alive[idx] = 'False'
'''