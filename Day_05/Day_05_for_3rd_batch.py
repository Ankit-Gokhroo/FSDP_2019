

"""
What is a Generator?
"""

"""
A generator is a function that behaves like an iterator. 
An iterator loops (iterates) through elements of an object, 
like items in a list or keys in a dictionary. 
A generator is often used like an array, but there are a few differences:

It does not hold results in memory,
It may take longer to run (Trade off using more time for using less space),
It is ‘lazy’: it does not compute results till you need them,
That is, your list is constructed in bits and pieces, 
with each element calculated when you ask for the element.
You can only iterate over them once.
You’ll get a better feel for what generators are as we go through examples in this post.
"""

# How to code a generator
# The first and more tedious way of coding a generator is defining a function 
# that loops over elements in an object and yields elements as it loops.


def my_function (my_list):
    list2=[]
    for item in my_list:
       list2.append(item*item) 
    
    return list2

my_function([1,2,3,4,5])

def my_function2 (my_list):
    for item in my_list:
       yield item*item 

my_function2([1,2,3,4,5])
 

#Method 1:

def my_generator(my_list):
    print("This runs the first time you call next().")
    for i in my_list:
        yield i*i

input_list =[1,2,3,4,5]
# Full 'list' would be [1, 4, 9, 16, 25]
gen1 = my_generator(input_list)

next(gen1)
# This runs the first time you call next(). <- printout
# 1

next(gen1)
# 4 (since 2*2=4)


# After running out of elements
next(gen1)
# StopIteration
#Yield is used like return, but (1) it returns a generator, 
#and (2) when you call the generator function, 
#the function does not run completely. 
#[1] The function just returns the generator object. 
#Every time you call next() on the generator object, 
#the generator runs from where you stopped before to the next occurrence of yield.


#Method 2:

#The second way of coding generators is similar to that of coding list comprehensions. It’s much more compact than the previous method:

input_list =[1,2,3,4,5]
# Full 'list' would be [1, 4, 9, 16, 25]
gen2 = (i*i for i in input_list)
#When the generator has run out of entries, it will give you a StopIteration exception.

next(gen2)


"""
Regular Expressions
"""

import re
"""
search() versus match()
The match() function checks for a match only at the beginning of the string (by default) 
The search() function checks for a match anywhere in the string.
"""

"""
findAll()
findall(pattern, string, flags=0)
Finds all the possible matches in the entire sequence and 
returns them as a list of strings. Each returned string 
represents one match.
"""
#-------------------------------------
"""
There are methods like start() and end() to know the 
start and end position of matching pattern in the string.
"""


result = re.search(r'forsk', 'Forsk forsk Summer Bootcamp')

print (result.start())
print (result.end())

result = re.match(r'Forsk', 'Forsk forsk forsk Summer Bootcamp')

print (result.start())
print (result.end())

#-------------------------------------

pattern=re.compile('mm')

result=pattern.findall('Forsk Summer Bootcammp')
print (result)
     
#------------------------------------
result=re.findall(r'\w{3}','ForskSummerBootcamp')
print (result)

#to skip blanks
result=re.findall(r'\w+','Forsk Summer Bootcamp')
print (result)

#-----------------------------------
result=re.findall(r'^\w+','Forsk Summer Bootcamp')
print (result)

#To find end
result=re.findall(r'\w+$','Forsk Summer Bootcamp')
print (result)

result=re.findall(r'\w\w','Forsk Summer Bootcamp')
print (result)

#-----------------------------------
result=re.findall(r'@\w+\.\w+\.*\w*','abc.test@gmail.com, xyz@test.in, test.first@company.com nimish@gmail.co.in')
print (result)



#-----------------------------------
#find date format numbers
result=re.findall(r'\d{2}-\d{2}-\d{4}','Kunal 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print (result)

#----------------------------------

li=['+91-7999999999', \
    '399999-999', \
    '99999x9999', '2999999999']


for val in li:
 if re.findall(r'\+?[0-9]{0,2}-?[1-9]{1}[0-9-]{9}',val):
     print ('yes')
 else:
     print ('no')




