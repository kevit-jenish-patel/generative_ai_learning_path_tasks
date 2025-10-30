from apps.core.db_config import get_collection
from apps.ingestion.brochure_extraction import get_text_from_brochures
from apps.ingestion.chunking import chunk_text

collection = get_collection()

def run_ingestion_pipeline():
    # extract all the text from the brochure files
    text = get_text_from_brochures()

    # chunk the text
    chunks = chunk_text(text)

    #add to database
    ids = [f"chunk_{i+1}" for i in range(len(chunks))]
    collection.add(documents=chunks,ids=ids)
