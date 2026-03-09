import chromadb
from sentence_transformers import SentenceTransformer


client = chromadb.Client()
collection = client.create_collection("documents")

model = SentenceTransformer("all-MiniLM-L6-v2")


def store_chunks(chunks):

    embeddings = model.encode(chunks).tolist()

    for i, chunk in enumerate(chunks):

        collection.add(
            documents=[chunk],
            embeddings=[embeddings[i]],
            ids=[str(i)]
        )


def search_chunks(query):

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    return results["documents"][0]