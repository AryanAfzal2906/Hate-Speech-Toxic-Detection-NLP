# Hate Speech & Toxic Comment Detection using NLP

This project builds a machine learning-based system to detect whether online comments are toxic or not using Natural Language Processing (NLP) techniques.

## 🧠 Problem Statement
Online platforms often face challenges with toxic and abusive comments. This model classifies comments as toxic or non-toxic to support automated moderation.

## 📊 Dataset
We use the Kaggle **Toxic Comment Classification Challenge** dataset which contains labeled comments from Wikipedia talk page edits. Each comment is labeled as toxic or non-toxic. 

## 🛠️ Tech Stack
- Python
- Scikit-learn
- NLTK
- TF-IDF Vectorizer
- Logistic Regression

## 🚀 Methodology
1. Text preprocessing (tokenization, stop word removal).  
2. Feature extraction using TF-IDF.  
3. Classification using Logistic Regression.

## 📈 Evaluation Metrics

| Metric      | Value |
|-------     -|-------|
| Accuracy    | 91% |
| Precision   | 89% |
| Recall      | 87% |

## 📌 How to Run
```bash
git clone https://github.com/AryanAfzal2906/Hate-Speech-Toxic-Detection-NLP
cd Hate-Speech-Toxic-Detection-NLP
pip install -r requirements.txt
jupyter notebook
