from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

def create_index(chunks, model_name="vinai/phobert-base", index_path="retriever/index.faiss", metadata_path="retriever/metadata.pkl"):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks, convert_to_numpy=True, show_progress_bar=True)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    faiss.write_index(index, index_path)
    with open(metadata_path, "wb") as f:
        pickle.dump(chunks, f)
    return index, embeddings

if __name__ == "__main__":
    chunk_dir = "data/chunks"
    chunks = []
    for file in sorted(os.listdir(chunk_dir)):
        with open(os.path.join(chunk_dir, file), "r", encoding="utf-8") as f:
            chunks.append(f.read())
    index, embeddings = create_index(chunks)
    print(f"Đã lập chỉ mục {len(chunks)} đoạn văn với embedding kích thước {embeddings.shape[1]}.")