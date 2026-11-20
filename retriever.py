from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "vectorstore",
    embedding,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_kwargs={"k":3}
)

query = input("Ask your question: ")

results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n========== Result {i+1} ==========")
    print(doc.page_content)