'''
Author: Grace Miguel
I pledge my honor that I've abided by the the Stevens Honor Code.
'''
import sys
import os
sys.path.append(os.path.abspath('../src/UserStories'))
    #"c:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\src")
sys.path.append(os.path.abspath('../src/seeds'))
    #"C:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\seeds")
import pandas as pd 
import Project02
from datetime import datetime
import copy

#this function is to determine if the marriage date is after the birth date
def user02(gedcom_file):
    individuals = Project02.createIndividualsDataFrame(gedcom_file)
    families = Project02.createFamiliesDataFrame(gedcom_file)
    indiv = copy.deepcopy(individuals[["Name", "Birthday"]]) #makes a copy of original inviduals dataframe
    fam = copy.deepcopy(families[["Wife Name", "Husband Name", "Married"]])
    lst = []
    for i, row in indiv.iterrows():
        for k, rows in fam.iterrows():
            if row["Name"] == rows["Wife Name"]:
                if type(rows["Married"]) == float and pd.isna(rows["Married"]):
                    pass
                elif pd.to_datetime(row["Birthday"]) < pd.to_datetime(rows["Married"]):
                    pass
                else: 
                    lst.append(row["Wife Name"])
        
            if row["Name"] == rows["Husband Name"]:
                if type(rows["Married"]) == float and pd.isna(rows["Married"]):
                    pass
                elif pd.to_datetime(row["Birthday"]) < pd.to_datetime(rows["Married"]):
                    pass
                else: 
                    lst.append(row["Husband Name"])
        
    if len(lst) > 0:
        return "The following people have births after marriage" + str(lst)
    else: 
        return ""
            
            



