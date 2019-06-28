# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:32:28 2019

@author: Ankit Gokhroo
"""


"""
Code Challenge 

import Automobile.csv file.

Using MatPlotLib create a PIE Chart of top 10 car makers according to the number 
of their cars and explode the largest car maker


"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('Automobile.csv')
df.info()

a=df['make'].value_counts()
slices=a[0:10].tolist()
labels =a.index[0:10].tolist()
explode=(0.1,0,0,0,0,0,0,0,0,0)
plt.pie(slices,labels=labels,autopct='%.0f%%',explode=explode)
plt.show()

a[0:10].max()