import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage


# load environment variables
load_dotenv()


# initialize LLM (same model for consistency)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


# grade answer against documents
def grade_answer(query: str, documents: list[str], answer: str):
    # basic sanity check
    if not answer or len(answer.strip()) < 20:
        return "fail"

    answer_lower = answer.lower()

    # reject weak answers
    bad_phrases = ["i don't know", "not sure", "cannot answer"]
    if any(p in answer_lower for p in bad_phrases):
        return "fail"

    # MULTI-QUESTION CHECK (with normalization)
    if " and " in query.lower():
        parts = query.lower().split(" and ")

        for part in parts:
            part = part.strip()

            # normalization for common abbreviations
            if part == "ml":
                part = "machine learning"
            elif part == "rag":
                part = "retrieval augmented generation"

            if part not in answer_lower:
                return "fail"

    # combine context
    context_text = " ".join(documents).lower()

    # keyword overlap check
    answer_words = answer_lower.split()
    overlap = sum(1 for word in answer_words if word in context_text)

    if overlap >= 5:
        return "pass"

    return "fail"


# debug test
def debug_grader():
    docs = [
        "Python is a high-level programming language.",
        "It supports object-oriented programming."
    ]

    query = "What is Python?"

    good_answer = "Python is a high-level programming language."
    bad_answer = "Python is a database system."

    print("\nTesting GOOD answer:")
    print("Result:", grade_answer(query, docs, good_answer))

    print("\nTesting BAD answer:")
    print("Result:", grade_answer(query, docs, bad_answer))


# main test
if __name__ == "__main__":
    debug_grader()