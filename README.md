# VeriRAG

VeriRAG is a self-healing Retrieval-Augmented Generation (RAG) system that improves answer reliability through verification, query decomposition, and iterative refinement.

Unlike standard RAG pipelines, VeriRAG can handle multi-intent queries, detect incomplete answers, and automatically retry with improved queries to produce more accurate responses.

---

## Key Features

- Multi-intent query handling (automatic query splitting)
- Self-healing retry mechanism with query rewriting
- Context-grounded answer generation
- Lightweight answer verification (grading system)
- Clean Streamlit interface
- Modular and extensible architecture

---

## System Architecture


User Query
↓
Query Splitter
↓
Retriever → Generator → Grader
↑ ↓
Rewriter ← Retry Loop
↓
Final Answer (Merged)


---

## Project Structure


VeriRAG/
│
├── app/
│ ├── retriever.py
│ ├── generator.py
│ ├── grader.py
│ ├── rewriter.py
│ ├── rag_agent.py
│ └── query_splitter.py
│
├── data/
│ ├── machine_learning.txt
│ ├── python_basics.txt
│ └── rag_concepts.txt
│
├── ui/
│ └── dashboard.py
│
├── requirements.txt
├── .gitignore
└── README.md


---

## Installation

### 1. Clone the repository

git clone https://github.com/your-username/VeriRAG.git
cd VeriRAG
### 2. Create a virtual environment

python -m venv venv
venv\Scripts\activate
### 3. Install dependencies

pip install -r requirements.txt
### 4. Add API Key

Create a .env file in the root directory:

GROQ_API_KEY=your_api_key_here

### 5. Run the Application
streamlit run ui/dashboard.py

## Example Queries
what is machine learning and rag
python uses and features
what is rag
## How It Works
The system detects multi-intent queries
It splits the query into sub-queries
Each sub-query goes through:
Retrieval (ChromaDB)
Generation (LLM)
Verification (Grader)
If the answer is incomplete:
Query is rewritten
System retries
Final answers are merged and returned
## Tech Stack
Python
LangChain
Groq LLM API
ChromaDB
Sentence Transformers
Streamlit
## Current Limitations
Rule-based query splitting
Basic grading logic (not semantic)
No source attribution in UI
## Future Improvements
LLM-based query decomposition
Confidence scoring instead of pass/fail
Source grounding with citations
Parallel execution for faster responses
Cloud deployment
