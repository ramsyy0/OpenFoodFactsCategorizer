import joblib

class Predictor()
    def __init__(self):
        pass

    def predict(self, path, X_sample, threshold=0.012)

        model = joblib.load(path_model)

        proba = model.decision_function([X_sample])  
        indices_max = np.argsort([-x for x in proba])
        
        if (proba[indices_max[0]] - proba[indices_max[1]]) > threshold:
            return self.list_cat[indices_max[0]]
        
        return {"class_1": self.list_cat[indices_max[0]],
                "proba_1": proba[indices_max[0]],
                "class_2": self.list_cat[indices_max[1]],
                "proba_2": proba[indices_max[1]]}