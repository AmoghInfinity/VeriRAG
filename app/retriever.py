import chromadb
from chromadb.utils import embedding_functions


# initialize embedding model
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


# initialize ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="knowledge_base",
    embedding_function=embedding_function
)


# retrieve documents
def retrieve_documents(query: str, n_results: int = 5):
    results = collection.query(
        query_texts=[query],
        n_results= 5
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    return documents, metadatas


# debug retrieval
def debug_retrieval(query: str):
    print(f"\nQuery: {query}")

    docs, _ = retrieve_documents(query)

    print(f"\nRetrieved {len(docs)} documents:\n")

    for i, doc in enumerate(docs):
        print(f"--- Document {i+1} ---")
        print(doc)
        print()


# test cases
def run_tests():
    test_queries = [
        "what is python",
        "types of machine learning",
        "what is rag",
        "python data types",
        "overfitting in machine learning"
    ]

    for query in test_queries:
        debug_retrieval(query)


# main execution
if __name__ == "__main__":
    choice = input("Choose mode: (1) manual (2) auto test: ")

    if choice == "1":
        while True:
            query = input("\nEnter query (or 'exit'): ")

            if query.lower() == "exit":
                break

            debug_retrieval(query)

    elif choice == "2":
        run_tests()