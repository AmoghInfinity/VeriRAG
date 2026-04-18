import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage


# load environment variables
load_dotenv()


# initialize LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


# generate answer from documents
def generate_answer(query: str, documents: list[str]):
    if not documents:
        return "No relevant documents found."

    context = "\n\n".join(documents)

    system_prompt = """You are a precise and helpful AI assistant.

Rules:
- Answer ALL parts of the question
- Combine information from multiple documents if needed
- If part of the answer is missing, try to infer from context
- Only say "I don't know" if absolutely no relevant information is available
"""

    user_prompt = f"""
Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ])

    # safety handling
    if not response or not response.content:
        return "I could not generate a response."

    answer = response.content.strip()

    # prevent weak/empty answers
    if len(answer) < 20:
        return "I could not generate a complete answer."

    return answer


# debug generation
def debug_generation():
    sample_docs = [
        "Machine learning is a subset of artificial intelligence that enables systems to learn from data.",
        "Retrieval-Augmented Generation (RAG) combines retrieval with generation to produce grounded responses."
    ]

    query = "What is ML and RAG?"

    print("\nQuery:", query)
    print("\nContext:")
    for doc in sample_docs:
        print("-", doc)

    answer = generate_answer(query, sample_docs)

    print("\nGenerated Answer:\n")
    print(answer)


# main test
if __name__ == "__main__":
    debug_generation()
