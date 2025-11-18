import os
import datetime
from modules.connect_sftp import connect_sftp
from modules.get_and_decompress import get_and_decompress
from common.config import NFOLDER, LIMIT_DATE

def carrier():
    ssh, sftp = connect_sftp()
    if not sftp:
        return
    
    try:
        remote_dir = "receber"
        local_folder = NFOLDER

        now = datetime.datetime.now()
        time_limit = now - datetime.timedelta(days=LIMIT_DATE)

        remote_files = sftp.listdir_attr(remote_dir)

        for file_attr in remote_files:
            file_time = datetime.datetime.fromtimestamp(file_attr.st_mtime)
            file_name = file_attr.filename

            if file_time >= time_limit and file_name.endswith(".gz"):
                remote_path = f"{remote_dir}/{file_name}"
                final_file = get_and_decompress(sftp, remote_path, local_folder)
                if file_name:
                    print(f"File ready: {os.path.basename(final_file)}\n")
    
    finally:
        sftp.close()
        ssh.close()
        print("Connection closed.\n")