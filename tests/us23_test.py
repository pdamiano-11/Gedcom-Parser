# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:29:04 2020

@author: ptrda
"""
import os
os.chdir(os.path.dirname(os.path.abspath('../tests')))

import sys
sys.path.append(os.path.abspath('../Team-4-Code/src/UserStories'))
sys.path.append(os.path.abspath('../Team-4-Code/src'))

cwd = os.getcwd()
os.chdir(os.path.join(cwd, 'seeds'))

from us23 import us23
import Project02

import unittest



class us23_test(unittest.TestCase):
    def test1(self):
        individuals = Project02.createIndividualsDataFrame('seed.ged')
        df = individuals[0:3]
        df = df.append(individuals.iloc[0]).reset_index(drop = True)
        res = "not unique"
        self.assertEqual(us23(df), res)
        
    def test2(self):
        individuals = Project02.createIndividualsDataFrame('seed.ged')
        df = individuals[0:5]
        res = "unique"
        self.assertEqual(us23(df), res)
    
    def test3(self):
        individuals = Project02.createIndividualsDataFrame('seed.ged')
        df = individuals[0:7]
        df = df.append(individuals.iloc[3]).reset_index(drop = True)
        res = "not unique"
        self.assertEqual(us23(df), res)
        
    def test4(self):
        individuals = Project02.createIndividualsDataFrame('seed.ged')
        df = individuals[0:9]
        df = df.append(individuals.iloc[11]).reset_index(drop = True)
        res = "unique"
        self.assertEqual(us23(df), res)
        
    def test5(self):
        individuals = Project02.createIndividualsDataFrame('seed.ged')
        df = individuals[0:11]
        df = df.append(individuals.iloc[4]).reset_index(drop = True)
        res = "not unique"
        self.assertEqual(us23(df), res)

unittest.main(argv=['first-arg-is-ignored'], exit=False)