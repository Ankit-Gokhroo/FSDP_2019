# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:31:31 2019

@author: Ankit Gokhroo
"""

"""

Code Challenge 1
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""
import sqlite3
from pandas import DataFrame

conn=sqlite3.connect('db_University.db')

c=conn.cursor()

c.execute ("""CREATE TABLE student(
          student_Name Text,
          Student_Age  Integer,
          Student_rollno Integer,
          Branch Text
          )""")

c.execute("INSERT INTO student VALUES ('ankit',21,1,'cse')")
c.execute("INSERT INTO student VALUES ('abhinav',19,4,'me')")

c.execute("INSERT INTO student VALUES ('jethalal',24,2,'cse')")

c.execute("INSERT INTO student VALUES ('champaklal',20,5,'cse')")

c.execute("INSERT INTO student VALUES ('popatlal',23,3,'ce')")

c.execute("INSERT INTO student VALUES ('sohanlal',23,6,'ec')")
conn.commit()

c.execute("SELECT * FROM student")
c.fetchall()
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["name","age","rollno","branch"]


conn.close()




