from transformers import AutoTokenizer, AutoModel
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.settings import Settings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load a pre-trained model and tokenizer from Hugging Face
model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Load your product data (assuming you have a directory with text files)
documents = SimpleDirectoryReader('docs').load_data()

# Create a custom embedding model for LlamaIndex
embed_model = HuggingFaceEmbeddings(model_name=model_name)

# Configure LlamaIndex settings with the custom embedding model
Settings.embed_model = embed_model

# Create an index using LlamaIndex
index = VectorStoreIndex.from_documents(documents)

# Create a query engine
query_engine = index.as_query_engine(similarity_top_k=1)

# Function to perform semantic search
def search_products(query):
    results = query_engine.query(query)
    return results

# Get user input and perform search
if __name__ == "__main__":
    while True:
        # Get user input
        query = input("Enter your search query (or type 'exit' to quit): ")
        
        if query.lower() == 'exit':
            print("Exiting...")
            break
        
        # Perform semantic search
        results = search_products(query)
        
        # Display results
        if results:
            print("\nSearch Results:")
            for i, result in enumerate(results.source_nodes, 1):
                print(f"{i}. Product: {result.node.text}\n   Similarity: {result.score}\n")
        else:
            print("No results found.\n")