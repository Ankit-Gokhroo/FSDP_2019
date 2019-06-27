"""
Web Scraping with BeautifulSoup and Requests
"""

# Parsing the content from the website and pulling  the exact information you want


# pip install beautifulsoup4
# pip install lxml
# pip install html5lib

"""
Introduce the concept of basic HTML tags
HTML
  HEAD
    
  HEAD

  BODY
    
  BODY
HTML

"""

from bs4 import BeautifulSoup
import requests

# Create simple html files and 
# parse that using bs4 to make the students understand with title, div etc

with open("simple.html") as html_file :
  soup = BeautifulSoup(html_file, "lxml")
    
print (soup)

print (soup.prettify())


print (soup.title)
print (soup.title.text)


print (soup.div)
print (soup.div.h1)
print (soup.div.h1.text)


# Crome browser ( use the inspect tool to use the find function )
match = soup.find('div')
print (match)
print (soup.find_all('div')[1])

match = soup.find("div", class_= "footer")
print (match)

print ( match.h2 )
print ( match.h2.text )

print ( match.p )
print ( match.p.text )



for article in soup.find_all("div") :
  headline = article.p.text
  print (headline)

# Give students a challenge to print some information from the HTML pages 




# Reading from the Internet
from bs4 import BeautifulSoup   


source = requests.get("http://httpbin.org/html").text
print(source)

soup = BeautifulSoup(source,"lxml")

print (soup)

print (soup.prettify())

print (soup.head)


print (soup.body)

print (soup.body.h1)

print (soup.body.div)

print (soup.body.div.p)

#------------------------------------------------
# Web Scrapping a real Page 

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup
import requests
#import urllib



#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source = requests.get(wiki).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(source,"lxml")

print (soup.prettify())



right_table=soup.find('table', class_='wikitable')

print (right_table.prettify())


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.findAll('tr'):
    # first row has no TH, but other rows have one TH and 6 TD
    cells = row.findAll('td') 
    # first row has 7 TH 
    states = row.findAll('th')
    # other than first row
    if len(cells) == 6:
        A.append(states[0].text.strip())
        #skip the sequence number column
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())


from collections import OrderedDict

col_name = ["State or UN","Admin Cap","Legis Cap","Judi Cap","Year","Capital"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))


# If you want to store the data in a csv file
import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")




"""
Web Scrapping using Selenium
"""
# pip install selenium


#Download 

#https://www.seleniumhq.org/download/
#installation for firefox
#https://github.com/mozilla/geckodriver/
#installation for chrome
#https://sites.google.com/a/chromium.org/chromedriver/




import pandas as pd
from selenium import webdriver

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"


#driver = webdriver.Chrome("C:/Users/rohit/Downloads/chromedriver_win32/chromedriver.exe")
driver = webdriver.Firefox(executable_path="D:/Forsk Technologies/geckodriver")

driver.get(wiki)    # Opening the submission url



right_table=driver.find_element_by_class_name('wikitable')


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
    if len(cells) == 6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["State or UN","Admin Cap","Legis Cap","Judi Cap","Year","Capital"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E,F]))
df = pd.DataFrame(col_data) 
df.to_csv("data/former.csv")


driver.quit()



"""
Real website data scrapping for Kerela Results
"""

from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

#url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"



#browser = webdriver.Chrome("C:/Users/rohit/Downloads/chromedriver_win32/chromedriver.exe")
browser = webdriver.Firefox(executable_path="D:/Forsk Technologies/geckodriver")
browser.get(url)


sleep(2)

 
school_code = browser.find_element_by_name("treg")
code="2000"
school_code.send_keys(code)


sleep(2)


get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')
get_school_result.click()


sleep(5)
 
html_page = browser.page_source

soup = BS(html_page)


sleep(3)


browser.quit()

