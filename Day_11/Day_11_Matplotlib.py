"""
Basics of Matplotlib
    Line Plot
    Scatter Plot
    Bar Chart
    Pie Chart
    Histogram
    Box Plot
"""

# www.https://matplotlib.org/gallery/index.html



import matplotlib
matplotlib.__version__



from matplotlib import pyplot as plt
# Stackoverflow Annual Developer Day Survey

# Age of the developer
x = [25,26,27,28,29,30,31,32,33,34,35]  

# Median Salary of the developer
y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]


plt.plot(x,y)
plt.show()







# Setting the X Label 
plt.xlabel("Ages")

# Setting the Y Label
plt.ylabel("Median Salary (USD)")

plt.title("Median Salary (USD) by Age")
#plt.title("Median Salary (USD) by Age", fontname='Ubuntu', fontsize=14, fontstyle='italic', fontweight='bold')

# Displaying the Grid
plt.grid(True)

# Changing the x axes limits of the scale
plt.xlim(25, 35)

# Changing the y axes limits of the scale
plt.ylim(35000, 75000)

# Or
plt.axis([25, 35, 35000, 75000]);

# Putting a label for the points in the legend
plt.plot(x,y,label='Developer')

plt.legend()

plt.show()







# Setting the style of the plotting
# main visual aspects of the plot such as xticks, legends and labels. 
plt.style.available

#plt.style.use('classic')
#plt.style.use('ggplot')
#plt.style.use('seaborn')
#plt.style.use('fivethirtyeight')
#plt.style.use('grayscale')
#plt.xkcd()

 

#Changing the Color,marker and Line Style
plt.plot(x, y,'k-X')  # 'b-X'  Using Format String techniques (marker,line style,color)
                      

# Changing the marker of the line
plt.plot(x, y, marker='o') # o  .  , x  +  v  ^  <  >  s d 
                     
# Changing the color of the line
plt.plot(x, y, color='green') # #000000    k is for black

# Changing the style of the line
plt.plot(x, y, linestyle='dashed') # solid dashed  dashdot dotted
                                   # -- -. - 

# Changing the width of the line
plt.plot(x, y, linewidth=5) 


plt.show()

plt.savefig("scatter.jpg")





"""
Plotting a Scatter Plot
"""


# For Plotting Scatter Plot
plt.plot(x, y, 'gs') 

# Showing the points on the graph
plt.scatter(x, y)
#plt.scatter(x, y, marker='o')

# Scatter Plot with scatter method 
# o  .  , x  +  v  ^  <  >  s d 
plt.scatter(x, y, marker='.', color='black',label="marker='{0}'".format('.')); 


plt.show()

      

"""
Converting a Line to Bar chart
"""

from matplotlib import pyplot as plt

# Age of the developer
x = [25,26,27,28,29,30,31,32,33,34,35]  

# Median Salary of the developer
y = [38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]

# Setting the X Label 
plt.xlabel("Ages")

# Setting the Y Label
plt.ylabel("Median Salary (USD)")

plt.title("Median Salary (USD) by Age")

# Change the plot funciton to Bar function Vertically
plt.bar(x,y,label='Developer')

plt.legend()

plt.show()



"""
Plotting a Bar chart
"""
import matplotlib.pyplot as plt
 
labels = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
x_index = [0,1,2,3,4,5]

performance = [10,8,6,4,2,1]


# indexes is the first parameter 
plt.bar(x_index, performance, width = 0.8, align='center', alpha=1.0)

# First Parameters is the indexes and second paramters is the labels
plt.xticks(x_index, labels)

plt.ylabel('Usage')

plt.title('Programming Language Usage')
 
plt.show()





"""
Advanced Example of Bar Chart
"""
	
import matplotlib.pyplot as plt

 
# 14 categories of movies
label = ['Adventure', 'Action', 'Drama', 'Comedy', \
         'Thriller/Suspense', 'Horror', 'Romantic Comedy', 'Musical', \
         'Documentary', 'Black Comedy', 'Western', 'Concert/Performance', \
         'Multiple Genres', 'Reality']
index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
 
no_movies = [941,854,4595,2125,942,509,548,149,1952,161,64,61,35,5]



plt.bar(index, no_movies)
plt.xlabel('Genre', fontsize=15)
plt.ylabel('No of Movies', fontsize=15)
plt.xticks(index, label, fontsize=10, rotation=45)
plt.title('Market Share for Each Genre 1995-2017')
plt.show()






"""
Pie chart, where the slices will be ordered and plotted counter-clockwise:
Shows the proportions 
"""

import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')

slices = [60,40]
plt.pie(slices)
plt.show()




import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')

slices = [120,80] 
labels = ['Sixty','Forty']
plt.pie(slices,labels=labels)
plt.show()



# Some Seperators 
import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')

slices = [120,80] 
labels = ['Sixty','Forty']
plt.pie(slices,labels=labels, wedgeprops={'edgecolor':'black'})
plt.show()



# Colors 
# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f

import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')

slices = [120,80,30,20] 
labels = ['Sixty','Forty','Extra1','Extra2']
colors =['blue','red','yellow','green']
#colors =['#008fd5','#fc4f30','#e5ae37','#6d904f']

plt.pie(slices,labels=labels, colors=colors, wedgeprops={'edgecolor':'black'})

plt.show()



import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')          
labels = ('CSE', 'ECE', 'IT', 'EE')
slices = [15, 30, 25, 10]
explode = (0.1, 0, 0, 0)  # explode 1st slice to 10% of the radius

plt.pie(slices, explode=explode,labels=labels, autopct='%.0f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()



# Pie Chart does not look good when comparing more than 5 data 
# Better to use Bar Chart

import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')
# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

plt.pie(slices, labels=labels, autopct='%1.1f%%', shadow=True, startangle=0)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

          
          
        



"""
Histogram - Bar Graph of Frequency 

A histogram is used to summarize discrete or continuous data. 
In other words, it provides a visual interpretation of numerical data by 
showing the number of data points that fall within a specified range of 
values (called "bins").
However, a histogram, unlike a vertical bar graph, shows no gaps between the bars.


X Axis = width = Class Interval
Y Axis = height = Frequency

Creating a histogram provides a visual representation of data distribution.
The median and distribution of the data can be determined by a histogram.
It can show any outliers or gaps in the data.

Types of Distribution
1. Normal distribution
    Points on one side of the average are as likely to occur as on the other 
    side of the average

2. Bimodal distribution
    There are two peaks
    The data should be separated and analyzed as separate normal distributions
    
3. Right-skewed distribution
    A large number of the data values occur on the left side 

4. Left-skewed distribution
    A large number of the data values occur on the right side

5. Random distribution
    Has several peaks

"""


"""
Ramesh is the branch manager at a local bank. 
Recently, Ramesh’s been receiving customer feedback saying that the wait times 
for a client to be served by a customer service representative are too long. 
Ramesh decides to observe and write down the time spent by each customer on waiting.

Write down the wait times spent by 20 customers
[43.1,35.6,37.6,45.3,43.5,40.3,50.2,47.3,31.2,42.2,45.5,30.3,31.4,35.6,45.2,
54.1,45.6,36.5,43.1]

# [25 to 30]                                          [0]
# [30 to 35]     30.3, 31.2, 31.4                     [3]
# [35 to 40]     35.6, 35.6, 36.5, 37.6               [4]
# [40 to 45]     40.3, 42.2, 43.1, 43.1, 43.5         [5]
# [45 to 50]     45.2, 45.3, 45.5, 45.6, 47.3         [5]
# [50 to 55]     50.2, 54.1                           [2]
# [55 to 60]                                          [0]


"""



import matplotlib.pyplot as plt
# Customers wait times in seconds ( n = 20 customers )
customerWaitTime = [43.1,35.6,37.6,45.3,43.5,40.3,50.2,47.3,31.2,42.2,45.5,30.3\
                    ,31.4,35.6,45.2,54.1,45.6,36.5,43.1]

customerWaitTime.sort()
print (customerWaitTime)
# [30.3, 31.2, 31.4, 35.6, 35.6, 36.5, 37.6, 40.3, 42.2, 43.1, 43.1, 43.5, 45.2,
# 45.3, 45.5, 45.6, 47.3, 50.2, 54.1]

# [25 to 30]                                          [0]
# [30 to 35]     30.3, 31.2, 31.4                     [3]
# [35 to 40]     35.6, 35.6, 36.5, 37.6               [4]
# [40 to 45]     40.3, 42.2, 43.1, 43.1, 43.5         [5]
# [45 to 50]     45.2, 45.3, 45.5, 45.6, 47.3         [5]
# [50 to 55]     50.2, 54.1                           [2]
# [55 to 60]                                          [0]


#Ramesh can conclude that the majority of customers wait between 35 and 50 seconds.
 
plt.hist(customerWaitTime,bins=[25,30,35,40,45,50,55,60]) 

plt.axis([25, 60, 0, 6]) 
plt.xlabel('Seconds')
plt.ylabel('Customers')
plt.show()
