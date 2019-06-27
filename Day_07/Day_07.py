
"""
JSON has become popular method for exchange of structured information over a 
network and sharing information across platforms.

It is basically text with some structure and saving it as .json

It stores data as key:value pairs.
Anything before : is called key and after : is called value.

This is very similar to Python dictionaries

You can see that the data are separated by , and that curly braces define objects.

Square brackets are used to define arrays in more complex JSON files

Other data types supported are string , number , boolean and null 

encoding is for writing data to disk ( serialisation )

decoding is for reading data into memory ( deserialisation ) 

The process of encoding JSON is usually called serialization.

Naturally, deserialization is the reciprocal process of decoding data that
 has been stored or delivered in the JSON standard.

Think of it like this: encoding is for writing data to disk, 
while decoding is for reading data into memory.

The following table is used to do a conversion from JSON Data types to Python Data Types

Python          JSON
dict            object  { }
list            array   [  ]
str             string  "  "
int             number  89, 98.67
True            true    true
False           false   false 
None            null    null


"""



# Loading raw json data into python specific data 
import json

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
print (type(json_string))

# Converts  JSON Data types to Python Data Types 
my_data = json.loads(json_string)

print (type(my_data) )  # its a python dictionary  , it uses the table to convert 
print (my_data) 
print (my_data['researcher'])

print (my_data['researcher']['relatives'])

print (my_data['researcher']['relatives'][0])

print (my_data['researcher']['relatives'][0]['name'])



# Converts Python Data types to JSON Data Types
new_json_string = json.dumps(my_data)

print (type(new_json_string) )
print (new_json_string) 

new_json_string = json.dumps(my_data, indent=2 )
print (new_json_string) 

new_json_string = json.dumps(my_data, indent=2, sort_keys=True)
print (new_json_string)



# Writing/Storing the JSON data in a File 

with open("data_file.json", "w") as write_file:
    json.dump(json_string, write_file)
    # json.dump(json_string, write_file, indent=2   )


# Reading from a JSON file

with open("data_file.json", "r") as read_file:
    jsondata=json.load(read_file)
    print(jsondata)
    print(type(jsondata))
    
 
    # JSON in python data structure 
    my_data = json.loads(jsondata)
    print ( my_data)
    print(type(my_data))




"""
DO NOT READ THIS, SKIP NOW 

Format of the HTTP Request 
	
1	Request-Line	
    GET|POST [uri] HTTP/[version]	
    
    GET /xml HTTP/1.1

	GET is for viewing any resource on the server
	POST are used for making a change or updating 

	
2   Header	
    [Header Name]: [Header Value]	
    Host:httpbin.org
	User-Agent:telnet								
	Accept-Language:en-US									

3	Blank Line
	
4	Request Body
    (optional, only for POST)
    ( also known as payload)


Format of the HTTP Response 

1	 Status-Line	
     HTTP/[version] [status code] [status message]	
     HTTP/1.1 200 OK

    100 means Informational Messages 
    200 means all OK ( success messages ) 
    301 means  ( Resouce requested is moved to different location from the server )
    404 means not found ( Something went wrong in client request ) 
    500 means Server Errors ( Something went working on server side while processing the request ) 

2	Headers		
    [Header Name]: [Header Value]	
    Server: nginx
	Date: 									
	Content-Type: application/xml										

3	 Blank Line

4	Response Body	[payload]					XML or HTML						



How to send data using the POST method of HTTP protocol 
	
	telnet httpbin.org 80
	POST /post HTTP/1.1 
	Host: httpbin.org
	Content-Length: 32 and press enter twice for blank line
	
	firstname=Chris&language=English
     	and press enter to send the command 

"""



"""

Introduce to the concept of Web Services ( REST API ) using openweathermap.org


http://api.openweathermap.org/data/2.5/weather?q=Jaipur

http://api.openweathermap.org/data/2.5/weather?q=Jaipur&appid=e9185b28e9969fb7a300801eb026de9c


# if you hit the URL in the browser and try to visualise the JSON, you will come to see that it has 12 items in the object 
# copy and paste this on json lint and visualise 

# coord as Object
    {
     #   lon as Number
     #   lat as Number
    }
# weather as List
    [ 
     {
         #  id as Number
         #  main as String
         #  description as String
         #  icon as String
     }
     ]
# base as String
# main as Object 
    {
        # temp as Number
        # pressure as Number
        # humidity as Number
        # temp_min as Number
        # temp_max as Number
    }
# visibility as Number
# wind as Object
    {
        # speed as Number
        # deg as Number
    }
# clouds as Object
    {
     # all as Number
    }
# dt as Number
# sys as Object
    # type as Number 
    # id as Number
    # message as Number
    # country as String
    # sunrise as Number
    # sunset as Number
# id as Integer
# name as String
# cod as Number



how to parse the response of a HTTP request which is in JSON format.

http://jsonplaceholder.typicode.com/
http://httpbin.org 
https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json
"""



"""
Get me the temperature of the city from the openweathermap.org
"""


import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Udaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
response.content

# Content in binary form
print (type(response.content))

print ("Status code: " + str(response.status_code))
print ("Headers : " + str(response.headers))
print ("Data : " + response.text)


for key, value in response.headers.items():
    print (key, ":" ,value , "\n")
   
print ("Content type: " + response.headers['content-type'])


print ("Content or Response Body : " + str(response.content))


# Since we know that the content type is json we can call the json() function to get the data converted to python data type (dict)
jsondata = response.json()
# response has the original JSON String
# jsondata has the convert string in the python data type dictionary

#print (str(type(jsondata)))
print (type(jsondata))

print (jsondata)

print (jsondata.keys())

print (jsondata.values())

print (len(jsondata.items()))

for key, value in jsondata.items():
    print (key, ":" ,value , "\n")
   
jsondata["main"]["temp"]




"""
Sample code to POST data
"""



import json
import requests

Host = "http://httpbin.org/post"

data = {"firstname":"dev","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )


def get_method():
    response = requests.get("http://httpbin.org/get?firstname=Dev&language=English")
    return response

print (get_method().text)




