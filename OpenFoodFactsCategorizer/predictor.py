import joblib
import numpy as np
from OpenFoodFactsCategorizer.helpers import list_categories


def predict(path, X_sample, threshold=0.012):
    """ This function return the prediction for a given OCR"""

    model = joblib.load(path)
    list_cat = list_categories
    d = model.decision_function([X_sample])
    probabilities = [np.exp(x) / np.sum(np.exp(d)) for x in d]
    proba = list(probabilities[0])
    indices_max = np.argsort([-x for x in proba])

    """ This function return the prediction for a given OCR. if
    the probalité between the first and the second class is > thresold, it
    return directly the category. If not, the model return the two categories
     between which it hesitate"""

    if (proba[indices_max[0]] - proba[indices_max[1]]) > threshold:
        return list_cat[indices_max[0]]
    else:

        return {"class_1": list_cat[indices_max[0]],
                "proba_1": proba[indices_max[0]],
                "class_2": list_cat[indices_max[1]],
                "proba_2": proba[indices_max[1]]}




