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

    indiv_list = pd.DataFrame(columns = [individuals.Name, individuals.Birthday])
    fam_list = pd.DataFrame(columns = [families["Wife Name"], families["Husband Name"], families.Married])
    '''

    for i, row in indiv_list.iterrows():
        for k, row in fam_list.iterrows():
            if indiv_list[individuals.Name][i]== fam_list[families["Wife Name"]][k] or indiv_list[individuals.Name][i]==fam_list[families["Husband Name"]][k]:
                if indiv_list[individuals.Birthday][i] == fam_list[families.Married]:
                    return True
                else:
                    return False


    '''
 

    print(fam_list)


user02("testFiles/test3.ged")

