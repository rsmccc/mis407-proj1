# -*- coding: utf-8 -*-
"""
Created on Mon Nov 04 22:12:21 2015

@authors: Riley McCloskey, Michael Tuttle, Will Smith, Miranda Fisher
"""

import requests
import pandas as pd
import xlrd

wb = xlrd.open_workbook('../data/SuperstoreSales.xlsx')

df = pd.read_excel(wb, sheetname='Orders', index_col='Order Date', engine='xlrd')