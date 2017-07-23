# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 19:54:10 2017

@author: Naruto_kathi
"""

import nltk

from nltk.corpus import state_union

from nltk.tokenize import PunktSentenceTokenizer

traintext = state_union.raw("2005-GWBush.txt")
sampletext = state_union.raw("2006-GWBush.txt")

custom_sentence_tokenizer = PunktSentenceTokenizer(traintext)

tokenized_text = custom_sentence_tokenizer.tokenize(sampletext)

reply_text = custom_sentence_tokenizer.tokenize("This is Sravan.")

chunkGrammer = r"""Kathi : {<RB.?>*<VB.?>*<NNP><NN>?}"""
replyWithName = r"""Kathiiihtak:{<NNP>+}
                        }<DT|VBZ>+{"""
chunkParser = nltk.RegexpParser(chunkGrammer)

def process_tokenized_text():
    
    try:
        for i in reply_text:
            words = nltk.word_tokenize(i)
            pos_tagged = nltk.pos_tag(words)
                #print(tup)
            print(pos_tagged)
            #print(nltk.RegexpParser(replyWithName).parse(pos_tagged))
            #chunkParser.parse(pos_tagged).draw()
            
    
    except Exception as e:
        print(str(e))

process_tokenized_text()