import os
import datetime

def clean_old_files(folder_path, days=30):
    """Delete files older than <days> from the given folder using datetime."""
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(days=days)
    deleted = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if not os.path.isfile(file_path):
            continue

        file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        if file_mtime < cutoff:
            os.remove(file_path)
            print(f"Deleted old file: {os.path.basename(filename)}")
            deleted += 1

    print(f"Cleanup complete. {deleted} file(s) removed.\n")
