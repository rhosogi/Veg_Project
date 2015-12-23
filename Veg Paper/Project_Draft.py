# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:45:03 2015

@author: reneehosogi
"""

import csv
with open('fmld142.csv', mode='rU') as f:
    file_nested_list = [row for row in csv.reader(f)]
    
header = file_nested_list[0]
data = file_nested_list[1:]

print header
print data

_______________________________________________________________
# Read in packages

import pandas as pd
import matplotlib.pylab as plt

veg = pd.read_table('/Users/reneehosogi/Documents/GitHub_Clones/project/diary14/veg14.csv', sep=',')

# Test the read-in
veg.head()
veg.tail()
veg.describe()
veg.index
veg.dtypes
veg.shape
veg.AGE_REF.describe()
veg.FOODTOT.describe()
veg.BEEF.value_counts()

# Check for missing data

veg.FOODTOT.isnull().sum()

# Parameters for graphs 

plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 12

# Scatter plots for meats individually 

my_cols = ['FAM_SIZE', 'AGE_REF', 'FOODTOT', 'FOODHOME', 'CEREAL', 'BAKEPROD', 'BEEF', 'PORK', 'OTHMEAT', 'POULTRY', 'SEAFOOD', 'EGGS', 'MILKPROD', 'OTHDAIRY', 'FRSHFRUT', 'FRSHVEG', 'PROCFRUT', 'PROCVEG','SWEETS','NONALBEV', 'OILS', 'MISCFOOD', 'FOODAWAY']
veg.plot(kind='scatter', x='AGE_REF', y='BEEF')
veg.plot(kind='scatter', x='AGE_REF', y='POULTRY')
veg.plot(kind='scatter', x='AGE_REF', y='PORK')

# New columns for meat and produce numbers

veg['MEAT']=veg.BEEF + veg.POULTRY + veg.PORK + veg.SEAFOOD + veg.OTHMEAT
veg['PRODUCE']= veg.FRSHFRUT + veg.FRSHVEG + veg.PROCFRUT + veg.PROCVEG 

# Scatter plots for meat and produce consumption by dollar amount

pd.scatter_matrix(veg[['MEAT', 'PRODUCE']])
pd.scatter_matrix(veg[['FOODHOME', 'FOODAWAY']])

# Scatter plots for varying x-axis

veg.plot(kind='scatter', x='FAM_SIZE', y='MEAT', title='Meat consumption by Family Size')
plt.savefig('MEAT_FAM.png', dpi=1000)

veg.plot(kind='scatter', x='AGE_REF', y='MEAT', title='Meat consumption by Age')
plt.savefig('MEAT_AGE.png', dpi=1000)

veg.plot(kind='scatter', x='REGION', y='MEAT', title='Meat consumption by Region')
plt.savefig('MEAT_REG.png', dpi=1000)

# Other types of graphs for meats

veg.hist(column='MEAT', by='FAM_SIZE')
veg.MEAT.plot(kind='hist', bins=3)

# Reading in other quarters for 2014

