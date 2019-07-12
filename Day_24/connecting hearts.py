# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 11:20:06 2019

@author: Ankit Gokhroo
"""

"""
Q2. Code Challenge (Connecting Hearts)


What influences love at first sight? (Or, at least, love in the first four minutes?) 
This dataset was compiled by Columbia Business School Professors Ray Fisman and Sheena Iyengar 
for their paper Gender Differences in Mate Selection: Evidence from a Speed Dating Experiment.

Data was gathered from participants in experimental speed dating events from 2002-2004. 
During the events, the attendees would have a four minute "first date" with 
every other participant of the opposite sex. At the end of their four minutes, 
participants were asked if they would like to see their date again.

They were also asked to rate their date on six attributes: Attractiveness, 
Sincerity, Intelligence, Fun, Ambition, and Shared Interests.

The dataset also includes questionnaire data gathered from participants at different points in the process.

These fields include: demographics, dating habits, self-perception across 
key attributes, beliefs on what others find valuable in a mate, and lifestyle information.

See the Key document attached for details of every column and for the survey details.

What does a person look for in a partner? (both male and female)


For example: being funny is more important for women than man in selecting 
a partner! Being sincere on the other hand is more important to men than women.

    What does a person think that their partner would look for in them? Do you 
    think what a man thinks a woman wants from them matches to what women 
    really wants in them or vice versa. TIP: If it doesn’t then it will be one sided :)

    Plot Graphs for:
            How often do they go out (not necessarily on dates)?
            In which activities are they interested?
    
    If the partner is from the same race are they more keen to go for a date?
    What are the least desirable attributes in a male partner? Does this differ for female partners?
    How important do people think attractiveness is in potential mate selection vs. its real impact?
"""





import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

dataset=pd.read_csv('Dating_Data.csv', sep=',', engine='python')

dataset.info()
col=list(dataset.columns)

d=dataset[['attr1_1','sinc1_1','intel1_1','fun1_1','amb1_1','shar1_1','match','gender']][dataset['match']==1]
d=d.dropna()

d.info()

d.plot(x='my_timestampe', y='col_A', kind='bar') 
d.plot(x=d['match'], y=['attr1_s','sinc1_s','intel1_s','fun1_s','amb1_s','shar1_s'], kind="barh")
plt.show()




d['gender'].groupby(['attr1_1','sinc1_1','intel1_1','fun1_1','amb1_1','shar1_1'])

d_male=d[['attr1_1','sinc1_1','intel1_1','fun1_1','amb1_1','shar1_1','gender']][d['gender']==1]
d_female=d[['attr1_1','sinc1_1','intel1_1','fun1_1','amb1_1','shar1_1','gender']][d['gender']==0]


a=[np.mean(d_male['attr1_1']),np.mean(d_male['sinc1_1']),np.mean(d_male['intel1_1']),np.mean(d_male['fun1_1']),np.mean(d_male['amb1_1']),np.mean(d_male['shar1_1'])]

labels=['attr1_1','sinc1_1','intel1_1','fun1_1','amb1_1','shar1_1']

index = [0,1,2,3,4,5]
 
plt.bar(index,a)

plt.xticks(index,labels, fontsize=10, rotation=45)
plt.title('Market Share for Each Genre 1995-2017')
plt.show()



b=[np.mean(d_female['attr1_1']),np.mean(d_female['sinc1_1']),np.mean(d_female['intel1_1']),np.mean(d_female['fun1_1']),np.mean(d_female['amb1_1']),np.mean(d_female['shar1_1'])]

labels=['attr1_1','sinc1_1','intel1_1','fun1_1','amb1_1','shar1_1']

index = [0,1,2,3,4,5]
 
plt.bar(index,b)

plt.xticks(index,labels, fontsize=10, rotation=45)
plt.title('Market Share for Each Genre 1995-2017')
plt.show()













