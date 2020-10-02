'''
Created on 09/26/20
@author:   Michael McCreesh
Pledge:    I pledge my honor to abide by the Stevens Honor System
SSW555 - Sprint 1
'''
import sys
import os
import datetime
import unittest

''' Goal: Ensure all dates are before current date - returns true if the date is before and false if the date is after'''
def usecase01(date):
    today = datetime.datetime.now()
    if date.year > today.year:
        return 'This date is after current date.'
    elif date.year == today.year and date.month > today.month:
        return 'This date is after current date.'
    elif date.year == today.year and date.month == today.month and date.day > today.day:
        return 'This date is after current date.'
    return 'This date is valid'

''' Goal: Ensure that death is less than 150 years after birth '''
def usecase07(date):
    return date

# ----------------------------------- Test Cases for Use Case 41 -----------------------------------
class usecase01_test(unittest.TestCase):
    def test1(self):
        val = datetime.datetime(2020, 9, 25)
        self.assertEqual(usecase01(val),'This date is valid')

    def test2(self):
            val = datetime.datetime(1999, 12, 29)
            self.assertEqual(usecase01(val),'This date is valid')

    def test3(self):
            val = datetime.datetime(1800, 3, 15)
            self.assertEqual(usecase01(val),'This date is valid')

    def test4(self):
            val = datetime.datetime(2021, 9, 26)
            self.assertEqual(usecase01(val),'This date is after current date.')

    def test5(self):
            val = datetime.datetime(3000, 9, 26)
            self.assertEqual(usecase01(val),'This date is after current date.')

unittest.main() 
