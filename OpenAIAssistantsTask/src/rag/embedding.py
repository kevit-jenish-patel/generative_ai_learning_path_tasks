from sentence_transformers import SentenceTransformer

from src.core.db_config import database, DBCollections


def embed_chunks(chunks):
    # Load a specific model
    model_name = "all-MiniLM-L6-v2"  # You can change to any available HF model
    model = SentenceTransformer(model_name)

    embeddings = model.encode(chunks)

    return embeddings

async def insert_embeddings(chunks,embeddings):

    embedding_data = [{"text":embedding[0],"embedding":embedding[1]} for embedding in zip(chunks,embeddings)]

    result = await database[DBCollections.EMBEDDINGS].insert_many(embedding_data)

    if not result.acknowledged:
        raise Exception("Failed to insert embeddings")

    return True
