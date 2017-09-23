# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import random

class Classifier:

    def __init__(self,whoText, sampleText,test_sent,fL):
        self.fL = fL
        self.features = self.featuresets(whoText,sampleText)
        self.classifier(self.features)
        self.sents = sent_tokenize(test_sent)
        self.printSentences(self.sents) 


    def featuresets(self,whoTxt,sampleTxt):
        self.who_text = whoTxt
        self.sample_text = sampleTxt
        self.who_words = [(self.feature_extractor(word),'KATHI') for word in self.sample_text.read().split('\n')] + [(self.feature_extractor(word),'PER@') for word in self.who_text.read().split('\n') if '#' not in word]
        random.shuffle(self.who_words)
        return(self.who_words)
        
    def classifier(self,train_data):
        self.classifier = nltk.NaiveBayesClassifier.train(train_data)
        
    def feature_extractor(self,word):
        return {'who':word}
        
    def printSentences(self, sentences):
        self.finalList = []
        for s in sentences:
            for(a,b) in nltk.pos_tag(word_tokenize(s)):
                if 'NN' in b and self.classifier.classify(self.feature_extractor(a)) == 'PER@':
                    self.finalList.append(s)
        self.fL += self.finalList
    
    

    