# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 21:36:09 2017

@author: Naruto_kathi
"""

from nltk.corpus import genesis

from nltk.tokenize import sent_tokenize

english_text = genesis.raw("english-web.txt")


#usning genesis corpus
sentences = sent_tokenize(english_text)
for i in sentences[0:10]:
    print(i)