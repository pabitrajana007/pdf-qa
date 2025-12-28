from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.document_loaders import PyPDFLoader


embedding = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

def ingest_pdf(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    docs = splitter.split_documents(pages)

    db = Chroma.from_documents(
        docs,
        embedding,
        persist_directory="chroma_db"
    )
    db.persist()

def query_pdf(question):
    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding
    )

    docs = db.similarity_search(question, k=3)
    context = "\n".join([d.page_content for d in docs])
    return context
