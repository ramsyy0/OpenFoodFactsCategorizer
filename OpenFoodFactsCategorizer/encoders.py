from sklearn.base import TransformerMixin, BaseEstimator
from spellchecker import SpellChecker
import re
import string
import unicodedata
import pandas as pd
import nltk

# Transformer with SpellCheck
class CustomPreprocessor(TransformerMixin, BaseEstimator):
# TransformerMixin generates a fit_transform method from fit and transform
# BaseEstimator generates get_params and set_params methods

#TO DO:

    def __init__(self):
        return None


    def fit(self, X, y=None):
         """Required for sklearn compatibility; Checking NLTK requirements for transform"""
         #stop_words = set(stopwords.words('french'))
         return self

    def transform(self, X, y=None):
         """Expects a Dataframe of text; Returns a DataFrame of transformed text"""
         return self

    def remove_punc(text):
        """Expects a string; Returns a string without punctuation"""
        for punctuation in string.punctuation:
            text = text.replace(punctuation, ' ')
            text = re.sub(" +", " ", text)
            return text

    def remove_nonalpha(text):
        """Expects a string; Returns a string without non alphanumeric characters"""
        text = ''.join(c for c in text if c.isalpha() or c == ' ')
        return re.sub(" +", " ", text)

    def corrected(text):
        """Expects a string in French; Returns a string without spelling mistakes"""
        # Init SpellChecker
        spell = SpellChecker(language='fr', distance=1, case_sensitive=False)
        # Get misspellings and corrections
        text_splitted = text.split()
        misspelled = spell.unknown(text_splitted)
        correction = {word:spell.correction(word) for word in misspelled}

        # Replace misspellings in text
        for k,v in correction.items():
            text = text.replace(k,v)
        return text

    def remove_accents(text):
        """Expects a string; Returns a string without accentuated characters"""
        return ''.join(c for c in unicodedata.normalize('NFKD', text)
                        if unicodedata.category(c) != 'Mn')

    def clean_ocr_text(text, spellcheck=SpellChecker):
        """Expects a string; Returns a string without punctuation, non-alphanum characters, spelling mistakes"""
        text = text.lower().replace('\n',' ')

        if spellcheck:
            clean_funcs = [remove_punc, remove_nonalpha, corrected, remove_accents]
        else:
            clean_funcs = [remove_punc, remove_nonalpha, remove_accents]

        for func in clean_funcs:
            text = func(text)
        return text.strip(" ")

        X = X.apply(lambda x: clean_ocr_text(x, spellcheck=False))
        return X
