# 🚨 Toxic Comment & Hate Speech Detector

An end-to-end Machine Learning web application that classifies text comments as **Toxic** or **Non-Toxic** using Natural Language Processing.

![App Screenshot](<img width="766" height="437" alt="Output" src="https://github.com/user-attachments/assets/dabf2cd2-9a40-4377-9232-0650b9b0997a" />
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
* `model/`: Contains the serialized `.pkl` files (Logistic Model & TF-IDF Vectorizer).
* `Hate_Speech_Detection.ipynb`: Google Colab notebook used for data cleaning and model training.
* `requirements.txt`: List of necessary Python libraries.

## 💻 How to Run Locally
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/AryanAfzal2906/Your-Repo-Name.git](https://github.com/AryanAfzal2906/Hate-Speech-Toxic-Detection-NLP.git)
   cd Hate-Speech-Toxic-Detection-NLP
