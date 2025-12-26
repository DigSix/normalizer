import os
from datetime import datetime
from common.config import NFOLDER, FOLDER
from modules.extract_name_from_file import extract_name_from_file
from modules.process_file import process_file

def processor():
    # Maping files
    existing_prefixes = set()

    for f in os.listdir(FOLDER):
        if f.lower().endswith(".txt"):
            base = f.split("_", 1)[0]  # Remove date
            existing_prefixes.add(base)

    for file in os.listdir(NFOLDER):
        if ".txt" in file.lower() and not file.lower().endswith(".gz"):
            src_path = os.path.join(NFOLDER, file)

            # Extract the output name before processing
            file_name = extract_name_from_file(src_path)
            if not file_name:
                continue
            
            if file_name in existing_prefixes:
                print(f"Skipping: {file_name} already exists locally.")
                continue

            process_file(src_path, FOLDER)
