import joblib
import pandas as pd
from scipy.sparse import hstack


class FeatureAgent:

    def __init__(self):
        self.model = joblib.load("model.pkl")
        self.vectorizer = joblib.load("vectorizer.pkl")

    def predict_churn(self, ticket_text, complaint_count, refunds_taken, subscription_months):

        text = [ticket_text]

        # Transform text
        X_text = self.vectorizer.transform(text)

        # Combine numeric features
        X_other = pd.DataFrame([[complaint_count, refunds_taken, subscription_months]])
        X = hstack([X_text, X_other])

        # Predict probability
        prob = self.model.predict_proba(X)[0][1]

        return float(prob)