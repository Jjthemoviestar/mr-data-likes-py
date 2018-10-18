# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:56:00 2018

@author: joshcole
"""
import F1_import as f1
import AskTotalIncome as ATInc
import statistics 
import pandas as pd

edu = f1.loan_data['Education']
gen = f1.loan_data['Gender']
inc = ATInc.totinc

inc_avg = statistics.mean(inc)
print (inc_avg)

int_inc_avg = int(inc_avg)
print (int_inc_avg)


"""
This create a sub set of urban property, then another subset
using the education and gender, placing them in charts
"""
f1.loan_data['Property_Area'].value_counts(normalize=True)
f1.loan_data['Property_Area'].value_counts().plot(kind='bar')

urb = (f1.loan_data['Property_Area'] == 'Urban').value_counts(normalize=True)

urb_data = (f1.loan_data['Property_Area'] == 'Urban').value_counts(normalize=True)
urb_data_bar = (f1.loan_data['Property_Area'] == 'Urban').value_counts().plot(kind='bar')
print (urb_data)

prop_urb = f1.loan_data[urb]

edu_data = prop_urb['Education'].value_counts(normalize=True)
prop_urb['Education'].value_counts().plot(kind='barh')
print (edu_data)

gen_data = prop_urb['Gender'].value_counts(normalize=True)
prop_urb['Gender'].value_counts().plot(kind='bar')
prop_urb['Gender'].value_counts().plot(kind='pie')
print (gen_data)

"""
This code takes the income and loan amount and groups by
urban property. Then displays the average of each group
in a bar chart.
"""
inc_data = inc.value_counts(normalize=True)
inc.value_counts().plot(kind='bar')
print (inc_data)
#For some reason this isn't working, and I don't know why.
#I can't seem to filter the total income by just urban
#I also can't seem to get the average of total income for urban
#after I figure that out then I can try to get the loan amount
#then they both need to go into a bar chart.

df_filtered = f1.loan_data[(f1.loan_data.Property_Area == 'Urban')]
print(df_filtered)

#I think there are a couple of ways to fix this. I can either make a new column
#with the data I want, but really I just want the average income and average loan amt
#within that filtered dataset
#I think a function, read this https://www.tutorialspoint.com/python/python_functions.htm



urb_inc_data = prop_urb[inc_data].value_counts(normalize=True)
prop_urb[inc_data].value_counts().plot(kind='barh')
print (urb_inc_data)


inc_ln_ratio = f1.loan_data['Income to Loan Ratio'] = totinc/(lnamt*1000) 


