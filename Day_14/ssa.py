# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 15:48:37 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    SSA Analysis
  Filename: 
    ssa.py
  Problem Statement:
    (Baby_Names.zip)
    The United States Social Security Administration (SSA) has made available 
    data on the frequency of baby names from 1880 through the 2010. 
    (Use Baby_Names.zip from Resources)  
    
    Read data from all the year files starting from 1880 to 2010, 
    add an extra column named as year that contains year of that particular data
    Concatinate all the data to form single dataframe using pandas concat method
    Display the top 5 male and female baby names of 2010
    Calculate sum of the births column by sex as the total number of births 
    in that year (use pandas pivot_table method)
    Plot the results of the above activity to show total births by sex and year  
     

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
l=os.listdir('baby')

df=pd.DataFrame()

for  i in range(1880,2011):
    df1=pd.DataFrame()

    print('yob'+str(i)+'year')
    
    with open('yob'+str(i)+'.txt',"rt") as rf:
        a=rf.readlines()
    
        df1[i]=a
        df=pd.concat([df,df1],axis=1)

import pandas as pd

df1=pd.DataFrame(columns = ['Name', 'Sex', 'Number','Year'])
for i in range(1880,2011):
    filename="yob"+str(i)+".txt"
    df2 = pd.read_csv(filename,header=None)
    df2.columns = ['Name', 'Sex', 'Number']
    df2['Year']=i
    df2 = df2.sort_values(by=['Number'], ascending=False)
    df1=pd.concat([df1, df2])        
        
