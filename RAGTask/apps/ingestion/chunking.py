from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text, chunk_size=500, overlap=100):
    # Create the text splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    # Split the text
    chunks = splitter.split_text(text)

    return chunks