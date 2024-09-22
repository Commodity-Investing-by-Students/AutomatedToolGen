import os
import pandas as pd

# Using HT repo as base directory (adjust this to your HT repo path)
base_dir = r"C:/Users/aaronboateng/Desktop/COINS Quant/Hokie-Terminal"  # Prefix with 'r' for raw string
file_data = []

def get_ht_data():
# Walk through all directories and subdirectories in HT repo
    for root, files in os.walk(base_dir):
        for file in files:
         if file.endswith(('.py', '.js', '.jsx', '.html', '.css', '.txt', '.csv', '.ipynb')): 
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
            
                file_data.append([file_path, code])
            
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    df = pd.DataFrame(file_data, columns=['File', 'Code'])
    return df

print("HT Data successfully retrieved!")


