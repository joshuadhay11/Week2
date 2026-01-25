'''
CYBV-475
Cyber Deception Week 2
Using NLTK and Pandas to extract parts of speech from text
Spring 2026
'''

import pandas as pd
import nltk
from tabulate import tabulate
from examples.nltk_setup import setup_nltk

import re


''' Part of Speech Dictionary Lookup Table '''

POS_LOOKUP = {
    "CC":   " Coordinating conjunction ",
    "CD":   " Cardinal number ",
    "DT":   " Determiner ",
    "EX":   " Existential there ",
    "FW":   " Foreign word ",
    "IN":   " Preposition or subordinating conjunction ",
    "JJ":   " Adjective ",
    "JJR":  " Adjective, comparative ",
    "JJS":  " Adjective, superlative ",
    "LS":   " List item marker ",
    "MD":   " Modal ",
    "NN":   " Noun, singular or mass ",
    "NNS":  " Noun, plural ",
    "NNP":  " Proper noun, singular ",
    "NNPS": " Proper noun, plural ",
    "PDT":  " Predeterminer ",
    "POS":  " Possessive ending ",
    "PRP":  " Personal pronoun ",
    "PRP$": " Possessive pronoun ",
    "RB":   " Adverb ",
    "RBR":  " Adverb, comparative ",
    "RBS":  " Adverb, superlative ",
    "RP":   "  Particle ",
    "SYM":  " Symbol ",
    "TO":   " to ",
    "UH":   " Interjection ",
    "VB":   " Verb, base form ",
    "VBD":  " Verb, past tense ",
    "VBG":  " Verb, gerund or present participle ",
    "VBN":  " Verb, past participle ",
    "VBP":  " Verb, non-3rd person singular present ",
    "VBZ":  " Verb, 3rd person singular present ",
    "WDT":  " Wh-determiner ",
    "WP":   "  Wh-pronoun ",
    "WP$":  " Possessive wh-pronoun ",
    "WRB":  " Wh-adverb "
}

SPEECH_EXCERPT = '''I believe that this Nation should commit itself to achieving the goal, 
before this decade is out, of landing a man on the Moon and returning him safely to Earth.'''

SPECIAL_TEXT = "It's so cool! I <3 my Cyber Deception Detection Course! "

if __name__ == "__main__":
    setup_nltk() # You really only need to run this once then can comment it out

    text = SPEECH_EXCERPT
    # text = SPEECH_EXCERPT + SPECIAL_TEXT

    # Consider how using the above would change your results

    text = nltk.word_tokenize(text)
    tags = nltk.pos_tag(text)

    # Add Verbose Definition to tags
    tags_verbose = []

    for word, pos in tags:
        verbose_definition = POS_LOOKUP.get(pos, "Unknown")
        if verbose_definition == "Unknown":
            continue # this skips the rest of the code below

            # You can also choose other ways to handle Unknown parts of speech
            # Perhaps scrubbing symbols before using a regular expression
            # Such as: text = re.sub("[^a-zA-Z ]", ' ', text)

        tags_verbose.append((word, pos, verbose_definition))

    df = pd.DataFrame(tags_verbose)

    df.columns = ['Word', 'POS', "Verbose POS Definition"]
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=True))
