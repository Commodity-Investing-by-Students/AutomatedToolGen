import os
import pandas as pd
import chromadb 
from langchain.embeddings import SentenceTransformerEmbeddings 
from langchain.vectorstores import Chroma

# Define the base directory for the repo (adjust this to your actual repo location)
base_dir = r"C:\Users\shahd\.vscode\COINS\Hokie-Terminal"  # Prefix with 'r' for raw string

# Create an empty list to hold the data
file_data = []

# Walk through all directories and subdirectories in the base_dir
for root, dirs, files in os.walk(base_dir):
    for file in files:
        # Consider only code files (e.g., .py files, but you can extend this to others)
        if file.endswith(('.py', '.js', '.jsx', '.html', '.css', '.java', '.txt')):  # Add other extensions as needed
            file_path = os.path.join(root, file)
            try:
                # Open the file and read its contents
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                
                # Append file name and its code to the list
                file_data.append([file_path, code])
            
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

# Create a DataFrame with the file data
df = pd.DataFrame(file_data, columns=['File', 'Code'])

# Set up the Chroma Vector Store
chroma_client = chromadb.PersistentClient(path='chroma_git_repo')  # Directory to store the Chroma vector database
sentence_transformer_ef = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Prepare the texts and metadatas for Chroma
texts = []
metadatas = []
for index, row in df.iterrows():
    file_path = row['File']
    file_content = row['Code']
    
    # Use file content as text and file path as metadata
    texts.append(file_content)
    metadatas.append({'file_path': file_path})

# Store the file content and metadata in Chroma
vectordb = Chroma.from_texts(
    texts, 
    collection_name='git_code_files', 
    persist_directory='chroma_git_repo',  # Directory where embeddings are persisted
    embedding=sentence_transformer_ef, 
    metadatas=metadatas
)

# Persist the Chroma database
vectordb.persist()

# Print success message
print("File contents have been embedded and stored in Chroma vector database.")
