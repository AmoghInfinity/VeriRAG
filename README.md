# 🔍 VeriRAG  
### Self-Healing Retrieval-Augmented Generation System

VeriRAG is an advanced RAG system designed to improve answer reliability through verification, query decomposition, and iterative refinement.

Unlike traditional RAG pipelines, VeriRAG can handle multi-intent queries, detect incomplete answers, and automatically self-correct using a retry mechanism to generate more accurate and complete responses.

---

## 🚀 Features

### 🧠 Self-Healing RAG Pipeline
- Iterative retry mechanism for answer improvement  
- Query rewriting for better retrieval  
- Automatic correction of incomplete responses  

### 🔀 Multi-Intent Query Handling
- Splits complex queries into sub-queries  
- Processes each query independently  
- Merges final answers intelligently  

### 📚 Retrieval-Augmented Generation (RAG)
- Context-based answer generation  
- ChromaDB vector database  
- Sentence-transformer embeddings  
- Reduced hallucination through grounding  

### ✅ Answer Verification System
- Rule-based grading (pass/fail)  
- Detects incomplete or incorrect responses  
- Triggers retry loop when needed  

### 💻 Minimal & Clean UI
- Built with Streamlit  
- Progress-based execution feedback  
- Focused on final output clarity  

---

## 🏗️ Architecture

User Query  
↓  
Query Splitter  
↓  
Retriever → Generator → Grader  
                ↑        ↓  
            Rewriter ← Retry Loop  
↓  
Final Answer (Merged)  

---

## ⚙️ Tech Stack

- LLM: Groq (llama-3.3-70b-versatile)  
- Framework: LangChain  
- Embeddings: Sentence Transformers (all-MiniLM-L6-v2)  
- Vector Database: ChromaDB  
- Backend: Python  
- Frontend: Streamlit  

---

## 📁 Project Structure

```
VeriRAG/
│
├── app/
│   ├── retriever.py
│   ├── generator.py
│   ├── grader.py
│   ├── rewriter.py
│   ├── rag_agent.py
│   └── query_splitter.py
│
├── data/
│   ├── machine_learning.txt
│   ├── python_basics.txt
│   └── rag_concepts.txt
│
├── ui/
│   └── dashboard.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/VeriRAG.git
cd VeriRAG
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

### 5. Run the Application

```
streamlit run ui/dashboard.py
```

---

## 🧪 Example Queries

```
what is machine learning and rag
python uses and features
what is rag
```

---

## 🧠 Key Highlights

- Handles multi-question queries intelligently  
- Implements self-healing retry mechanism  
- Ensures context-grounded responses  
- Modular architecture for easy extension  

---

## ⚠️ Limitations

- Rule-based query splitting (not semantic yet)  
- Basic grading logic (non-LLM based)  
- No source attribution in UI  

---

## 🔮 Future Improvements

- LLM-based query decomposition  
- Confidence scoring system  
- Source grounding with citations  
- Parallel processing for speed  
- Cloud deployment  

---

## 👨‍💻 Author

Amogh Gupta  

---

## ⭐ Acknowledgements

- Groq API  
- LangChain  
- HuggingFace  
- ChromaDB  
- Streamlit  
