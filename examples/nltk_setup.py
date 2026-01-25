'''
CYBV-475
Cyber Deception Week 2
Setting up NLTK
Spring 2026
'''

import nltk

def setup_nltk():
    # The Code Below Avoids SSL Errors When Downloading the NLTK Data
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    # Rule of thumb with NTLK
    # If you use word_tokenize() download punkt -> More details here: https://www.nltk.org/api/nltk.tokenize.punkt.html#module-nltk.tokenize.punkt
    # If you use pos_tag() download averaged_perceptron_tagger -> More details here:

    nltk.download("punkt", quiet=True)
    nltk.download("averaged_perceptron_tagger", quiet=True)
    # quiet=True makes it so the terminal doesn't yell at you if this is already installed
