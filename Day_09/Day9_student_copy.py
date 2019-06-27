"""
Database Handling ( sqlite, mysql online, mongodb and mongo atlas )
"""


"""
Database handling using sqlite 
"""

import sqlite3
from pandas import DataFrame


# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'employee.db' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE employees(
          id INTEGER,
          first  TEXT,
          last TEXT,
          pay INTEGER
          )""")


# STEP 2
c.execute("INSERT INTO employees VALUES (01,'Sylvester', 'Fernandes', 50000)")
c.execute("INSERT INTO employees VALUES (02,'Yogendra', 'Singh', 70000)")
c.execute("INSERT INTO employees VALUES (03,'Pradeep', 'Natani', 30000)")
c.execute("INSERT INTO employees VALUES (04,'Kunal', 'Vaid', 30000)")
c.execute("INSERT INTO employees VALUES (05,'Devendra', 'Shekhawat', 30000)")


# STEP 3
c.execute("SELECT * FROM employees")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM employees")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]


# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()







"""
Database handling using MySQL on Local Machine
"""
#use below command in anaconda prompt
# pip install mysql-connector-python

from pandas import DataFrame
import mysql.connector



# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = mysql.connector.connect ( user='root', password='', host='localhost')
# database = '' can be used if we want to connect to already defined database


# creating cursor
c = conn.cursor()

# STEP 0 if exists
c.execute("DROP DATABASE employee;")

# STEP 1
c.execute("CREATE DATABASE employee;")

# STEP 2
c.execute("USE employee;")

# STEP 3
c.execute ("""CREATE TABLE employees(
          id INTEGER,
          first  TEXT,
          last TEXT,
          pay INTEGER
          )""")


# STEP 4
c.execute("INSERT INTO employees VALUES (01,'Sylvester', 'Fernandes', 50000)")
c.execute("INSERT INTO employees VALUES (02,'Yogendra', 'Singh', 70000)")
c.execute("INSERT INTO employees VALUES (03,'Pradeep', 'Natani', 30000)")
c.execute("INSERT INTO employees VALUES (04,'Kunal', 'Vaid', 30000)")
c.execute("INSERT INTO employees VALUES (05,'Devendra', 'Shekhawat', 30000)")

# c.execute("INSERT INTO employee VALUES ({},'{}', '{}', {})".format(idd, first,last,pay))


c.execute("SELECT * FROM employees")

# STEP 5
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM employees")



# STEP 6
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]

# field_names = [i[0] for i in c.description]
# print field_names

conn.commit()
conn.close()



"""
Database handling using MySQL on Cloud
"""


"""
https://www.db4free.net
https://www.db4free.net/phpMyAdmin/
MySQL Host Name : db4free.net
Port : 3306
MySQL database name:  yourdbname
MySQL username: yourusername
MySQL user password: dbpassword 
Email address:  your emailid
MYSQL URL : mysql://yourusername:dbpassword@db4free.net/yourdbname

"""


import mysql.connector 
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='yourusername', password='dbpassword',
                              host='db4free.net', database = 'yourdbname')
#, database = 'forsk_test'

# creating cursor
c = conn.cursor()

# STEP 0
#c.execute("DROP DATABASE employee;")

# STEP 1
#c.execute("CREATE DATABASE employee;")

# STEP 2
c.execute("DROP Table employees;")

# STEP 3
c.execute ("""CREATE TABLE employees(
          id INTEGER,
          first  TEXT,
          last TEXT,
          pay INTEGER
          )""")


# STEP 4
c.execute("INSERT INTO employees VALUES (01,'Sylvester', 'Fernandes', 50000)")
c.execute("INSERT INTO employees VALUES (02,'Yogendra', 'Singh', 70000)")
c.execute("INSERT INTO employees VALUES (03,'Rohit', 'Mishra', 30000)")
c.execute("INSERT INTO employees VALUES (04,'Kunal', 'Vaid', 30000)")
c.execute("INSERT INTO employees VALUES (05,'Devendra', 'Shekhawat', 30000)")

# c.execute("INSERT INTO employee VALUES ({},'{}', '{}', {})".format(idd, first,last,pay))


c.execute("SELECT * FROM employees")


# STEP 5
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM employees")


# STEP 6
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]




"""
Database handling using MongoDB locally 
"""

#use below command in anaconda prompt
#pip install pymongo


from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# create the database if does not exists
mydb = client.employee



# adding the employee in the employee collection
def add_employee(idd, first, last, pay):
    unique_employee = mydb.employees.find_one({"id":idd})
    if unique_employee:
        return "Employee already exists"
    else:
        mydb.employees.insert(
                {
                "id" : idd,
                "first" : first,
                "last" : last,
                "pay" : pay
                })
        return "Employee added successfully"

def fetch_all_employee():
    user = mydb.employees.find()
    for i in user:
        print (i)



add_employee('01','Sylvester', 'Fernandes', 50000)
add_employee('02','Yogendra', 'Singh', 70000)
add_employee('03','Rohit', 'Mishra', 30000)
add_employee('04','Kunal', 'Vaid', 30000)
add_employee('05','Devendra', 'Shekhawat', 30000)


fetch_all_employee()
    


"""
Database handling using MongoDB on Cloud -  Mongo Atlas
"""


import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
client = pymongo.MongoClient("mongodb://yourusername:dbpassword@cluster0-shard-00-00-tdcf5.mongodb.net:27017,cluster0-shard-00-01-tdcf5.mongodb.net:27017,cluster0-shard-00-02-tdcf5.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.yourdbname

def add_employee(idd, first, last, pay):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.yourcollectionname.insert_one(
            {
            "id" : idd,
            "first" : first,
            "last" : last,
            "pay" : pay
            })
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.yourcollectionname.find()
    for i in user:
        print (i)




add_employee(1,'Sylvester', 'Fernandes', '50000')
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(5,'Devendra', 'Shekhawat', 30000)

fetch_all_employee()