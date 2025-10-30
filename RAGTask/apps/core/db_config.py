import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

# Define embedding function using a pre-trained model
embedding_function = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# Persistent Chroma client
chroma_client = chromadb.Client()
chroma_collection = chroma_client.get_or_create_collection("my_collection",embedding_function=embedding_function)

def get_collection():
    return chroma_collection
