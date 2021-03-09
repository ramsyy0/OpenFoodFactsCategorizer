import os
import pandas as pd
from sklearn.model_selection import train_test_split


def get_data_from_image():
"""If OCR integrated, Expects a path to a folder with images and get ocr text for each of them"""
    pass

def get_data_from_text(n_rows=1000, path=".", holdout=0.3):
"""Expects a path to a csv with ocr text and labels; Returns splitted train-test data"""
    # ADD JSON TO CSV
    
    # df = pd.read_csv(f"{path}/ocr_labeled_spellcheck.csv", nrows=n_rows)
    X = #???
    y = #???

    return train_test_split(X, y, test-size=holdout)

if __name__ == '__main__':
    get_data()
