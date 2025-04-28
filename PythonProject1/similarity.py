import os
import spacy

nlp = spacy.load('en_core_web_lg')

collection = "../DIGIT_210/SCP_Texts-2025"

from collections import Counter

def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        stringFile = str(readFile)
        tokens = nlp(stringFile)
        vectors = tokens.vector
        wordOfInterest = nlp(u'hero')
        highSimilarityDict = {}
        sorted_similarity = sorted(highSimilarityDict.items(), key=lambda item: item[1], reverse=True)
        wordCounts = Counter()

        for token in tokens:
            if (token and token.vector_norm):
                if wordOfInterest.similarity(token) > .4:
                    wordCounts[token.text] += 1
                    highSimilarityDict[token] = wordOfInterest.similarity(token)

        print(f'This is a dictionary of words most similar to the word "{wordOfInterest.text}" in "{file}".')
        for word, similarity in highSimilarityDict.items():
            count = wordCounts[word.text]
            print(f"{word}: similarity={similarity:.3f}, count={count}")
        print('\n')


for file in os.listdir(collection):
    if file.endswith(".txt"):
        filepath = f"{collection}/{file}"
        readTextFiles(filepath)