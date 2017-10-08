# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import random

class Classifier:

    def __init__(self,whenText, whereText,test_sent,fL):
        self.fL = dict()
        self.features = self.featuresets(whenText,whereText)
        self.classifier(self.features)
        self.sents = sent_tokenize(test_sent)
        self.printSentences(self.sents) 


    def featuresets(self,whenTxt,whereTxt):
        self.when_text = whenTxt
        self.where_text = whereTxt
        self.wh_words = [(self.feature_extractor(word),'WHERE') for word in self.where_text.read().split(',') if '#' not in word] + [(self.feature_extractor(word),'WHEN') for word in self.when_text.read().split(',') if '#' not in word]
        random.shuffle(self.wh_words)
        return(self.wh_words)
        
    def classifier(self,train_data):
        self.classifier = nltk.NaiveBayesClassifier.train(train_data)
        
    def feature_extractor(self,word):
        return {'wh':word}      
    def printSentences(self, sentences):
        self.finalWho = []
        self.finalWhere = []
        self.finalWhen = []
        self.finalWhat = []
        for s in sentences:
            for(a,b) in nltk.pos_tag(word_tokenize(s)):
                count = 0
                if 'NN' in b and self.classifier.classify(self.feature_extractor(a)) == 'WHERE':
                    self.finalWhere.append(s)
                    count+=1
                if 'NN' in b and self.classifier.classify(self.feature_extractor(a)) == 'WHEN' or 'CD' in b:
                    self.finalWhen.append(s)
                    count+=1
                if 'VBD' in b or 'VBG' in b or 'VBN' in b:
                    self.finalWhat.append(s)
                    count+=1
                if count == 0:
                    self.finalWho.append(s)
        
        self.fL.update({"0":self.finalWho})
        self.fL.update({"1":self.finalWhere})
        self.fL.update({"2":self.finalWhen})
        self.fL.update({"3":self.finalWhat})
        print(self.fL)
        #self.fL = self.wh_dict
    
    

    