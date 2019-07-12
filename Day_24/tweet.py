# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 20:48:29 2019

@author: Ankit Gokhroo
"""

import pandas as pd

# Importing the dataset
dataset_train = pd.read_csv('tweetertrain.csv')
dataset_test=pd.read_csv('tweetertest.csv')

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


from nltk.stem.porter import PorterStemmer
#from nltk.stem.wordnet import WordNetLemmatizer 


corpus = []
#perform row wise noise removal and stemming

for i in range(0,31962):
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
    
    
    
    
        
    
    
    