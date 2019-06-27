# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:33:20 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge ( Line Plot and Bar Plot )

After a survey by the stackoverflow on its Annual Developer Day the following data were created.

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]



The Median/Avergae salary of the Developer from the age of 18  to  55
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 
49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 
98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]


The Median/Avergae salary of the Python Developer from the age of 18  to  55
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 
57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 
112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]



The Median/Avergae salary of the Jav Script Developer from the age of 18  to  55
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 
49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 
102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]



Plot all the three data for the developer, Python Developer and Java Script Developer
on the same plot
The plot should have the valid title,labels, ticks ( x and y ), legend
It should habe different ways to show each 3 lines in different marker, colors, style

Compare all the three types of developer and analyse the plot

Optional :
    Also show the data for all the 3 types of developers using the Bar Chart
Hint: 
    You need to use the index with some padding value to show all the three bars

"""
ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]



#The Median/Avergae salary of the Developer from the age of 18  to  55
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 
49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 
98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]


#The Median/Avergae salary of the Python Developer from the age of 18  to  55
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 
57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 
112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]



#The Median/Avergae salary of the Jav Script Developer from the age of 18  to  55
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 
49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 
102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

import matplotlib
from matplotlib import pyplot as plt


plt.plot(ages_x,dev_y,label='developer',color='red',marker='s',linestyle='-',linewidth=1)


plt.plot(ages_x,py_dev_y,label='python developer',color='blue',marker='+')
plt.plot(ages_x,js_dev_y,label='javascript developer',color='black',marker='*')

# Setting the X Label 
plt.xlabel("Ages")

# Setting the Y Label
plt.ylabel("Median Salary (USD)")

plt.title("Median Salary (USD) by Age")
plt.grid(True)
plt.legend()

plt.show()

from matplotlib import pyplot as plt

x_index=[0]
y1_index=[1]
y2_index=[2]

width=0.30
x_1=[i-width/3 for i in x]
x_2=[+width/3 for i in x]

plt.bar(x_1,y,width=width/3)
plt.bar(x,y_1,width=width/3)
plt.bar(x_2,y_2,width=width/3)

plt.xticks(y_index,)
plt.xticks(y1_index,)
plt.xticks(y2_index,y2)

plt.title('Median Salary (USD) by Age')

plt.show()






























