# -*- coding: utf-8 -*-
"""
Task 2: Use "people" to produce "acquisition_facts"
and save it to the current directory. 

Created on Fri Jul 30 18:15:25 2021

"""

import pandas as pd
import os


# import people.csv 

people = pd.read_csv('people.csv')


# transform series of datetimes into dates

dates = people.loc[:, 'updated_dt']
dates = pd.to_datetime(dates).dt.date


# calculate date frequencies and sort them by date

acquisition_facts = dates.value_counts().sort_index().to_frame()


# fix column names

acquisition_facts.index.name = "acquisition_date"
acquisition_facts = acquisition_facts.rename(columns = {'updated_dt':'acquisitions'})


# save to working directoy as acquisition_facts.csv

cwd = os.getcwd()
path = cwd + "/acquisition_facts.csv"
acquisition_facts.to_csv(path)