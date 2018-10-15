# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:40:46 2018

@author: joshcole

Creating ln_status_index and ln_status_Y filters down the data
in the same dataframe, do I don't need to create an IF statement,
I just need to filter it down further. This can be done by calling the previous
index that was placed in the variable.
It also means that I don't need to get the number of Y for the loan status and
compare it against the number of blanks or 0.0, I can simply creat the ratio
within the step.

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import F1_import as f1 #importing import code

#print (loan_data.dtypes)

f1.loan_data['Loan_Status'].str.contains('Y') #which rows have a Y

f1.loan_data['Loan_Status'] == 'Y' #which rows have a Y

f1.loan_data = f1.loan_data.fillna('blank') #replaces missing data with blank string

#loan_data.head()  #useful for when looking at a new DF
 
ln_status_index = (f1.loan_data['Loan_Status'] == 'Y') #creates subset of rows with Y

ln_status_Y = f1.loan_data[ln_status_index] #creates subset of true values

ln_status_index.count()
ln_status_Y.count()

#creates output
ln_status_Y['Credit_History'].value_counts(normalize=True)

ln_status_Y['Credit_History'].value_counts().plot(kind='pie')

#why does this overlap????
#f1.loan_data['Loan_Status'].value_counts('Y').plot(kind='barh')


