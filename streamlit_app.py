import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# App title
st.title("Spam Mail Classifier")

# Input box
email = st.text_area("Enter your email:")

# Predict button
if st.button("Check"):
    if email:
        # Transform and predict
        input_features = vectorizer.transform([email])
        prediction = model.predict(input_features)
        
        # Show result
        if prediction[0] == 1:
            st.success("✅ Ham Mail")
        else:
            st.error("❌ Spam Mail")
    else:
        st.warning("Please enter an email!")

