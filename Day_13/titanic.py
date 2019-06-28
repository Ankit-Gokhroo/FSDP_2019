"""
Code Challenge
  Name: 
    Exploratory Data Analysis - Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""
import pandas as pd
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

df=pd.read_csv('training_titanic.csv')
df.info()
#age,cabin,embarked has null values

df.describe()
df.columns
df.dtypes
df.head()
#How many people in the given training set survived the disaster ?
a=df['Survived'].value_counts()
#342 people survived 


#How many people in the given training set died ?
#549 people died
#Calculate and print the survival rates as proportions (percentage) by setting the normalize argument to True.
b=df['Survived'].value_counts(normalize=True)*100
slices = [b[0],b[1]] 
labels = ['dead','survived']
plt.pie(slices,labels=labels,autopct='%.0f%%')
plt.show()
#61.61% were died
#38.38% were survived

# Males that survived vs males that passed away
df[(df['Sex']=='male') & (df['Survived']==1)]
df1.info()
#109 males are survived

# Males that not survived vs males that passed away
df2=df[(df['Sex']=='male') & (df['Survived']==0)]
df2.info()
#468 males are not survived

# Females that survived vs males that passed away
df3=df[(df['Sex']=='female') & (df['Survived']==1)]
df3.info()
#233 females are survived

# Females that not survived vs males that passed away
df4=df[(df['Sex']=='female') & (df['Survived']==0)]
df4.info()
#81 females are not survived


df['Age'] = df['Age'].fillna(df['Age'].mean())
#average age is 29.69 years filled at nan places

df['bool_child_age']=df['Age'].map(lambda x:0 if x>18 else 1)

df5=df[(df['bool_child_age']==1) & (df['Survived']==1)]
#70 childrens were survived

df6=df[(df['bool_child_age']==1) & (df['Survived']==0)]
#69 children were died

df7=df[(df['bool_child_age']==0) & (df['Survived']==1)]
#272 people of age greater than 18 are survived

#Compare the normalized survival rates for those who are <18 and those who are older. 
data = df["bool_child_age"][df["Survived"]==1].value_counts(normalize=True)*100
#79.5% people of age gretaer than 18 survived and 20.46% childrens survived
 