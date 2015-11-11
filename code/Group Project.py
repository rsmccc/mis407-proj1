# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 09:48:07 2015

@author: mfisher
"""
import pandas as pd

fn1 = 'C:\\Users\\mfisher\\Desktop\\candidate-list-2016.xlsx'
fn2 = 'C:\\Users\\mfisher\\Desktop\\candidate-list-2012.xlsx'

df1 = pd.read_excel(fn1, sheetname='candidate-list-2016', index_col='cand_nm')
df2 = pd.read_excel(fn2, sheetname='candidate-list-2012', index_col='cand_nm')

print (df1)
print (df2)

"""2016"""
print ("Year 2016")
amtByParty=df1['contb_receipt_amt'].groupby(df1['cand_pty_aff'])
print(amtByParty.mean())

indContribByParty=df1['ind_contrib'].groupby(df1['cand_pty_aff'])
print(indContribByParty.mean())

amtByCand=df1['contb_receipt_amt'].groupby(df1['cand_nm_title'])
print(amtByCand.mean())

"""2012"""
print ("Year 2012")
amtByParty=df2['contb_receipt_amt'].groupby(df2['cand_pty_aff'])
print(amtByParty.mean())

indContribByParty=df2['ind_contrib'].groupby(df2['cand_pty_aff'])
print(indContribByParty.mean())

amtByCand=df2['contb_receipt_amt'].groupby(df2['cand_nm_title'])
print(amtByCand.mean())