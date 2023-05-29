import os
from typing import TextIO

import openai
import pandas as pd
import streamlit as st
from langchain.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain.llms import OpenAI

def get_answer_csv(file_path: str, query: str) -> str:
    """
    Returns the answer to the given query by querying a CSV file.

    Args:
    - file_path (str): the file path to the CSV file to query.
    - query (str): the question to ask the agent.

    Returns:
    - answer (str): the answer to the query from the CSV file.
    """

    agent = create_csv_agent(OpenAI(temperature=0), file_path, verbose=True)
    answer = agent.run(query)
    return answer
