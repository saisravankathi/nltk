# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 07:44:58 2017

@author: Naruto_kathi
"""

import nltk
import random
from nltk.corpus import movie_reviews
import pickle

documents = [(list(movie_reviews.words(fileid)),category)
             for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)
             ]

random.shuffle(documents)

allwords = list(w.lower() for w in movie_reviews.words())

allwords = nltk.FreqDist(allwords)
#print(allwords.most_common(20))

word_features = list(allwords.keys())[:3000]
#print(word_features,"List of top 50 most common words")

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return(features)

#This for the moview review documens, which are random    
#find_features(documents[1])

#print(find_features(movie_reviews.words("neg/cv000_29416.txt")))

featuresets = [(find_features(rev),category) for (rev,category) in documents]

#print(featuresets)

training_set = featuresets[:1000]
testing_set = featuresets[1000:]

#classifier = nltk.NaiveBayesClassifier.train(training_set)
#load classifier from pickle
classifier_f = open("naivebayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("The accuracy of Naive Bayes classifier is : ", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

#saving it in a pickle file

#save_classifier = open("naivebayes.pickle","wb")
#pickle.dump(classifier, save_classifier)
#save_classifier.close()


