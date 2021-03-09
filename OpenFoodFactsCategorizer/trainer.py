from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.linear_model import RidgeClassifier
from sklearn.pipeline import Pipeline
import joblib

from OpenFoodFacts.helpers import list_categories
from OpenFoodFacts.encoders import CustomPreprocessorNoSpellCheck
from OpenFoodFacts.data import get_data

class Trainer():

    def __init__(self):
        self.pipeline = None
        self.list_cat = list_categories

        return self

    def create_pipeline(self):
    """Returns a full pipeline with preprocessing and model"""
        self.pipeline = Pipeline([
            ("custom_preprocessor", CustomPreprocessorNoSpellCheck()),
            ("tfidf", TfidfVectorizer(ngram_range=(2, 2), min_df=50)),
            # ("lsa", TruncatedSVD(n_components=2500)),
            ("model", RidgeClassifier())
        ])
        
        return self.pipeline
    
    def train_model(self, X_train, y_train):
    """Requires a created pipeline; Returns a trained pipeline"""
        self.pipeline.fit(X_train, y_train)

        return self.pipeline

    def evaluate_model(self, X_test, y_test):
    """Expects a trained pipeline; Returns a cross-validated score for the trained pipeline"""
        return cross_val_score(self.pipeline,
                        X_test, y_test,
                        scoring="accuracy",
                        n_jobs=-1) \
                    .mean()
    
    def save_model(self, filename="model.joblib"):
    """Saves the current pipeline"""
        joblib.dump(self.pipeline, filename)
        
        return None

    def predict(self, X_sample, threshold=0.012)

        proba = self.pipeline.decision_function([X_sample])  
        indices_max = np.argsort([-x for x in proba])
        
        if (proba[indices_max[0]] - proba[indices_max[1]]) > threshold:
            return self.list_cat[indices_max[0]]
        
        return {"class_1": self.list_cat[indices_max[0]],
                "proba_1": proba[indices_max[0]],
                "class_2": self.list_cat[indices_max[1]],
                "proba_2": proba[indices_max[1]]}

if __name__ == '__main__':
    X_train, X_test, y_train, y_test = get_data()
    Trainer().set_pipeline()
    Trainer().train_model(X_train, y_train)
    Trainer().evaluate_model(X_test, y_test)
    Trainer().save_model()