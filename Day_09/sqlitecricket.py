# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 13:17:19 2019

@author: Ankit Gokhroo
"""
"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi
"""




from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text
print(source)

soup = BeautifulSoup(source,"lxml")

print (soup)

print (soup.prettify())

right_table=soup.find('table', class_='table')

print (right_table.prettify())

import sqlite3
from pandas import DataFrame        

conn=sqlite3.connect('icccricketrankingodi.db')

c=conn.cursor()
c.execute ("""CREATE TABLE odiranking(
          Position Integer,
          Team  Text,
          Weighted_matches Integer,
          Points Integer,
          Ratings Integer
          )""")
conn.commit()



for row in right_table.findAll('tr'):
    
    cells = row.findAll('td') 
    
    if len(cells) == 5:
        Position = int(cells[0].text.strip())
        Team = cells[1].text.strip()
        Weighted_matches = int(cells[2].text.strip())
        Points = int(cells[3].text.strip().replace(",",""))
        Ratings = int(cells[4].text.strip().replace(",",""))
        c.execute("INSERT INTO odiranking VALUES({},'{}',{},{},{})".format(Position,Team,Weighted_matches,Points,Ratings))
        conn.commit()
        
c.execute("SELECT * FROM odiranking")

df = DataFrame(c.fetchall())  
df.columns = ["Rank","Team","Weighted Matches","Points","Rating"]

conn.close()    



















