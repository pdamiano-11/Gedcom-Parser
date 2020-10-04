import sys
import copy
import numpy as np
import pandas as pd
sys.path.append("c:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\src")
sys.path.append("C:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\testFiles")
import Project02

#user03 checks to see if birth dates are before death dates.
def user03(gedcom_file):
    individuals = Project02.createIndividualsDataFrame(gedcom_file)
    indiv = copy.deepcopy(individuals[["Birthday", "Dead"]]) #makes a copy of original inviduals dataframe
    
    for index, row in indiv.iterrows(): #iterates through indiv 
        if type(row["Dead"]) == float and pd.isna(row["Dead"]):  #checks if the Dead row is empty
            pass
        else:
            if row["Birthday"] < row["Dead"]:    #if Death date is AFTER birth, it's valid
                print("Valid")
                print(row["Birthday"],row["Dead"] )
                
            else: 
                print("Invalid")                 #if Death date is BEFORE birth, it's invalid
                print( row["Birthday"],row["Dead"])
        


user03("testFiles/test6.ged")