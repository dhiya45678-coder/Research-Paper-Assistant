from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from chunking import chunks

# Create Embedding Model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create FAISS Vector Database
vector_db = FAISS.from_texts(
    texts=chunks,
    embedding=embedding
)

# Save the database locally
vector_db.save_local("vectorstore")

print("Vector Database Created Successfully!")