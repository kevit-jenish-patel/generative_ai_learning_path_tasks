from apps.augmentation.augmentation_pipeline import generate_prompt
from apps.core.db_config import get_collection
from apps.generation.generation_pipeline import generate_llm_response
from apps.retrieval.retrieval_pipeline import retrieve_similar_results
from apps.utils.response_handlers import write_to_file

collection = get_collection()

def run_rag_pipeline(query):

    print("Retrieving Similar results")
    results = retrieve_similar_results(collection, query)
    write_to_file("results.txt", "\n".join(results))

    print("Generating prompt")
    prompt = generate_prompt(query, results)

    print("Generating LLM response")
    response = generate_llm_response(prompt)
    print(f"{response=}")

    return response