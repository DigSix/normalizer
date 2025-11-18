from common.config import LINE_NAME, COL_START, COL_END

def extract_name_from_file(file_path: str):
    """Reads only enough lines to extract the output filename."""
    try:
        with open(file_path, "r", encoding="windows-1252") as f:
            lines = f.readlines()
            line_name = lines[LINE_NAME]
            file_name = line_name[COL_START:COL_END].strip()
            return file_name
    except Exception as e:
        print(f"[ERROR] Cannot extract name from {file_path}: {e}")
        return None