import os
import uuid

def uniqid(prefix=''):
    return f"{f'{prefix}-' if bool(prefix) else ''}{uuid.uuid4().hex[:13]}"

def createDir(path: str) -> None:
    """
    Create a directory (and any necessary parent directories).
    If the directory already exists, does nothing.
    """
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory created (or already existed): {path}")
    except Exception as e:
        print(f"Failed to create directory {path}: {e}")