import hashlib

def calculate_hash(file_path, algorithm="sha256"):
    hash_func = getattr(hashlib, algorithm)()
    
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        return None


def compare_hash(file_hash, expected_hash):
    return file_hash.lower() == expected_hash.lower()
