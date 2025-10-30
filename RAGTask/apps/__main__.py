from apps.ingestion.ingestion_pipeline import run_ingestion_pipeline
from apps.utils.rag_pipeline import run_rag_pipeline
from apps.utils.response_handlers import write_to_file

def main():
    print("Running Ingestion pipeline")
    run_ingestion_pipeline()

    query = ["Can you please share Placement Facts at the Healthcare Program?"]

    print("Running RAG pipeline")
    response = run_rag_pipeline(query)

    write_to_file("response.txt", response)

if __name__ == "__main__":
    main()
