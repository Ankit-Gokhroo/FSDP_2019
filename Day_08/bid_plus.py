# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:12:40 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
import pandas as pd
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

url="https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome(executable_path="C:\\Users\\Ankit Gokhroo\\Downloads\\Compressed\\chromedriver.exe")

browser.get(url)

sleep(2)

A=[]
B=[]
C=[]
D=[]
E=[]
f=[]
i=1
while i<=10:
    get_site_result = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]')
    get_site_result.click()
    
    
    
    get_items_result1 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text
    B.append(get_items_result1.strip())
     
    get_Departmentname_result1 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text
    C.append(get_Departmentname_result1.strip())
    
    get_startdate_result1 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div[1]/div[4]/p[1]/span').text
    D.append(get_startdate_result1.strip())
    
    get_enddate_result1 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text
    E.append(get_enddate_result1.strip())
    
    get_bidno_result1 = browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]').text
    A.append(get_bidno_result1.strip())
    
    i=i+1
    
    

from collections import OrderedDict

col_name = ["bidno","item","department","startdate","enddate"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))

import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("icccricket.csv",index=False)


    






