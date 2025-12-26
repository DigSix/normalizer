import os
from datetime import datetime
from modules.clean_state_preserving import clean_state_preserving
from modules.extract_name_from_file import extract_name_from_file

def process_file(input_path: str, output_path: str):
    try:
        with open(input_path, "r", encoding="windows-1252") as f_in:
            lines = f_in.readlines()
    except Exception as e:
        print(f"[ERROR] Failed to read {input_path}: {e}")
        return

    # Use the shared name extractor
    file_name = extract_name_from_file(input_path)
    if not file_name:
        print(f"[ERROR] Could not extract name from {input_path}")
        return

    # Clean the lines
    new_lines = [clean_state_preserving(l) for l in lines]

    # Get date
    timestamp = datetime.now().strftime("%d.%m.%Y_%H.%M")

    new_path = os.path.join(output_path, f"{file_name}_{timestamp}.txt")

    # Save the new file
    new_path = os.path.join(output_path, f"{file_name}_{timestamp}.txt")
    with open(new_path, "w", encoding="windows-1252") as f_out:
        f_out.writelines(new_lines)

    print(f"[OK] {os.path.basename(input_path)} → {file_name}_{timestamp}.txt")
