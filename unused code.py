# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 15:20:20 2018

@author: joshcole
"""
import matplotlib.pyplot as plt
import F1_import as f1


askcredloan_credhistnum = f1.loan_data['Credit_History_Num'] #see AskCreditLoans_Regression Analysis for more info
askcredloan_lnstatnum = f1.loan_data['Loan_Status_Num']

# Plot
#plt.scatter(askcredloan_credhistnum, askcredloan_lnstatnum)
askcredloan_totalincome = sum(f1.loan_data['ApplicantIncome'], f1.loan_data['CoapplicantIncome'])

plt.scatter(askcredloan_credhistnum, askcredloan_totalincome)
plt.title('Credit History Regression Analysis for Loan Status')
plt.xlabel('Credit History')
plt.ylabel('Loan Status')
plt.show()


f1.loan_data.dtypes
