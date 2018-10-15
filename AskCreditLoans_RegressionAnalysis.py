"""
Created on Fri Oct  5 00:19:46 2018

@author: joshcole

"""
import scipy.stats
import F1_import as f1

"""
the IV is going to be credit history, and the DV is loan status. 
Hypothesis = Loan status does not change based on credit history. 
Null hypothesis = Loan status does change beased on credit history. 
"""

"""
First I have to make a new column which transforms the loan status to integer
"""
def ln_stat_num(row):
    if row['Loan_Status'] == 'Y' :
        val = 2.0
    if row['Loan_Status'] == 'N' :
        val = 1.0
    return val

f1.loan_data['Loan_Status_Num'] = f1.loan_data.apply(ln_stat_num, axis=1)  #this creates the new column from the function

"""
Second I have to clean the data in Credit_History to be all numbers.
"""

def cred_hist_num(row):
    global b
    if row['Credit_History'] == 1.0 :
        b = 1.0
    if row['Credit_History'] == 0.0 :
        b = 0.0
    if row['Credit_History'] == 'nan' :
        b = 0.0
    return b

f1.loan_data['Credit_History_Num'] = f1.loan_data.apply(cred_hist_num, axis=1)  #this creates the new column from the function

print (f1.loan_data) #this confirms/tests the change 

askcredloan_credhistnum = f1.loan_data['Credit_History_Num']
askcredloan_lnstatnum = f1.loan_data['Loan_Status_Num']

ln_cred_lineregress = scipy.stats.linregress(askcredloan_credhistnum,askcredloan_lnstatnum)

print (ln_cred_lineregress)

