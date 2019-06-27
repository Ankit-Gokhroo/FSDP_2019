# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:52:28 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Population Counting
  Filename: 
    Population.py
  Problem Statement:
      
      The given input has a number of rows, each with four fields from a table, containing:
          

          Rank,City,Population,State or union territory
          1,Mumbai,"124.42",Maharashtra


    You are required to output:

        Country, State, Population of the state (obtained by summing up the population of each city in that state)  


    Sample Input

    1,Mumbai,"124.42",Maharashtra
    9,Pune,"31.24",Maharashtra
    13,Nagpur,"24.05",Maharashtra
    6,Chennai,"46.46",Tamil Nadu
    59,Salem,"8.31",Tamil Nadu


    Sample Output

    {"key":"India,Tamil Nadu","value":54.77}
    {"key":"India,Maharashtra","value":179.72}


    Explanation

    The population of India,Tamil Nadu is obtained by adding the population of 
    Chennai and Salem. 
    This process is repeated for India,Maharashtra. 


    Refer to population.csv

"""
import  csv

with open ('population.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    next(csv_reader)
    dict1={}
    for i in csv_reader:
        if dict1.get(i[3]):
            value = i[2].replace(',','')
            dict1["India,"+i[3]] += int(value)
        else:
            value = i[2].replace(',','')
            dict1["India,"+i[3]] =  int(value)
    
    
    



