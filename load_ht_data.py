import chromadb 
from chromadb.utils import embedding_functions
from get_ht_data import get_ht_data


df = get_ht_data()
emb_fn = embedding_functions.DefaultEmbeddingFunction()

# Chroma initialization
client = chromadb.Client()
collection = client.create_collection(name="ht_collection", embedding_function=emb_fn)

# Iterate through DataFrame and embed code
for index, row in df.iterrows():
    code = row['Code']
    file_name = row['File']
    embedding = emb_fn(code)
    
    # Add embedding metadata (file path) to Chroma collection
    collection.add(
        embeddings=[embedding],
        documents=[code],  
        metadatas=[{"file": file_name}]
    )

print("Data successfully stored in Chroma!")