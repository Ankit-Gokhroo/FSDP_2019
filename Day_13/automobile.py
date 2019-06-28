# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 17:05:12 2019

@author: Ankit Gokhroo
"""


"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""

import pandas as pd
import numpy as np

data1=pd.read_csv('Automobile.csv')
data1.info()
data1.describe()
data1.columns
data1.dtypes
data1.head()

data1.isnull()
data1.isnull().any(axis=0)

data1['price'] = data1['price'].fillna(data1['price'].mean())

data1['price'].describe()

e=np.array(data1['price'])
