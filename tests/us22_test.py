#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.chdir(os.path.dirname(os.path.abspath('../tests')))


# In[2]:


import sys
sys.path.append(os.path.abspath('../Team-4-Code/src/UserStories'))
sys.path.append(os.path.abspath('../Team-4-Code/src'))


# In[3]:


cwd = os.getcwd()
os.chdir(os.path.join(cwd, 'seeds'))


# In[5]:


from us22 import us22
import Project02


# In[6]:


import unittest


# In[7]:


class us22_test(unittest.TestCase):
    def test1(self):
        individuals = Project02.createIndividualsDataFrame('seed.ged')
        df = individuals[0:3]
        df = df.append(individuals.iloc[4]).reset_index(drop = True)
        res = []
        self.assertEqual(us22('seed.ged'), res)
        
    def test2(self):
        families = Project02.createFamiliesDataFrame('test1.ged')
        df = families[0:len(families) - 2]
        res = []
        self.assertEqual(us22('test1.ged'), res)
    
    def test3(self):
        individuals = Project02.createIndividualsDataFrame('test2.ged')
        df = individuals[0:7]
        df = df.append(individuals.iloc[3]).reset_index(drop = True)
        res = []
        self.assertEqual(us22('test2.ged'), res)
        
    def test4(self):
        families = Project02.createFamiliesDataFrame('test3.ged')
        df = families[0:len(families)]
        df = df.append(families.iloc[len(families) - 1]).reset_index(drop = True)
        res = []
        self.assertEqual(us22('test3.ged'), res)
        
    def test5(self):
        individuals = Project02.createIndividualsDataFrame('test5.ged')
        df = individuals[0:11]
        df = df.append(individuals.iloc[4]).reset_index(drop = True)
        res = []
        self.assertEqual(us22('test5.ged'), res)

unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:




