# Semantic Search for E-Commerce

This project implements a **semantic search system** for e-commerce applications using state-of-the-art natural language processing (NLP) techniques. It leverages Hugging Face's pre-trained models, LlamaIndex for document indexing, and LangChain for embeddings to enable **semantic search** over product data.

Semantic search allows users to search for products based on the **meaning** of their query rather than just keyword matching. This makes the search experience more intuitive and accurate.

---

## Features

- **Semantic Search**: Search for products using natural language queries.
- **Custom Embeddings**: Uses Hugging Face's `sentence-transformers/all-MiniLM-L6-v2` model for generating embeddings.
- **Scalable Indexing**: Indexes product data from text files for efficient querying.
- **Interactive Interface**: Allows users to input queries and view search results in real-time.
- **Top-K Results**: Returns the top 5 most relevant results for each query.

---

## Prerequisites

Before running the code, ensure you have the following installed:

- Python 3.8 or higher
- Required Python libraries (install via `pip`)

---

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/semantic-search-ecommerce.git
   cd semantic-search-ecommerce
   ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```
    
3. Place your product data (text files) in the docs directory.


---

## Usage

1. Run the script:

```
python semantic_search.py
```

2. Enter your search query when prompted. For example:

```
Enter your search query (or type 'exit' to quit): lightweight laptop
```
3. View the search results:

```
Search Results:
1. Product: Laptop XYZ - Ultra-lightweight and portable, perfect for travel.
   Similarity: 0.92

2. Product: Laptop ABC - Lightweight design with long battery life.
   Similarity: 0.89
```

4. Type exit to quit the program.

---

## Code Overview
The project consists of the following components:

- `Hugging Face Model`: Uses sentence-transformers/all-MiniLM-L6-v2 for generating embeddings.

- `LlamaIndex`: Handles document indexing and querying.

- `LangChain`: Provides a wrapper for Hugging Face embeddings.

- `Interactive Search`: Allows users to input queries and view results.

---

## File Structure

```
semantic-search-ecommerce/
├── docs/                     # Directory containing product data (text files)
├── semantic_search.py        # Main script for semantic search
├── requirements.txt          # List of dependencies
├── README.md                 # This file
└── .env                      # Environment variables (if needed)
```

---

## Configuration

- Embedding Model: You can change the embedding model by modifying the model_name variable in the script. For example:

```
model_name = "sentence-transformers/all-mpnet-base-v2"
```
- Top-K Results: Adjust the number of results returned by changing the similarity_top_k parameter:

```
query_engine = index.as_query_engine(similarity_top_k=10)
```

---

## Dependencies
The project relies on the following Python libraries:

- `transformers` (Hugging Face)

- `llama-index` (LlamaIndex)

- `langchain-huggingface` (LangChain)

- `python-dotenv` (for environment variables)

Install them using:

```
pip install transformers llama-index langchain-huggingface python-dotenv
```

---

## License
This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/license/mit)  file for details.


