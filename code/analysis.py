# -*- coding: utf-8 -*-
"""
Created on Mon Nov 04 22:12:21 2015

@authors: Riley McCloskey, Michael Tuttle, Will Smith, Miranda Fisher
"""

#import requests
import pandas as pd
import numpy as np

#campaign = pd.read_csv('../data/2009_Campaign_Contributions.csv')
candidate = pd.read_csv('../data/2012_Candidate_Summary.csv')
#committee = pd.read_csv('../data/2012_Committee_Summary.csv')

sharedCols = ['tot_rec', 'tot_dis', 'cas_on_han_clo_of_per']

candCols = ['can_nam', 'deb_owe_by_com', 'can_off', 'can_par_aff']
commCols = ['com_nam']

# how to combine arrays?

cd = candidate[candCols + sharedCols]


print ('\nColumn Names')
for col in cd.columns:
  print (col)

