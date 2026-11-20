# 📚 Research Paper Assistant

An AI-powered Research Paper Assistant that helps users understand research papers and get answers to their questions using Retrieval-Augmented Generation (RAG).

## 🎯 Project Overview

The Research Paper Assistant allows users to ask questions about uploaded research papers. It retrieves relevant information from PDF documents and generates context-based answers using a Large Language Model (LLM).

## ✨ Features

- Reads research papers in PDF format.
- Extracts and splits text into chunks.
- Generates embeddings using Sentence Transformers.
- Stores document vectors using FAISS.
- Retrieves relevant information based on user questions.
- Generates answers using Groq LLM.
- Provides a simple question-and-answer interface.

## 🛠️ Technologies Used

- Python
- LangChain
- Groq LLM
- FAISS
- Sentence Transformers
- PDFPlumber
- Retrieval-Augmented Generation (RAG)

## 📂 Project Structure

```text
ResearchPaperAssistant/
│
├── data/
│   └── Research Paper PDFs
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
├── read_pdf.py
├── chunking.py
├── embedding.py
├── vector_store.py
├── retriever.py
├── chatbot.py
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/dhiya45678-coder/Research-Paper-Assistant.git
```

2. Open the project folder:

```bash
cd Research-Paper-Assistant
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key
```

5. Run the chatbot:

```bash
python chatbot.py
```

## 🔄 Working Process

1. PDF Document Loading
2. Text Extraction
3. Text Chunking
4. Embedding Generation
5. FAISS Vector Storage
6. Relevant Document Retrieval
7. LLM-Based Answer Generation

## 🚀 Future Enhancements

- Interactive web interface
- Multiple PDF uploads
- Chat history
- Source-based answers
- Improved document summarization

## 👩‍💻 Developer

**AI & Data Science Student**

GitHub: https://github.com/dhiya45678-coder

---

*Built using Python, RAG, FAISS, and Generative AI.*