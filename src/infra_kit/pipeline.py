# src/infra_kit/pipeline.py

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

class DummyPrivacyClassifier:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = LogisticRegression()

    def load_data(self):
        return pd.DataFrame({
            "text": [
                "I want to delete my account",
                "How do I update my email?",
                "Please remove my data",
                "I forgot my password",
                "Export my data please"
            ],
            "label": [1, 0, 1, 0, 1]  # 1 = privacy request, 0 = general
        })

    def preprocess(self, df):
        X = self.vectorizer.fit_transform(df["text"])
        y = df["label"]
        return X, y

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, texts):
        X_new = self.vectorizer.transform(texts)
        preds = self.model.predict(X_new)
        return list(zip(texts, preds))

    def run(self):
        df = self.load_data()
        X, y = self.preprocess(df)
        self.train(X, y)
        results = self.predict([
            "I want to erase my personal info",
            "How can I change my username?"
        ])
        return results
