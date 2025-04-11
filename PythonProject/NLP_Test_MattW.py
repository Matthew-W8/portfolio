#Imports:
import os

from nltk import word_tokenize
from nltk.corpus import wordnet as wn

wn.synsets('clear')
wn.synset('net.v.02').lemmas()

cwd = os.getcwd()
print(cwd)

filepath = 'xwing.txt'
print(filepath)

f = open(filepath, 'r', encoding='utf8').read()
print(f)

text = nltk.Text(word.lower() for word in filepath)
text.similar('the')