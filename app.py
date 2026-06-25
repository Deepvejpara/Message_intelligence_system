import streamlit as st
import pickle
import numpy as np

# Load model and scaler
model = pickle.load(open("models/model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

# Title
st.title("📩 Spam Detection App")

st.write("Enter feature values to predict whether message is Spam or Ham")

# Input fields
message_length = st.number_input("Message Length")
word_count = st.number_input("Word Count")
num_urls = st.number_input("Number of URLs")
num_digits = st.number_input("Number of Digits")
num_special_chars = st.number_input("Special Characters Count")
spam_keyword_score = st.number_input("Spam Keyword Score")
legit_keyword_score = st.number_input("Legit Keyword Score")
sender_activity_score = st.number_input("Sender Activity Score")
sender_account_age_days = st.number_input("Account Age (days)")
messages_sent_last_24h = st.number_input("Messages in last 24h")
hour_of_day = st.number_input("Hour of Day")
day_of_week = st.number_input("Day of Week")

# Predict button
if st.button("Predict"):

    input_data = np.array([[message_length,
                            word_count,
                            num_urls,
                            num_digits,
                            num_special_chars,
                            spam_keyword_score,
                            legit_keyword_score,
                            sender_activity_score,
                            sender_account_age_days,
                            messages_sent_last_24h,
                            hour_of_day,
                            day_of_week]])

    # Apply scaling
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("🚨 Spam Message")
    else:
        st.success("✅ Legit (Ham) Message")
    
    prob = model.predict_proba(input_scaled)[0]

    st.write(f"Spam Probability: {prob[1]:.2f}")
    st.write(f"Ham Probability: {prob[0]:.2f}")