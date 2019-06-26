# Taking multiple input from user
list1 = []
while True:
    user_input = input("Enter values >")
    
    #append this entry to other data structure
    list1.append(user_input)
    
    if not user_input:
        break
    

"""
  Enumerate
  Dictionary - key, value pairs
  Sets - collection of distinct values
"""


# Enumerate 

"""
A lot of times when dealing with iterators, we also get a need to keep a count of iterations.
Python eases the programmers’ task by providing a built-in function enumerate() for this task.

Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

Syntax:
enumerate(iterable, start=0)

"""


# Python program to illustrate 
# enumerate function 
l1 = ["eat","sleep","repeat"] 

for item in l1:
    print (item)
 
    
counter = 0
for item in l1:
    print (counter, item)
    counter += 1


    
s1 = "geek"
    
for item in s1:
    print (item)
    
    
  
# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 
  
print (type(obj1) )
print (list(enumerate(l1)) )
  

print (list(enumerate(s1)))

# changing start index to 2 from 0 
print (list(enumerate(s1,2)))


# Python program to illustrate  enumerate function in loops 
l1 = ["eat","sleep","repeat"]    
  
# printing the tuples in object directly 
for ele in enumerate(l1):      
    print (ele)  
    print (type(ele))

# changing index and printing separately 
for index,ele in enumerate(l1):     
    print (index,ele) 


for index,ele in enumerate(l1,100):     
    print (index,ele) 



# Using the concept of enumeration to iterate the tuple 
names_of_days = ( 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' )


for index, item in enumerate(names_of_days):
  print("{} : {} ". format (index, item ))
 

for step in enumerate(names_of_days):
  print("{} : {} ". format (step[0], step[1] ))
 

for step in enumerate(names_of_days):
    print("{} : {} ". format (*step))
    
#single * denotes tuple and ** denotes dictionary 
 


"""
Create a custom function to return a tuple   
"""


def my_func():
    return (1,2,3)
 
my_func()

tup = my_func()
 
a,b,c = my_func()

print (a)
print (b)
print (c)


"""
Hands On
"""
#Create a function similar to divmod 




"""
Dictionaries
How to store phone number in a phone book ? 
You would have a list of names and attached to each name a phone number 

Dictionaries is a key value un-ordered pair ( name : mobile number )
Unordered set of key: value pairs where keys are unique
Dictionaries consist of zero or more comma-separated key-value pairs that are enclosed in braces { }
The key and its value are separated by a colon :

We declare dictionaries using {} braces
Like lists dictionaries are also mutable
"""

"""

phonebook = [
    ("John Doe", "555-555-5555"),
    ("Albert Einstein", "212-555-5555"),
]


def find_phonenumber(phonebook, name):
    for n, p in phonebook:
        if n == name:
            return p
    return None

print "John Doe's phone number is", find_phonenumber(phonebook, "John Doe")


phonebook = {
    "John Doe": "555-555-5555",
    "Albert Einstein" : "212-555-5555",
}
print "John Doe's phone number is", phonebook["John Doe"]

"""


# Create empty  dictionary 
dict1 = {} 
print(type(dict1))

dict1 = dict() 
print(type(dict1))

dict1 = dict({})  
print(type(dict1))

print (dict1)
  
dict1 = { 'name':'mobile_number'}
print(dict1)
print(type(dict1))

phone_book = { 'Vidhan':8504982228, 'Aayushi':8905336615, 'Vibhooti':9414701291 }
print(phone_book)
print(type(phone_book))


# Creation of dictionaries
dict1 = {'fname':'John', 'lname':'Mille', 'profession':'plumber',  'age':'32'}
print(dict1)


# Add/Update
dict1['lname'] = 'Miller'
dict1['profession'] = 'electrician'
dict1['age'] = '36'
dict1['city'] = 'NY' #add
print(dict1)

dict1['city'] = 'MA' #update
print(dict1)

dict1.update ( {'age':32, 'city':'NY' } )
print(dict1)

# Printing Values
print (dict1["lname"])
print (dict1.get('lname'))
print (dict1.get('name'))
print (dict1.get('name', 'Not Found'))


# Usage of Dictionary for String Formatting

# This is the old way  
my_string = "Hi ! My name is {name} and I live in {city}.".format(name='John Miller', city='MA')


# Assume that your have 
dict1 = { 'name': 'John Miller', 'city':'MA'}
 
my_string = "Hi ! My name is {name} and I live in {city}.".format(**dict1)


# Remove from dictionary
del dict1['city']
print(dict1)

dict1.pop('city')

dict1.pop('age')
print(dict1)


dict1 = {'fname':'John', 'lname':'Miller', 'profession':'plumber',  'age':'32'}


# To list all the keys
a  = dict1.keys()
print(a)
print(list(a))

print(type(a)) 


# To list all the values  
print(dict1.values())
print(list(dict1.values()))

# To list all the values  
print(dict1.items())



# To list all keys  
for key in dict1.keys() :
  print ( key)


# To list all values   
for value in dict1.values():
  print ( value )

 
# To list all values and keys  
for key in dict1:
  print ( key , dict1[key] )

for key in dict1:
  print ( key , dict1.get(key) )


# Looping the dictionary 
for key, value in dict1.items() :
  print ( key, value )



# Way to use ast to convert string to dictionary
# this concept would be used in a Code Challenge
  
  
str1= "{'a':2}"
import ast
dict1 = ast.literal_eval(str1)



  
  

"""
Collections or Iterables in Python  
Sets
"""


# Set Methods and Operations to Solve Common Problems 

"""
Sets is like a list without duplicate values
 
unordered collection of unique items
no duplicate data
No indexing and No Slicing applicable

Good way to remove duplicate values from a list 
"""

# Creating empty set
empty_set = set()
print(empty_set)
print(type(empty_set))

empty_set = {} #will create an empty dictionary 
print(type(empty_set))


a = { 1,2,2,3,3,4,5 }
print(type (a) ) 
print (a)   
# will print set ( {1 2 3 4 5 } )
# It removes the duplicate values from the list 

 
a  = set("abcdef")
print (a)

a = {'a','b','c','d','e','f'}   # not a dictionary
print (a)




# Set Operations 
# ( add, clear, copy, difference, discard, remove, union, intersection)
# ( isdisjoint, issubset, issuperset, pop )
s1 = {1,2,3,4,5}
print (s1)

s1.add(6)   # add() function can be used to add element to a set
print (s1)

s1.update ([6,7,8])
print (s1) 
 
s2 = {7,8,9}
s1.update([6,7,8],s2)
print (s1)
 
s1.remove(5) # if it doesnt exits it will give Keyerror
print(s1)

s1.discard(5) # this won’t throw key error  
print(s1)

s1.remove(5) # if it doesnt exits it will give Keyerror
print(s1)


"""
It is similar to Mathematical sets.
  Union 
  Difference
  Intersection 
"""

s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}
# They have some unique values
# They have overlapping values 


# Question: get a set of values which are in all in these sets 
# Using Intersection method of Set we can find this
 
s4 = s1.intersection(s2) 
print (s4) # which are common in s2 and s1 {2,3}
s5 = s4.intersection(s3)
print (s5)

# Short Cut
s4 = s1.intersection(s2,s3) 
print (s4) # which are common in s3, s2 and s1 {3}



# Question: get a set of values which are different in all these sets 
# Using Difference  method of Set we can find this


s4 = s1.difference(s2) 
print (s4) # which is present in s1 but not present in s2 {1}


s4 = s2.difference(s1) 
print (s4) # which is present in s2 but not present in s1 {4}
 

s4 = s3.difference(s1,s2) 
print (s4) # which is present in s3 but not present in s1or s2 {5}
 


"""
REAL WORLD USAGE OF SETS 
"""

# Question: remove duplicate values from a list 
l1 = [1,2,3,1,2,3]

# You need to traverse the list one by one and create another empty list and 
# check whether it is present in that or no and add it 
# or a simple solution using sets which is more efficient 

l2 = list ( set ( l1 ) ) 
print (l2)



# Real Life Example 
employees = ['Sita', 'Rohit', 'Sylvester', 'Ram', 'Kunal', 'Yogendra', 'Laxman', 'Dev' ]
gym_members = ['Ram', 'Laxman', 'Sita']
developers = ['Kunal', 'Sita', 'Sylvester', 'Dev', 'Ram']


  
#Question:  Which employers have gym membership and are also employees 
#Intersect gym members with developers 

result = list ( set(gym_members).intersection(set(developers)) )
print (result)   # Ram and Sita 



#Question: All the employees who are not either gym members or developers 
#Difference between employees and gym members and developers 

result = set(employees).difference (set(gym_members), set(developers))
print (result)
# sets can replace a lot of membership tests 
