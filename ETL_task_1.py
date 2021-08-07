# -*- coding: utf-8 -*-
"""
Task 1: Produce a "people" file and save it as a CSV with a header
to the current directory. 

Created on Fri Jul 30 15:05:57 2021
 
"""

import pandas as pd
import os


# import CSV files as dataframes

cons = pd.read_csv('cons.csv')
ce = pd.read_csv('cons_email.csv')
cecs = pd.read_csv('cons_email_chapter_subscription.csv')


# inner join 3 dataframes on common columns
# filter joined frame to the rows where chapter_id = 1
# NOTE: takes modified_dt and create_dt_x from cons

df = pd.merge(cecs, ce, on='cons_email_id')
df = pd.merge(cons,df,on='cons_id')
df = df.loc[df.chapter_id == 1, :]


# select the series needed from the joined dataframe

created = df.loc[:, 'create_dt_x']
updated = df.loc[:, 'modified_dt']
code = df.loc[:, 'source']
email = df.loc[:, 'email']
is_unsub = df.loc[:, 'isunsub']


# concatenate the series to yield "people" 
# rename columns to match assignment conventions

people = pd.concat([email, code, is_unsub, created, updated], axis=1)
people = people.rename(columns={"create_dt_x": "created_dt", 
                                "modified_dt": "updated_dt", 
                                "source": "code", 
                                "isunsub": "is_unsub"})


# save "people" as a CSV in the working directory

cwd = os.getcwd()
path = cwd + "/people.csv"
people.to_csv(path)
