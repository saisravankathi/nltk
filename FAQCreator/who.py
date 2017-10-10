# -*- coding: utf-8 -*-
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
import random

class Classifier:

    def __init__(self,whenText, whereText,whoText,test_sent,question,fL):
        self.fL = dict()
        self.fSet = set([])
        self.features = self.featuresets(whenText,whereText,whoText)
        self.classifier(self.features)
        self.sents = sent_tokenize(test_sent)
        self.printSentences(self.sents,question) 


    def featuresets(self,whenTxt,whereTxt, whoTxt):
        self.when_text = whenTxt
        self.where_text = whereTxt
        self.who_text = whoTxt
        self.wh_words = [(self.feature_extractor(word),'WHERE') for word in self.where_text.read().split(',') if '#' not in word] + [(self.feature_extractor(word),'WHEN') for word in self.when_text.read().split(',') if '#' not in word]+[(self.feature_extractor(word),'WHO') for word in self.who_text.read().split(',')]
        random.shuffle(self.wh_words)
        return(self.wh_words)
        
    def classifier(self,train_data):
        self.classifier = nltk.NaiveBayesClassifier.train(train_data)
        
    def feature_extractor(self,word):
        return {'wh':word.lower()}      
    def printSentences(self, sentences,question):
        self.finalWho = []
        self.finalWhere = []
        self.finalWhen = []
        self.finalWhat = []
        vExList = ['is','are','was','were','be','been','being','born']
        for s in sentences:
            count = 0
            for(a,b) in nltk.pos_tag(word_tokenize(s)):
                #print("classiffication for : "+a+" is -"+ self.classifier.classify(self.feature_extractor(a)))
                if 'NN' in b and self.classifier.classify(self.feature_extractor(a)) == 'WHERE':
                    self.finalWhere.append(s)
                    count+=1
                if ('NN' in b and self.classifier.classify(self.feature_extractor(a)) == 'WHEN') or 'CD' in b:
                    self.finalWhen.append(s)
                    count+=1
                if ('VB' in b) and a not in vExList:
                    self.finalWhat.append(s)
                    count+=1
            if count == 0:
                    self.finalWho.append(s)
                    
        self.fL.update({"0":self.finalWho})
        self.fL.update({"1":self.finalWhere})
        self.fL.update({"2":self.finalWhen})
        self.fL.update({"3":self.finalWhat})
        if 'who' in question.lower():
            self.fSet =  self.sendReleventResponses(question, set(self.finalWho))
        if 'when' in question.lower():
            self.fSet =  self.sendReleventResponses(question, set(self.finalWhen))
        if 'where' in question.lower():
            self.fSet =  self.sendReleventResponses(question, set(self.finalWhere))
        if 'what' in question.lower():
            self.fSet =  self.sendReleventVerbalResponses(question, set(self.finalWhat))
            
    def sendReleventResponses(self, questionTxt, finalSet):
        questionWords = ['who','when','where']
        if questionTxt.lower() in questionWords:
            return finalSet
        else:
            tagged_sent = nltk.pos_tag(word_tokenize(questionTxt))
            for (c,d) in tagged_sent:
                #print((c,d))
                if 'NN' in d or 'JJ' in d:
                    return set([s for s in finalSet if c.lower() in s.lower()])
                
    def sendReleventVerbalResponses(self, questionTxt, finalSet):
        vExList = ['is','are','was','were','be','been','being','born']
        ps = PorterStemmer()
        if questionTxt.lower() == 'what':
            return finalSet
        else:
            tagged_sent = nltk.pos_tag(word_tokenize(questionTxt))
            verbalList = []
            #for (c,d) in tagged_sent:
                #if 'VB' in d:
                # we need to filter the sentences based on noun and filter those sentences from the stemmed verbs.
            for s in finalSet:
                for (a,b) in nltk.pos_tag(word_tokenize(s)):
                    if 'VB' in b and a.lower() not in vExList:
                        for (c,d) in tagged_sent:
                            if 'VB' in d and c.lower() not in vExList:
                                print(ps.stem(a))
                                if ps.stem(a) == ps.stem(c):
                                    verbalList.append(s)
            return set(verbalList)
                        
                    
    
    

    