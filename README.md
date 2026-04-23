# LegalEase – AI-Powered Legal Assistant using RAG

## Overview
LegalEase is an AI-powered legal assistant that helps users retrieve relevant information from Indian legal resources using Retrieval-Augmented Generation (RAG).

The system uses:
- Indian Penal Code (IPC) dataset
- Constitution of India dataset
- Sentence embeddings
- FAISS vector search
- Streamlit chatbot interface

Users can ask legal questions such as:

- What is the punishment for theft?
- Is cheating a bailable offense?
- What is Article 21?

The system retrieves relevant legal provisions and shows source references.

---

## Features

- Legal document retrieval using semantic search  
- IPC and Constitution-based question answering  
- FAISS vector database for fast similarity search  
- Citation/source links in responses  
- Similarity threshold fallback to reduce hallucinations  
- Streamlit chatbot interface  

---

## Tech Stack

- Python  
- Sentence Transformers  
- FAISS  
- Streamlit  
- Pandas  
- PyPDF  

---

## Project Architecture

```text
User Query
   ↓
Query Embedding
   ↓
FAISS Similarity Search
   ↓
Retrieve Relevant Legal Chunks
   ↓
Generate Response
   ↓
Display Answer + Citation
```

---

## Project Structure

```text
LegalEase/
│
├── data/
│   ├── raw/
│   │   ├── ipc_dataset.csv
│   │   └── constitution_of_india.pdf
│   └── processed/
│       ├── constitution_text.json
│       └── chunks.json
│
├── embeddings/
│   ├── chunk_embeddings.pkl
│   └── vector_store/
│       └── faiss_index.bin
│
├── src/
│   ├── preprocessing/
│   │   ├── extract_pdf.py
│   │   ├── clean_text.py
│   │   └── chunking.py
│   │
│   ├── retrieval/
│   │   ├── embed_documents.py
│   │   ├── build_faiss.py
│   │   └── retrieve.py
│   │
│   ├── generation/
│   │   └── generate_response.py
│   │
│   └── app/
│       └── chatbot_app.py
│
├── tests/
│   └── test_queries.json
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/MohdGhouse04/LegalEase.git
cd LegalEase
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Preprocessing

Extract Constitution text:

```bash
python src/preprocessing/extract_pdf.py
```

Create chunks:

```bash
python src/preprocessing/chunking.py
```

Generate embeddings:

```bash
python src/retrieval/embed_documents.py
```

Build FAISS index:

```bash
python src/retrieval/build_faiss.py
```

---

## Run Chatbot

```bash
streamlit run src/app/chatbot_app.py
```

Open browser:

```text
http://localhost:8501
```

---

## Sample Queries

Try asking:

```text
Punishment for theft
Is cheating bailable?
What is Article 21?
Fundamental Rights
```

Out-of-scope test:

```text
How to get divorce in France?
```

Expected fallback:

```text
Relevant statute not found in dataset.
```

---

## Datasets Used

### Indian Penal Code Dataset
Source:
Kaggle IPC dataset

Contains:
- Offense descriptions  
- Punishment details  
- Cognizable / Non-cognizable  
- Bailable / Non-bailable  
- Court jurisdiction  

---

### Constitution of India
Source:
Official Constitution of India PDF

Contains:
- Articles  
- Fundamental Rights  
- Constitutional provisions  

---

## Hallucination Reduction
The system reduces incorrect answers using:

- Retrieval-first pipeline  
- Similarity threshold filtering  
- “No statute found” fallback response  

---

## Future Enhancements

- Real LLM-based response generation  
- Multilingual legal support  
- User-uploaded legal document analysis  
- Conversational memory  
- Deployment to cloud  

---

## Example Workflow

```text
User asks:
"What is punishment for theft?"

System:
1. Converts query into embedding
2. Searches FAISS vector database
3. Retrieves relevant IPC section
4. Displays legal provision
5. Shows citation URL
```

---

## Author

Mohd Ghouse

B.Tech Artificial Intelligence and Machine Learning

---

## License

For academic and educational purposes.