'''
Created on 09/26/20
@author:   Michael McCreesh
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 1
'''
import sys
import os
import datetime
import pandas as pd
import Project02

''' Goal: Ensure all dates are before current date'''
def usecase01(gedcom_name):
    today = datetime.datetime.today()
    df = Project02.createIndividualsDataFrame(gedcom_name)
    df2 = Project02.createFamiliesDataFrame(gedcom_name)
    dateDict = []

    for index, row in df.iterrows(): #iterates through dataframe
        day = row['Birthday']
        dateDict.append(day)
    for index, row in df.iterrows(): #iterates through dataframe
        day = row['Dead']
        dateDict.append(day)
    for index, row in df2.iterrows(): #iterates through dataframe
        dateDict.append(row['Married'])
        '''
    for index, row in df2.iterrows(): #iterates through dataframe
       dateDict.append(row['Divorced'])
       '''
    for date in dateDict:
        if date == 'nan':
            continue
        else:
            day = pd.to_datetime(date)
            if day > today: return "There is at least one date later than the current date"
    return "All dates are before today"
if __name__ == '__main__':
    file_name = input("Enter the name of the GEDCOM file: ")
    usecase01(file_name)
