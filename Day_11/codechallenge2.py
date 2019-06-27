# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:43:51 2019

@author: Ankit Gokhroo
"""


"""
Code Challenge ( Line Plot )

We have to find sea level rise in past 100 years
Read the file sealevel.csv which has data for 135 years

It has two parts in the data, year and the sea level rise in inches

Read the csv file using the csv reader and create two list
    1) Which stores the years from 1880 to 2014
    2) Which stores the sealevel increase in inches
    
Now plot the data using Line Plot
The plot should have the valid title,labels, ticks ( x and y ), legend

Is the  sea level increasing almost every year.

"""

import pandas as pd
df=pd.read_csv('sealevel.csv')

list1=list(df['Year'])
list2=list(df['inches'])


import matplotlib
from matplotlib import pyplot as plt

plt.plot(list1,list2,label='sealevel in inches')


plt.xlabel("year")
plt.ylabel("inches")
plt.title("sealevel increarses in inch")
plt.legend()
plt.grid(True)
plt.xtick()
plt.show()

a=df['inches'].max()
df[df['inches']==a]













