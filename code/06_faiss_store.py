from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Free local embeddings (runs fully offline)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create FAISS vector database
vector_store = FAISS.from_documents(chunks, embeddings)

print("FAISS index created successfully 🚀")
