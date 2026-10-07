"""Avant-goût de la semaine 5 : interface de démonstration.

Usage : streamlit run exemples/app_streamlit.py
(entraîner d'abord : python exemples/train_sentiment.py)
"""
from pathlib import Path

import joblib
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "models" / "sentiment.joblib"

st.title("Analyse de sentiment — démonstration")

if not MODEL.exists():
    st.warning("Aucun modèle trouvé. Lancez d'abord : python exemples/train_sentiment.py")
    st.stop()

pipeline = joblib.load(MODEL)
texte = st.text_area("Avis client", "Livraison rapide et produit conforme, je recommande.")

if st.button("Classer"):
    label = pipeline.predict([texte])[0]
    proba = pipeline.predict_proba([texte]).max()
    st.metric("Sentiment", label, f"confiance {proba:.0%}")
