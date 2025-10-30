from src.core.db_config import connect_db, disconnect_db
from src.rag.llm import generate_prompt, generate_llm_response
from src.rag.semantic_search import search_query
from src.rag.embedding import embed_chunks

async def rag_pipeline():
    await connect_db()

    user_query = input("Please enter a query: ")

    embeddings = embed_chunks([user_query])

    result = await search_query(embeddings[0])

    result = [r["text"] for r in result]

    prompt = generate_prompt(user_query, result)

    response = generate_llm_response(prompt)

    print(response)

    await disconnect_db()

    return response