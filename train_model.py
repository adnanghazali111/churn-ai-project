import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
from scipy.sparse import hstack

# Load dataset
df = pd.read_csv("data.csv")

# Convert text to numbers
vectorizer = TfidfVectorizer()
X_text = vectorizer.fit_transform(df["ticket_text"])

# Other numeric features
X_other = df[["complaint_count", "refunds_taken", "subscription_months"]]

# Combine features
X = hstack([X_text, X_other])
y = df["churn"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Model trained and saved successfully!")