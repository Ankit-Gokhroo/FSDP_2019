# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:41:57 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""
import numpy as np
import matplotlib.pyplot as plt
                           #mean, sd, total
uni_data = np.random.normal(150.0, 20, 1000)

print (type(uni_data))
print (uni_data.size)
print (uni_data)
print (len(uni_data))
print (uni_data.ndim)
print (uni_data.shape)
print (uni_data.dtype)

print("Mean value is: ", np.mean(uni_data))
print("Median value is: ", np.median(uni_data))
print("Standard Deviation is: ", np.std(uni_data))

from scipy import stats
print("Mode value is: ", stats.mode(uni_data)[0])
 

print("Minimum value is: ", np.min(uni_data))
print("Maximum value is: ", np.max(uni_data))


plt.hist(uni_data,100)
plt.show()

plt.boxplot(uni_data)
plt.show()

np.var(uni_data)


