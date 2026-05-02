[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)] https://hate-speech-toxic-detection-nlp-hnahzkt8j7ho2q7i9jysm5.streamlit.app/#hate-speech-and-toxic-comment-detection

# 🚨 Toxic Comment & Hate Speech Detector

An end-to-end Machine Learning web application that classifies text comments as **Toxic** or **Non-Toxic** using Natural Language Processing.

 App Screenshot(<img width="766" height="437" alt="Output" src="https://github.com/user-attachments/assets/dabf2cd2-9a40-4377-9232-0650b9b0997a" />
.png) 

## 🚀 Overview
This project provides a real-time interface to detect harmful online content. It leverages a **Logistic Regression** model and **TF-IDF Vectorization** to analyze the sentiment and toxicity of user-provided text.

## 🛠️ Features
* **Real-time Prediction:** Get instant results upon typing.
* **Confidence Scoring:** Shows how certain the model is about its classification.
* **Clean UI:** Simple and intuitive interface built with Streamlit.
* **Notebook Included:** Full training process documented in `Hate_Speech_Detection.ipynb`.

## 📂 Project Structure
* `app.py`: Main Streamlit application code.
* `Logistic Model & TF-IDF Vectorizer).
* `Hate_Speech_Detection.ipynb`: Google Colab notebook used for data cleaning and model training.
* `requirements.txt`: List of necessary Python libraries.

## 💻 How to Run Locally
1. **Clone the repo:**
   git clone(https://github.com/AryanAfzal2906/Hate-Speech-Toxic-Detection-NLP.git)
   cd Hate-Speech-Toxic-Detection-NLP

## 📊 Model Performance

I evaluated the Logistic Regression model using a test set. The results are as follows:

| Metric | Score |
| :--- | :--- |
| **Accuracy** | 94.2% |
| **Precision** | 91.5% |
| **Recall** | 89.8% |
| **F1-Score** | 90.6% |

### Confusion Matrix
The confusion matrix shows how many comments were correctly classified versus those that were missed.
