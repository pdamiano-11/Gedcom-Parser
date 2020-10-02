#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd
import datetime
from tabulate import tabulate

file_name = input("Enter the name of the GEDCOM file: ")
file = open(file_name, "r")
lines = []
for line in file:
    lines.append(str(line))

for idx, line in enumerate(lines):
    lines[idx] = line.replace('\n', '').replace('@', '').replace('_MARNM', 'MARR')
input_lines = ['0 NOTE Team-4-Project'] + lines


# In[32]:


indexes = []
for idx, line in enumerate(input_lines):
    lst = line.strip().split()
    if lst[0] == '0':
        indexes.append(idx)

fam_split = []
for n in range(len(indexes)):
    try:
        fam_split.append(' '.join(input_lines[indexes[n]:indexes[n+1]]))
    except:
        continue

del fam_split[0:2]


# In[33]:


indi_list = []
fam_list = []            
for text in fam_split:
    sub_text = text.strip().split()
    char = list(sub_text[1])
    if char[0] == 'I':
        indi_list.append(text)
    elif char[0] == 'F':
        fam_list.append(text)


# In[35]:


individuals = pd.DataFrame(index = range(len(indi_list)), columns = 
                           ['ID', 'Name', 'Gender', 'Birthday', 'Age', 
                            'Alive', 'Dead', 'Child', 'Spouse'])

now = pd.to_datetime('now')

for idx, indi in enumerate(indi_list):
    lst = indi.strip().split()
    individuals.ID[idx] = lst[1]
    
    if "NAME" in lst:
        i = lst.index("NAME")
        individuals.Name[idx] = ' '.join(lst[i+1:i+3]).replace('/', '')
    
    if "SEX" in lst:
        i = lst.index("SEX")
        individuals.Gender[idx] = lst[i+1]
    
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
    else:
        individuals.Alive[idx] = 'True'
        individuals.Age[idx] = int((now - date_b).days/365)
    
    if "FAMC" in lst:
        i = lst.index("FAMC")
        individuals.Child[idx] = lst[i+1]
    
    if "FAMS" in lst:
        i = lst.index("FAMS")
        individuals.Spouse[idx] = lst[i+1]


# In[36]:


families = pd.DataFrame(index = range(len(fam_list)), 
                        columns = ['ID', 'Married', 'Divorced', 'Husband ID', 
                                   'Husband Name', 'Wife ID', 'Wife Name', 'Children'])

for idx, fam in enumerate(fam_list):
    lst = fam.strip().split()
    families.ID[idx] = lst[1]
    
    if "MARR" in lst:
        i = lst.index("MARR")
        families.Married[idx] = pd.to_datetime('-'.join(lst[i+3:i+6])).strftime("%b %d %Y")
        
    div_case = lst.index("_CURRENT")
    if lst[div_case+1] == "N":
        families.Divorced[idx] = "True"
    else:
        families.Divorced[idx] = "False"
    
    if 'HUSB' in lst:
        i = lst.index('HUSB')
        families['Husband ID'][idx] = lst[i+1]
        families['Husband Name'][idx] = list(individuals.Name[individuals.ID == lst[i+1]])[0]
        
    if 'WIFE' in lst:
        i = lst.index('WIFE')
        families['Wife ID'][idx] = lst[i+1]
        families['Wife Name'][idx] = list(individuals.Name[individuals.ID == lst[i+1]])[0]
    
    chil_ids = [idx for idx, val in enumerate(lst) if val in lst[:idx] and val == "CHIL"]
    chil_ids = [lst.index("CHIL")] + chil_ids
    for n in range(len(chil_ids)):
        chil_ids[n] += 1
        chil_ids[n] = lst[chil_ids[n]]
    families.Children[idx] = chil_ids


# In[37]:


otp = open("Project03_Output.txt", "w")
otp.truncate(0)
otp.write("Individuals: \n")
otp.write(tabulate(individuals, headers='keys', tablefmt='psql'))
otp.write("\n")
otp.write("Families: \n")
otp.write(tabulate(families, headers='keys', tablefmt='psql'))
otp.close()


# In[38]:


supported = ['INDI', '0 NOTE', '0 HEAD', '0 TRLR', 'FAM', '1 NAME', '1 SEX', '1 BIRT', '1 DEAT', '1 FAMC', 
             '1 FAMS', '1 MARR', '1 HUSB', '1 WIFE', '1 CHIL', '1 DIV', '2 DATE']

output_lines = []
for line in input_lines:
    if any(s in line for s in supported):
        t = line.strip().split()
        if 'INDI' in t:
            idx = t.index('INDI')
            output_lines.append('|'.join([t[0]] + [t[idx]] + ['Y'] + [' '.join(t[1:idx])]))
        elif 'FAM' in t:
            idx = t.index('FAM')
            output_lines.append('|'.join([t[0]] + [t[idx]] + ['Y'] + [' '.join(t[1:idx])]))
        else:
            output_lines.append('|'.join(t[0:2] + ['Y'] + [' '.join(t[2:])]))
    else:
        t = line.strip().split()
        output_lines.append('|'.join(t[0:2] + ['N'] + [' '.join(t[2:])]))


# In[39]:


otp = open("outputProject02.txt", "w")
for n in range(len(input_lines)):
    otp.write("\n" + "--> " + input_lines[n])
    otp.write("\n" + "<-- " + output_lines[n] + "\n")
otp.close()


# In[ ]:




