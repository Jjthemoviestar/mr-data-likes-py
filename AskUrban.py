# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 22:56:00 2018

@author: joshcole
"""
import F1_import as f1
import AskTotalIncome as ATInc
import statistics 

edu = f1.loan_data['Education']
gen = f1.loan_data['Gender']
inc = ATInc.totinc
#print (inc)
#inc.plot(kind='barh')

inc_avg = statistics.mean(inc)
print (inc_avg)


urb = (f1.loan_data['Property_Area'] == 'Urban')
urb.count()

prop_urb = f1.loan_data[urb]

prop_urb['Education'].value_counts(normalize=True)
prop_urb['Education'].value_counts().plot(kind='pie')

prop_urb['Gender'].value_counts(normalize=True)
prop_urb['Gender'].value_counts().plot(kind='pie')

prop_urb[inc.plot(kind='barh')]
prop_urb[inc_avg]


"""
As a developer, I want to display the gender pct, salary avg, 
and education pct for loan applicants that are listed as Urban
so that the business can better understand the customers segmentation.

Salary average run chart or scatter with best fit line -- 
    scatter doesn't make sense, because it's an avg. 
        What would be better is the average income and average loan_amount
            in a bar chart.

"""