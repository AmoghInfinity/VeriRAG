import sys
import os

# add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import time

from app.rag_agent import run_verirag


st.set_page_config(page_title="VeriRAG", layout="centered")

st.title("VeriRAG")

query = st.text_input("Enter your question")


if st.button("Run"):

    if not query:
        st.warning("Please enter a question")
        st.stop()

    progress_bar = st.progress(0)
    status_text = st.empty()

    status_text.text("Analyzing query...")
    progress_bar.progress(20)
    time.sleep(0.3)

    status_text.text("Processing...")
    progress_bar.progress(60)
    time.sleep(0.3)

    status_text.text("Finalizing answer...")
    progress_bar.progress(90)
    time.sleep(0.3)

    # run system
    result = run_verirag(query)

    progress_bar.progress(100)
    status_text.empty()
    progress_bar.empty()

    # extract data
    final_answer = result["answer"]
    sub_queries = result["sub_queries"]
    total_subqueries = result["total_subqueries"]
    total_retries = result["total_retries"]

    # metadata (clean + subtle)
    st.caption(f"Sub-queries: {', '.join(sub_queries)}")
    st.caption(f"Total retries: {total_retries}")

    # output
    st.subheader("Answer")

    if final_answer:
        st.success(final_answer)
    else:
        st.error("Could not generate a reliable answer.")