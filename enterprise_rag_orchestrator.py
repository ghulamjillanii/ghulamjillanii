import os
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

class RAGOrchestrator:
    def __init__(self, vector_store):
        self.llm = OpenAI(model_name="gpt-4o")
        self.vector_store = vector_store

    def get_answer(self, query):
        qa_chain = RetrievalQA.from_chain_type(llm=self.llm, retriever=self.vector_store.as_retriever())
        return qa_chain.run(query)

if __name__ == "__main__":
    # Example usage in enterprise production
    print("RAG Orchestrator initialized.")
