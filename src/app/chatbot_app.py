import sys
import os
import streamlit as st

# Fix import path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from src.retrieval.retrieve import retrieve_query


# ---------------- UI ----------------

st.title("LegalEase")
st.write("Ask questions about IPC or Constitution.")

query = st.text_input("Ask a legal question")

if query:

    results = retrieve_query(query)

    # if fallback message returned
    if isinstance(results[0], str):
        st.write(results[0])

    else:
        for r in results:

            # Retrieved answer
            st.subheader("Legal Answer")
            st.write(r["text"])

            # Citation source (if exists)
            if "metadata" in r and "url" in r["metadata"]:
                st.subheader("Source")
                st.write(r["metadata"]["url"])