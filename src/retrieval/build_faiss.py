import pickle
import faiss
import numpy as np

with open("embeddings/chunk_embeddings.pkl","rb") as f:
    embeddings=pickle.load(f)

dimension=384

index=faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

faiss.write_index(
 index,
 "embeddings/vector_store/faiss_index.bin"
)

print("Vectors indexed:",index.ntotal)