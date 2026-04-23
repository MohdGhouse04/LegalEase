import json
import pickle
from sentence_transformers import SentenceTransformer

model=SentenceTransformer("all-MiniLM-L6-v2")

with open("data/processed/chunks.json") as f:
    chunks=json.load(f)

texts=[c["text"] for c in chunks]

embeddings=model.encode(texts)

with open("embeddings/chunk_embeddings.pkl","wb") as f:
    pickle.dump(embeddings,f)

print("Embedding shape:",embeddings.shape)