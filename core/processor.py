import os
from common.config import NFOLDER, FOLDER
from modules.extract_name_from_file import extract_name_from_file
from modules.process_file import process_file

def processor():
    for file in os.listdir(NFOLDER):
        if ".txt" in file.lower() and not file.lower().endswith(".gz"):
            src_path = os.path.join(NFOLDER, file)

            # Extract the output name before processing
            file_name = extract_name_from_file(src_path)
            if not file_name:
                continue

            dst_path = os.path.join(FOLDER, f"{file_name}.txt")

            if os.path.exists(dst_path):
                print(f"Skipping: {file_name}.txt already exists locally.")
                continue

            process_file(src_path, FOLDER)
