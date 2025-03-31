from nltk.corpus import PlaintextCorpusReader
corpus_root = 'C:\Users\mattw\OneDrive\Documents\Digital_Media_Arts_and_Technology\GitHub\portfolio\python-nlp\grimm.txt'
wordList = PlaintextCorpusReader(corpus_root, '.*')
print(corpus_root.count('the'))
