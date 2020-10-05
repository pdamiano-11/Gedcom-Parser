'''
Author:     Samantha Inneo
Sprint:     Sprint 1
Use Case:   Birth dates of siblings should be more than 8 months apart or less than 2 days apart 
            (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
'''
import sys
sys.path.append("c:\\Users\\Stevens User\\555_Team_4\\Team-4-Code\\src")
import Project02
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
    children = copy.deepcopy(families["Children"])
    print(children)
    #for index, row in children.iterrows():
        #indiv = copy.deepcopy(individuals[["Name", "Birthday", "Dead"]])
        

siblingsAgeGap("testing.ged")        



       