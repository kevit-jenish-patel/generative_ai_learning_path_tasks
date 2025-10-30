from enum import StrEnum

from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase
from pymongo.operations import SearchIndexModel

from src.core.config import settings

class DBCollections(StrEnum):
    EMBEDDINGS = "embeddings"

db_client: AsyncMongoClient | None = None
database: AsyncDatabase | None = None

search_index_model = SearchIndexModel(
  definition={
    "fields": [
      {
        "type": "vector",
        "path": "embedding",
        "numDimensions": 384,
        "similarity": "dotProduct",
        "quantization": "scalar"
      }
    ]
  },
  name="embedding_vector_index",
  type="vectorSearch"
)

async def create_vector_index():
    try:
        cursor = await database[DBCollections.EMBEDDINGS].list_search_indexes()
        existing_indexes = await cursor.to_list()
        existing_names = [idx["name"] for idx in existing_indexes]

        if search_index_model.document["name"] not in existing_names:
            search_index = await database[DBCollections.EMBEDDINGS].create_search_index(model=search_index_model)
            print("✅ Created new vector search index.")
            return search_index
        else:
            print("ℹ️ Vector search index already exists.")
    except Exception as e:
        print("❌ Error creating search index:", e)

async def create_collection():
    collections = await database.list_collection_names()
    if DBCollections.EMBEDDINGS not in collections:
        collection = await database.create_collection(DBCollections.EMBEDDINGS)
        print(collection)

async def connect_db():
    global db_client, database
    db_client = AsyncMongoClient(settings.MONGODB_URI)
    database = db_client["openai-assistants-task"]
    await create_collection()
    await create_vector_index()
    print("Connected to DB")

async def disconnect_db():
    global db_client
    await db_client.close()
    print("Disconnected to DB")

def get_db():
    return database
