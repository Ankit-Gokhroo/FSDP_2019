
# Taking multiple input from user
while True:
    user_input = input("Enter values >")
    
    
    #append this entry to other data structure
    # List
    
    if not user_input:
        break
    
    
    
"""
Collections or Iterables in Python  
  List  - ordered values
  Tuples - *immutable* ordered values
"""


"""
Lists
  Introduce the concept of grouping of items in Python  
  Arrays in other programming language 
  How to store a long list of information, which does change over time?
  Collection of different data types similar to array and mutable 
"""


#Creating empty list   
empty_list = [] 
print (empty_list)
print (type(empty_list))


#Creating empty list
empty_list = list ( ) 
print (empty_list)
print (type(empty_list))



#List Creation
my_list = [ 1, 2, 3 ]
print(my_list)

#Adding single items in the list in the last 
my_list.append( 5 ) 
print(my_list)
 
#Adding single item in the list at a specific position in the list
my_list.insert ( 0, 0 )
print(my_list)


# Removing values using the value itself 
#Remove a specific item by its value from the list 
my_list.remove ( 3 )   #( ValueError here since 4 is not in the list )



#Removes always the last item from the list 
# Removing values using the index 
print(my_list)
my_list.pop ( )
print(my_list)
 
myindex = my_list.index(2)
print(myindex)

my_list.pop (myindex)
print(my_list)

my_list.pop ( 0 )
print(my_list)


# Accessing the values of the list using index
print(my_list[0])

 
#Deletion of items from the list at a given index using Global Functions
del my_list[0]         #deletes the item from given index
print(my_list)

 
my_list = [7,1,2,3,5]
#Replacing in a List
print(my_list)
my_list[0]  = 0
print(my_list)

#my_list [ START : END ] = NEW LIST or ITERABLE
  

#List Slicing 
my_list = [0,5,2,4,3,1 ]
print (my_list[1:])
print (my_list[1:5:2])



#How to make big list which spans to multiple lines 
list1 = ['a', 'b','c' ]
list1 = ['a', 'b', \
         'c' ]
print (list1)



#Sorting of the list items  
print(my_list)
my_list.sort()
print (my_list)


#Sorting using Global function  
my_list = [0,5,2,4,3,1 ]
print (my_list) 
sorted ( my_list )
print (my_list)


#Appending multiple items in a list to another list 
x = [0,1,2]
y = [3,4,5]
x.append (y)      # to add y itself, not its values  
print (x)
# [0, 1, 2, [3, 4, 5]]



#Referencing using the 2D Array concept  
print (x[3])
print(type(x[3]))
print(x[3][0])
x[3][0] = 2   #Visualise it like a 2D array
print (x)

#[0, 1, 2, [2, 4, 5]]


# Extending a list with another list ( adding multiple items to a list )
x = [0,1,2]
y = [3,4,5]

x.extend (y)  #to add values of y, not y itself
print (x)


#this could be achievable by + operator also
x = [0,1,2]
y = [3,4,5]
   
x + y
x = x + y
print (x)

x + 5 #should give an error , since you cannot add a int to list data type 

#try x * 2 will have two copies 

x + [5]


"""
Membership Operators 
# in   ,  not in 
"""

# Used to check if some single item is in a larger collection  
# Return True if the item is in list
# Return False if the item is not in list  

# Example
some_list = [1,2,3,5,6,2,4,3,5,6,7,8,1,2,3]

3 in some_list  # will return True

3 not in some_list # will return False

12 not in some_list  # will return True


"""
Hands On
"""
# Remove all 3 from the list 


#Solution
while (3 in some_list):
    some_list.remove(3)
print (some_list)
    
    
    
"""
Identity Operators 
# is ,    is not
"""

# is and is not Operator ( Object Identity )
# is   used to check if objects are same 
# == used to check if values are same

a = [1,2]
b = [1,2]

print ( id(a) )
print ( id (b) )
 
a is b # will return False
a == b # will return True
c = a
print ( id (c) )


a is c # will return True
a == c # will return True


"""
Introduce the isInstance function usage  
"""


isinstance(45.5, float)

isinstance(45, int)

isinstance(True, bool)

isinstance(None, type(None))


"""
Looping technique using for each

for LOOP_VARIABLE in SEQUENCE_LIST :
    STATEMENTS
"""
my_list = [0,1,2,3,4,5,6]
for number in my_list:
  print (number)


#Introduce the range function to generate a list of numbers

# default the range starts from 0

our_list = list(range(13))
print (type(our_list))
print (our_list)

for number in list(range (13)):
  print (number)


for number in list(range (1,13)):
  print (number)



"""
Hands On 1
"""
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 


# simple foreach statements 
# THIS WILL PRINT ALL THE NUMBERS FROM 12,16,17,24,29,30 and done
for number in [12, 16, 17, 24, 29, 30]:
  print (number)
print("done")


#foreach statement with break statements 
#THIS WILL PRINT 12,16 and done

for number in [12, 16, 17, 24, 29, 30]:
  if number % 2 == 1:  # if the number is odd
    break        # immediately exit the loop
  print(number)
print("done")


#foreach statement with continue  statements 
#THIS WILL PRINT 12,16,24,30 and done
for number in [12, 16, 17, 24, 29, 30]:
  if number % 2 == 1:  # if the number is odd
    continue        # don't process and skip to next iteration
  print(number)
print("done")


#foreach statement with pass statements 
#THIS WILL PRINT 12,16,17,24,29,30 and done

for number in [12, 16, 17, 24, 29, 30]:
  if number % 2 == 1:  # if the number is odd
    pass            # its like comment but is processed   
  print(number)
print("done")




"""
Introduction to Function 


Functions are group of statements which perform specific tasks 
Functions reduce repetition of code 
Functions can be used to extend functionality in future 
Keep your code Dry ( Don’t Repeat Yourself ) 

"""


# Explain the calling of the function with the example of outsourcing your work to someone else ,
# Take Ashwani use case for taking attendance 

# Calling a global function
c = len("Test")
print(c)

print ( len ("Test") ) 


#Defining an empty function 
def hello_func():
  pass


#Calling the function 
hello_func()
 
# Printing the calling of the function will print None since our function is not returning anything 
print ( hello_func() ) 

# if we miss the () then it will not execute or 
# run the function but will print the address of the function 
hello_func

id(hello_func)



#Defining the function 
def hello_func():
  print ('Hello Forsk')


print ( hello_func() ) 



#Defining the function with return statements 
def hello_func():
  return 'Hello Forsk'



print ( hello_func() ) 



#Defining the function with argument 
def hello_func(greeting):
  return 'Welcome {}'.format ( greeting ) 



print ( hello_func("Sylvester") ) 


#Best Practice 
print ( hello_func(greeting = "Sylvester") ) 



#Defining the function with argument and default 
def hello_func(greeting, name ='You' ):
  return '{} {} Function'.format ( greeting, name ) 


print ( hello_func("Sylvester") ) 

print ( hello_func("Sylvester","Fernandes") ) 

print ( hello_func(greeting="Sylvester",name="Fernandes") ) 

print ( hello_func(name="Fernandes", greeting="Sylvester") ) 



#Introduce the concept of doc string for documentation of the function 
def hello_func(greeting, name ='You' ):
    """ My Greeting function """
    return '{} {} Function'.format ( greeting, name ) 

print ( hello_func("Sylvester") ) 

help(hello_func)
  
    


#Create a new package/module of your own function and 
# import it and use it ( mylibrary.py )

import mylibrary

print (mylibrary.__file__)

dir(mylibrary)

help ( mylibrary.hello_func)

print (mylibrary.hello_func("Sylvester", "Fernandes"))




"""
Collections or Iterables in Python  
  Tuples ( Ordered on Key collection ) 
  
How to store a long list of information, which doesn't change over time? 
Tuples cannot be modified and is IMMUTABLE
Collection of Constant values of different data types 
Represented by ( and ) brackets with a comma or only comma operator
"""

a = 7

#Introduce the concept of Simultaneous Assignment 
a , b = 1 , 2.7

print (a)
print (b)
type (a)
type(b) 


c = (3, 4) #PACKING 
print (c)
type(c) 

  

d , e = c #UNPACKING 
print (d)
print (e)
type (d)
type (e)
type(c)


my_tuple = (1,2,3)

print (type(my_tuple)) 

my_sec_tuple = 1, 2, 3
print (type(my_sec_tuple)) 

my_sec_tuple = 1 
print (type(my_sec_tuple)) 

my_sec_tuple = (1) 
print (type(my_sec_tuple))

my_sec_tuple = 1, 
print (type(my_sec_tuple)) 

my_sec_tuple = (1,) 
print (type(my_sec_tuple)) 


# Represented by ( and ) brackets with a comma or only comma operator
# Actually Left ( and right ) are not required only to represent tuples


# Tuples concept to swap the variables
# Explain the concept of swapping two variables using third variable 

a = 1
b = 2

a , b = b , a

print (a)
print(b)


# Introduce the unpacking using the function returning a tuple using 
# divmod(23,2) 
# Function returning a tuple, so on left hand side you can multiple variables 

23 / 2

23 // 2  #( Quotient)
23 % 2   #( Remainder)

print (divmod ( 23 , 2 ) ) #will print ( 11 , 1 ) 

x, y = divmod ( 23 , 2 )

print(x)
print(y)

# x will be 11 and y will be 1
# Tuple unpacking requires that the list of variables on the left has the same # number of elements as the length of the tuple.



#Creating empty tuple 
empty_tuple = ()
print(type(empty_tuple))

empty_tuple = tuple()
print(type(empty_tuple))

# Slicing of tuples similar to slicing of string  

names_of_days = ( 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' )
print (names_of_days)
print (type(names_of_days))



names_of_days [0]

names_of_days [ 1: ]


# Tuples are IMMUTABLE similar to string 

names_of_days[0] = 'some other value'  


