from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter

def chunk_markdown(md):
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2")
    ]

    # MD splits
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=False)
    markdown_header_chunks = markdown_splitter.split_text(md)

    # Char-level splits
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=100
    )

    # Split
    chunks = text_splitter.split_documents(markdown_header_chunks)

    chunks = [chunk.page_content for chunk in chunks]

    return chunks