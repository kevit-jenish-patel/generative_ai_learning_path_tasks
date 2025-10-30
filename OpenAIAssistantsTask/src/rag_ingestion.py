import asyncio

from src.core.config import settings
from src.core.db_config import connect_db, disconnect_db
from src.rag.chunking import chunk_markdown
from src.utils.data_extraction import fetch_page_soup, convert_to_markdown
from src.rag.embedding import embed_chunks, insert_embeddings


async def rag_ingestion():
    await connect_db()

    soup = fetch_page_soup(settings.WEBSITE_URL_TO_SCRAP)

    main_div = soup.select_one("main#main-content>div")

    md = convert_to_markdown(main_div)

    chunks = chunk_markdown(md)

    embeddings = embed_chunks(chunks)

    await insert_embeddings(chunks,embeddings)

    await disconnect_db()

if __name__ == "__main__":
    asyncio.run(rag_ingestion())