def retrieve_similar_results(collection,query):
    results = collection.query(query_texts=query, n_results=3)
    return results["documents"][0]
