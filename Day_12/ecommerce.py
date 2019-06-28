# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:11:50 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    E-commerce Data Exploration
  Filename: 
    ecommerce.py
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers 
          
  Hint:
      Execute the code snippet below.
      import numpy as np
      import matplotlib.pyplot as plt
      incomes = np.random.normal(100.0, 20.0, 10000)
      print (incomes)
 
    outlier is an observation that lies an abnormal distance from other values 
    
"""

import numpy as np
import matplotlib.pyplot as plt
                           #mean, sd, total
incomes = np.random.normal(100.0, 20.0, 10000)

print (type(incomes))
print (incomes.size)
print (incomes)
print (len(incomes))
print (incomes.ndim)
print (incomes.shape)
print (incomes.dtype)

print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))
print("Standard Deviation is: ", np.std(incomes))

from scipy import stats
print("Mode value is: ", stats.mode(incomes)[0])
 

print("Minimum value is: ", np.min(incomes))
print("Maximum value is: ", np.max(incomes))

#print("Correlation coefficient value is: ", np.corrcoef(incomes))
plt.hist(incomes, 50)
plt.show()

plt.boxplot(incomes)
plt.show()

incomes = np.append(incomes, [1000])
print (type(incomes))
print (incomes.size)
print (incomes)
print (len(incomes))
print (incomes.ndim)
print (incomes.shape)
print (incomes.dtype)

plt.hist(incomes, 50)
plt.show()


plt.boxplot(incomes)
plt.show()






