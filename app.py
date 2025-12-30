import streamlit as st
import joblib
import numpy as np

# Load model & vectorizer using the paths you described
# 'model/' refers to the subfolder inside ARYAN
try:
    model = joblib.load("logistic_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
except Exception as e:
    st.error(f"Error loading files: {e}")

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
        
        # Get probability for the predicted class
        probabilities = model.predict_proba(text_vector)[0]
        confidence = np.max(probabilities)

        if prediction == 1:
            st.error(f"🚫 Toxic Comment\n\n")
        else:
            st.success(f"✅ Non-Toxic Comment\n\n")
