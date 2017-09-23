# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import os

class Classifier:
    def __init__(self,whoText, sampleText):
       test_sent = "kathi is a Boy. He is from Hyderabad. He daily exercises and drinks a lot of water. He likes to ride his bike." 
       self.features = self.featuresets(whoText,sampleText)
       self.nbclassifier = self.classifier(self.features)
       self.sents = sent_tokenize(test_sent)
       self.printSentences(self.sents) 


    def featuresets(self,whoTxt,sampleTxt):
        self.who_text = whoTxt
        self.sample_text = sampleTxt
        self.who_words = [(self.feature_extractor(word),'KATHI') for word in self.sample_text.read().split('\n')] + [(self.feature_extractor(word),'PER@') for word in self.who_text.read().split('\n') if '#' not in word]
        return self.who_words
        
    def classifier(self,train_data):
        self.classifier = nltk.NaiveBayesClassifier.train(train_data)
        return self.classifier
        
    def feature_extractor(self,word):
        return {'who':word}
        
    def printSentences(self, sentences):
        for s in sentences:
            for(a,b) in nltk.pos_tag(word_tokenize(sent)):
                if 'NN' in b and self.classifier.classify(self.feature_extractor(a)) == 'PER@':
                    print(s)
    
    
def main():
    scriptpath = os.path.dirname(__file__)
    filename_who = os.path.join(scriptpath,'who.txt')
    filename_sample = os.path.join(scriptpath, 'sample.txt')
    
    whoText = open(filename_who, 'r')
    sampleText = open(filename_sample, 'r')
    Classifier(whoText, sampleText)
main()
    