#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

file_name = input("Enter the name of the GEDCOM file: ")
file = open(file_name, "r")
lines = []
for line in file:
    lines.append(str(line))

for idx, line in enumerate(lines):
    lines[idx] = line.replace('\n', '').replace('@', '').replace('_MARNM', 'MARR')
input_lines = ['0 NOTE Team-4-Project'] + lines


# In[3]:


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


# In[4]:


indi_list = []
fam_list = []            
for text in fam_split:
    sub_text = text.strip().split()
    char = list(sub_text[1])
    if char[0] == 'I':
        indi_list.append(text)
    elif char[0] == 'F':
        fam_list.append(text)


# In[5]:


individuals = pd.DataFrame(index = range(len(indi_list)), columns = 
                           ['ID', 'Name', 'Gender', 'Birthday', 'Age', 
                            'Alive', 'Dead', 'Child', 'Spouse'])

for idx, indi in enumerate(indi_list):
    lst = indi.strip().split()
    individuals.ID[idx] = lst[1]
    
    if "NAME" in lst:
        i = lst.index("NAME")
        individuals.Name[idx] = ' '.join(lst[i+1:i+3]).replace('/', '')
    
    if "SEX" in lst:
        i = lst.index("SEX")
        individuals.Gender[idx] = lst[i+1]
    
    if "DEAT" in lst:
        individuals.Dead[idx] = 'Y'
    else:
        individuals.Alive[idx] = 'Y'
    
    if "FAMC" in lst:
        i = lst.index("FAMC")
        individuals.Child[idx] = lst[i+1]
    
    if "FAMS" in lst:
        i = lst.index("FAMS")
        individuals.Spouse[idx] = lst[i+1]

print("Individuals: ")
print(individuals.head(len(individuals))


# In[7]:


families = pd.DataFrame(index = range(len(fam_list)), 
                        columns = ['ID', 'Married', 'Divorced', 'Husband ID', 
                                   'Husband Name', 'Wife ID', 'Wife Name', 'Children'])

for idx, fam in enumerate(fam_list):
    lst = fam.strip().split()
    families.ID[idx] = lst[1]
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

print("Families: ")
print(families.head(len(families)))


# In[23]:


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
print(output_lines)


# In[27]:


otp = open("outputProject02.txt", "w")
for n in range(len(input_lines)):
    otp.write("\n" + "--> " + input_lines[n])
    otp.write("\n" + "<-- " + output_lines[n] + "\n")
otp.close()

