from langchain_text_splitters import RecursiveCharacterTextSplitter
from read_pdf import all_text

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_text(all_text)

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\n------ Chunk {i+1} ------")
    print(chunk)