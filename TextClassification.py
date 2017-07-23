# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 23:16:15 2017

@author: Naruto_kathi
"""

import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)),category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]

#shuffling the documents
random.shuffle(documents)

#printing to test a document
#print(documents[1])

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)


#print top 10 commmonly used words
#print(all_words.most_common(10))

#print the occurance of a word
print(all_words["awesome"])
