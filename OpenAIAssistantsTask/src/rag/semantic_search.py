from src.core.db_config import database, DBCollections


async def search_query(embedding):
    pipeline = [
        {
            '$vectorSearch': {
                'index': 'vector_index',
                'path': 'embedding',
                'queryVector': embedding,
                'numCandidates': 150,
                'limit': 5
            }
        }, {
            '$project': {
                '_id': 0,
                'text': 1,
                'score': {
                    '$meta': 'vectorSearchScore'
                }
            }
        }
    ]

    # run pipeline
    cursor = await database[DBCollections.EMBEDDINGS].aggregate(pipeline)
    result = await cursor.to_list()

    return result