import os
from collections import Counter

def count_file_extensions(folder_path):
    extensions = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            _, ext = os.path.splitext(file)
            if ext:  # Only count files with an extension
                extensions.append(ext)
    return Counter(extensions)

# Input from user
folder_path = input("Enter folder path: ")

# Count and display extensions
extension_counts = count_file_extensions(folder_path)

for ext, count in extension_counts.items():
    print(f"{ext}: {count}")
