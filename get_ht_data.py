import os
import subprocess
import pandas as pd

def get_git_root():
    try:
        # Run the git command to get the top-level directory
        base_dir = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).strip().decode('utf-8')
        return base_dir
    except subprocess.CalledProcessError as e:
        print("Error getting Git repository root:", e)
        return None

# Get the base directory of the Git repository
base_dir = get_git_root()

if base_dir:
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

# Show the DataFrame
print(df)