import sys
import copy
import numpy as np
import pandas as pd
import datetime
sys.path.append("c:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\src")
sys.path.append("C:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\seeds")
import Project02

#user03 checks to see if birth dates are before death dates.
def user03(gedcom_file):
    individuals = Project02.createIndividualsDataFrame(gedcom_file)
    indiv = copy.deepcopy(individuals[["Name", "Birthday", "Dead"]]) #makes a copy of original inviduals dataframe
    lst = ""

    for index, row in indiv.iterrows(): #iterates through indiv 
        if type(row["Dead"]) == float and pd.isna(row["Dead"]):  #checks if the Dead row is empty
            pass
        else:
            if pd.to_datetime(row["Birthday"]) < pd.to_datetime(row["Dead"]):    #if Death date is AFTER birth, it's valid
                pass
            else:
                lst = lst + row["Name"] + " "
                                #if Death date is BEFORE birth, it's invalid
    if len(lst) >0:
        return "The following have deaths before birth which is incorrect: " + str(lst)
    else:
        return ""



