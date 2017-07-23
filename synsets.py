# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 22:15:56 2017

@author: Naruto_kathi
"""

from nltk.corpus import wordnet

synsets = wordnet.synsets("good")
synonyms = []
antonyms = []

for syn in synsets:
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())
            



print(set(synonyms))
print(set(antonyms))



word1 = wordnet.synset("ship.n.01")
word2 = wordnet.synset("submarine.n.01")

#symentic similarity of words
print(word2.wup_similarity(word1))