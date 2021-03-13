import os
import pandas as pd
from sklearn.model_selection import train_test_split


def get_data_from_image():
    """If OCR integrated, Expects a path to a folder with images and get ocr text for each of them"""
    pass

def get_data(path='.'):
    #change the path in parameters
    df = pd.read_csv(path)

    return df

def get_data_from_text(path='.', holdout=0.3):
      #change the path in parameters
    """Expects a path to a csv with ocr text and labels; Returns splitted train-test data"""
    # ADD JSON TO CSV

    #df = pd.read_csv(f"{path}/ocr_labeled_spellcheck.csv", nrows=n_rows)
    df = pd.read_csv(path, nrows=n_rows)

    #X = #???
    #y = #???
    X= df['clean_text']
    y = df['pnns_groups_2']
    train_test_split(X, y, test_size=holdout)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 1)
    return X_train, X_test, y_train, y_test



#if __name__ == '__main__':


