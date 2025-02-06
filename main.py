# Go to terminal and run the following 
# streamlit run .\main.py

import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load a pre-trained Hugging Face model
chatbot = pipeline("text-generation", model="distilgpt2")

def healthcare_chatbot(user_input):
    if "symptom" in user_input:
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input:
        return "Would you like me to schedule an appointment with a doctor?"
    elif "medication" in user_input:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    else:
        response = chatbot(user_input, max_length=300, num_return_sequences=1)
        return response[0]['generated_text']

# Streamlit web app interface
def main():
    # Apply dark theme
    st.markdown(
        """
        <style>
            body {
                background-color: #121212;
                color: #FFFFFF;
            }
            .stTextInput>div>div>input {
                background-color: #333333;
                color: white;
            }
            .stButton>button {
                background-color: #6200EA;
                color: white;
            }
            .chat-container {
                padding: 15px;
                background-color: #1E1E1E;
                border-radius: 10px;
                margin-bottom: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    st.sidebar.write("💡 This is a healthcare chatbot powered by AI.")
    
    # Main chat interface
    st.title("🩺 Healthcare Assistant Chatbot")
    st.write("Hello! How can I assist you today?")
    
    user_input = st.text_input("Your Query:", "", key="input")
    
    if st.button("Send"): 
        if user_input:
            st.markdown(f'<div class="chat-container">👤 <b>User:</b> {user_input}</div>', unsafe_allow_html=True)
            response = healthcare_chatbot(user_input)
            st.markdown(f'<div class="chat-container">🤖 <b>Assistant:</b> {response}</div>', unsafe_allow_html=True)
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()
