import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage


# load environment variables
load_dotenv()


# initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


# clean model output
def clean_output(text: str):
    text = text.strip()

    # take only first line to avoid chaining
    text = text.split("\n")[0]

    # remove arrow chains like "->"
    if "->" in text:
        text = text.split("->")[-1]

    # remove unwanted prefixes
    text = text.replace("Rewritten question:", "")
    text = text.replace('"', '')

    return text.strip()


# rewrite query for better retrieval
def rewrite_query(query: str):
    prompt = f"""
You are a query optimizer for a technical AI knowledge base.

Rewrite the question to improve clarity and retrieval accuracy.

Rules:
- Keep the meaning the same
- Stay within AI, programming, or machine learning context
- Do NOT introduce unrelated meanings
- Do NOT add explanations
- Do NOT add quotes or labels
- Return ONLY the rewritten question

Original question:
{query}
"""

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return clean_output(response.content)


# debug test
def debug_rewriter():
    queries = [
        "what is ml",
        "python uses",
        "rag meaning"
    ]

    for q in queries:
        print("\nOriginal:", q)
        print("Rewritten:", rewrite_query(q))


# main test
if __name__ == "__main__":
    debug_rewriter()