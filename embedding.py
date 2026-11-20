from langchain_huggingface import HuggingFaceEmbeddings
from chunking import chunks

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector = embedding_model.embed_query(chunks[0])

print(vector)