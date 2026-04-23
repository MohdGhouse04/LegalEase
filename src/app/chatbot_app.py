import sys
import os
import streamlit as st

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from src.retrieval.retrieve import retrieve_query

st.title("LegalEase")

query = st.text_input("Ask a legal question")

if query:
    results = retrieve_query(query)

    for r in results:
        st.write(r)