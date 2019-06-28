"""
Panel Data = Pandas 

EDA ( Exploratory Data Analysis )

Using Pandas, we can accomplish five typical steps in the processing and 
analysis of data, regardless of the origin of data — 
load, prepare, manipulate, model, and analyze.

pip install pandas

Pandas deals with the following three data structures −
    Series      -   1 Dimensional 
    DataFrame   -   2 Dimensional 
    Panel       -   3 Dimensional 

DataFrame is a container of Series, Panel is a container of DataFrame.
(Visualisation of Data Frame)


Series is a one-dimensional array like structure with homogeneous data with immutable size. 


DataFrame ( tabular Data ) is a two-dimensional array with heterogeneous data with mutable size.
think of index (the rows) and the columns rather than axis 0 and axis 1.


Panel is a three-dimensional data structure with heterogeneous data.
Graphical Representation is similar to the 3D Array
Layers for tabular data 
(3d_visualisation.jpg)

"""

#Import Python Libraries

import pandas as pd

"""
Create an Empty Series
"""
s = pd.Series()
print (type(s))
print (s)


"""
Create a Series from list
"""
import pandas as pd

thelist = [ 'sentence 1', 'sentence 2', 'sentence 3' ]
s = pd.Series( thelist )
print (s)



"""
Create a Series from ndarray
"""
import numpy as np
import pandas as pd
data = np.array(['a','b','c','d'])
print (type(data ))

s = pd.Series(data)
print (type(s))
print (s)
# We did not pass any index, so by default, 
# it assigned the indexes ranging from 0 to len(data)-1

# This returns range which can be converted to list
print (s.index[:])

# This returns ndarray 
print (s.values[:])




"""
Customised Index value
"""
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print (s)


"""
Accessing Data from Series with Position
"""
# Data in the series can be accessed similar to that in an ndarray.
# No doubt we have given indexes, but we are accessing using position 
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print (s)

#retrieve the first element
print (s[0])

#retrieve the first three element
print (s[:3])


#retrieve the last three element
print (s[-3:])


"""
A Data frame is a two-dimensional data structure, i.e., 
data is aligned in a tabular fashion in rows and columns.
You can think of it as an SQL table or a spreadsheet data representation
"""




"""
Create an Empty DataFrame
"""
import pandas as pd
df = pd.DataFrame()
print (df)


"""
Create a DataFrame from Lists
"""
import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df) 



"""
Create a DataFrame from List of Lists
"""
import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)





"""
# Create a DataFrame from Dict of Series
# Dictionary of Series can be passed to form a DataFrame. 
# The resultant index is the union of all the series indexes passed.
import pandas as pd
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)



# Row Selection by Label or index
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)

print (type(df.loc['b']))
print (df.loc['d'])
# The result is a series with labels as column names of the DataFrame.
# And, the Name of the series is the label with which it is retrieved.


# Selection by integer location
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print (df)
print (type(df.iloc[1]))
print (df.iloc[1]) # position by default starts from 0 for the indexes 

"""

"""
1. Getting and Knowing Your Data
2. Filtering and Sorting
3. Grouping
4. Apply
5. Merge
6. Stats
7. Visualisation
8  Creatig Series and Data FRame
9. Time Series
10. Deleting
11 Indexing

    Read and examine a dataset and classify variables by their type: quantitative vs. categorical
    Handle categorical variables with numerically coded values
    Perform univariate and bivariate analysis and derive meaningful insights about the dataset
    Identify and treat missing values and remove dataset outliers
    Build a correlation matrix to identify relevant variables

Indexing
Computation
Grouping
Aggregation

"""

#df = pd.read_csv("https://bitbucket.org/ntpl_sylvester/dataset/raw/467616310ddfaf8abbbbc13bdf1e32cdf0842cbd/Salaries.csv")
#df = pd.read_csv("https://bitbucket.org/ntpl_sylvester/dataset/raw/467616310ddfaf8abbbbc13bdf1e32cdf0842cbd/training_titanic.csv")

import pandas as pd
#Read csv file
df = pd.read_csv("Salaries.csv")

# Not a good technique to print the Data Frame
print (df)


df.info()  # phd and salary column has 76 entries, 2 missing or not null values


#number of dimensions
df.ndim   


#return a tuple representing the dimensionality
df.shape 


#number of elements
df.size    #( 78 * 6 = 468 )


#List first 5 records
df.head()


#Try to read the first 10, 20, 50 records;
#Can you guess how to view the last few records;


df.tail(5)


# Gives the row Indexes
df.index        # list(df.index) or df.index.tolist()


#list the column names / column Indexes
df.columns      # list(df.columns) df.columns.tolist()


#Check types for all the columns
df.dtypes


#list the row labels/index and column names
df.axes


#numpy representation of the data
df.values   # return ndarray of ndarray


# generate descriptive statistics (for numeric columns only)
# Standard Deviation is quite useful tool to figure out 
# how the data is spread above or below the mean.
# The higher the value, the less is reliable or vice versa. 
df.describe() # For Numeric Columns only
              # This gives a missing values in salary and phd columns


# In order to see statistics on non-numerical features,
#df.describe(include=['object', 'bool','float64','int64'])
df.describe(include=['object', 'bool'])
#df.describe(include=['float64','int64'])
df.describe(include=['object','float64','int64'])


#return max/min values for all columns in form of Series
df.max() 
df.min()

#return max/min values for all numeric columns
df.mean()
df.median()
df.std()

#What are the mean values of the first 50 records in the dataset?
df.head(50).mean()

#returns a random sample of the data frame
df.sample(5) 




"""
Data Frames: method loc

If we need to select a range of rows, using their labels/index 
we can use method loc
"""

df.loc[:1]   # Both are inclusive for row
df.loc[10:20]

df.loc[10:20,['rank', 'phd']]


"""
Data Frames: method iloc

If we need to select a range of rows and/or columns, 
using their positions we can use method iloc
"""

df.iloc[:2] # 2 is not inclusive for row
df.iloc[ 10:21]

df.iloc[ 10:21 , [0,4] ]


df.iloc[0] # First row of a data frame

df.iloc[1:5, :-1] # Leave last columns

df.iloc[:, 0] # First column

df.iloc[:, -1] # Last column

df.iloc[0:7] #First 7 rows

df.iloc[:, 0:2] #First 2 columns

df.iloc[1:3, 0:2] #Second through third rows and first 2 columns

df.iloc[[0,5], [1,3]] #1st and 6throws and 2nd and 4thcolumns




"""
some_df = df.iloc[10:20,]
print(some_df)

# Since some_df is a new dataframe has total 10 records 
some_df.iloc[11:20,:]  # Accessing 11th record which is not there
some_df.iloc[0:10,:]

some_df.iloc[0]

some_df.loc[0]  # 0 is not there in the Row Index, 
some_df.loc[10]

# Position is starting from 0 onwards but the 
# index is same starting from 10 
some_df.loc[10:19,:]
"""


"""
Selecting a column in a Data Frame with all rows
"""

df.iloc[:,2]

df.loc[:,'phd']
 
# Read the data from a specific Series
df.phd
# Dont use this technique
df.rank

#Use this one
df['rank']
# This is the best practice 
df['phd']



#Select column rank and salary:
df[['rank','salary']]


# Find unique values in a Series / Column
#df['rank'].unique()
#df['discipline'].unique()
df['sex'].unique()
list1 = df['sex'].unique().tolist()
print(list1)


# intuition about a Rank Series
df['rank']

series=df['rank'].value_counts()
print (series.index[:].tolist())
print (series.values[:].tolist())
#Or
list2 = df['rank'].value_counts().tolist()
print(list2)



# to show in Percentage 
df['sex'].value_counts(normalize = True)


# To know the count of male and female candidates
df['sex'] 
df['sex'].value_counts()
df['sex'].value_counts(normalize = True)

# count missing values 
# ( It also counts the NaN Values in the Series/Column)
#df['sex'].value_counts(dropna=True)
#df['sex'].value_counts(dropna=False)

df['phd'].value_counts()
df['phd'].value_counts(dropna=False)

#df['salary'].value_counts()
#df['salary'].value_counts(dropna=False)


#calculate the basic statstics on the salary column
df['salary'].mean()
df['salary'].std()
df['salary'].describe()


#Find how many values in the salary column which are non NaN (use count method);
df['salary'].count()
df['phd'].count()


"""
Boolean Indexing
"""
# Find those rows which has null values in salary/phd column
df['salary'].isnull()
df[df['salary'].isnull()]
#or
df.loc[df['salary'].isnull()]


df['phd'].isnull()
df[df['phd'].isnull()]
#or
df.loc[df['phd'].isnull()]

 

"""
Data Frames groupby method

Using "group by" method we can:
Split the data into groups based on some criteria
Calculate statistics (or apply a function) to each group
"""

"""
Want to calculate how many are Assoc, Asst and Professors
"""
#Group data using rank
df_rank= df.groupby(['rank'])
df['rank'].value_counts()
df_rank.size()
df_rank.count() 


df_rank.groups    # Groups returns a dictionary object with list as its value and group name as key
df_rank.groups['AssocProf']  # df['rank'].unique() 
df_rank.groups['AssocProf'][0]

df.loc[df_rank.groups['AssocProf'][0]]



#group data using rank followed  by discipline and sex
df_rank=df.groupby(['rank', 'discipline','sex'])
df_rank.size()
df_rank.count() 

df_rank.groups
df_rank.groups.keys()

 
#Calculate mean value for each numeric column per each group
df_rank.mean()


#Calculate min/max/mean salary for each type(Assoc,Asst,Prof) of professor rank:
df.groupby('rank')[['salary','phd']].min()
df.groupby('rank')[['salary','phd']].max()
df.groupby('rank')[['salary','phd']].mean()
        


"""
Data Frame: filtering

To subset the data we can apply Boolean indexing. 
This indexing is commonly known as a filter. 
For example if we want to subset the rows in which the salary
 value is greater than $120K:

"""

# Boolean Indexing in Pandas
# select only those professors who has salary more than 120000
df['salary'] > 120000
df_sub= df[df['salary'] > 120000 ] # return DataFrame
df_sub

#or

df.loc[df['salary'] > 120000]


# to display only the selected series/column
df.loc[df['salary'] > 120000,'salary']
# or
df_sub['salary']



#filter using multiple columns

df_sub= df[(df['salary'] > 120000) & \
           (df['phd'] > 10) & \
           (df['sex'] == 'Female' )
           ]
df_sub
# Or

df.loc[(df['salary'] > 120000) & \
           (df['phd'] > 10) & \
           (df['sex'] == 'Female' )]



#Select salary and sex of only those rows that contain female faculty:
df_sub = df[df['sex'] == 'Female' ][['salary','sex']]
df_sub

# Or

df.loc[df['sex'] == 'Female' ][['salary','sex']]


"""
Deleting outliers
"""
#df = df.drop(df[(df['GrLivArea']>3000) & (df['GrLivArea']<6000)].index)



"""
DataFrame sorting
"""

# Create a new data frame from the original sorted by the column Salary
df_sorted= df.sort_values( by='service')
df_sorted.head()

# To find the lowest salary of the employee
df_sorted= df.sort_values( by='salary', ascending = [True])
df_sorted.head(1)


# To find the highest salary of the employee
df_sorted= df.sort_values( by='salary', ascending = [False])
df_sorted.head(1)


#We can sort the data using 2 or more columns:
df_sorted= df.sort_values( by=['service','salary'], ascending = [True,True])
df_sorted.head(10)

df_sorted= df.sort_values( by=['service','salary'], ascending = [True,False])
df_sorted.head(10)


"""
Missing Values

Missing values are marked as NaN
dropna(how='all') >> Drop observations where all cells is NaN
dropna(axis=1, how='all') >> Drop column if all the values are missing
dropna(thresh = 5) >> Drop rows that contain less than 5 non-missing values
fillna(0) >> Replace missing values with zeros
isnull() >> returns True if the value is missing
notnull() >> Returns True for non-missing values


Code to find missing values

total = df.isnull().sum(axis=1).sort_values(ascending=False)
percent = (df.isnull().sum(axis=1)/df.isnull().count(axis=1)).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total_missing_values_per_row', 'Percent'])
missing_data.head(20)



"""

# mark zero values as missing or NaN
df['salary'] = df['salary'].replace(0, np.NaN)


df.info()

#return a matrix by checking individual values
df.isnull()

#which column has null values in the Data Frame
df.isnull().any(axis=0)

#Check the rows that has atleast one NaN values
df.isnull().any(axis=1)

# Select the rows that have at least one missing value
df[df.isnull().any(axis=1)]

# Find those rows in which phd column has NaN
df[df['phd'].isnull()]

# Find those rows in which salary column has NaN
df[df['salary'].isnull()]

  

#There are a number of methods to deal with missing values in the data frame:
new_df = df.dropna()
new_df.count()

"""
Approach: Remove records (rows) that contain a missing value
df_copy = df.copy().dropna(how='any')
df_copy.shape


df_copy = df.copy().dropna(how='all')
df.shape
"""


new_df2 = df.fillna(100)
new_df2.count()


# Fill All columns with missing values, with mean of that column
df = df.fillna(df.mean())
df

# fill all the records with missing values, with mean of that column
df['phd'] = df['phd'].fillna(df['phd'].mean())

# fill all the records with missing values, with mean of that column
df['salary'] = df['salary'].fillna(df['salary'].median())



# How to drop columns
df.drop('discipline',axis=1, inplace=True)

"""
# Remove the $ Sign from the Salary Column and then converted the string field into numeric
df['salary'] = df['salary'].str.replace('INR','').str.replace(',','')
df['salary'] = pd.to_numeric(df['salary'])

"""
# Creating a new Column based on some other columns values 
# Male == 0 and Female == 1
df["bool_sex"] = df["sex"].map(lambda x: 0 if x == 'Male' else 1 )
df



"""
Value Conversion using apply function 
# Male == 0 and Female == 1
"""

df = pd.read_csv("Salaries.csv")
df["sex"]

def gender_code(gender_string):  
    if (gender_string == "Male") :
        return 0
    elif (gender_string == "Female") :
        return 1   
    
#    if isinstance(gender_string, float) and math.isnan(gender_string):

df["sex"].value_counts(dropna=False)

df["sex"] = df["sex"].apply(gender_code)

df["sex"].value_counts(dropna=False)
df['sex']


# Iterating over rows 
for i, row in df.iterrows():
    print("Index {}".format(i))
    print("Row \n{}".format(row))


# Add examples to use eval and query and where

# Create a new column called df.Child where the value is yes
# if df.age is greater than 50 and no if not
# df['child'] = np.where(df['age']<18, 'yes', 'no')




"""
Analysis of Salaries Data ( Hand On Activity )

1. Which Male and Female Professor has the highest and the lowest salaries
2. Which Professor takes the highest and lowest salaries.
3. Missing Salaries - should be mean of the matching salaries of those 
   whose service is the same
4. Missing phd - should be mean of the matching service 
5. How many are Male Staff and how many are Female Staff. 
   Show both in numbers and Graphically using Pie Chart.  
   Show both numbers and in percentage
6. How many are Prof, AssocProf and AsstProf. 
   Show both in numbers adn Graphically using a Pie Chart
7. Who are the senior and junior most employees in the organization.
8. Draw a histogram of the salaries divided into bin starting 
   from 50K and increment of 15K
"""



# Data Preeprocessing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Loading the dataset
data = pd.read_csv("Salaries.csv")
    
"""
1. Which Male and Female Professor has the highest and the lowest salaries
"""
# Use the concept of Filtering and Boolean Indexing
male_professor = data[(data['sex']=='Male') & (data['rank']=='Prof')].sort_values('salary')
female_professor = data[(data['sex']=='Female') & (data['rank']=='Prof')].sort_values('salary')

print(male_professor[male_professor['salary'] == male_professor['salary'].max()])
print(male_professor[male_professor['salary'] == male_professor['salary'].min()])

print(female_professor[female_professor['salary'] == female_professor['salary'].max()])
print(female_professor[female_professor['salary'] == female_professor['salary'].min()])

"""
2. Which Professor takes the highest and lowest salaries.
"""
prof_data = data[data['rank']=='Prof'].sort_values('salary')
#prof_data['salary'] = prof_data['salary'].fillna(np.mean(prof_data['salary']))
#prof_data['salary'] = prof_data.groupby('service')['salary'].apply(lambda x: x.fillna(x.mean()))

print(prof_data[prof_data['salary'] == prof_data['salary'].max()])
print(prof_data[prof_data['salary'] == prof_data['salary'].min()])

   
"""
#Alternative 1 
prof_data = data[data['rank']=='Prof']
prof_data['salary'] = prof_data.groupby('service')['salary'].apply(lambda x: x.fillna(x.mean()))
max_salary = max(prof_data['salary'])
min_salary = min(prof_data['salary'])
    

#Alternative 2
prof_data = data[data['rank']=='Prof']
salary_data = np.array(prof_data['salary'])
salary_data = salary_data[~np.isnan(salary_data)]
max_salary = np.max(salary_data)
min_salary = np.min(prof_data['salary'])
"""
   
"""
3. Missing Salaries - should be mean of the matching salaries of those whose service is the same
"""
#data['salary'] = data.groupby('discipline')['salary'].apply(lambda x: x.fillna(x.mean()))
   
# First Finding the mean of the salries according to the different discipline 
a = data['salary'][data['discipline'] == 'A'].mean()
b = data['salary'][data['discipline'] == 'B'].mean()
    
# Filling the mean salaries for the different categories of discipline
data['salary'][data['discipline'] == 'A'] = data['salary'].fillna(a)
data['salary'][data['discipline'] == 'B'] = data['salary'].fillna(b)

    
"""
4. Missing phd - should be mean of the matching service 
"""
#data['phd'] = data.groupby('discipline')['phd'].apply(lambda x: x.fillna(x.mean()))
    
# First Finding the mean of the phd according to the different discipline 
a1 = data['phd'][data['discipline'] == 'A'].mean()
b1 = data['phd'][data['discipline'] == 'B'].mean()
    
# Filling the mean phd by rounding its value for the different categories of discipline
data['phd'][data['discipline'] == 'A'] = data['phd'].fillna(round(a1))
data['phd'][data['discipline'] == 'B'] = data['phd'].fillna(round(b1)) 


"""
5. How many are Male Staff and How many are Female Staff. 
"""
# Show both in numbers and Graphically using Pie Chart.  
# Show both numbers and in percentage
data_gender = data['sex'].value_counts().reset_index()
"""Alternative-
1.data_gender = data.groupby('sex').size().reset_index()
2. data_gender = pd.DataFrame(data['sex'].value_counts())
"""
data_gender_ref = pd.DataFrame()
data_gender_ref['Male'] = [data_gender['sex'][0]]
data_gender_ref['Female'] = [data_gender['sex'][1]]   
 
vis1 = plt.pie([data_gender_ref['Male'], data_gender_ref['Female']], explode=[0, 0], labels=['male','female'], autopct="%1.1f%%")
plt.axis('equal')
plt.show(vis1)
    
# Function to show the actual values in pie chart
def absolute_value(val):
   a  = np.round(val/100.*(np.array([39,39])).sum(), 0)
   return a

vis2 = plt.pie([data_gender_ref['Male'], data_gender_ref['Female']], explode=[0, 0], labels=['male','female'], autopct=absolute_value)
plt.axis('equal')
plt.show(vis2)
    
"""
6. How many are Prof, AssocProf and AsstProf. 
"""
# Show both in numbers and Graphically using a Pie Chart
data_rank = data['rank'].value_counts().reset_index()
data_rank_ref = pd.DataFrame()
data_rank_ref['Prof'] = [data_rank['rank'][0]]
data_rank_ref['AsstProf'] = [data_rank['rank'][1]]
data_rank_ref['AsscProf'] = [data_rank['rank'][2]]
    
vis3 =  plt.pie([data_rank_ref['Prof'], data_rank_ref['AsstProf'],data_rank_ref['AsscProf'] ], explode=[0, 0,0], labels=['Prof','AsstProf', 'AsscProf'], autopct="%1.1f%%")
plt.axis('equal')
plt.show(vis3)


def absolute_value(val):
    a  = np.round(val/100.*(np.array([46,19,13])).sum(), 0)
    return a

vis4 = plt.pie([data_rank_ref['Prof'], data_rank_ref['AsstProf'],data_rank_ref['AsscProf'] ], explode=[0, 0,0], labels=['Prof','AsstProf', 'AsscProf'], autopct=absolute_value)
plt.axis('equal')
plt.show(vis4)
    
"""
7. Who are the senior and junior most employees in the organization.
"""
data_service = data.sort_values(['service'])
print(data_service[data_service['service'] == data_service['service'].max()])
print(data_service[data_service['service'] == data_service['service'].min()])
   

"""
8. Draw a histogram of the salaries divided into bin starting from 50K and increment of 15K
"""
import matplotlib.pyplot as plt
plt.hist(data['salary'].dropna(), bins=range(50000, 190000, 15000), facecolor='g')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Salary distribution')
plt.grid(True)
plt.show()

"""
plt.hist(data['salary'].dropna(), bins=range(50000, 190000, 15000), facecolor='g')
This error occurs among other things when you have NaN values in the Series. Could that be the case?

These NaN's are not handled well by the hist function of matplotlib.
"""

#distribution of salary using histogram with pandas
new_df = df['salary']
new_df.hist(bins=20,grid=False)




