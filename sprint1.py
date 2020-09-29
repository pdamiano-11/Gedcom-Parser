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
                else 
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
       gedcome_file = Grace_Miguel_famtree
       result = 
        self.assertEquals(user02(gedcome_file, result)

    def test2(self):
        individuals = pd.DataFrame({'ID': ['01', '02'], 'Name': ['Letty', 'Atticus'], 
        'Birthday': ['01 OCT 1945', '14 APR 1948']})
        families = pd.DataFrame({'ID': ['01', '02'], 'Name': ['Letty', 'Atticus'], 'Married': ['13 JUN 1970', '13 JUN 1970']})
        indiv_id = '02'
        result = "13 JUN 1970"
        self.assertTrue(user02(indiv_id), result)
    
    def test3(self):
        individuals = pd.DataFrame({'ID': ['01', '02', '03', '04'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald'], 
        'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977']})
        families = pd.DataFrame({'ID': ['01', '02', '03', '04'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald'], 'Married': ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
        indiv_id3 = '03'
        result = '5 MAY 2000'
        self.assertEquals(user02(indiv_id3), result)

    def test4(self):
        individuals = pd.DataFrame({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
        'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000']})
        families = pd.DataFrame({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], 'Married': ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
        indiv_id4 = '04'
        result = '5 MAY 2000'
        self.assertTrue(user02(indiv_id4), result)

    def test5(self):
        individuals = pd.DataFrame({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
        'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000']})
        families = pd.DataFrame({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], 'Married': ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
        indiv_id5 = '05'
        result = 'not married'
        self.assertTrue(case02(indiv_id5), result)
#---------------------Unit Test for User Case 03---------------------
    class usecase03_test(unittest.TestCase):
        def test1(self):
            individuals = pd.DataFrame({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
            'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000'], 'Death': [None, "5 SEPT 2012", "2 DEC 2017", None, None]})
            families = pd.DataFrame({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], 'Married': ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
            indiv_id1= '01'
            result = "Is alive."
            self.assertTrue(case03(indiv_id1), result)
        def test2(self):
            individuals = pd.DataFrame({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
            'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000'], 'Death': [None, "5 SEPT 2012", "2 DEC 2017", None, None]})
            families = pd.DataFrame({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], 'Married': ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
            indiv_id2 = '02'
            result = "5 SEPT 2012"
            self.assertTrue(case03(indiv_id2), result)
        def test3(self):
            individuals = pd.DataFrame({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
            'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000'], 'Death': [None, "5 SEPT 2012", "2 DEC 2017", None, None]})
            families = pd.DataFrame({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], 'Married': ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
            indiv_id3 = '03'
            result = '2 DEC 2017'
            self.assertTrue(case03(indiv_id3), result)
        def test4(self):
            individuals = pd.DataFrame({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
            'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000'], 'Death': [None, "5 SEPT 2012", "2 DEC 2017", None, None]})
            families = pd.DataFrame({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], 'Married': ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
            indiv_id4 = '04'
            result = 'Is alive.'
            self.assertTrue(case03(indiv_id4), result)

        def test5(self):
            individuals = pd.DataFrame({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
            'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000'], 'Death': ["", "5 SEPT 2012", "2 DEC 2017", "", ""]})
            families = pd.DataFrame({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], 'Married': ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
            indiv_id5 = '05'
            result = 'Is alive.'
            self.assertTrue(case03(indiv_id5), result)
unittest.main()

    






        

