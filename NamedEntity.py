# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 19:54:10 2017

@author: Naruto_kathi
"""

import nltk

from nltk.corpus import state_union

from nltk.tokenize import PunktSentenceTokenizer

traintext = state_union.raw("2005-GWBush.txt")
sampletext = """For decades, while astronomers have detected black holes equal in mass either to a few suns or millions of suns, the missing-link black holes in between have eluded discovery. Now, a new study suggests such intermediate-mass black holes may not exist in the modern-day universe because of the rate at which black holes grow.

Scientists think stellar-mass black holes — up to a few times the sun's mass — form when giant stars die and collapse in on themselves. Over the years, astronomers have detected a number of stellar-mass black holes in the nearby universe, and in 2010, researchers detected the first such black hole outside the local cluster of nearby galaxies known as the Local Group.

As big as stellar-mass black holes might seem, they are tiny in comparison to the so-called supermassive black holes that are millions to billions of times the sun's mass, which form the hearts of most, if not all, large galaxies. The oldest supermassive black holes found to date include one found in 2015 — with a mass of about 12 billion solar masses — that existed when the universe was only about 875 million years old. This finding and others suggest that many black holes were born in the dawn of time, back when the universe was smaller and matter was more concentrated, making it easier for them to form and grow."""

custom_sentence_tokenizer = PunktSentenceTokenizer(traintext)

tokenized_text = custom_sentence_tokenizer.tokenize(sampletext)


def process_tokenized_text():
    
    try:
        for i in tokenized_text:
            words = nltk.word_tokenize(i)
            pos_tagged = nltk.pos_tag(words)
            namedEntity = nltk.ne_chunk(pos_tagged, binary=True)
            namedEntity.draw()
            
    
    except Exception as e:
        print(str(e))

process_tokenized_text()