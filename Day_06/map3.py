# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:49:53 2019

@author: Ankit Gokhroo
"""

"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""



def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result

productOfOdds([1,2,3,4,5])

list1=[1,2,3,4,5]

a=list(filter(lambda i :  i%2==1,list1))

b=reduce(lambda i,j:i*j,a)


def productOfOdds(list1):
    return reduce(r_func, filter(f_func, map(m_func, list)))

