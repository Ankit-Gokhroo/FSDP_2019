# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 23:19:11 2019

@author: Ankit Gokhroo
"""


"""
Code Challenge:
    
http://forsk.in/images/Forsk_logo_bw.png"

Download the image from the url above and store in your workking diretory with the same
name as the image name.

Do not hardcode the name of the image

"""


import requests
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
from PIL import Image
import os


from io import BytesIO
url='https://www.pexels.com/photo/blue-bmw-sedan-near-green-lawn-grass-170811/'

browser = webdriver.Chrome(executable_path="C:\\Users\\Ankit Gokhroo\\Downloads\\Compressed\\chromedriver.exe")

browser.get(url)

get_site_result = browser.find_element_by_xpath('//*[@id="photo-page-top"]/div/div[2]/div/div/div/div/a/span')

img = Image.open(BytesIO(get_site_result.click().content))
img.save("car.png")










from PIL import Image
import requests
from io import BytesIO

url = "http://forsk.in/images/Forsk_logo_bw.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.save("forsk-logo.png")



from PIL import Image
import requests
from io import BytesIO

url='https://www.pexels.com/photo/blue-bmw-sedan-near-green-lawn-grass-170811/'
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.save("car.png")










