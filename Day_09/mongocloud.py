# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:52:31 2019

@author: Ankit Gokhroo


Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.
"""



import pymongo
import dns
client = pymongo.MongoClient("mongodb+srv://Ankit:luckyjain%4012345@lucky-fs5kd.mongodb.net/test?retryWrites=true&w=majority")
db = client.db_University




def add_student(name, age, rollno, branch):
    db.student.insert_one(
            
            {
            "name" : name,
            "age" : age,
            "rollno" : rollno,
            "branch" : branch
            })
    return "Employee added successfully"

def fetch_all_student():
    user = db.student.find()
    for i in user:
        print (i)



add_student('ankit',21,1,'cse')
add_student('abhi',19,4,'cse')
add_student('avi',18,6,'ec')
add_student('abhishek',15,4,'ee')
add_student('abhay',12,9,'ce')

fetch_all_student()

