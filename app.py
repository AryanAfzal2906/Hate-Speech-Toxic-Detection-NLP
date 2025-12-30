import streamlit as st
import pickle
import numpy as np

# Load model & vectorizer
model = pickle.load(open("model/logistic_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

st.set_page_config(page_title="Toxic Comment Detector", page_icon="🚫")

st.title("🚨 Hate Speech & Toxic Comment Detection")
st.write("Enter a comment below to check whether it is **Toxic** or **Non-Toxic**.")

# Input text
user_input = st.text_area("✍️ Enter your comment here")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Vectorize input
        text_vector = vectorizer.transform([user_input])

        # Prediction
        prediction = model.predict(text_vector)[0]
        probability = model.predict_proba(text_vector).max()

        if prediction == 1:
            st.error(f"🚫 Toxic Comment\nConfidence: {probability:.2%}")
        else:
            st.success(f"✅ Non-Toxic Comment\nConfidence: {probability:.2%}")

