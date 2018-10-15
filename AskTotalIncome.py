# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:24:19 2018

@author: joshcole
"""
import F1_import as f1
import AskCreditLoans_RegressionAnalysis as ACL
import scipy.stats
import matplotlib.pyplot as plt


appinc = f1.loan_data['ApplicantIncome']
coappinc = f1.loan_data['CoapplicantIncome']
totinc = (appinc + coappinc)*10

print (totinc)

f1.loan_data['LoanAmount'].fillna(0)

lnamt = (f1.loan_data['LoanAmount'])

print (lnamt)

totinc_lineregress = scipy.stats.linregress(totinc,lnamt)

print (totinc_lineregress)


slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(totinc,lnamt)
plt.plot(totinc,lnamt,'o',label='loan data') #this scatter is for all loans
plt.plot(totinc, intercept + slope*totinc,'r',label='best fit')
plt.title('Correlation between Total Income and Loan Amount')
plt.xlabel('Total Income')
plt.ylabel('Loan Amount')
plt.legend()
plt.show()

f1.loan_data['Income to Loan Ratio'] = totinc/(lnamt*1000) 
f1.loan_data[:5]

"""
some of the data needs to be scrubbed, there are loans approved with no loan amount
"""

