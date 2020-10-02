#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Project02 import *


# In[7]:


import unittest


# In[42]:


def userstory23(ppl_df):
    for idx in range(len(ppl_df)):
        current_name = ppl_df.Name[idx]
        current_bday = ppl_df.Birthday[idx]
    
        check = ppl_df.drop([idx])
        for name in check.Name:
            if current_name == name:
                i = check[check.Name == current_name].index.values[0]
                if current_bday == check.Birthday[i]:
                    unique = "false"
                    break
                else:
                    unique = "true"
            else:
                unique = "true"
    
    if unique == "true":
        return "unique"
    else:
        return "not unique"


# In[44]:


class userstory23_test(unittest.TestCase):
    def test1(self):
        df = individuals[0:3]
        df = df.append(individuals.iloc[0]).reset_index(drop = True)
        res = "not unique"
        self.assertEqual(userstory23(df), res)
        
    def test2(self):
        df = individuals[0:5]
        res = "unique"
        self.assertEqual(userstory23(df), res)
    
    def test3(self):
        df = individuals[0:7]
        df = df.append(individuals.iloc[3]).reset_index(drop = True)
        res = "not unique"
        self.assertEqual(userstory23(df), res)
        
    def test4(self):
        df = individuals[0:9]
        df = df.append(individuals.iloc[11]).reset_index(drop = True)
        res = "unique"
        self.assertEqual(userstory23(df), res)
        
    def test5(self):
        df = individuals[0:11]
        df = df.append(individuals.iloc[4]).reset_index(drop = True)
        res = "not unique"
        self.assertEqual(userstory23(df), res)

unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:




