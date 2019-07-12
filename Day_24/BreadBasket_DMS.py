# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 22:44:12 2019

@author: Ankit Gokhroo
"""
"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
"""
import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('BreadBasket_DMS.csv')
dataset.info()

dataset=dataset[dataset['Item']!="NONE"]
sell_items_most=dataset['Item'].value_counts().head(15)

sell_items_most1=list(sell_items_most)
l=list(sell_items_most.index)
import matplotlib.pyplot as plt


slices = sell_items_most1
labels = l

plt.pie(slices,labels=labels, wedgeprops={'edgecolor':'black'},autopct='%.0f%%')

plt.show()

df1=pd.DataFrame()
i=1
uniq=set(dataset['Transaction'])

list1=[]
for i in uniq:
    list1.append(list(dataset['Item'][dataset['Transaction']==i]))
 
df1=pd.DataFrame(list1)


# Training Apriori on the dataset

rules = apriori(list1, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

# Visualising the results
results = list(rules)


for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")








