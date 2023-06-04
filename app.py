import streamlit as st
import os
import openai  # Add this line
from src.utils import get_answer_csv  # Assuming you have this file and function

st.header("Chat with any CSV")
uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])

with st.sidebar:
    st.markdown(
        """
Get your own OpenAI API key:

- Go to [openai.com](https://platform.openai.com/account/api-keys).
- Click on `+ Create new secret key`.
- Enter an identifier name (optional) and click on the `Create secret key` button.
- Copy the API key and paste it here
        """
    )
    openai_api_key = st.sidebar.text_input(
        "OpenAI API Key",
        label_visibility="collapsed",
        placeholder="OpenAI API Key",
    )
    openai.api_key = openai_api_key

if uploaded_file is not None:
    query = st.text_area("Ask any question related to the document")
    button = st.button("Submit")
    if button:
        # Save the uploaded file temporarily and get its path
        with open('temp.csv', 'wb') as f:
            f.write(uploaded_file.getbuffer())
        file_path = 'temp.csv'
        st.write(get_answer_csv(file_path, query))

        # Remove the temporary file
        os.remove(file_path)
