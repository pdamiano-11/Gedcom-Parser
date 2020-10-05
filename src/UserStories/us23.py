#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Project02


# In[7]:

import os
import sys
import pandas as pd

# In[42]:


def us23(ppl_df):
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


# In[ ]:




