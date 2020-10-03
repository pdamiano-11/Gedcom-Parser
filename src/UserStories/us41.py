'''
Created on 09/26/20
@author:   @arana23 - Aparajita Rana
Pledge:    I pledge my honor to abide by the Stevens Honor System

SSW555 - Sprint 1
'''
import sys
import os
import datetime

''' Goal: Include partial dates - accept and use dates without days or without days and months '''
def us41(date):
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