# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 18:34:26 2017

@author: Naruto_kathi
"""

from nltk.tokenize import sent_tokenize, word_tokenize

from nltk.corpus import stopwords

import logging

logging.basicConfig(filename = "nltklog.log",
                              level = logging.DEBUG)

logger = logging.getLogger()

logger.info("#######3This is sentence and word tokenizer class and the exeuted results would be logged at DEBUG levels#######")
example = "This is kathi. I would like to check for myself how the sentence and words would be tokenized."  
stop_words = set(stopwords.words("english"))

filtered_words = []

#printing the tokenized sentences
logger.info("#######The results of the sentence tokenizer are: ",sent_tokenize(example))

#printing the tokenized words
logger.info("#######The results of the word tokenizer are: ",word_tokenize(example))

#printing the list of filtered words. (one line for and if statements)

logger.info("********This is how to write one liners and that would be printed in warning LEVELS********")
logger.info("@@@@@@@@[w for w in word_tokenize(example) if not w in stop_words]@@@@@@@@")


#general way of printing the filtered words is
for w in word_tokenize(example):
    if w not in stop_words:
        filtered_words.append(w)
        
logger.info("########The filtered words are: ",filtered_words)

