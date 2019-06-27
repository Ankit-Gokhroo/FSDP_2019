# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:47:06 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""



import requests
url="http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=180b49bf2663d564295c"
response = requests.get(url)
jsondata = response.json()

print(jsondata["USD_INR"])