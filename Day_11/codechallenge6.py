# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:55:54 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge ( Pie Chart )

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area

Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 

Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""

wiki='https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area'

from bs4 import BeautifulSoup
import requests
source = requests.get(wiki).text

soup = BeautifulSoup(source,"lxml")

right_table=soup.find('table', class_='wikitable')

print (right_table.prettify())

tab_bod=right_table.find('tbody')
B=[]
A=[]

for row in tab_bod.findAll('tr'):
    # first row has no TH, but other rows have one TH and 6 TD
    cells = row.findAll('td') 
    # first row has 7 TH 
    #states = row.findAll('th')
    # other than first row
    if len(cells) == 7:
        
        #skip the sequence number column
        A.append(cells[1].text.strip())
        B.append(cells[4].text.strip())
        
        
import matplotlib.pyplot as plt        
        
plt.pie(B[0:6],labels=A[0:6],autopct='%1.1f%%')
plt.show()
        











