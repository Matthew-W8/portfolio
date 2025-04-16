import spacy
import os
import pandas as pd
nlp = spacy.load("en_core_web_lg")

collPath = '../PythonProject1'
def wordCollector(words, unit):
    wordList = []
    nodeAtts = []
    unitList = []
    for token in words:
        if token.pos_ == "ADJ":
            wordList.append(token.lemma_)
            nodeAtts.append(token.pos_)
            unitList.append(unit)

    data = {
        'word': wordList,
        'nodeType': nodeAtts,
        'unit': unitList
    }
    df = pd.DataFrame(data)
    return df

allDataFrames = []

for file in os.listdir(collPath):
    if file.endswith(".txt"):
        filepath = f"{collPath}/{file}"
        name, extension = os.path.splitext(file)
        with open(filepath, 'r', encoding='utf8') as f:
            readFile = f.read()
            spacyRead = nlp(readFile)
            myDataFrame = wordCollector(spacyRead, name)
            allDataFrames.append(myDataFrame)

outputFilePath = 'networkData.tsv'
fullDataFrame = pd.concat(allDataFrames, ignore_index=True)
fullDataFrame.to_csv(outputFilePath, sep='\t', index=False)
print('I just saved a dataframe as a TSV file.')