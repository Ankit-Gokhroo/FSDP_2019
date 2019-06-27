# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:14:35 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge ( Scatter Plot )

Suppose the result was announced for a class. 
In this class both guys and girls appeared in the exam. 
The goal is to find out who performed better and how to get rid of shortcomings.
We are going to make a scatter plot for that.
Boys are in green while girls in red. 

girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

Are their any outliers

Hint: 
    Use the Scatter method to scatter the data on the plot

"""

import matplotlib
from matplotlib import pyplot as plt

girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


plt.scatter(girls_grades,grades_range,color='red',label='girls')
plt.scatter(boys_grades,grades_range,color='blue',label='boys')
plt.plot(girls_grades,grades_range,color='red')
plt.plot(boys_grades,grades_range,color='blue')

plt.xlabel('grades')
plt.ylabel('grades range')
plt.title('girls vs boys grades')
plt.grid(True)
plt.legend()
plt.show()

