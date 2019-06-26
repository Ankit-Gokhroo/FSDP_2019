# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:02:27 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""

input_file=input('enter file name')
char = 0
word=0
unique_words=set()

with open(input_file+".txt",mode='rt') as rf:
    
    l=rf.readlines()
    lines=len(l)
    for i in rf:
        char += len(i)
        word+=  len(i.split())
        unique_words.update(i.split())
   
#print(char)
#print(word)
#print(len(unique_words))

        lines=len(l)
        a= i.split()
        for j in a:
            if j not in unique_words:
                unique_words.append(j)
            else:
                pass
    
            
    #r=str(l)
    #char=len(r.split())
    
    