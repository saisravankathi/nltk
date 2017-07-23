# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 07:44:58 2017

@author: Naruto_kathi
"""

import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

documents = [(list(movie_reviews.words(fileid)),category)
             for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)
             ]

random.shuffle(documents)

allwords = list(w.lower() for w in movie_reviews.words())

allwords = nltk.FreqDist(allwords)
#print(allwords.most_common(20))

word_features = list(allwords.keys())[:5000]
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

training_set = featuresets[:1500]
testing_set = featuresets[1500:]

#classifier = nltk.NaiveBayesClassifier.train(training_set)
#load classifier from pickle
classifier_f = open("naivebayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("The accuracy of Naive Bayes classifier is : ", (nltk.classify.accuracy(classifier, testing_set))*100)
#classifier.show_most_informative_features(15)

MultinomialNB_classifier = SklearnClassifier(MultinomialNB())
MultinomialNB_classifier.train(training_set)
print("MultinomialNB classifiers accuracy is :",(nltk.classify.accuracy(MultinomialNB_classifier,testing_set)*100))

BerunoulliNB_classifier = SklearnClassifier(BernoulliNB())
BerunoulliNB_classifier.train(training_set)
print("BerunoulliNB_classifier's accuracy is : ",(nltk.classify.accuracy(BerunoulliNB_classifier, testing_set)*100))

 #LogisticRegression, SGDClassifier
#SVC, LinearSVC, NuSVC

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier's accuracy is : ",(nltk.classify.accuracy(LogisticRegression_classifier, testing_set)*100))

SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier's accuracy is : ",(nltk.classify.accuracy(SGDClassifier_classifier, testing_set)*100))

SVC_classifier = SklearnClassifier(BernoulliNB())
SVC_classifier.train(training_set)
print("SVC_classifier's accuracy is : ",(nltk.classify.accuracy(SVC_classifier, testing_set)*100))

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier's accuracy is : ",(nltk.classify.accuracy(LinearSVC_classifier, testing_set)*100))

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier's accuracy is : ",(nltk.classify.accuracy(NuSVC_classifier, testing_set)*100))
