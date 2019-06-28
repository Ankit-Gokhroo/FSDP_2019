# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:53:27 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Telecom Churn Analysis
  Dataset:
    Telecom_churn.csv
  Filename: 
    telecom_churn.py
  Problem Statement:
    Read the telecom_churn.csv file and perform the following task :
    
To perfrom analysis on the Telecom industry churn dataset -
1. Predict the count of Churned customer availing both voice mail plan and international plan schema
2. Total charges for international calls made by churned and non-churned customer and visualize it
3. Predict the state having highest night call minutes for churned customer
4. Visualize -
    a. the most popular call type among churned user
    b. the minimum charges among all call type among churned user
5. Which category of customer having maximum account lenght?
   Predict and print it
6. Predict a relation between the customer and customer care service that 
whether churned customer have shown their concern to inform the customer care 
service about their problem or not
7. In which area code the international plan is most availed?
"""
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

d1=pd.read_csv('Telecom_churn.csv')
d1.info()
d1.describe()
d1.columns.tolist()

#1. Predict the count of Churned customer availing both voice mail plan and international plan schema
d1['churn'][(d1['voice mail plan']=='yes') & (d1['international plan']=='yes')].value_counts()

#2. Total charges for international calls made by churned and non-churned customer and visualize it
i=d1['total intl charge'][d1['churn']==True].sum()
j=d1['total intl charge'][d1['churn']==False].sum()

labels = ('churn','non churn')
x_index = [0,1]
plt.xticks(x_index, labels)
plt.bar(x_index,[i,j],color=['blue','red'])
plt.xlabel('type of customer')
plt.ylabel('total intl charge')
plt.title('total charge')

plt.show()

#3. Predict the state having highest night call minutes for churned customer
x=d1['total night minutes'][d1['churn']==True].max()
x=d1['state'][d1['churn']==True].max()

b=d1[['total night minutes','churn','state']][d1['churn']==True].max()
c=pd.DataFrame()

c['churn']=[b[1]]
c['total night minutes']=[b[0]]
c['state']=[b[2]]
d1['state'][d1['total night minutes']==(d1['total night minutes'][d1['churn']==True].max())]



#4. Visualize -
#    a. the most popular call type among churned user
#    b. the minimum charges among all call type among churned user

#a
z=d1[['churn','total day calls','total eve calls','total night calls','total intl calls','customer service calls']][d1['churn']==True]
b=z['total eve calls'].sum()
a=z['total day calls'].sum()
c=z['total night calls'].sum()
d=z['total intl calls'].sum()
e=z['customer service calls'].sum()


labels = ('total day calls','total eve calls','total night calls','total intl calls','customer service calls')
x_index = [0,1,2,3,4]
plt.xticks(x_index, labels,rotation=-90)
plt.bar(x_index,[a,b,c,d,e],color=['blue','red','pink','green','orange'])
plt.xlabel('type of call')
plt.ylabel('total no. of call')
plt.title('total call of each type')

plt.show()

#b
y=z=d1[['churn','total day charge','total eve charge','total night charge','total intl charge']][d1['churn']==True]

b=y['total eve charge'].mean()
a=y['total day charge'].mean()
c=y['total night charge'].mean()
d=y['total intl charge'].mean()

labels=('total day charge','total eve charge','total night charge','total intl charge')
x_index = [0,1,2,3]
plt.xticks(x_index, labels,rotation=-90)
plt.bar(x_index,[a,b,c,d],color=['blue','red','pink','green'])
plt.xlabel('call type')
plt.ylabel('total charge')
plt.title('total charge of each call type')

plt.show()


#5. Which category of customer having maximum account lenght?
# Predict and print it

i=d1[['churn','account length']][d1['account length']==d1["account length"].max()]
print(i)

#6. Predict a relation between the customer and customer care service that 
#  whether churned customer have shown their concern to inform the customer care 
#  service about their problem or not

w1=d1['customer service calls'][d1['churn']==True].sum()
w2=d1[['total day calls','total eve calls','total night calls','total intl calls','customer service calls']][d1['churn']==True].sum()

#7. In which area code the international plan is most availed?
b=d1.groupby([d1['area code'][d1['international plan']=='yes']]).size()

