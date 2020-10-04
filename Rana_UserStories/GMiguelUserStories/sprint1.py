'''
Created on 09/26/20
@author:   @arana23 - Aparajita Rana
Pledge:    I pledge my honor to abide by the Stevens Honor System

SSW555 - Sprint 1
'''
import sys
import os
import datetime
import unittest

''' Goal: Include partial dates - accept and use dates without days or without days and months '''
def usecase41(date):
    split_date=date.split(" ")
    # correct date structure -> return given
    if len(split_date)==3:
        return date
    # missing days -> return with default 01 day using literal string interpolation
    elif len(split_date)==2:
        return f'01 {split_date[0]} {split_date[1]}'
    # missing days and month -> return with default 01 day and JAN month 
    elif len(split_date)==1:
        return f'01 JAN {split_date[0]}'
    # wrong input
    else:
        return 'invalid'

''' Goal: Reject illegitimate dates - all dates should be legitimate dates for the months specified '''
def usecase42(date):
    try:
        datetime.datetime.strptime(date, '%d %b %Y')
    # valueError -> strptime did not create valid result
    except ValueError:
        return 'invalid'
    return date

# ----------------------------------- Test Cases for Use Case 41 -----------------------------------
class usecase41_test(unittest.TestCase):
    def test1(self):
        val = "SEPT 2020"
        val2 = "01 SEPT 2020"
        self.assertEqual(usecase41(val),val2)

    def test2(self):
            val = "2020"
            val2 = "01 JAN 2020"
            self.assertEqual(usecase41(val),val2)

    def test3(self):
            val = "26 SEPT 2020"
            val2 = "26 SEPT 2020"
            self.assertEqual(usecase41(val),val2)

    def test4(self):
            val = "26 SEPT 2020 20"
            val2 = "invalid"
            self.assertEqual(usecase41(val),val2)

    def test5(self):
            val = "26 SEPT OK 2020"
            val2 = "invalid"
            self.assertEqual(usecase41(val),val2)

unittest.main()