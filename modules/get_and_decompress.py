import gzip
import shutil
import os

def get_and_decompress(sftp, remote_path, local_folder):
    """Downloads and decompresses a .gz file from an open SFTP connection,
    skipping if the decompressed file already exists locally."""
    try:
        local_gz = os.path.join(local_folder, os.path.basename(remote_path))
        local_file = local_gz[:-3]  # remove .gz from the name

        # If the decompressed version already exists, skip everything
        if os.path.exists(local_file):
            print(f"Skipping: {os.path.basename(local_file)} already exists locally.")
            return local_file

        # Download the .gz file
        print(f"Downloading: {os.path.basename(remote_path)}")
        sftp.get(remote_path, local_gz)

        # Decompress
        with gzip.open(local_gz, "rb") as f_in, open(local_file, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
        print(f"Decompressed: {os.path.basename(local_file)}")

        # Remove the .gz after decompression
        os.remove(local_gz)

        return local_file

    except Exception as e:
        print(f"Error processing {remote_path}: {e}")
        return None