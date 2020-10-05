#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os


# In[2]:


import sys


# In[4]:


import pandas as pd


# In[5]:


import Project02


# In[7]:


def us22(gedcom_file):
    families = Project02.createFamiliesDataFrame(gedcom_file)
    individuals = Project02.createIndividualsDataFrame(gedcom_file)
    
    invalid = []
    
    for idx in range(len(families.ID)):
        vfy = families.ID.drop([idx])
        if families.ID[idx] in vfy:
            invalid.append(families.ID[idx])
    
    for idx in range(len(individuals.ID)):
        vfy = individuals.ID.drop([idx])
        if individuals.ID[idx] in vfy:
            invalid.append(individuals.ID[idx])
    
    return invalid
            

if __name__ == '__main__':
    invalid = us22('seed.ged')
    print(invalid)


# In[ ]:




