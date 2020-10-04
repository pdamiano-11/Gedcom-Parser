#sprint1 user stories 2 and 3
import sys
import os
import datetime 
import pandas as pd 
import unittest
import Project02 
#user story 2 checks if the marriage date is after the birth date

def user02(gedcome_file):
    individuals = Project02.CreateIndividualsDataFrame(gedcom_file) #retrieves individuals DataFrame
    families = Project02.CreateFamiliesDataFrame(gedcom_file)       #retrieves Families DataFrame

    couple = []
    indiv = []
    for index, row in families.iterrows(): #iterates through DataFrame
        couple.append(
            couple_info = [families["Husband ID"], families["Wife ID"], families["Married"]])   #creates a list of lists for each family with IDs and marriage dates

    for index, row in individuals.iterrows():
        indiv.append(                                           #creates a list of lists of individuals with birthdays
            indiv_info = [individuals.ID, individuals["Birthday"]]
        )
    
    for k in couple:                    #iterates through couple list to check if IDs match with those in indiv list and checks if birth is before marriage
        for m in indiv:
            if couple[k][0] == indiv[m][0]:
                if couple[k][2]> indiv[m][1]:
                    return "Marriage after birth"
                else: 
                    return "Error, marriange before birth"
            if couple[k][1]==indiv[m][0]:
                if couple[k][2]> indiv[m][1]:
                    return "Marriage after birth"
                else:
                    return "Error, marriage before birth"
    for i in couple: 
        ID = couple["Husband ID"][i]
        marr_date = couple["Married"][i]
        for k in indivs:
            if indivs["ID"][k]== ID:
                if indivs["Birthday"][k] > marr_date:
                    print('Error ' + ID + " birth is before marriage")
                else: 
                    print('Correct, marriage after birth')

#User story 03 checks to see if the death date is before the birth date 
def user03(gedcom_file):
    individuals = Project02.CreateIndividualsDataFrame(gedcom_file) #retrieves individuals DataFrame
    families = Project02.CreateFamiliesDataFrame(gedcom_file)       #retrieves Families DataFrame
    indiv = []
   
    for index, row in individuals.iterrows():
        if individuals["Birthday"]< individuals["Death"]:
            print("Error, Death before Birth")
        else:
            print(individuals["Death"])

#--------------Test Case for Use Case 02----------------
class usecase02_test(unittest.TestCase):
    
    def test1(self):
       gedcome_file = Grace_Miguel_famtree.ged
       result = "Marriage after birth."
       self.assertEquals(user02(gedcome_file, result))


    def test2(self):
        gedcome_file = seed.ged
        result = "Marriage after birth."
        self.assertTrue(user02(gedcome_file), result)
    

    def test3(self):
        gedcome_file = disney_fam.ged
        result = 'Marriage after birth.'
        self.assertEquals(user02(gedcome_file), result)

    def test4(self):
        gedcome_file = export-BloodTree.ged
        result = 'Marriage after birth.'
        self.assertTrue(user02(gedcome_file), result)

    def test5(self):
        gedcome_file = doe.ged
        result = 'Marriage after birth.'
        self.assertTrue(case02(gedcome_file), result)
unittest.main()

    






        

