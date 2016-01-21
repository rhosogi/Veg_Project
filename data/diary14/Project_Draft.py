# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:45:03 2015

@author: reneehosogi
"""

# Read in packages

import pandas as pd
import numpy as np
import operator as o
import matplotlib.pylab as plt
import matplotlib.cm as cm

# This will be how I combine quarterly data compiled by CE surveys
# In Terminal, combine all four FMLD .csv files 

# Renees-MacBook-Pro:diary14 reneehosogi    
# Renees-MacBook-Pro:diary13 reneehosogi$ cat < fmld131.csv <(tail +3 fmld132.csv) <(tail +3 fmld133.csv) <(tail +3 fmld134.csv) > veg13.csv
# Renees-MacBook-Pro:diary12 reneehosogi$ cat < fmld121.csv <(tail +3 fmld122.csv) <(tail +3 fmld123.csv) <(tail +3 fmld124.csv) > veg12.csv
# Renees-MacBook-Pro:diary11 reneehosogi$ cat < fmld111.csv <(tail +3 fmld112.csv) <(tail +3 fmld113.csv) <(tail +3 fmld114.csv) > veg11.csv
# Renees-MacBook-Pro:diary10 reneehosogi$ cat < fmld101.csv <(tail +3 fmld102.csv) <(tail +3 fmld103.csv) <(tail +3 fmld104.csv) > veg10.csv

# Create dataframe

veg14 = pd.read_table('/Users/reneehosogi/Documents/GitHub_Clones/Veg_Project/diaries10-14/veg14.csv', sep=',')
veg13 = pd.read_table('/Users/reneehosogi/Documents/GitHub_Clones/Veg_Project/diaries10-14/veg13.csv', sep=',')
veg12 = pd.read_table('/Users/reneehosogi/Documents/GitHub_Clones/Veg_Project/diaries10-14/veg12.csv', sep=',')
veg11 = pd.read_table('/Users/reneehosogi/Documents/GitHub_Clones/Veg_Project/diaries10-14/veg11.csv', sep=',')
veg10 = pd.read_table('/Users/reneehosogi/Documents/GitHub_Clones/Veg_Project/diaries10-14/veg10.csv', sep=',')
low_memory=False

# Test the read-in
veg12.head()
veg14.tail()
veg14.describe()
veg13.index
veg12.dtypes
veg14.shape
veg11.PROD_UNIT.mean()
veg11.FOODTOT.describe()
veg10.BEEF.value_counts()

# Check for missing data

veg14.FOODTOT.isnull().sum()
veg13.FOODTOT.isnull().sum()
veg12.FOODTOT.isnull().sum()
veg11.FOODTOT.isnull().sum()
veg10.FOODTOT.isnull().sum()

# Parameters for graphs 

plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 12

# Scatter plots for meats individually 

my_cols = ['FAM_SIZE', 'AGE_REF', 'FOODTOT', 'FOODHOME', 'CEREAL', 'BAKEPROD', 'BEEF', 'PORK', 'OTHMEAT', 'POULTRY', 'SEAFOOD', 'EGGS', 'MILKPROD', 'OTHDAIRY', 'FRSHFRUT', 'FRSHVEG', 'PROCFRUT', 'PROCVEG','SWEETS','NONALBEV', 'OILS', 'MISCFOOD', 'FOODAWAY']
veg.plot(kind='scatter', x='AGE_REF', y='BEEF')
veg.plot(kind='scatter', x='AGE_REF', y='POULTRY')
veg.plot(kind='scatter', x='AGE_REF', y='PORK')

# Converting obj into int 

veg11.PORK.describe()

veg12['BEEF']=veg12.BEEF.factorize()[0]
veg12['PORK']=veg12.PORK.factorize()[0]
veg12['POULTRY']=veg12.POULTRY.factorize()[0]
veg12['OTHMEAT']=veg12.OTHMEAT.factorize()[0]
veg12['SEAFOOD']=veg12.SEAFOOD.factorize()[0]

veg12['FRSHFRUT']=veg12.FRSHFRUT.factorize()[0]
veg12['FRSHVEG']=veg12.FRSHVEG.factorize()[0]
veg12['PROCFRUT']=veg12.PROCFRUT.factorize()[0]
veg12['PROCVEG']=veg12.PROCVEG.factorize()[0]

veg11['BEEF']=veg11.BEEF.factorize()[0]
veg11['PORK']=veg11.PORK.factorize()[0]
veg11['POULTRY']=veg11.POULTRY.factorize()[0]
veg11['OTHMEAT']=veg11.OTHMEAT.factorize()[0]
veg11['SEAFOOD']=veg11.SEAFOOD.factorize()[0]

veg11['FRSHFRUT']=veg11.FRSHFRUT.factorize()[0]
veg11['FRSHVEG']=veg11.FRSHVEG.factorize()[0]
veg11['PROCFRUT']=veg11.PROCFRUT.factorize()[0]
veg11['PROCVEG']=veg11.PROCVEG.factorize()[0]

veg10['BEEF']=veg10.BEEF.factorize()[0]
veg10['PORK']=veg10.PORK.factorize()[0]
veg10['POULTRY']=veg10.POULTRY.factorize()[0]
veg10['OTHMEAT']=veg10.OTHMEAT.factorize()[0]
veg10['SEAFOOD']=veg10.SEAFOOD.factorize()[0]

veg10['FRSHFRUT']=veg10.FRSHFRUT.factorize()[0]
veg10['FRSHVEG']=veg10.FRSHVEG.factorize()[0]
veg10['PROCFRUT']=veg10.PROCFRUT.factorize()[0]
veg10['PROCVEG']=veg10.PROCVEG.factorize()[0]

# New columns for meat and produce numbers

veg14['MEAT']=veg14.BEEF + veg14.POULTRY + veg14.PORK + veg14.SEAFOOD + veg14.OTHMEAT
veg14['PRODUCE']= veg14.FRSHFRUT + veg14.FRSHVEG + veg14.PROCFRUT + veg14.PROCVEG 
veg14['MEAT_UNIT']= (veg14.BEEF/5.71) + (veg14.POULTRY/2.04) + (veg14.PORK/3.83) + veg14.SEAFOOD + (veg14.OTHMEAT/3.01)
veg14['PROD_UNIT']= (veg14.FRSHFRUT/1.49) + (veg14.FRSHVEG/1.57) + (veg14.PROCFRUT/2.53) +(veg14.PROCVEG/1.47)

veg13['MEAT']=veg13.BEEF + veg13.POULTRY + veg13.PORK + veg13.SEAFOOD + veg13.OTHMEAT
veg13['PRODUCE']= veg13.FRSHFRUT + veg13.FRSHVEG + veg13.PROCFRUT + veg13.PROCVEG 
veg13['MEAT_UNIT']= (veg13.BEEF/4.76) + (veg13.POULTRY/2.02) + (veg13.PORK/3.43) + veg13.SEAFOOD + (veg13.OTHMEAT/3.05)
veg13['PROD_UNIT']= (veg13.FRSHFRUT/1.29) + (veg13.FRSHVEG/1.49) + (veg13.PROCFRUT/2.51) +(veg13.PROCVEG/1.42)

veg12['MEAT']=veg12.BEEF + veg12.POULTRY + veg12.PORK + veg12.SEAFOOD + veg12.OTHMEAT
veg12['PRODUCE']= veg12.FRSHFRUT + veg12.FRSHVEG + veg12.PROCFRUT + veg12.PROCVEG 
veg12['MEAT_UNIT']= (veg12.BEEF/4.57) + (veg12.POULTRY/1.97) + (veg12.PORK/3.37) + veg12.SEAFOOD + (veg12.OTHMEAT/2.92)
veg12['PROD_UNIT']= (veg12.FRSHFRUT/1.34) + (veg12.FRSHVEG/1.42) + (veg12.PROCFRUT/2.66) + (veg12.PROCVEG/1.44)

veg11['MEAT']=veg11.BEEF + veg11.POULTRY + veg11.PORK + veg11.SEAFOOD + veg11.OTHMEAT
veg11['PRODUCE']= veg11.FRSHFRUT + veg11.FRSHVEG + veg11.PROCFRUT + veg11.PROCVEG 
veg11['MEAT_UNIT']= (veg11.BEEF/4.34) + (veg11.POULTRY/1.89) + (veg11.PORK/3.35) + veg11.SEAFOOD + (veg11.OTHMEAT/3.15)
veg11['PROD_UNIT']= (veg11.FRSHFRUT/1.33) + (veg11.FRSHVEG/1.58) + (veg11.PROCFRUT/2.76) + (veg11.PROCVEG/1.42)

veg10['MEAT']=veg10.BEEF + veg10.POULTRY + veg10.PORK + veg10.SEAFOOD + veg10.OTHMEAT
veg10['PRODUCE']= veg10.FRSHFRUT + veg10.FRSHVEG + veg10.PROCFRUT + veg10.PROCVEG 
veg10['MEAT_UNIT']= (veg10.BEEF/5.26) + (veg10.POULTRY/1.96) + (veg10.PORK/3.10) + veg10.SEAFOOD + (veg10.OTHMEAT/3.22)
veg10['PROD_UNIT']= (veg10.FRSHFRUT/1.32) + (veg10.FRSHVEG/1.15) + (veg10.PROCFRUT/2.47) +(veg10.PROCVEG/1.33)


veg10.PROD_UNIT.describe()
veg12.MEAT.describe()
veg11.MEAT.describe()
veg13.MEAT_UNIT.describe()
veg11.BEEF.describe()

# Read in columns to work with closer
feature_cols = ['veg14.MEAT_UNIT', 'veg14.PROD_UNIT', 'veg13.MEAT_UNIT', 'veg13.PROD_UNIT''veg12.MEAT_UNIT', 'veg12.PROD_UNIT', 'veg11.MEAT_UNIT', 'veg11.PROD_UNIT', 'veg10.MEAT_UNIT', 'veg10.PROD_UNIT']
age_cols= ['veg14.AGE','veg13.AGE','veg12.AGE','veg11.AGE','veg10.AGE']
fam_cols = ['veg14.FAM_SIZE', 'veg13.FAM_SIZE', 'veg12.FAM_SIZE', 'veg11.FAM_SIZE', 'veg10.FAM_SIZE']
reg_cols = ['veg14.REGION', 'veg13.REGION', 'veg12.REGION', 'veg11.REGION', 'veg10.REGION']
meatveg = feature_cols + age_cols + reg_cols + fam_cols

veg14_url = '/Users/reneehosogi/Documents/GitHub_Clones/Veg_Project/diaries10-14/veg14.csv'
veg14_cols = ['veg14.BEEF', 'veg14.POULTRY', 'veg14.PORK', 'veg14.SEAFOOD', 'veg14.OTHMEAT', 'veg14.FRSHFRUT', 'veg14.FRSHVEG', 'veg14.PROCFRUT', 'veg14.PROCVEG', 'veg14.MEAT_UNIT', 'veg14.PROD_UNIT', 'veg14.AGE', 'veg14.FAM_SIZE', 'veg14.REGION']
veg14 = pd.read_table(veg14_url, names=veg14_cols)

veg14['MEAT_UNIT']=veg14.MEAT_UNIT.factorize()[0]

meatveg = pd.merge (veg14, veg13, veg12, veg11, veg10)

meatveg.describe()

# Experimental csv files for accurate renderings

veg12_v2 = pd.read_table('/Users/reneehosogi/Documents/GitHub_Clones/Veg_Project/veg12_v2.csv', sep=',')

veg12_v2.shape
veg12_v2.BEEF.mean()
veg12_v2['MEAT_UNIT']= (veg12_v2.BEEF/4.57) + (veg12_v2.POULTRY/1.97) + (veg12_v2.PORK/3.37) + veg12_v2.SEAFOOD + (veg12_v2.OTHMEAT/2.92)
veg12_v2['PROD_UNIT']= (veg12_v2.FRSHFRUT/1.34) + (veg12_v2.FRSHVEG/1.42) + (veg12_v2.PROCFRUT/2.66) + (veg12_v2.PROCVEG/1.44)
veg12_v2.MEAT_UNIT.mean()
veg12_v2.head(5)

#Different method for experimental csv files
veg11 = pd.read_table('/Users/reneehosogi/Documents/GitHub_Clones/Veg_Project/diary11/veg11.csv', sep=',')
veg11_v2 = pd.read_csv('veg11.csv', usecols=['AGE_REF', 'FAM_SIZE', 'REF_RACE', 'REGION', 'SEX_REF', 'FOODTOT', 'FOODHOME', 'CEREAL', 'BAKEPROD', 'BEEF', 'POULTRY', 'PORK', 'OTHMEAT', 'SEAFOOD', 'FRSHFRUT', 'FRSHVEG', 'PROCFRUT', 'PROCVEG', 'SWEETS', 'NONALBEV', 'OILS', 'MISCFOOD', 'FOODAWAY', 'ALCBEV'])
veg11_v2['MEAT_UNIT']= (veg11_v2.BEEF/4.34) + (veg11_v2.POULTRY/1.89) + (veg11_v2.PORK/3.35) + veg11_v2.SEAFOOD + (veg11_v2.OTHMEAT/3.15)
veg11_v2['PROD_UNIT']= (veg11_v2.FRSHFRUT/1.33) + (veg11_v2.FRSHVEG/1.58) + (veg11_v2.PROCFRUT/2.76) + (veg11_v2.PROCVEG/1.42)
veg11_v2.shape
veg11_v2.MEAT_UNIT.mean()

veg10_v2 = pd.read_csv('veg10.csv', usecols=['AGE_REF', 'FAM_SIZE', 'REF_RACE', 'REGION', 'SEX_REF', 'FOODTOT', 'FOODHOME', 'CEREAL', 'BAKEPROD', 'BEEF', 'POULTRY', 'PORK', 'OTHMEAT', 'SEAFOOD', 'FRSHFRUT', 'FRSHVEG', 'PROCFRUT', 'PROCVEG', 'SWEETS', 'NONALBEV', 'OILS', 'MISCFOOD', 'FOODAWAY', 'ALCBEV'])
veg10['MEAT_UNIT']= (veg10.BEEF/5.26) + (veg10.POULTRY/1.96) + (veg10.PORK/3.10) + veg10.SEAFOOD + (veg10.OTHMEAT/3.22)
veg10['PROD_UNIT']= (veg10.FRSHFRUT/1.32) + (veg10.FRSHVEG/1.15) + (veg10.PROCFRUT/2.47) +(veg10.PROCVEG/1.33)

# Scatter plots for meat and produce consumption by dollar amount

pd.scatter_matrix(veg[['MEAT_UNIT', 'PROD_UNIT']])
pd.scatter_matrix(veg10[['FOODHOME', 'FOODAWAY']])
plt.savefig('VEG12_HOMAWA.png', dpi=1000)

# Scatter plots for varying x-axis using meat data

veg14.plot(kind='scatter', x='FAM_SIZE', y='MEAT', title='Meat consumption by Family Size')
plt.savefig('MEAT_FAM.png', dpi=1000)

veg14.plot(kind='scatter', x='AGE_REF', y='MEAT', title='Meat consumption by Age')
plt.savefig('MEAT_AGE.png', dpi=1000)

veg14.plot(kind='scatter', x='REGION', y='MEAT', title='Meat consumption by Region')
plt.savefig('MEAT_REG.png', dpi=1000)

veg14.plot(kind='scatter', x='FAM_SIZE', y='PRODUCE', title='Produce consumption by Family Size')
plt.savefig('PROD_FAM.png', dpi=1000)

veg14.plot(kind='scatter', x='AGE_REF', y='PRODUCE', title='Produce consumption by Age')
plt.savefig('PROD_AGE.png', dpi=1000)

veg14.plot(kind='scatter', x='REGION', y='PRODUCE', title='Produce consumption by Region')
plt.savefig('PROD_REG.png', dpi=1000)

# Comparison graphs
veg12.REGION.value_counts()
veg10.PROD_UNIT.mean()
veg10.FAM_SIZE.mean()

# Meat by age
veg14.plot(kind='hist', x='MEAT_UNIT', y='AGE_REF')
veg13.plot(kind='hist', y='AGE_REF', x='MEAT_UNIT')
veg12.plot(kind='hist', y='AGE_REF', x='MEAT_UNIT')
veg11.plot(kind='hist', y='AGE_REF', x='MEAT_UNIT')
veg10.plot(kind='hist', y='AGE_REF', x='MEAT_UNIT')


# Food away vs. Food home
veg14.FOODHOME.mean()
veg12.FOODHOME.mean()
veg10.FOODTOT.mean()
veg13.FOODTOT.mean()
veg11.FOODAWAY.mean()
veg12.FOODAWAY.mean()

# Meat by region
veg14.groupby('REGION').MEAT_UNIT.mean()
veg13.groupby('REGION').MEAT_UNIT.mean()
veg12.groupby('REGION').MEAT_UNIT.mean()
veg11.groupby('REGION').MEAT_UNIT.mean()
veg10.groupby('REGION').MEAT_UNIT.mean()

# Produce by region

veg14.groupby('REGION').PROD_UNIT.mean()
veg13.groupby('REGION').PROD_UNIT.mean()
veg12.groupby('REGION').PROD_UNIT.mean()
veg11.groupby('REGION').PROD_UNIT.mean()
veg10.groupby('REGION').PROD_UNIT.mean()

# Meat by FAMILY SIZE
veg14.groupby('FAM_SIZE').MEAT_UNIT.mean()
veg13.groupby('FAM_SIZE').MEAT_UNIT.mean()
veg12.groupby('FAM_SIZE').MEAT_UNIT.mean()
veg11.groupby('FAM_SIZE').MEAT_UNIT.mean()
veg10.groupby('FAM_SIZE').MEAT_UNIT.mean()

# BEEF vs POULTRY 
veg14.plot(kind='scatter', x='REGION', y='FRSHFRUT', sharey='true')

# Produce by FAMILY SIZE
veg14.groupby('FAM_SIZE').PROD_UNIT.mean()
veg13.groupby('FAM_SIZE').PROD_UNIT.mean()
veg12.groupby('FAM_SIZE').PROD_UNIT.mean()
veg11.groupby('FAM_SIZE').PROD_UNIT.mean()
veg10.groupby('FAM_SIZE').PROD_UNIT.mean()

# Meat by Age groups
veg14.plot(column='MEAT_UNIT', by='AGE_REF')
plt.title("Distribution of users' ages")
plt.ylabel('count of users')
plt.xlabel('age')
plt.savefig('MEAT_AGE14.png', dpi=1000)

veg13.PROD_UNIT.plot(kind='hist', column='BEEF', by='AGE_REF')
plt.savefig('MEAT_AGE13.png', dpi=1000)
veg12.AGE_REF.hist(bins=30)
plt.savefig('MEAT_AGE12.png', dpi=1000)
veg11.AGE_REF.hist(bins=30)
plt.savefig('MEAT_AGE11.png', dpi=1000)
veg10.AGE_REF.hist(bins=30)
plt.savefig('MEAT_AGE10.png', dpi=1000)

# Consumption by Meat Type
veg11.MEAT.plot(kind='box', y='REGION', x='MEAT')
veg11.plot(kind='scatter', y='BEEF', x='POULTRY')

veg14.plot(kind='scatter', y='POULTRY', x='MEAT')
veg14.plot(kind='scatter', y='POULTRY', x='BEEF')

meatveg = ('veg14.MEAT' + 'veg13.MEAT'+ 'veg12.MEAT' + 'veg11.MEAT' + 'veg10.MEAT')

meatveg.describe()

meatveg.plot(kind='hist', y='MEAT', x='year')

import seaborn as sns 
sns.barplot(x='REGION', y='PROD_UNIT', hue='MEAT_UNIT', data=veg14);
from pdfrw import 
