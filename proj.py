import hashlib
import os


def merge_files(file1, file2, out_file):
    cmd = f"copy /b {file1}+{file2} {out_file}"
    os.system(cmd)


def calculate_hash(file_path):
    with open(file_path, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")
        return digest.hexdigest()
