import pandas as pd
import numpy as np
from OpenFoodFactsCategorizer.data import get_data_from_ocr



class Analyst():
    def __init__(self):
    """N_GRAMS per Category DataFrame + Graphics Matrices"""
        pass

    def get_ngrams(text_series, gram_size=1):
    '''Generates a list of n-grams for a given text with a given n_gram_size
       Returns a tuple: (n_gram_size, list of n_grams)

       Parameters
       ----------
       text_series : pd.Series where each row is a string
       gram_size : integer
       '''

    # convert text to list of words
    words = text_series.split()

    # extract n_grams
    patterns = list(nltk.ngrams(words, gram_size))

    # return n_grams strings instead of tuples
    if gram_size == 1:
        n_grams = [p[0] for p in patterns]
    else: n_grams = [
                    ' '.join(p[i] for i in range(len(p))) \
                    for p in patterns
                    ]

    # return gram_size and list of n_grams
    return (gram_size, n_grams)

    def get_patterns_df(text_series):
        indexes = []
        patterns = []
        n_gram_size = []

        # Iterate over each OCR
        for i,text in df['clean_text'].iteritems():

            # Initialize a vocab length
            len_vocab = 0

            # Iterate over each n_gram size
            for k in range(10):
                results = get_ngrams(text, gram_size=k+1)  # extract n_grams
                patterns.extend(results[1])                # store them in patterns
                len_vocab = len_vocab + len(results[1])    # store number of patterns
                n_gram_size.extend([f'{k+1}-grams'] * len(results[1])) # store size
            indexes.extend([i] * len_vocab)

        # Convert list to pd.Series
        indexes = pd.Series(indexes)
        patterns = pd.Series(patterns)
        n_gram_size = pd.Series(n_gram_size)

        # Initialize a DataFrame
        data = pd.DataFrame()


        # Create the Pattern DataFrame
        data[['index','size','pattern']] = pd.concat([indexes, n_gram_size, patterns], axis=1)

        # Retrieve categories, barcode, clean_text
        data.set_index('index', inplace=True)

        patterns_df = pd.DataFrame()
        patterns_df = pd.merge(
            data,
            df[['pnns_groups_2','clean_text','barcode','source']],
            left_index=True,
            right_index=True,
            )

        return patterns_df

    def get_patterns_csv(text_series, path_to_csv):
        patterns_df = get_patterns_df(text_series)
        patterns_df.to_csv('path_to_csv', index=False)


    def get_patterns_frequencies(text_series)




