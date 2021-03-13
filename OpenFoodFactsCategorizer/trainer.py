from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.linear_model import RidgeClassifier
from sklearn.model_selection import cross_val_score
import joblib
from OpenFoodFactsCategorizer.helpers import list_categories
from OpenFoodFactsCategorizer.encoders import CustomPreprocessor
from OpenFoodFactsCategorizer.data import get_data
from OpenFoodFactsCategorizer.data import get_data_from_text


class Trainer():

    def __init__(self, X, y):
        self.pipeline = None
        self.X = X
        self.y = y
        self.list_cat = list_categories


        #return self

    def create_pipeline(self):
        """Returns a full pipeline with preprocessing and model"""
        nltk.download('stopwords')
        stop_words = set(stopwords.words('french'))
        self.pipeline = Pipeline([
            ("custom_preprocessor", CustomPreprocessor()),
            ("tfidf", TfidfVectorizer(ngram_range=(2, 2), stop_words=stop_words)),
            ("ridge", RidgeClassifier())
        ])

    def train_model(self):
        """Requires a created pipeline; Returns a trained pipeline"""
        self.create_pipeline()

        return self.pipeline.fit(self.X, self.y)


    def evaluate_model(self, X_test, y_test):
        """Expects a trained pipeline; Returns a cross-validated score for the trained pipeline"""
        return cross_val_score(self.pipeline,
                        X_test, y_test,
                        scoring="accuracy",
                        n_jobs=-1) \
                    .mean()

    def save_model(self, filename="model2.joblib"):
        """Saves the current pipeline"""
        joblib.dump(self.pipeline, filename)

        return None

    def predict(self, X_sample, threshold=0.012):

        proba = self.pipeline.decision_function([X_sample])
        indices_max = np.argsort([-x for x in proba])

        if (proba[indices_max[0]] - proba[indices_max[1]]) > threshold:
            return self.list_cat[indices_max[0]]

        return {"class_1": self.list_cat[indices_max[0]],
                "proba_1": proba[indices_max[0]],
                "class_2": self.list_cat[indices_max[1]],
                "proba_2": proba[indices_max[1]]}

if __name__ == '__main__':


    X_train, X_test, y_train, y_test = get_data_from_text()
    trainer = Trainer(X=X_train, y=y_train)
    trainer.train_model()
    trainer.evaluate_model(X_test, y_test)
    trainer.save_model()

