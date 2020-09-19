#!/usr/bin/env python
# coding: utf-8

# In[7]:


file = open("DamianovPeterGedcomProject01.ged", "r")
lines = []
for line in file:
    lines.append(str(line))
    print(line)

for idx, line in enumerate(lines):
    lines[idx] = line.replace('\n', '').replace('@', '')
input_lines = ['0 NOTE Peter Damianov'] + lines
print(input_lines)


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

