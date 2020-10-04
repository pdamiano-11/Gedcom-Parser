'''
@author: Michael McCreesh

User Story #01: Less then 150 years old

Death should be less than 150 years after birth for 
dead people, and current date should be less than 
150 years after birth for all living people
'''

import sys
import os
import datetime

def us01(date):
    today = datetime.datetime.now()
    if date.year > today.year:
        return 'This date is after current date.'
    elif date.year == today.year and date.month > today.month:
        return 'This date is after current date.'
    elif date.year == today.year and date.month == today.month and date.day > today.day:
        return 'This date is after current date.'
    return 'This date is valid'

