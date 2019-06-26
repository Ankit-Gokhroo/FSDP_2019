
"""
Python in Industry
  In Google Python is one of the primary language
  Honeywell uses Python for generating documentation  
  Maya uses python for scripting 
  GIS heavy uses python for scripting 
  US Govt does statistical analysis and Data Visualisation
  NASA and Newyork Stock Exchange
  Disney/Pixar Films uses to provide more realistic effect in movies
  Youtube, Instagram, Reddit, Pinterest power their CMS ( Content Management System )
  Facebook uses a lot for internal scripting  
  Face/Speech Recognition
  Controlling Robots and Automation ( MicroPython )
  Data Scientist uses Anaconda with more than 400 packages for science, math, 
  engineering and data analysis

Where we can use Python
    1. For developing Desktop Applications
    2. For developing web Applications
    3. For developing database Applications
    4. For Network Programmings
    5. For developing games
    6. For Data Analysis Applications
    7. For Machine Learning
    8. For developing Artificial Intelligence Applications
    9. For IOT


History of Python
  Easy as ABC ( developed at Centrum Wiskunde & Informatica, Netherlands)
  20th Feb 1991 by Guido van Rossum, 
  British Comedy Troupe - Monty Python Flying Circus


Features of Python
    General Purpose Dynamic Compiled Language 
    Simple and Easy to Learn
    Freeware and Open Source
    High Level Programming Language
    Platform Independent
    Portable
    Dynamically Typed
    Procedure and Object Oriented and Functional  
    Interpreted
    Extensible ( CPython, JPython )
    Embedded
    Extensive Library
"""

"""
Installation of Spyder ( Anaconda )
  Explanation of the Different Windows
  Creation of first.py in this environment also
  Running of the Project
  Running of some part of code in Spyder
  Autocomplete variable names by using ATL + / in IDLE
"""


"""
Python Shell as a Calculator (Trainer Hands On)
"""


5 + 2

5 - 2

5 * 2

5 / 2 

#( Ver 2 always return integer value but ver 3 returns float)


#Comparision of C Syntax in Python
int a = 2;

a = 2
type(a)


#Printing on the Console (Trainer Hands On)
print ("Hello World")




"""
Literals using primitive data types
  Numeric ( int/long)
    4
  Floating Point ( float )
    10.6
  Boolean ( bool )
    True False
  String ( str )
    "Hello World"
  NoneType ( None )
    None

"""


#How to check the data type of a literal
type (4)

type (10.6)

type (True)
type (False)

type ('FORSK')
type ("FORSK")
type ('''FORSK''')
type ("""FORSK""")

type ( None )


"""
Type Conversion using Global Functions  
  int()
  float()
  str()
  bool()
"""


#How to convert the data type (Trainer Hands On)
int (4)
int (10.6)
int ("10")
int (True)
int (False)


float (4)
float (10.6)
float ("10")
float (True)
float (False)


str (4)
str (10.6)
str ("10")
str (True)
str (False)


bool (4)        # Any integer greater than zero is True
bool (0)

bool (10.6)     # Any float greater than 0.0 is True
bool(0.0)

bool ("10")bool (None)
bool("")

bool (True)
bool (False)





"""
Single Line Commenting (Trainer Hands On)
"""

#Using HASH or POUND ( # ) 

# This is a comment line

"""
How to store data in Python variables 
  Variable is like a Box and you put a literal in it 
  Literal can be of any above types
  Introduce the concept of Heap and Stack
  Python variables in Stack are references to objects in Heap
  Actual data is contained in the object
  In Python everything is object

  Identity function id() can be used to find the unique identity of the object it is pointing to 


"""

#   Example for explanation with visual
x = 42 
id(x)
print(x)


x = 78
id(x)
print(x)



# Both a and b point to the same object in heap
a = 42 
id(a)
print(a)

b = 42
id(b)
print(b)


"""
    List of Python inbuilt functions
    1. type() - to check the type of variable
    2. id() - to get address of object
    3. print() - to print the value
"""


"""
Naming Convention
    A name in Python program is called identifier

    Valid characters for variable names, class name, module name, function name ( Identifiers)
        "A" through "Z" 
        "a" through "z" 
        underscore _ 
        digits 0 through 9 (except for the first character) 
  
  Variable names and identifier names can additionally contain Unicode characters as well.
  
  Rules
      1. Alphabet Symbols (Either Upper case OR Lower case)
      2. If Identifier is start with Underscore (_) then it indicates it is private.
      3. Identifier should not start with Digits.
      4. Identifiers are case sensitive.
      5. We cannot use reserved words as identifiers
      6. There is no length limit for Python identifiers. But not recommended to use too lengthy
      identifiers.
      7. Dollor ($) Symbol is not allowed in Python.

"""

8p = "FORSK"   
!p = "FORSK"
$p = "FORSK"
# Cannot start with a number, Exclamation and $ sign

p!p = "FORSK"
p$p = "FORSK"
# Cannot have a Exclamation or  $ sign or any other special characters

p8 = "FORSK"
# Can have numbers within

+p = "FORSK"
-p = "FORSK"   
*p = "FORSK"
/p = "FORSK"
# Cannot start with or have any Arithmetic Operators
  

for = "FORSK"   
print = "FORSK"

# Cannot use keywords ( 33 Reserved Words)  used in python syntax
# and, as, assert, break, class, continue, def, del, elif, else,
# except, while, finally, for, from, global, if, import, in, is, 
# lambda, yield, nonlocal, not, or, pass, raise, return, with, try, 
# False, True, None



_for = "FORSK" 
# _ is the only special character which is allowed

my age  = 40  
# Space is not allowed between the variable names

my_age = 40 
# underscore is the best way to have long variable names


"""
Printing Output of a variable on console
"""

print ("Hello")
my_age = 40
print (my_age)


"""
One variable can hold different data type
"""

# Integer
my_var = 8
type(my_var)

# Float
my_var = 26.5
type(my_var)
  
# String
my_var = "FORSK"
type(my_var)
  
# Boolean
my_var = True
type(my_var)
  
# NoneType
my_var = None
type(my_var)


"""
Understanding Error Messages in Python (Trainer Hands On)
"""

#Syntax Error 
print("Hello)

#NameError happens when something does not exists
5 + z

#TypeError happens when there is data type mis match
5 + "a"

#Solution to convert the 5 using the str function to string first and then use it
"5" + "a"
str(5) + "a"




"""
Arithmetic Operator  
"""


#+ Addition
7 + 5 

#- Subtraction
7 - 5

#* Multiplication 
7 * 5

#/ Division   
7 / 5


#Ver 2 always return integer value 
#Ver 3 returns float value
#Division by 0 would return ZeroDivisionError
  
#% Modulus 
7 % 5

#** Exponent
7 ** 5

#// Integer Division or Floor Division , always returns integer
7 // 5


#Other Global Function
#Introduce the round function to show the rounding to nearest integer value 

int ( 5.9 )
round ( 5.9 )
round ( 5.4 )
round ( 5.5 )


"""
Assignment Operator  ( give a hands on using two different number )
  = Assignment 
    ( a = 5 )
  += Addition 
    ( a += 1 ) ( a = a + 1 )
  -= Subtraction 
    ( a -= 1 ) ( a = a - 1 )
  *= Multiplication 
    ( a *= 1 ) ( a = a * 1 )
  /= Division 
    ( a /= 1 ) ( a = a / 1 )
  %= Modulus 
    ( a %= 1 ) ( a = a % 1 )
  **= Exponent 
    ( a **= 1 ) ( a = a ** 1 )
  //= Integer Division or Floor Division 
    ( a //= 1 ) ( a = a // 1 )
"""



"""
Taking Integer Input from user
"""

age = input ( "Enter your Age > ")
print (age)
print (type(age))
  
age = int(age)
print (age)
print (type(age))


# Best Practice 
age = int(input ( "Enter your Age > "))
print (age)
print (type(age))


"""
Taking Floating Point Input from user 
"""

temperature  = input ( "Enter your temperature of your city > ")
print (temperature)
print (type(temperature))

  
temperature = float(temperature)
print (temperature)
print (type(temperature))

# Best Practice 
temperature  = float(input ( "Enter your temperature of your city > "))
print (temperature)
print (type(temperature))


"""
Taking String Input from user  
"""
name = input ( "Enter your Name >") #raw_input()
print (name)
print (type(name))

"""
Using + and , Operator
"""
#Adding two string using + operator  ( Concatenation ) 
"Hello" + "World"

#Add string and number using + operator 
"Hello " + 5

#Add string and number using + operator 
"Hello " + str(5)


#Printing output to the screen using the + operator
str1 = "FORSK"
str2 = "TECHNOLOGIES"
print ( str1 + str2 )
print (str1 + " " + str2)

#Printing output to the screen using the , COMMA operator
print (str1 , str2)


#String and number

"Hello " + 5

"Hello " + str(5)

"Hello " - str(5)

"Hello " / str(5)


#Multiply string and number
"Hello " * 5


#Printing Output to the screen using single quote
print ( 'FORSK TECHNOLOGIES' )

#Printing Output to the screen using double quote
print ( "FORSK TECHNOLOGIES" )


print ('FORSK\'S TECHNOLOGIES')


print ("FORSK'S TECHNOLOGIES")

print ("FORSK"S TECHNOLOGIES")

#Using Triple Quotes to print quotation marks in string
print ("""FORSK"S TECHNOLOGIES""")


#Triple quotes to maintain formatting of the text
long_str = """ this is a 
                multiple line string
                end of the string """
print ( long_str)



# Modular Programming and Modules



"""
Packages
    Modules
        Function
"""


# Importing Modules
 
import math

print(math.__file__)

 
math.sqrt ( 16 )
math.log ( 16, 2 )  
math.cos ( 0 )
math.isnan(90)

import math
x=float('nan')
math.isnan(x)



# Renaming a Namespace
#How to use package Aliasing in python  
import math as MT
 
MT.sqrt ( 16 )
MT.log ( 16, 2 )  
MT.cos ( 0 )


# Importing Names from a Module Directly
#How to use specific functions from packages or modules in python 
from math import sqrt
sqrt ( 16 )


#How to use specific functions from packages or modules
#and also aliasing
from math import sqrt as square 
square ( 16 )



#How to use generate random numbers in python 
import random 
print (random.__file__)

r1 = random.randint(0,10)
print (r1)



"""
import math
math.__file__

import random
random.__file__
   
import os
os.__file__
"""

# How to find the function within the Module/Package
dir ( math )

dir ( random )



help (math.sqrt)

help ( random.randint)


"""
Explain the String Slicing Concept Image
# Basic_python-slicing-example.png
"""


#Slicing of strings

newstr = "Monty Python"

# Indexing using Left to Right

#START
newstr[1] # 1st thing (0-indexed)
newstr[-12]

# Indexing using Right to Left
newstr [ -1 ]  # Last thing

 
#START and END
newstr[:3]  # First three things
newstr[-3:] # Last three things

newstr[3:]  # Everything *except* the first three
newstr[:-3] # Everything *except* the last three\

newstr [ 6:10 ]
newstr [ -12:-7 ]
newstr [ 6:12 ]
 
newstr [ : 5 ]
newstr [ 6 : ]
newstr [ : ]
   
#START END and STEPS or INTERVALS ( JUMPS)
#skip items while slicing
newstr [ ::]
newstr [ ::1 ]
newstr [ ::2 ]
newstr [ ::3 ]
   
#move backwards while slicing
newstr [ ::-1 ] # Reversed
# check this 



# Hands On 1
string = "Rajasthan"
#Print characters at the even index number 

# Answer
print(string[1:10:2])


# Hands On 2
string = "Rajasthan"
#Print the given string in reverse 

# Answer
print(string[::-1])


# Hands On 3
string = "Forsk Technologies"
#Print siesgolonhceT using slicing ( forward indexing Left to Right )  

# Answer
print(string[-1:-13:-1])


# Hands On 4
string = "Forsk Technologies"
#Print Technologies Forsk using slicing ( forward indexing Left to Right  )  

# Answer
print(string[6:20] + " " + string[0:5] )



"""
Strings in python are Immutable 
"""

newstr = "Monty Python"

newstr [ 0 ] = "m"
#or 
del newstr [ 0 ]
  
del newstr

print (newstr)

newstr = "Monty Python"
newstr = "monty Python"
# Explain this with the object reference visual


"""
Global Inbuilt function ( len and del )
"""

len ( newstr )
print ( newstr )
del ( newstr )



"""
String functions 
( lower, upper, find, replace, strip, lstrip, rstrip, split, join) 
creates a new copy of the string 
"""


newstr = "    Monty Python    "
print(newstr)

newstr.lower()
print(newstr)

newstr2= newstr.lower()
print(newstr2)

newstr.upper()
   
newstr.find('rr')
newstr.find('P')
newstr.replace(' ','\n')
 
newstr.lstrip()
newstr.rstrip()
newstr.strip()
  
newstr.split()
newstr.index('r')

string="Rajasthan"
"#".join( string )



#to list all the functions for an object  
dir ( str )

#to check the syntax for a specific function of the object 
help ( str.strip )


"""
Formatting the string 
"""

print("Hello {}, your balance is {}.".format("Ram", 23067.2346))
-
print("Hello {1}, your balance is {0}.".format("Ram", 23067.2346))

print("Hello {name1}, your balance is {blc1}.".format(name1="Ram", blc1=23067.2346))

name = input("Enter your Name >") #raw_input
blc = input("Enter your Balance  > ")

print("Hello {}, your balance is {}.".format(name, blc))
print("Hello {name1}, your balance is {blc1}.".format(name1=name, blc1=blc))


 
"""
Decision based on Comparison Operators ( Non Sequential )
==  Equal
!=  Not Equal
>   Greater Then
<   Less Then
>=  Greater Then and Equal To
<=  Less Then and Equal To 

  Perform the above comparison operators using some numbers to demonstrate True or False  
"""


"""
Control Flow using Conditional Statement ( if )
if BOOLEAN_EXPRESSION:
    STATEMENTS_WHEN_CONDITION_IS_TRUE  
"""

#Take the age as input from the user and print  
age = int(input("Enter your age>"))

if ( age > 0 ):
  print ("Valid Age")


"""
Control Flow using Conditional Statement ( if and else )
if BOOLEAN_EXPRESSION:
    STATEMENTS_WHEN_CONDITION_IS_TRUE  
else:
  STATEMENTS_WHEN_CONDITION_IS_FALSE
"""

#Take the age as input from the user and print  
age = int(input("Enter your age>"))
if ( age > 0 ):
  print ("Valid Age")
  
else:
  print ("Invalid Age")
  


"""
Logical Operators ( AND, OR, NOT )
and Logical AND ( True and True )
or Logical OR ( False or True )
! Logical NOT ( !True ) 
"""

# Hand On
# Take the age as input from the user and print whether he is an Adult or Child 
# If the age is between 0 and 18 he is a Child else he is Adult




"""
Chained Conditioning or switching Statement ( if elif and else )
if BOOLEAN_EXPRESSION:
    STATEMENTS_WHEN_CONDITION_IS_TRUE  
elif OTHER_EXPRESSION:
    STATEMENTS_WHEN_OTHER_CONDITION_IS_TRUE
else:
    STATEMENTS_WHEN_CONDITION_IS_FALSE
"""


# Hand On
# Take the age as input from the user and print whether he is a infant, Child , 
# Adult,  Senior Citizen
# 0 - 1 is Infant
# > 1 and < than 18 is Child 
# > 18 and < 60 is Adult
# > 60 is Senior Citizen 


"""## Truth, Falsity, and Comparison"""

#False Conditions Values using the bool function 
bool(False)
bool(0)

#Zero or any numeric value
bool(1)
bool(-90)
bool(90)  


# False Condition
bool(None)  
bool("") # Any empty sequence 
bool(()) # Any empty sequence 
bool([]) # Any empty sequence 
bool({}) # Any empty sequence 


#Perform the above comparison operators using some numbers to demonstrate True or False using the bool() function 

"""
Nested Conditional Statements
if BOOLEAN_EXPRESSION:
    STATEMENTS_WHEN_CONDITION_IS_TRUE  
else:
    if x > y: 
        STATEMENTS_WHEN_OTHER_CONDITION_IS_TRUE
    else:
        STATEMENTS_WHEN_CONDITION_IS_FALSE
"""


"""
Looping technique using while 
while BOOLEAN_EXPRESSION:
    STATEMENTS
""" 

n = 0
while (n < 10):
  print (n)
  n = n + 1
  #n += 1


n = 0 
while ( True ):
  print (n)
  n = n + 1
  if ( n == 10 ) :
    break # immediately exit the loop



# Taking multiple input from user
while True:
    user_input = raw_input("Enter values >")
    
    #append this entry to other data structure
    if not user_input:
        break
    
    
