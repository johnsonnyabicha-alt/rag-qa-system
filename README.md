# 🌍 Philosophy, Politics & Economics RAG Q&A System

A production-ready **Retrieval-Augmented Generation (RAG)** system for answering questions about philosophy, politics, and economics using modern AI and vector search.

## ✨ Features

✅ **Upload Documents** - Support for .txt, .pdf, .doc files  
✅ **Semantic Search** - Find relevant information using AI embeddings  
✅ **Sourced Answers** - AI generates answers with document citations  
✅ **Chat History** - Keep track of all conversations  
✅ **Confidence Scores** - See how confident the system is  
✅ **Beautiful UI** - Modern React frontend  
✅ **Production Ready** - Docker setup included  

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- OpenAI API Key
- Pinecone API Key

### 1. Setup
```bash
git clone https://github.com/johnsonnyabicha-alt/rag-qa-system.git
cd rag-qa-system
cp .env.example .env
```

### 2. Configure .env
```
OPENAI_API_KEY=your-key
PINCONE_API_KEY=your-key
PINCONE_INDEX_NAME=ppe-reg-qa-system
PINCONE_ENVIRONMENT=us-east-1
```

### 3. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### 4. Frontend Setup (New Terminal)
```bash
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:5173
Backend: http://localhost:8000

## 🐳 Docker

```bash
docker-compose up
```

Then visit: http://localhost:3000

## 📚 How to Use

1. Upload documents (PDFs, text files)
2. Ask questions about the content
3. Get AI-generated answers with source citations

## 📝 Project Structure

```
rag-qa-system/
├── backend/          # FastAPI + LangChain
│   ├── app.py
│   ├── config.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── requirements.txt
├── frontend/         # React app
│   ├── src/
│   ├── package.json
│   └── vite.config.js
├── docker-compose.yml
└── README.md
```

## 🛠 API Endpoints

### POST `/api/upload`
Upload a document

### POST `/api/query`
Query the RAG system

### GET `/health`
Health check

## 💡 How It Works

1. Upload documents → Split into chunks → Generate embeddings
2. Store in Pinecone vector database
3. User asks question → Convert to embedding → Semantic search
4. Retrieve relevant chunks → Pass to LLM with context
5. LLM generates answer with source citations

## 📚 Tech Stack

- **Backend**: FastAPI, LangChain, OpenAI, Pinecone
- **Frontend**: React, Vite
- **Deployment**: Docker, Railway

## 📖 Learning Resources

- [LangChain Docs](https://python.langchain.com/docs/)
- [Pinecone Learning](https://www.pinecone.io/learn/)
- [OpenAI API](https://platform.openai.com/docs/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/)

## 📝 License

MIT License

---

**Built with ❤️ using FastAPI, React, LangChain, and Pinecone**