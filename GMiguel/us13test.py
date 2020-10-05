'''
Author:     Samantha Inneo
Sprint:     Sprint 1
Use Case:   Birth dates of siblings should be more than 8 months apart or less than 2 days apart 
            (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
'''
import sys
import copy
sys.path.append("C:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\src")
import Project02
sys.path.append("C:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\seeds")
import pandas as pd
import datetime

def siblingsAgeGap(gedcom_name):
    # I need to gather all the siblings of each family
    # check if their birthdays are more than 8 months apart
    # check if their birthdays are less than 2 days apart
    #return true if they are valid, false if they are not
    eight_months = 240
    two_days = 2

    individuals = Project02.createIndividualsDataFrame(gedcom_name)
    families = Project02.createFamiliesDataFrame(gedcom_name)

    child = []
    children = copy.deepcopy(families[["Children"]])
    indi = copy.deepcopy(individuals[["ID", "Birthday"]])
    for index, row in children.iterrows():
        #indiv = copy.deepcopy(individuals[["Name", "Birthday", "Dead"]])
        if len(row["Children"]) > 1:
            for i in row["Children"]:
                lst = row["Children"]
                for j in lst:
                    for k, rows in indi.iterrows():
                        if lst[j] == rows[individuals["ID"]]:
                            child.append(rows[individuals["Birthday"]])
                for m in range(len(child)):
                    child2 = child[:m] + child[m:]
                    for l in range(len(child2)):
                        if  ((pd.to_datetime(child[k]) - pd.to_datetime(child2[l]))  > two_days) and  ((pd.to_datetime(child[k]) - pd.to_datetime(child[l])) < eight_months ):
                            print("invalid: sibling birthdays")
            

siblingsAgeGap("seeds/seed.ged")   