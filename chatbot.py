from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load .env file
load_dotenv()

# Check Current Folder
print("Current Folder:", os.getcwd())

# Get API Key
groq_api_key = os.getenv("GROQ_API_KEY")

# Check whether API Key is loaded
print("API Key Loaded:", "Yes" if groq_api_key else "No")

# Load Embedding Model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS Vector Database
db = FAISS.load_local(
    "vectorstore",
    embedding,
    allow_dangerous_deserialization=True
)

# Create Retriever
retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

# Load Groq LLM
llm = ChatGroq(
    api_key=groq_api_key,
    model="llama-3.3-70b-versatile"
)

print("\n======================================")
print(" Research Paper Assistant Chatbot ")
print(" Type 'exit' to quit")
print("======================================")

while True:

    query = input("\nAsk Your Question: ")

    if query.lower() == "exit":
        print("Thank You!")
        break

    # Retrieve relevant documents
    docs = retriever.invoke(query)

    # Combine retrieved chunks
    context = ""

    for doc in docs:
        context += doc.page_content + "\n\n"

    # Prompt
    prompt = f"""
You are a helpful Research Paper Assistant.

Answer the user's question only using the given context.

Context:
{context}

Question:
{query}

Answer:
"""

    # Get response from Groq
    response = llm.invoke(prompt)

    print("\n================ ANSWER ================\n")
    print(response.content)

    print("\n============= SOURCES =============")

    for i, doc in enumerate(docs):
        print(f"\nSource {i+1}")
        print(doc.page_content[:300])