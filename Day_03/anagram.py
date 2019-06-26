# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:30:30 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Anagram
  Filename: 
    anagram.py
  Problem Statement:
   Two words are anagrams if you can rearrange the letters of one to spell the second.  
   For example, the following words are anagrams:
   ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']
  
   create a function which takes two arguments and return whether they are angram or no ( True or False)
  Hint: 
   How can you tell quickly if two words are anagrams?  
   Dictionaries allow you to find a key quickly.  

"""

def pangram(first_word,second_word):
    if len(first_word)==len(second_word):
        if sorted(first_word)==sorted(second_word):
            return True
    else:
        return False
    
first_word=input('enter first word')
second_word=input('enter second word')

result=pangram(first_word,second_word)



if result==True:  
    print('pangram')
else:
    print('not pangram')    
        