from langfuse import observe

from src.core.config import settings
from src.core.openai_config import client
from src.retrieval_tool.vector_store import create_vector_store, upload_file_to_vector_store
from src.utils.data_extraction import fetch_page_soup, convert_to_markdown

@observe()
def create_assistant():
    soup = fetch_page_soup(settings.WEBSITE_URL_TO_SCRAP)

    main_div = soup.select_one("main#main-content>div")

    md = convert_to_markdown(main_div)

    vector_store = create_vector_store()

    vector_file = upload_file_to_vector_store("./documents/index.md",vector_store)

    system_prompt=\
        (
            "You are a Amazon rainforest guide that responds to user's queries with polite and accurate responses. "
            "You are a document-based assistant. "
            "You must only answer using the information found in the uploaded files. "
            "If the user asks something that is not found in the files,"
            "respond with: 'I don’t have that information in my knowledge base.' "
            "Do NOT use your own knowledge or assumptions. "
            "Always use the file search tool for every question. "
            "Respond only in Markdown format, using proper headings, lists, code blocks, or formatting where appropriate."
            "Include only this url `https://www.worldwildlife.org/places/amazon/` as source of your knowledge for each response"
        )

    assistant = client.beta.assistants.create(
        model="gpt-4.1-nano",
        name="The Amazon Rainforest Guide",
        instructions=system_prompt,
        temperature=0.3,
        tools=[{"type": "file_search"}],
        tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
    )

    print("OPENAI_ASSISTANT_ID = ",assistant.id)
    return assistant

if __name__ == "__main__":
    create_assistant()

