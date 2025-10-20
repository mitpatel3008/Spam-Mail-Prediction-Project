🧠 Project Overview

This project focuses on classifying email messages as Spam or Ham (legitimate) using Natural Language Processing (NLP) and Machine Learning techniques. The model learns textual patterns in emails to accurately detect unwanted messages and enhance email filtering systems.

⸻

📂 Dataset

The dataset used contains 5,572 labeled email messages, categorized into:
	•	Spam: Unwanted or promotional messages
	•	Ham: Legitimate non-spam messages

Dataset Source: SMS Spam Collection Dataset (UCI)

⸻

⚙️ Project Workflow
	1.	Data Preprocessing
	•	Removed stopwords, punctuation, and special symbols
	•	Tokenized text and normalized to lowercase
	2.	Feature Engineering
	•	Used TF-IDF Vectorizer (Term Frequency–Inverse Document Frequency) to convert textual data into numerical vectors
	3.	Model Development
	•	Trained a Logistic Regression model for binary classification
	•	Achieved 96.6% accuracy on the test set
	4.	Evaluation Metrics
	•	Accuracy, Precision, Recall, and F1-score
	•	Confusion Matrix visualization

⸻

🧰 Technologies Used
	•	Programming Language: Python
	•	Libraries: Pandas, NumPy, Scikit-learn, Matplotlib
	•	Key Modules: LogisticRegression, TfidfVectorizer

⸻

🚀 Results
	•	Achieved 96.6% accuracy on the testing dataset
	•	Demonstrated strong precision-recall balance for real-world email classification
	•	Optimized TF-IDF representation for improved feature discrimination

⸻

📊 Future Enhancements
	•	Implement advanced deep learning approaches like LSTM or BERT
	•	Build a Flask web app for real-time email spam detection
