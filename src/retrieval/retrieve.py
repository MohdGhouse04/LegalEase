import json
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/processed/chunks.json") as f:
    chunks = json.load(f)

index = faiss.read_index(
    "embeddings/vector_store/faiss_index.bin"
)

def retrieve_query(query, k=3):

    query_vector = model.encode([query])

    D, I = index.search(query_vector, k)

    results = []

    for i in I[0]:
        results.append(chunks[i]["text"])

    return results