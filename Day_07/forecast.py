# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 23:27:06 2019

@author: Ankit Gokhroo
"""


import requests
import json

dict1={"Rajasthan":["alwar","bharatpur","bhilwara","jaipur","bijainagar"],"Uttar Pradesh":["mathura","lucknow","agra","kanpur"]}

a=input('enter name of state whose cities temperature you want')

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+a+""
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
url=url1+url2+url3


for i in dict1[a]:
    
    url1 = "http://api.openweathermap.org/data/2.5/weather"
    url2 = "?q="+i+""
    url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
    url=url1+url2+url3
    
    response=requests.get(url)
    a=response.content


    jsondata = response.json()
    t=jsondata['main']['temp']-273
    z=((i,t))
    print((i,t))
    
    with open("forecast.txt",mode="a") as af:
        af.write(json.dumps(z))
        af.write("\n")
        
        
    

b=json.dumps(jsondata)    
    
    
    
    
    




