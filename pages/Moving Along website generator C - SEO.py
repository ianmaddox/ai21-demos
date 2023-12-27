import streamlit as st
from utils.studio_style import apply_studio_style
from constants import ai21
import requests  # You might need to import requests

st.set_page_config(
    page_title="AI21 Studio - AI Demos",
)

def get_chat_suggestions(text, system_description):
    payload = {
        "numResults": 1,
        "temperature": 0.7,
        "messages": [
            {
                "text": text,
                "role": "system"
            }
        ],
        "system": system_description
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer jKutZdBnfEIXD1P5hdUD3ZN5VRbCSsrW"
    }
    # Replace 'your_ai21_chat_api_endpoint' with the actual endpoint
    response = requests.post('https://api.ai21.com/studio/v1/j2-ultra/chat', json=payload, headers=headers)
    return response.json()

# Existing functions (get_suggestions, show_next, show_prev) remain unchanged

if __name__ == '__main__':
    apply_studio_style()

    st.title("AI21 Studio - AI Demos")

    # Existing Streamlit interface for the rewrite tool

    # New interface for the chat API
    st.header("AI21 Chat API Demo")
    user_input = st.text_area("Enter your text for SEO keyword generation:",
                              placeholder="Enter text here")
    system_description = "You are a SEO keyword generator. Your job is to help you turn business website text into SEO keywords. For example, if you have a business description like this: \"We are a fintech startup that provides market analysis tools for financial institutions.\" You might make SEO keywords like these: \"fintech, market analysis, financial institutions, startup, AI, ML, banking, charts, data\"."
    if st.button("Generate SEO Keywords"):
        chat_response = get_chat_suggestions(user_input, system_description)
        if chat_response.get("replies"):
            st.text_area("SEO Keywords", value=chat_response["replies"][0], height=300)


