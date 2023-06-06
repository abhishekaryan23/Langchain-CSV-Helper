import os
import openai
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from src.utils import download_button

def get_answer_csv(file_path: str, query: str) -> str:
    agent = create_csv_agent(OpenAI(temperature=0, openai_api_key= openai_api_key), file_path, verbose=True)
    answer = agent.run(query)
    return answer

st.header("Chat with any CSV")
uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])

# dataframe = pd.DataFrame()

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
    file_container = st.expander("Check your uploaded .csv")
    shows = pd.read_csv(uploaded_file)
    uploaded_file.seek(0)
    file_container.write(shows.head(31))

    query = st.text_area("Ask any question related to the document")
    button = st.button("Submit")
    if button:
        with open('temp.csv', 'w') as f:
            f.write(uploaded_file.getbuffer().tobytes().decode())
        file_path = 'temp.csv'
        st.write(get_answer_csv(file_path, query))

        # Remove the temporary file
        os.remove(file_path)
