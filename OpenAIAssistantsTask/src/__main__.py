import asyncio

from src.rag.rag_pipeline import rag_pipeline
from src.retrieval_tool.retrieval_tool_pipeline import retrieval_tool_pipeline

async def main():
    # await rag_pipeline()
    retrieval_tool_pipeline()

if __name__ == '__main__':
    asyncio.run(main())