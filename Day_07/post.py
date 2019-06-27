# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:01:46 2019

@author: Ankit Gokhroo
"""

"""
Research the below wesbite and post some data on it
https://requestbin.com
"""




host="https://encae93jrwcx9.x.pipedream.net"

data = {"firstname":"dev","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

response = requests.post(host,data,headers)


response1 = requests.get("")

response = requests.get("http://httpbin.org/get?firstname=Dev&language=English")