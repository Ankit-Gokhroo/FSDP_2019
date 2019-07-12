# -*- coding: utf-8 -*-
"""
Created on Mon Sep 04 14:53:30 2017

@author: Forsk Technologies
"""

# Natural Language Processing

# Importing the libraries
import pandas as pd

# Importing the dataset
# Ignore double qoutes, use 3 
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t')

# Cleaning the texts
# Noise removal
""" language stopwords 
(commonly used words of a language – is, am, the, of, in etc), 
URLs or links, social media entities (mentions, hashtags), 
punctuations and industry specific words. 
This step deals with removal of all types of noisy entities present 
in the text.
"""

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

#Stemming:  Stemming is a rudimentary rule-based process 
# of stripping the suffixes (“ing”, “ly”, “es”, “s” etc) from a word.
"""
The most common lexicon normalization practices are :

Stemming:  Stemming is a rudimentary rule-based process of stripping the 
suffixes (“ing”, “ly”, “es”, “s” etc) from a word.

Lemmatization: Lemmatization, on the other hand, is an 
organized 
& step by step procedure of obtaining the root form of 
the word, 
it makes use of vocabulary (dictionary importance of words) 
and 
morphological analysis (word structure and grammar relations).
"""

from nltk.stem.porter import PorterStemmer
#from nltk.stem.wordnet import WordNetLemmatizer 


corpus = []
#perform row wise noise removal and stemming

#let's do it on just first row data
review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][0])
review = review.lower()
review = review.split()

review = [word for word in review 
          if not word 
          in set(stopwords.words('english'))]
    
#lem = WordNetLemmatizer() #Another way of finding root word
ps = PorterStemmer()
review = [ps.stem(word) for word in review]
#review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
review = ' '.join(review)
corpus.append(review)

#now do the same for every row in dataset. run to loop for all rows

for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
# Also known as the vector space model
# Text to Features (Feature Engineering on text data)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()
labels = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.20, random_state = 0)

"""
# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_nb = confusion_matrix(labels_test, labels_pred)
"""

#applying knn on this text dataset
# Fitting Knn to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_knn = confusion_matrix(labels_test, labels_pred)







"""
https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/
https://www.analyticsvidhya.com/blog/2014/11/text-data-cleaning-steps-python/
"""

"""
Naive Bayes
https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/
"""

"""
What's the difference between  a naive Bayes classifier and a Bayesian network?


Naive Bayes assumes that all the features are conditionally 
independent of each other. This therefore permits us to use the 
Bayesian rule for probability. Usually this independence 
assumption works well for most cases, if even in actuality
 they are not really independent.
Bayesian network does not have such assumptions. 
All the dependence in Bayesian Network has to be modeled. 
The Bayesian network (graph) formed can be learned by the 
machine itself, or can be designed in prior, by the developer, 
if he has sufficient knowledge of the dependencies.

"""
"""
the usual deep learning libraries that provide 
tensor algebra primitives and few other utilities to 
code models, while at the same time making it more general than other specialized libraries like PyText, StanfordNLP, AllenNLP, and OpenCV.
"""

#Hands On


review = "Poornima got first rank in a tournament held last weak. #poornima"


import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer 

#perform row wise noise removal and stemming

#let's do it on just first row data
review = re.sub('[^a-zA-Z]', ' ', review)
review = review.lower()
review = review.split()

review = [word for word in review if not word in set(stopwords.words('english'))]
    
ps = PorterStemmer()
review = [ps.stem(word) for word in review]

lem = WordNetLemmatizer() #Another way of finding root word
review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]

review = ' '.join(review)





"""
https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568
https://stackabuse.com/implementing-word2vec-with-gensim-library-in-python/
https://www.youtube.com/watch?v=5PL0TmQhItY
https://www.youtube.com/watch?v=NHtohvD7gxY
https://www.samyzaf.com/ML/nlp/nlp.html
"""

"""
Make a code challenge
https://nlpforhackers.io/sentiment-analysis-intro/
"""

"""
https://blog.insightdatascience.com/how-to-solve-90-of-nlp-problems-a-step-by-step-guide-fda605278e4e
"""
