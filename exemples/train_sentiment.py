"""Avant-goût de la semaine 2 : TF-IDF + régression logistique.

Usage : python exemples/train_sentiment.py
"""
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

ROOT = Path(__file__).resolve().parents[1]


def main():
    df = pd.read_csv(ROOT / "data" / "sample_reviews.csv")
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["label"], test_size=0.3, random_state=42, stratify=df["label"]
    )
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("clf", LogisticRegression(max_iter=1000)),
    ])
    pipeline.fit(X_train, y_train)
    print(classification_report(y_test, pipeline.predict(X_test)))
    out = ROOT / "models" / "sentiment.joblib"
    joblib.dump(pipeline, out)
    print(f"Modèle sauvegardé : {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
