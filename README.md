## 📧 Spam-Mail Classifier (NLP & Machine Learning)

A machine learning web app that classifies emails as spam or ham (genuine) using Natural Language Processing and Logistic Regression.

⸻

## 🌐 Live Demo
	•	Try the live app here: https://spammail-classifier.streamlit.app/

⸻

## 🚀 Features
	•	Detects and classifies emails as “spam” or “ham” with high accuracy
	•	Uses TF-IDF for text feature extraction
	•	Logistic Regression model achieves 96.6% test accuracy
	•	User-friendly Streamlit web app for instant predictions
	•	Real-time analysis — paste your email and view results immediately

⸻

## 🧠 Tech Stack
	•	Programming Language: Python
	•	Libraries: Pandas, NumPy, Scikit-learn
	•	NLP: TfidfVectorizer
	•	Model: Logistic Regression
	•	App Framework: Streamlit
	•	Development Tools: Jupyter Notebook, VS Code

⸻

## 📊 Dataset
	•	Source: Public SMS/email data (mail_data.csv)
	•	Labels: “ham” (genuine) and “spam” (junk)
	•	Size: 5,500+ messages for model training and evaluation

⸻

## 🛠️ How It Works
	•	Data Loading & Preprocessing: Loads CSV, removes missing data, encodes labels (spam=0, ham=1)
	•	Feature Engineering: Extracts message text, applies TF-IDF, removes stopwords
	•	Model Development: Splits dataset (80% train, 20% test), trains Logistic Regression, achieves >96% accuracy
	•	Model Saving & Deployment: Saves model as spam_model.pkl and vectorizer as vectorizer.pkl for quick reuse
	•	Web App Interface: User pastes email → model predicts → displays “Ham Mail” ✅ or “Spam Mail” 🚨

⸻

## 📦 Files Included
	•	spam_model.pkl — Trained Logistic Regression model
	•	vectorizer.pkl — TF-IDF vectorizer for feature extraction
	•	streamlit_app.py — Streamlit web app source code
	•	spam-mail-classifier.ipynb — Model training & evaluation notebook
	•	mail_data.csv — Labeled dataset
	•	requirements.txt — Dependencies for environment setup
