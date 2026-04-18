import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

import chromadb
from chromadb.utils import embedding_functions


# load environment variables
load_dotenv()


# initialize embedding model
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


# load and split documents
def load_and_split_documents(folder_path: str):
    all_chunks = []

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        length_function=len
    )

    docs_path = Path(folder_path)

    for file in docs_path.glob("*.txt"):
        loader = TextLoader(str(file), encoding="utf-8")
        documents = loader.load()

        chunks = text_splitter.split_documents(documents)
        all_chunks.extend(chunks)

        print(f"Loaded {len(chunks)} chunks from {file.name}")

    return all_chunks


# store in ChromaDB with embeddings
def ingest_to_chromadb(chunks):
    client = chromadb.PersistentClient(path="./chroma_db")

    collection = client.get_or_create_collection(
        name="knowledge_base",
        embedding_function=embedding_function
    )

    documents = [chunk.page_content for chunk in chunks]
    ids = [f"chunk_{i}" for i in range(len(chunks))]
    metadatas = [
        {"source": chunk.metadata.get("source", "unknown")}
        for chunk in chunks
    ]

    collection.add(
        documents=documents,
        ids=ids,
        metadatas=metadatas
    )

    print(f"Stored {len(documents)} chunks in ChromaDB")


# test database content
def test_database():
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("knowledge_base")

    print("\nTesting database...")
    print("Total documents in DB:", collection.count())


# main execution
if __name__ == "__main__":
    print("Starting ingestion...")

    chunks = load_and_split_documents("data/docs")

    if not chunks:
        print("No documents found.")
    else:
        ingest_to_chromadb(chunks)
        print("Knowledge base ready.")

        # run test
        test_database()