import joblib
import numpy as np
from OpenFoodFactsCategorizer.helpers import list_categories
from OpenFoodFactsCategorizer.cleaner import Cleaner
from OpenFoodFactsCategorizer.data import get_data_from_ocr


class Predictor():

    model = None

    """ get text from json OCR """
    text = get_data_from_ocr('https://static.openfoodfacts.org/images/products/00390804/1.json')

    """ applies the same preprocessing as the model (but with a different class because it is a string and not a
     dataframe)"""
    cleaner = Cleaner()
    text = cleaner.clean_ocr_text(text=text, spellcheck=None)


    def __init__(self, text):
        self.text = text


    def load_model(self):
        if Predictor.model is None:
            # change the path whith your model name and location
            Predictor.model = joblib.load('bestridge.joblib')
        self.model = Predictor.model


    def predict(self, threshold=0.012):
        """ This function returns the prediction for a given OCR. If > thresold, it
        returns directly the category. If not, the model returns the two categories
        between which it hesitates"""
        list_cat = list_categories
        d = self.model.decision_function([self.text])
        probabilities = [np.exp(x) / np.sum(np.exp(d)) for x in d]
        proba = list(probabilities[0])
        indices_max = np.argsort([-x for x in proba])

        if (proba[indices_max[0]] - proba[indices_max[1]]) > threshold:
            return list_cat[indices_max[0]]
        else:
             return {"proba_1": list_cat[indices_max[0]],
                     "confidence_1": round(proba[indices_max[0]], 4),
                     "proba_2": list_cat[indices_max[1]],
                    "confidence_2": round(proba[indices_max[1]], 4)}




#if __name__ == '__main__':

    #predictor = Predictor(text=Predictor.text)
    #predictor.load_model()
    #print(predictor.predict(threshold=0.012))
