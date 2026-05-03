# 🚀 AI Study Coach — Offline RAG AI Assistant

An advanced AI-powered Study Assistant built using:

* React.js
* FastAPI
* Ollama
* ChromaDB
* Local LLMs
* RAG (Retrieval-Augmented Generation)

This project allows users to:

* Upload PDFs
* Chat with documents
* Get AI-generated answers
* Use offline local AI models
* Perform semantic search using embeddings
* Build a privacy-friendly AI assistant without API costs

---

# 📌 Features

## ✅ Current Features

* AI Chat Interface
* React Frontend
* FastAPI Backend
* Local LLM Integration (Ollama)
* Custom AI Personality
* CORS Enabled API
* Modular Backend Structure

---

## 🚀 Planned Features

* PDF Upload System
* RAG Pipeline
* ChromaDB Vector Storage
* Semantic Search
* Source Citations
* Chat History
* Voice Input & Output
* Quiz Generator
* Notes Generator
* Flashcards
* Telemetry Dashboard
* AI Evaluations
* Authentication
* Dark Mode

---

# 🧠 What is RAG?

RAG stands for:

## Retrieval-Augmented Generation

Instead of answering only from pre-trained knowledge, the AI:

1. Retrieves relevant document chunks
2. Uses those chunks as context
3. Generates accurate answers

This reduces hallucinations and enables custom knowledge-based AI systems.

---

# 🛠️ Tech Stack

| Technology            | Usage             |
| --------------------- | ----------------- |
| React.js              | Frontend UI       |
| Tailwind CSS          | Styling           |
| FastAPI               | Backend API       |
| Ollama                | Local LLM Runtime |
| Phi3 / Llama3         | AI Models         |
| ChromaDB              | Vector Database   |
| Sentence Transformers | Embeddings        |
| Python                | Backend Language  |
| Axios                 | API Calls         |

---

# 📂 Project Structure

```bash
AI-Study-Coach/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── package.json
│
├── backend/
│   ├── main.py
│   ├── rag.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── prompt.py
│   ├── requirements.txt
│   └── uploads/
│
└── README.md
```

---

# ⚙️ Backend Setup

## 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 2️⃣ Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🦙 Ollama Setup

## Install Ollama

Download and install:

[https://ollama.com](https://ollama.com)

---

## Pull AI Model

### Recommended Lightweight Model

```bash
ollama pull phi3
```

### Alternative Models

```bash
ollama pull llama3
```

```bash
ollama pull mistral
```

---

## Test Ollama

```bash
ollama run phi3
```

---

# ▶️ Run Backend

Go to backend folder:

```bash
cd backend
```

Run FastAPI server:

```bash
uvicorn main:app --reload
```

Backend runs on:

```bash
http://localhost:8000
```

Swagger Docs:

```bash
http://localhost:8000/docs
```

---

# ⚛️ Frontend Setup

Go to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run React app:

```bash
npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# 🔗 Frontend ↔ Backend Connection

React communicates with FastAPI using Axios.

Example:

```javascript
const res = await axios.post(
  "http://localhost:8000/ask",
  {
    question: question,
  }
);
```

---

# 🧩 API Example

## Endpoint

```http
POST /ask
```

---

## Request

```json
{
  "question": "What is DBMS?"
}
```

---

## Response

```json
{
  "answer": "DBMS stands for Database Management System..."
}
```

---

# 🧠 Custom AI Personality

The assistant uses custom system prompts to define:

* Name
* Behavior
* Tone
* Identity
* Rules

Example:

```python
{
    "role": "system",
    "content": "You are Titan AI created by Rohit Yadav."
}
```

---

# 🔥 Future RAG Workflow

```text
PDF Upload
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embeddings
    ↓
ChromaDB Storage
    ↓
Semantic Retrieval
    ↓
Context Injection
    ↓
LLM Response
```

---

# 📈 Future Improvements

## AI Features

* Multi-Agent System
* AI Memory
* Autonomous Research Agent
* Smart Quiz Generation
* Contextual Recommendations

---

## Production Features

* JWT Authentication
* Docker Deployment
* CI/CD
* Redis Caching
* PostgreSQL
* Logging System
* Monitoring Dashboard

---

# 🛡️ Why Offline AI?

## Advantages

* No API cost
* Privacy-friendly
* Fully customizable
* Works offline
* Faster experimentation
* Better learning experience

---

# 📚 Learning Outcomes

This project teaches:

* Full Stack Development
* AI Engineering
* Retrieval-Augmented Generation
* Vector Databases
* Embeddings
* Local LLMs
* FastAPI APIs
* React Integration
* Semantic Search
* AI System Design

---

# 🧑‍💻 Author

## Rohit Yadav

B.Tech CSE Student
AI • Full Stack • Cybersecurity • Machine Learning

---

# ⭐ Contributing

Contributions, suggestions, and improvements are welcome.

Fork the repository and create a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 🌟 Acknowledgements

Special thanks to:

* Ollama
* FastAPI
* React
* ChromaDB
* Open-source AI community

---

# 🚀 Final Goal

Build a production-level AI Study Assistant capable of:

* Understanding documents
* Answering questions
* Generating notes
* Teaching concepts
* Working fully offline

This project is designed as:

* A portfolio project
* Internship showcase
* Final year project
* AI engineering learning platform
