#sprint1 user stories 2 and 3
import sys
import os
import datetime 
import pandas as pd 
import unittest
#user story 2 checks if the marriage date is before the birth date
def user02(indiv_ID):
    index = individuals.index(indiv_ID)
    birthday = individuals.birth(index)
    index2 = families.index(indiv_ID)
    try:                                #checks to see if the person is married.
         families.Married(index2) 
    except NameError:
        return "not married"
    else:
        marr_date = families.married(index2)
    if marr_date > birthday:
        return "Error, birthday is after marriage."
    else: 
        return marr_date 

#User story 03 checks to see if the death date is before the birth date 
def user03(indiv_ID):
    index = individuals.index(indiv_ID)
    birthday = individuals.birth(index)
    if individuals.Dead[index]:             #checks to see if person is alive.
        death = individuals.Dead[index]
        pass
    else: 
        return "Is alive."
    if death > birthday :
        return "Error, death before birthday"
    else: 
        return death

#--------------Test Case for Use Case 02----------------
class usecase02_test(unittest.TestCase):
    
    def test1(self):
        individuals = pd.Dataframe({'ID': ['01', '02'], 'Name': ['Letty', 'Atticus'], 
        'Birthday': ['01 OCT 1945', '14 APR 1948']})
        families = pd.Dataframe({'ID': ['01', '02'], 'Name': ['Letty', 'Atticus'], Married: ['13 JUN 1970', '13 JUN 1970']})
        indiv_id = '01'
        result = '13 JUNE 1970'
        self.assertEquals(user02(indiv_id), result)

    def test2(self):
        individuals = pd.Dataframe({'ID': ['01', '02'], 'Name': ['Letty', 'Atticus'], 
        'Birthday': ['01 OCT 1945', '14 APR 1948']})
        families = pd.Dataframe({'ID': ['01', '02'], 'Name': ['Letty', 'Atticus'], Married: ['13 JUN 1970', '13 JUN 1970']})
        indiv_id = '02'
        result = "13 JUN 1970"
        assertTrue(user02(indiv_id), result)
    
    def test3(self):
        individuals = pd.Dataframe({'ID': ['01', '02', '03', '04'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald'], 
        'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977']})
        families = pd.Dataframe({'ID': ['01', '02', '03', '04'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald'], Married: ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
        indiv_id3 = '03'
        result = '5 MAY 2000'
        assertEquals(user02(indiv_id3), result)

    def test4(self):
        individuals = pd.Dataframe({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
        'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000']})
        families = pd.Dataframe({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], Married: ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
        indiv_id4 = '04'
        result = '5 MAY 2000'
        assertTrue(user02(indiv_id4), result)

    def test5(self):
        individuals = pd.Dataframe({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
        'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000']})
        families = pd.Dataframe({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], Married: ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
        indiv_id5 = '05'
        result = 'not married'
        assertTrue(case02(indiv_id5), result)
#---------------------Unit Test for User Case 03---------------------
    class usecase03_test(unittest.TestCase):
        def test1(self):
            individuals = pd.Dataframe({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
            'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000'], 'Death': [null, "5 SEPT 2012", "2 DEC 2017", null, null]})
            families = pd.Dataframe({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], Married: ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
            indiv_id1= '01'
            result = "Is alive."
            assertTrue(case03(indiv_id1), result)
        def test2(self):
            individuals = pd.Dataframe({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
            'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000'], 'Death': [null, "5 SEPT 2012", "2 DEC 2017", null, null]})
            families = pd.Dataframe({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], Married: ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
            indiv_id2 = '02'
            result = "5 SEPT 2012"
            assertTrue(case03(indiv_id2), result)
        def test3(self):
            individuals = pd.Dataframe({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
            'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000'], 'Death': [null, "5 SEPT 2012", "2 DEC 2017", null, null]})
            families = pd.Dataframe({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], Married: ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
            indiv_id3 = '03'
            result = '2 DEC 2017'
            assertTrue(case03(indiv_id3), result)
        def test4(self):
            individuals = pd.Dataframe({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
            'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000'], 'Death': [null, "5 SEPT 2012", "2 DEC 2017", null, null]})
            families = pd.Dataframe({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], Married: ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
            indiv_id4 = '04'
            result = 'Is alive.'
            assertTrue(case03(indiv_id4), result)

        def test5(self):
            individuals = pd.Dataframe({'ID': ['01', '02', '03', '04', '05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', "Rob"], 
            'Birthday': ['01 OCT 1945', '14 APR 1948', '3 SEPT 1977', '20 JAN 1977', '22 JUL 2000'], 'Death': [null, "5 SEPT 2012", "2 DEC 2017", null, null]})
            families = pd.Dataframe({'ID': ['01', '02', '03', '04','05'], 'Name': ['Letty', 'Atticus', 'Ruby', 'Donald', 'Rob'], Married: ['13 JUN 1970', '13 JUN 1970', '5 MAY 2000', '5 MAY 2000']})
            indiv_id5 = '05'
            result = 'Is alive.'
            assertTrue(case03(indiv_id5), result)

    






        

