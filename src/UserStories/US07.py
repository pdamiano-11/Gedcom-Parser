'''
Created on 09/26/20
@author:   Michael McCreesh
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 1
'''
import datetime
import pandas as pd
import project02
from dateutil.relativedelta import relativedelta

''' Goal: Ensure that no individuals live more than 150 years'''
def usecase07(gedcom_name):
    today = datetime.datetime.today()
    df = project02.createIndividualsDataFrame(gedcom_name)
    for index, row in df.iterrows(): #iterates through dataframe
        birth = pd.to_datetime(row['Birthday'])
        if row['Dead'] == 'nan':
            death = today
        else:
            death = pd.to_datetime(row['Dead'])
        dif = death.year - birth.year
        if death.month < birth.month or (death.month == birth.month and death.day < birth.day):
            dif -= 1
        if dif >= 150:
            return "At least one individual lived to be over 150"
    return "All ages are less than 150"
if __name__ == '__main__':
    file_name = input("Enter the name of the GEDCOM file: ")
    usecase07(file_name)