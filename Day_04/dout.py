# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:42:02 2019

@author: Ankit Gokhroo
"""

//*[@id="container"]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div/a/div[3]/div[1]/div[1]




import requests
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
from PIL import Image
import os



url="https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

source=requests.get(url).text

print(source)

soup = BeautifulSoup(source,"lxml")

print (soup)

print (soup.prettify())

right_price=soup.find('price', class_='!-- Twitter Meta Data --')

print (right_price.prettify())
