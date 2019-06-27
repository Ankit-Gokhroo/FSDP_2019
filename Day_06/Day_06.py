"""
Any

Returns true if any of the items is True. 
It returns False if empty or all are false.
Any can be thought of as a sequence of OR operations on the provided iterables.
It short circuit the execution i.e. stop the execution as soon as the result is known.

"""


# Since all are false, false is returned 
print (any([False, False, False, False])) 
  
# Here the method will short-circuit at the 
# second item (True) and will return True. 
print (any([False, True, False, False])) 
  
# Here the method will short-circuit at the 
# first (True) and will return True. 
print (any([True, False, False, True])) 


"""
All

Returns true if all of the items are True (or if the iterable is empty). 
All can be thought of as a sequence of AND operations on the provided iterables. 
It also short circuit the execution i.e. stop the execution as soon as the result is known.

"""


# Here all the iterables are True so all 
# will return True and the same will be printed 
print (all([True, True, True, True])) 
  
# Here the method will short-circuit at the  
# first item (False) and will return False. 
print (all([False, True, True, False])) 
  
# This statement will return False, as no 
# True is found in the iterables 
print (all([False, False, False])) 



"""
Advanced Collection ( Counter, OrderedDict, NamedTuple) 
"""

# check the frequency of the words

words = ["one", "two", "one", "two", "three", "four", "one"]
freq = dict()

for word in words:
    if word in freq:
        freq[word] += 1
    else: 
        freq[word] = 1
print(freq)


for key in freq.keys(): 
    print (key, ":", freq[key])
 
for key,value in freq.items():
    print (key, ":", value)



#Using default dict


from collections import defaultdict

words = ["one", "two", "one", "two", "three", "four", "one"]

freq = defaultdict(int)

# We have removed the logic to check whether key is present or not
for word in words:
    freq[word] += 1
     
print(freq)
    
for key in freq.keys(): 
    print (key, ":", freq[key])
 
for key,value in freq.items():
    print (key, ":", value)



# Alternate solution using Counter class 
    
from collections import Counter

words = ["one", "two", "one", "two", "three", "four", "one"]
frequency = Counter(words)
print (frequency)

for key,value in dict(frequency).items():
    print (key,value)

 
    
"""
OrderedDict 
"""
    
# An OrderedDict is a dictionary subclass that remembers the order that 
# keys were first inserted. 
  
# OrderedDict preserves the order in which the keys are inserted. 
# A regular dict doesn’t track the insertion order, and iterating it gives the 
# values in an arbitrary order.
    
import collections
d = collections.OrderedDict()   


"""
When to Use Namedtuples
"""

"""
Namedtuples can be an easy way to clean up your code and to make it more 
readable by enforcing a better structure for your data.

I find, for example, that going from ad-hoc data types like dictionaries 
with a fixed format to namedtuples helps me express my intentions more 
clearly. Often when I attempt this refactoring I magically come up with 
a better solution for the problem I’m facing.

"""
    
import collections
# regular tuple 
# 55 represents RED, 155 represents GREEN and 255 represents BLUE 
color = ( 55, 155, 255 ) 
print ( color[0] ) # This leads to non readable tuples 


#Solution is NAMEDTUPLE
Color = collections.namedtuple('myColor', ['red','green','blue'])

print (type(Color))


color = Color ( blue=255, green=155, red = 55 )

print (type(color))

print ( color[0] ) 

print ( color.red )



"""
List Comprehension 
"""

""""
List comprehensions are used for creating new list from another iterables.
As list comprehension returns list, they consists of brackets containing 
the expression which needs to be executed for each element along with the 
for loop to iterate over each element.

new_list = [expression for_loop_one_or_more_conditions]
"""

# Find squares of a number using for loop.
numbers = [1, 2, 3, 4]
squares = []

for n in numbers:
    squares.append(n**2)
print(squares)  



# Finding squares using list comprehensions
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares)  


[1,4,9,16]
[2,5,10,17]
a = [1,2,3,4]
print ([ x**2 for x in a ])
print ([ x + 1 for x in [x**2 for x in a ]])



"""
Lambda
"""

"""
Lambda is a way to create anonymous function i.e. functions without name 
Lambda function are mainly used with Filter, Map and Reduce 
Lambda operator or lambda function is used for creating small, 
one-time and anonymous function objects in Python.

Syntax:
lambda arguments: expression
This function can have any number of arguments but only one expression, 
which is evaluated and returned.

"""

 
# showing difference between def() and lambda(). 
def cube(y): 
    return y*y*y 

print(cube(5))


# Converting the function to lambda function  
g = lambda y: y*y*y 
print (type(g))
print(g(5))  


# Lambda with two arguments 
f  = lambda x,y : x + y
print(f(1,1))


# Explain the concept of filter map reduce using the example of getting multiple  
# Temperature every sec using an IoT device


"""
Filter 
"""

"""
The filter() function in Python takes in a function and a list as arguments. 
This offers an elegant way to filter out all the elements of a sequence "sequence", 
for which the function returns True.
""" 

def f(x) :
    return x%3 ==0 or x%5 ==0 


my_list = list(range(2,25 ))
print(my_list)

my_filter_list = filter ( f, my_list)
print(list(my_filter_list))


# Filter with Lambda function 
my_filter_list = filter ( lambda x:x%3==0 or x%5==0, my_list)
print(list(my_filter_list))



"""
Map 
"""


"""
map() function returns a list of the results after applying the given function
to each item of a given iterable (list, tuple etc.)

Syntax :

map(fun, iter)
Parameters :

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

Returns :
Returns a list of the results after applying the given function to each item 
of a given iterable (list, tuple etc.) 
"""

# Return double of n 
def addition(n): 
  return n + n 

# We double all numbers using map() 
numbers = [1, 2, 3, 4] 
result = map(addition, numbers) 
print(list(result)) 


# Double all numbers using map and lambda 
numbers = [1, 2, 3, 4] 
result = map(lambda n: n + n, numbers) 
print(list(result)) 



# Need to get multiple integer inputs in the same line

#Way 1:
s = input(">")
print (s)
print(type(s))
s = s.split(',')
print(s)

s = [int(i) for i in s]
print(s)

#Way 2:
s = [int(i) for i in input().split(',')]
print(s)

#Way 3:
s = map(int, input().split(','))
print(list(s))



# How to use if within the map and lambda

list (map(lambda x: True if x % 2 == 0 else False, range(1, 11)))




"""
Reduce
"""

"""
The reduce() function in Python takes in a function and a list as argument. 
The function is called with a lambda function and a list and a new reduced result is returned. 
This performs a repetitive operation over the pairs of the list. 
This is a part of functools module
"""


from functools import reduce

def add(x,y):
    return x+y

print (reduce ( add, [2,18,9,22,17,24,8,12,27]) )


# Reduce with Lambda function 
print (reduce (lambda x,y : x + y,[2,18,9,22,17,24,8,12,27]))


"""
zip
"""

"""
In Python3, zip methods returns a zip object instead of a list. 
This zip object is an iterator. Iterators are lazily evaluated.
Lazy evaluation, or call-by-need is an evaluation strategy which 
delays the evaluation of an expression until its value is needed 
and which also avoids repeated evaluations
Iterators returns only element at a time. 
len function cannot be used with iterators. 
We can loop over the zip object or the iterator to get the actual list
"""


list_a = [1, 2, 3]
list_b = [4, 5, 6,7]

zipped = zip(list_a, list_b) # Output: Zip Object. <zip at 0x4c10a30>

len(zipped) # TypeError: object of type 'zip' has no len()

zipped[0] # TypeError: 'zip' object is not subscriptable


# To iterate the zipped object call next method multiple times
next(zipped)


# Another way 

list_a = [1, 2, 3]
list_b = [4, 5, 6,7]

zipped = zip(list_a, list_b)
list_c = list(zipped) #Output: [(1, 4), (2, 5), (3, 6)]
print (list_c)


# Once we have iterated through the zipped elements, it gets exhausted
list_d = list(zipped) # Output []... Output is empty list becuase by the above statement zip got exhausted.
print (list_d)