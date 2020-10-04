import sys
sys.path.append("c:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\src")
sys.path.append("C:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\testFiles")
import pandas as pd 
import Project02
from datetime import datetime
import copy

#this function is to determine if the marriage date is after the birth date
def user02(gedcom_file):
    individuals = Project02.createIndividualsDataFrame(gedcom_file)
    families = Project02.createFamiliesDataFrame(gedcom_file)
    indiv = copy.deepcopy(individuals[["Name", "Birthday"]]) #makes a copy of original inviduals dataframe
    print(indiv)
    fam = copy.deepcopy(families[["Wife Name", "Husband Name", "Married"]])
    print(fam)
    
    for i, row in indiv.iterrows():
        for k, rows in fam.iterrows():
            if row["Name"] == rows["Wife Name"] or row["Name"] == rows["Husband Name"]:
                if type(rows["Married"]) == float and pd.isna(rows["Married"]):
                    print("no marriage date")
                elif row["Birthday"] < rows["Married"]:
                    print("Valid")
                else: 
                    print("Invalid")
            
        #for k, row in fam.iterrows():


user02("testFiles/test6.ged")

