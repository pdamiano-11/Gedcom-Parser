#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import datetime
from tabulate import tabulate

def collectInputFile(gedcom_name):
    file = open(gedcom_name, "r")
    lines = []
    for line in file:
        lines.append(str(line))

    for idx, line in enumerate(lines):
        lines[idx] = line.replace('\n', '').replace('@', '').replace('_MARNM', 'MARR')
    input_lines = ['0 NOTE Team-4-Project'] + lines

    return input_lines

def organizeInput(gedcom_name):
    input_lines = collectInputFile(gedcom_name)

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

    return fam_split


def createIndiList(gedcom_name):
    fam_split = organizeInput(gedcom_name)
    indi_list = []
    for text in fam_split:
        sub_text = text.strip().split()
        char = list(sub_text[1])
        if char[0] == 'I':
            indi_list.append(text)
    
    return indi_list

def createFamList(gedcom_name):
    fam_split = organizeInput(gedcom_name)
    fam_list = []
    for text in fam_split:
        sub_text = text.strip().split()
        char = list(sub_text[1])
        if char[0] == 'F':
            fam_list.append(text)

    return fam_list

def createIndividualsDataFrame(gedcom_name):
    indi_list = createIndiList(gedcom_name)

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

    return individuals


def createFamiliesDataFrame(gedcom_name):
    fam_list = createFamList(gedcom_name)
    individuals = createIndividualsDataFrame(gedcom_name)

    families = pd.DataFrame(index = range(len(fam_list)), 
                            columns = ['ID', 'Married', 'Divorced', 'Husband ID', 
                                       'Husband Name', 'Wife ID', 'Wife Name', 'Children'])

    for idx, fam in enumerate(fam_list):
        lst = fam.strip().split()
        families.ID[idx] = lst[1]
        
        if "MARR" in lst:
            i = lst.index("MARR")
            if lst[i+1]=="2":
                date_m = pd.to_datetime('-'.join(lst[i+3:i+6]))
                families.Married[idx] = date_m.strftime("%b-%d-%Y")
        if "_CURRENT" in lst:
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
        if "CHIL" in lst:
            chil_ids = [idx for idx, val in enumerate(lst) if val in lst[:idx] and val == "CHIL"]
            chil_ids = [lst.index("CHIL")] + chil_ids
            for n in range(len(chil_ids)):
                chil_ids[n] += 1
                chil_ids[n] = lst[chil_ids[n]]
            families.Children[idx] = chil_ids

    return families
