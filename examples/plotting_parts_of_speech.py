'''
CYBV-475
Cyber Deception Week 2
Using NLTK and Pandas to extract parts of speech from text
Spring 2026
'''

import pandas as pd
import matplotlib.pyplot as plt
import nltk
import re
from examples.nltk_setup import setup_nltk

if __name__ == "__main__":
    setup_nltk()

    with open('../texts/jules.txt') as julesText:
        jules_content = julesText.read(1000)
    with open('../texts/doyle.txt') as doyleText:
        doyle_content = doyleText.read(1000)


    # In this approach, we scrub texts to remove special symbols using a regular expression
    # Replace non letters with spaces

    jules_text = re.sub("[^a-zA-Z ]", ' ', jules_content)
    doyle_text = re.sub("[^a-zA-Z ]", ' ', doyle_content)

    jules_tokens = nltk.word_tokenize(jules_text)
    jules_tags = nltk.pos_tag(jules_tokens)

    doyle_tokens = nltk.word_tokenize(doyle_text)
    doyle_tags = nltk.pos_tag(doyle_tokens)

    posList = [0, 0, 0, 0]

    # [0] = Jules-Noun Count
    # [1] = Jules-Verb Count
    # [2] = Doyle-NounCount
    # [3] = Doyle-VerbCount

    for eachTag in jules_tags:
        if eachTag[1] in ["NN", "NNP", "NNPS"]:
            posList[0] += 1
        elif eachTag[1] in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]:
            posList[1] += 1

    posList[0] = (posList[0] / len(jules_tags)) * 100.0 # Percent Nouns in Jules Text
    posList[1] = (posList[1] / len(jules_tags)) * 100.0 # Percent Verbs in Jules Text

    for eachTag in doyle_tags:
        if eachTag[1] in ["NN", "NNP", "NNPS"]:
            posList[2] += 1
        elif eachTag[1] in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]:
            posList[3] += 1

    posList[2] = (posList[2] / len(doyle_tags)) * 100.0  # Percent Nouns
    posList[3] = (posList[3] / len(doyle_tags)) * 100.0  # Percent Verbs

    print(posList)

    df = pd.DataFrame(posList, index=['Jules Nouns', 'Jules Verbs', 'Doyle Nouns', 'Doyle Verbs'])
    df.columns = ['Count']

    print(df)
    df.plot(kind='bar')

    plt.show()

