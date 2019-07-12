# -*- coding: utf-8 -*- 
"""
Created on Sun Jul  7 21:10:23 2019

@author: Ankit Gokhroo
"""

import pandas as pd

# Importing the dataset
# Ignore double qoutes, use 3 
dataset_train = pd.read_csv('tweetertrain.csv')
dataset_train = dataset_train.sample(n = 1000)
dataset_train= dataset_train.reset_index() 

dataset_test = pd.read_csv('tweetertest.csv')
dataset_test = dataset_test.sample(n = 600)
dataset_test= dataset_test.reset_index()

dataset_train['label'].value_counts()
df1=dataset_train[dataset_train['label']==1]
df2=dataset_train[dataset_train['label']==0]

import re 
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
 
from nltk.stem.porter import PorterStemmer
#from nltk.stem.wordnet import WordNetLemmatizer 
 
corpus = []
#perform row wise noise removal and stemming

for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset_train['tweet'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
     
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
dataset_train['format_tweet']=corpus    
    
 
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 5000)
features = cv.fit_transform(corpus).toarray()
labels = dataset_train['label']

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.40, random_state = 0)



corpus1 = []
#perform row wise noise removal and stemming
        
for i in range(0, 600):
    review = re.sub('[^a-zA-Z]', ' ', dataset_test['tweet'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus1.append(review)
    

cv = CountVectorizer(max_features = 5000)
features1 = cv.fit_transform(corpus1).toarray()
    
    

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)
 
# Predicting the Test set results
labels_pred_knn = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix 
cm_knn = confusion_matrix(labels_test, labels_pred_knn)
score_knn1=classifier.score(features_test,labels_test)+-

 
a=classifier.predict(corpus1)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train,labels_train)
  

# Predicting the Test set results
labels_pred_lr1 = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm1_log1 = confusion_matrix(labels_test, labels_pred_lr1)
score_log1=classifier.score(features_test,labels_test)
score_rf1=classifier.score(features_test,labels_test)

a=dataset_train['label'].value_counts()

from matplotlib import pyplot as plt
# 14 categories of movies
label = ['0','1']
index=[0,1]
no_ = [a[0],a[1]]
plt.bar(index, no_)
plt.xlabel('type', fontsize=15)
plt.ylabel('count', fontsize=15)
plt.xticks(index, label, fontsize=10, rotation=0)
plt.show()

df=pd.DataFrame(labels_test)
df['label'].value_counts()
 
labels_pred_new = classifier.predict(features1)
dataset_test['label']=labels_pred_new

dataset_test['label'].value_counts(0)



