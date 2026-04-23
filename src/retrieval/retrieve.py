import json,pickle,faiss
from sentence_transformers import SentenceTransformer

model=SentenceTransformer("all-MiniLM-L6-v2")

with open("data/processed/chunks.json") as f:
    chunks=json.load(f)

index=faiss.read_index(
"embeddings/vector_store/faiss_index.bin"
)

query="punishment for theft"

query_vector=model.encode([query])

D,I=index.search(query_vector,3)

for i in I[0]:
    print("\nRetrieved:\n")
    print(chunks[i]["text"][:500])