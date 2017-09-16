# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 22:59:59 2017

@author: Naruto_kathi
"""

"""Modes to open a file"""

#    'r' : use for reading
#    'w' : use for writing
#    'x' : use for creating and writing to a new file
#    'a' : use for appending to a file
#    'r+' : use for reading and writing to the same file


import nltk
from nltk.tokenize import word_tokenize, sent_tokenize


def featuresets():
    who_text = open('Questions\\who.txt', 'r')
    sample_text = open('Questions\\sample.txt', 'r')
    who_words = [(feature_extractor(word),'KATHI') for word in sample_text.read().split('\n')] + [(feature_extractor(word),'PER@') for word in who_text.read().split('\n') if '#' not in word]
    return who_words
def classifier(train_data):
    classifier = nltk.NaiveBayesClassifier.train(train_data)
    return classifier
def feature_extractor(word):
    return {'who':word}
    
    
if __name__ == '__main__':
    test_sent = "kathi is a Boy. He is from Hyderabad. He daily exercises and drinks a lot of water. He likes to ride his bike."
    l = featuresets()
    c= classifier(l)
    sents = sent_tokenize(test_sent)
    #print(c.classify(feature_extractor('Hyderabad')))
    #print(nltk.classify.accuracy(c,[({'who':'Boy'},'PER@'),({'who':'Kathi'},'KATHI')]))
    for sent in sents:
       for (a,b) in nltk.pos_tag(word_tokenize(sent)):
           if 'NN' in b and c.classify(feature_extractor(a)) == 'PER@':
               print(sent)
    