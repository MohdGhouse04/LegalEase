import json
import faiss
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load chunked legal data
with open("data/processed/chunks.json") as f:
    chunks = json.load(f)

# Load FAISS index
index = faiss.read_index(
    "embeddings/vector_store/faiss_index.bin"
)

def retrieve_query(query, k=3):

    query_vector = model.encode([query])

    D, I = index.search(query_vector, k)

    print("Distance:", D[0][0])   # Debug

    # Safety threshold
    if D[0][0] > 5:
        return ["Relevant statute not found in dataset."]

    results=[]

    for i in I[0]:
        results.append(chunks[i]["text"])

    return results