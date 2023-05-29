import streamlit as st
import os
from src.utils import get_answer_csv

st.header("Chat with any CSV")
uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])

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
