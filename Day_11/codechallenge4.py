# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:32:56 2019

@author: Ankit Gokhroo
"""


"""
Code Challenge ( Bar Plot )
  Name: 
    Zoo Visualisation
  Filename: 
    zoo_visual.py
  Problem Statement:
    Read the zoo.csv file
    Print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    Show the total number of water needs by individual animal using a Bar Chart
  Hint:
      Use the concept of Dictionary
import csv
zoo_data = {}
with open('zoo.csv','rt') as ani:
    reader = csv.reader(ani,delimiter = ',')
    next(reader)
    for i in reader:
        if i[0] in zoo_data:
            zoo_data[i[0]] += int(i[2])
        else:
            zoo_data[i[0]] = int(i[2])

objects = tuple(map(lambda x: x ,zoo_data.keys()))
performance = list(map(lambda x: x ,zoo_data.values()))

"""

import pandas as pd
df1=pd.read_csv('zoo.csv')

import csv
zoo_data = {}
with open('zoo.csv','rt') as ani:
    reader = csv.reader(ani,delimiter = ',')
    next(reader)
    for i in reader:
        if i[0] in zoo_data:
            zoo_data[i[0]] += int(i[2])
        else:
            zoo_data[i[0]] = int(i[2])

objects = tuple(map(lambda x: x ,zoo_data.keys()))
performance = list(map(lambda x: x ,zoo_data.values()))

import matplotlib
from matplotlib import pyplot as plt


color=['red','blue','green','black','pink']

x_index = [0,1,2,3,4]



# indexes is the first parameter 
plt.bar(x_index, performance, width = 0.8, align='center', alpha=1.0,label='water need',color=color)

# First Parameters is the indexes and second paramters is the labels
plt.xticks(x_index, objects)

plt.xlabel('animals')

plt.title('water need by individual animal')

plt.ylabel('water')

plt.legend()

plt.show()





