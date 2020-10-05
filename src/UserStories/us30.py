''' Author:     Samantha Inneo
    Sprint:     Sprint 1
    User Story: List all living married people in a GEDCOM file
    '''
import datetime
import unittest

import sys
sys.path.append("c:\\Users\\Stevens User\\555_Team_4\\Team-4-Code\\src")
import Project02
import pandas as pd


def listLivingMarried(gedcom_name):
    # iterate through dataframe and check if current individual is married
    # if not, continute to next individual
    # if they are, check if they are alive
    #if they are, add to list
    # if not, continue
    #return list
    living_married = []
    individuals = Project02.createIndividualsDataFrame(gedcom_name)
    for ind, row in individuals.iterrows():
        if(type(row['Spouse']) == float and pd.isna(row['Spouse'])):
            pass
        elif (individuals['Alive'][ind] == 'True'):
            living_married.append(individuals['Name'][ind])
            # print(individuals['Name'][ind])
    return living_married
            
# # listLivingMarried("testing.ged")
# '''testing'''
# class Inneo_Tests_HW4(unittest.TestCase):
#     def test1(self):
#         filename = "testing.ged" 
#         ret = ['John Smith', 'Susan Jones', 'Frank Jones', 'Emily Michaels', 'Bernard Smith', 'Theresa Kelly', 'Kevin Brown', 'Diane Brown']
#         self.assertEqual(listLivingMarried(filename),ret)


# if __name__ == '__main__':
#         unittest.main() 