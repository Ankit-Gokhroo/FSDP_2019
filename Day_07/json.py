# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:22:59 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Bangalore"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url=url1+url2+url3
import requests

response = requests.get(url)

a=(response.content)

jsondata = response.json()

type(jsondata)

print(jsondata.keys())
print(jsondata.values())

for key, value in jsondata.items():
    print (key, ":" ,value , "\n")
    
print(jsondata['coord'])
print(jsondata['weather'])
print(jsondata['wind']['speed'])
print(jsondata['sys']['sunrise'])
print(jsondata['sys']['sunset'])


print (response.text)
print ("Status code: " + str(response.status_code))
print ("Headers : " + str(response.headers))

for key, value in response.headers.items():
    print (key, ":" ,value , "\n")
   
print ("Content type: " + response.headers['content-type'])


print (type(response.content))
print ("Content or Response Body : " + str(response.content))



print (jsondata.keys())

print (jsondata.values())

print (len(jsondata.items()))

for key, value in jsondata.items():
    print (key, ":" ,value , "\n")








