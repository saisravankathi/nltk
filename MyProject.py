# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 08:03:54 2017

@author: Naruto_kathi
"""
import nltk
from nltk import word_tokenize, sent_tokenize

#kathi = "How are you? What is your name? What are you doing? wassup?"

short_pos = open("positive.txt","r").read()

def parse_pos_text(kathi):
    pos_tagged = []
    #plain_sent_list = []
    #tagged_sent_list = []
    
    
    for sentence in sent_tokenize(kathi):
        pos_tagged.append(nltk.pos_tag(word_tokenize(sentence)))
    
    
    for stagged in pos_tagged:
        tagged_sent = ' '
        plain_sent = ' '
        for i in range(0,len(stagged)):
            tagged_sent = tagged_sent + stagged[i][1] + ' '
            plain_sent = plain_sent + stagged[i][0] + ' '
        print(plain_sent)
        print(tagged_sent)
    
                                   
parse_pos_text(short_pos)









        
#print(pos_tagged[0][0][0])
        