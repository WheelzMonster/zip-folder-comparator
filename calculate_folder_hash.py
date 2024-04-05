import hashlib
import os


def calculate_folder_hash(folder_path):
    sha256_hash = hashlib.sha256()
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                # Read the file in chunks to handle large files
                while chunk := f.read(4096):
                    sha256_hash.update(chunk)
    return sha256_hash.hexdigest()
