# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 19:39:12 2017

@author: Naruto_kathi
"""

from nltk.stem import PorterStemmer

from nltk.tokenize import word_tokenize

ps = PorterStemmer()

sentence = "This is my laptop being with me for ever  I've started learing things. I think I might not forget this beautiful machine."

for w in word_tokenize(sentence):
    print(ps.stem(w))