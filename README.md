## 📄 PDF Question Answering System (RAG-based AI App)

### 🏠 Home Screen
![Home Screen](screenshots/home.png)

### 💬 Question Answering
![Question Answering](screenshots/answer.png)

## 🚀 Approach

### Overview
The system follows a RAG (Retrieval-Augmented Generation) approach:
- Users upload a PDF document
- The backend extracts and chunks text
- Each chunk is converted into embeddings
- Embeddings are stored in a vector database
- User questions are embedded and matched against stored chunks
- Relevant context is sent to the LLM
- The LLM answers only using retrieved context

This ensures accuracy, traceability, and minimal hallucination.

### Tools & Design Choices
| Tool | Purpose | Reason |
|------|----------|--------|
| **FastAPI** | Backend API | Fast, async, production-ready |
| **React (Vite)** | Frontend | Lightweight, modern UI |
| **ChromaDB** | Vector database | Local, persistent, ideal for RAG |
| **LangChain** | RAG utilities | Clean abstraction for loaders & chunking |
| **Sentence Transformers** | Embeddings | Efficient semantic representation |
| **OpenAI** | LLM | High-quality text generation |

**Design Decisions:**
- Used RAG to prevent hallucinations
- Chose ChromaDB for simplicity and local persistence
- Used environment variables for API key security
- Clean separation between retrieval and generation
- Minimal but elegant frontend for clarity and usability

## 🔧 Project Structure

```
pdf-qa/
├── backend/
│   ├── main.py
│   ├── rag.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.css
│   └── package.json
│
├── screenshots/
│   ├── home.png
│   └── answer.png
│
├── .gitignore
└── README.md
```

## 📦 Installation

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/pabitrajana007/pdf-qa.git
cd pdf-qa
```

### 2️⃣ Backend Setup:
```bash
cd backend
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create .env file:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

4. Run backend:
```bash
python -m uvicorn main:app --reload
```
### 3️⃣ Frontend Setup:
```bash
cd frontend
npm install
npm run dev
```
