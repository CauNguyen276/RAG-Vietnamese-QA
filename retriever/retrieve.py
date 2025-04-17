from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np

def retrieve(query, top_k=3, model_name="vinai/phobert-base", index_path="retriever/index.faiss", metadata_path="retriever/metadata.pkl"):
    model = SentenceTransformer(model_name)
    index = faiss.read_index(index_path)
    with open(metadata_path, "rb") as f:
        chunks = pickle.load(f)
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, top_k)
    results = [(chunks[idx], distances[0][i]) for i, idx in enumerate(indices[0])]
    return results

if __name__ == "__main__":
    query = "Hồ Chí Minh sinh ngày nào?"
    results = retrieve(query)
    for chunk, distance in results:
        print(f"Khoảng cách: {distance:.4f}\nĐoạn văn: {chunk[:100]}...\n")