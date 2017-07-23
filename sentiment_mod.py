# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:10:25 2017

@author: Naruto_kathi
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 11:59:15 2017

@author: Naruto_kathi
"""

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
from sklearn.svm import  LinearSVC, NuSVC
from statistics import mode

from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize


class VotedClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
        
    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choosen_votes = votes.count(mode(votes))
        conf_probability = choosen_votes/ len(votes)
        return conf_probability

documents = []
short_pos = open("positive.txt","r").read()
short_neg = open("negative.txt","r").read()

for r in short_pos.split("\n"):
    documents.append((r,"pos"))
for r in short_neg.split("\n"):
    documents.append((r,"neg"))

short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

allwords = []
for w in short_pos_words:
    allwords.append(w.lower())
for w in short_neg_words:
    allwords.append(w.lower())
    
#random.shuffle(allwords)

allwords = nltk.FreqDist(allwords)
#print(allwords.most_common(20))

word_features = list(allwords.keys())[:5000]
#print(word_features,"List of top 50 most common words")

def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return(features)

#This for the moview review documens, which are random    
#find_features(documents[1])

#print(find_features(movie_reviews.words("neg/cv000_29416.txt")))

featuresets = [(find_features(rev),category) for (rev,category) in documents]

#featuresets_save = open("featuresets/featuresets.pickle","rb")
#featuresets = pickle.load(featuresets_save)
#featuresets_save.close()
random.shuffle(featuresets)
#print(featuresets)

training_set = featuresets[:8000]
testing_set = featuresets[8000:]

classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_NB_save = open("classifier/classifier_NB.pickle","wb")
pickle.dump(classifier, classifier_NB_save)
classifier_NB_save.close()

#load classifier from pickle
#classifier_f = open("naivebayes.pickle","rb")
#classifier = pickle.load(classifier_f)
#classifier_f.close()

print("The accuracy of Naive Bayes classifier is : ", (nltk.classify.accuracy(classifier, testing_set))*100)
#classifier.show_most_informative_features(15)

#MultinomialNB_classifier = SklearnClassifier(MultinomialNB())
#MultinomialNB_classifier.train(training_set)
#
##MultinomialNB_classifier_save = open("classifier/MultinomialNB_classifier.pickle","wb")
##pickle.dump(MultinomialNB_classifier, MultinomialNB_classifier_save)
##MultinomialNB_classifier_save.close()
##print("MultinomialNB classifiers accuracy is :",(nltk.classify.accuracy(MultinomialNB_classifier,testing_set)*100))
#
#BerunoulliNB_classifier = SklearnClassifier(BernoulliNB())
#BerunoulliNB_classifier.train(training_set)
#
##BerunoulliNB_classifier_save = open("classifier/BerunoulliNB_classifier.pickle","wb")
##pickle.dump(BerunoulliNB_classifier, BerunoulliNB_classifier_save)
##BerunoulliNB_classifier_save.close()
##print("BerunoulliNB_classifier's accuracy is : ",(nltk.classify.accuracy(BerunoulliNB_classifier, testing_set)*100))
#
# #LogisticRegression, SGDClassifier
##SVC, LinearSVC, NuSVC
#
#LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
#LogisticRegression_classifier.train(training_set)
#
##LogisticRegression_classifier_save = open("classifier/LogisticRegression_classifier.pickle","wb")
##pickle.dump(LogisticRegression_classifier, LogisticRegression_classifier_save)
##LogisticRegression_classifier_save.close()
##print("LogisticRegression_classifier's accuracy is : ",(nltk.classify.accuracy(LogisticRegression_classifier, testing_set)*100))
#
#SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
#SGDClassifier_classifier.train(training_set)
#
##SGDClassifier_classifier_save = open("classifier/SGDClassifier_classifier.pickle","wb")
##pickle.dump(SGDClassifier_classifier, SGDClassifier_classifier_save)
##SGDClassifier_classifier_save.close()
##print("SGDClassifier_classifier's accuracy is : ",(nltk.classify.accuracy(SGDClassifier_classifier, testing_set)*100))
#
#LinearSVC_classifier = SklearnClassifier(LinearSVC())
#LinearSVC_classifier.train(training_set)
#
##LinearSVC_classifier_save = open("classifier/LinearSVC_classifier.pickle","wb")
##pickle.dump(LinearSVC_classifier, LinearSVC_classifier_save)
##LinearSVC_classifier_save.close()
##print("LinearSVC_classifier's accuracy is : ",(nltk.classify.accuracy(LinearSVC_classifier, testing_set)*100))
#
#NuSVC_classifier = SklearnClassifier(NuSVC())
#NuSVC_classifier.train(training_set)
#
##NuSVC_classifier_save = open("classifier/NuSVC_classifier.pickle","wb")
##pickle.dump(NuSVC_classifier, NuSVC_classifier_save)
##NuSVC_classifier_save.close()
##print("NuSVC_classifier's accuracy is : ",(nltk.classify.accuracy(NuSVC_classifier, testing_set)*100))
#
#
#vote_classifier = VotedClassifier(classifier,
#                                  MultinomialNB_classifier,
#                                  BerunoulliNB_classifier,
#                                  LogisticRegression_classifier,
#                                  SGDClassifier_classifier,
#                                  LinearSVC_classifier,
#                                  NuSVC_classifier)
#
#print("vote_classifier's accuracy is : ",(nltk.classify.accuracy(vote_classifier, testing_set)*100))
#print("vote_classifier's classification vote is : ",vote_classifier.classify(testing_set[0][0]), "vote_classifier's confidence is: ", vote_classifier.confidence(testing_set[0][0]))
#
#
#
