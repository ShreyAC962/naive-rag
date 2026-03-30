# Load docs

import os

def load_docs(data_path="data/docs"):
    docs = []
    for file in os.listdir(data_path):
        with open(os.path.join(data_path, file), "r") as f:
            docs.append(f.read())
    return docs

