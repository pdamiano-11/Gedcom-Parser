'''
Created on 09/28/20
@author:   @arana23 - Aparajita Rana
Pledge:    I pledge my honor to abide by the Stevens Honor System

SSW555 - Sprint 1
'''
import sys
import os
import datetime

''' Goal: Reject illegitimate dates - all dates should be legitimate dates for the months specified '''
def us42(date):
    try:
        datetime.datetime.strptime(date, '%d %b %Y')
    # valueError -> strptime did not create valid result
    except ValueError:
        return 'invalid'
    return date