import sys
import copy
import numpy as np
import pandas as pd
sys.path.append("c:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\src")
sys.path.append("C:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\testFiles")
import Project02

def user03(gedcom_file):
    individuals = Project02.createIndividualsDataFrame(gedcom_file)
    indiv = copy.deepcopy(individuals[["Birthday", "Dead"]])
    
    for index, row in indiv.iterrows():
        if type(row["Dead"]) == float and pd.isna(row["Dead"]):
            pass
        else:
            if row["Birthday"] < row["Dead"]:
                print("Valid")
                print(row["Birthday"],row["Dead"] )
                
            else: 
                print("Invalid")
                print( row["Birthday"],row["Dead"])
        


user03("testFiles/test6.ged")