import time

from langfuse import observe

from src.core.openai_config import client

@observe()
def create_vector_store():
    try:
        vector_stores = client.vector_stores.list()
        for vs in vector_stores.data:
            print("Deleting:",vs.id, vs.name)
            client.vector_stores.delete(vector_store_id=vs.id)
    except Exception as e:
        print(e)

    vector_store = client.vector_stores.create(name="Amazon Rainforest")

    return vector_store

@observe()
def upload_file_to_vector_store(filename,vector_store):
    with open(filename, "rb") as f:
        vector_file = client.vector_stores.files.upload(vector_store_id=vector_store.id, file=f)

    time.sleep(3)

    return vector_file