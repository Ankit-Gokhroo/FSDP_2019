"""
Code Challenge ( Line Plot and Bar Plot )

After a survey by the stackoverflow on its Annual Developer Day the following data were created.

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]


The Median/Avergae salary of the Developer from the age of 18  to  55
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 
49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 
98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]


The Median/Avergae salary of the Python Developer from the age of 18  to  55
py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 
57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 
112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]



The Median/Avergae salary of the Jav Script Developer from the age of 18  to  55
js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 
49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 
102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]



Plot all the three data for the developer, Python Developer and Java Script Developer
on the same plot
The plot should have the valid title,labels, ticks ( x and y ), legend
It should habe different ways to show each 3 lines in different marker, colors, style

Compare all the three types of developer and analyse the plot

Optional :
    Also show the data for all the 3 types of developers using the Bar Chart
Hint: 
    You need to use the index with some padding value to show all the three bars

"""



"""
Code Challenge ( Line Plot )

We have to find sea level rise in past 100 years
Read the file sealevel.csv which has data for 135 years

It has two parts in the data, year and the sea level rise in inches

Read the csv file using the csv reader and create two list
    1) Which stores the years from 1880 to 2014
    2) Which stores the sealevel increase in inches
    
Now plot the data using Line Plot
The plot should have the valid title,labels, ticks ( x and y ), legend

Is the  sea level increasing almost every year.

"""




"""
Code Challenge ( Scatter Plot )

Suppose the result was announced for a class. 
In this class both guys and girls appeared in the exam. 
The goal is to find out who performed better and how to get rid of shortcomings.
We are going to make a scatter plot for that.
Boys are in green while girls in red. 

girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

Are their any outliers

Hint: 
    Use the Scatter method to scatter the data on the plot

"""


"""
Code Challenge ( Bar Plot )
  Name: 
    Zoo Visualisation
  Filename: 
    zoo_visual.py
  Problem Statement:
    Read the zoo.csv file
    Print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    Show the total number of water needs by individual animal using a Bar Chart
  Hint:
      Use the concept of Dictionary
import csv
zoo_data = {}
with open('zoo.csv','rt') as ani:
    reader = csv.reader(ani,delimiter = ',')
    next(reader)
    for i in reader:
        if i[0] in zoo_data:
            zoo_data[i[0]] += int(i[2])
        else:
            zoo_data[i[0]] = int(i[2])

objects = tuple(map(lambda x: x ,zoo_data.keys()))
performance = list(map(lambda x: x ,zoo_data.values()))

"""


"""
Code Challenge ( Bar Plot )
  Name: 
    Most Popular Programming Language out of 28 Languages
  Filename: 
    popular.py
  Problem Statement:
    Read the bardata.csv file
    It has a the survey of 87,570 people at the StackOverFlow Annual Developer Day
    The data has two parts
      1) ID of the Responser
      2) Semicolon seperated data of the languages known by them
    
    We need to now read the csv file using the csv reader and create a dictionary 
    This dictionary should store the Language as the key and value as the number 
    of times the responder has voted for it.
    
    Now display the data in the form of Horizontal Bar Chart to show the popularity of the 
    top 10 languages and the votes from the developer 

  Hint:
      Use the concept of DictReader from csv 
      Also use the concept of Counter class from collections 
      and update it for each row of data
      
      with open ('data.csv') as csv_reader :
          csv_reader = csv.DictReader()
          
          language_counter = Counter()
          
          for row in csv_reader:
              language_counter.update(row['LanguageWorkedWith'].split(';'))
      
      # You could have used the zip function here 
      print(language_counter.most_common(10))
      languages=[]
      popularity=[]
      for item i language_counter.most_common(10):
          languages.append(item[0])
          popularity.append(item[1])
                 
"""




"""
Code Challenge ( Pie Chart )
  Name: 
    university data
  Filename: 
    university_pie.py
  Problem Statement:
    Write a python code and make a pie chart using following conditions:
        1.Read data from csv (University_data.csv)
        2.count GRE score for each university and plot a pie chart
        3.explode minimun gre score university
"""



"""
Code Challenge ( Pie Chart )

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area

Scrap the data from State/Territory and National Share (%) columns for top 6 
states basis on National Share (%). 

Create a Pie Chart using MatPlotLib and explode the state with largest national share %.

"""


