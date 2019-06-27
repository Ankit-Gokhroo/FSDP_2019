"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
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




# Code Challenge

"""
Research the below wesbite and post some data on it
https://requestbin.com
"""



# Code Challenge

"""
Create a client REST API that sends and receives some information from the Server by calling server's REST API.
You are expected to create two functions each for Sending and Receiving data.

    You need to make two api calls, one with POST method for sending data and the other with GET method to receive data

    All the communication i.e. sending and receiving of data with the server has to be in JSON format

    First send the data to cloud using the "http://13.127.155.43/api_v0.1/sending" api with the following fields (Field names should be same as shown ):
            Phone_Number (pass phone number as string and not as integer)
            Name
            College_Name
            Branch

    Now receive the data from cloud using the "http://13.127.155.43/api_v0.1/receiving" api with     
    “Phone_Number” along with the number you are looking for as query parameter
    Print the server responses from both the cases. 
   
    The first one will give response-code : 200 and response-message : "Data added Successfully", if all goes well. 
    The second one will give all the details stored with the phone number you provided as query parameter. 
    Both the responses will be in JSON format.
    
"""