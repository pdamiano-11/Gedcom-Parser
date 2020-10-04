import sys
sys.path.append("c:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\src")
sys.path.append("C:\\Users\\Stevens User\\Documents\\GitHub\\Team-4-Code\\testFiles")
import pandas as pd 
import Project02
import datetime
import copy

def user02(gedcom_file):
    individuals = Project02.createIndividualsDataFrame(gedcom_file)
    families = Project02.createFamiliesDataFrame(gedcom_file)
    indi = pd.DataFrame(columns = [individuals.ID, individuals.Birthday])
    fam = pd.DataFrame(columns = [families.ID, families.Married])
    if(indiv)

    print(df)

user02("testFiles/test1.ged")
