import os
from dotenv import load_dotenv

# configuration
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
NFOLDER = os.path.join(ROOT_DIR, "notnormalizedfiles")      # name of the folder with the not normalized files
FOLDER = os.path.join(ROOT_DIR, "normalizedfiles")          # name of the folder with the normalized files
LINE_NAME = 4                                               # line index (5th line)
COL_START = 6                                               # start column
COL_END = 16                                                # end column
LIMIT_DATE = 1                                              # n of days
CLEAN_DATE = 30                                             # n of days to clean folders

STATES = [
    "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",
    "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
    "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"
]

#server
PORT = 8080
IP = "localhost"

# .env
ENV_PATH = os.path.join(ROOT_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH)

SFTP_HOST = os.getenv("SFTP_HOST")
SFTP_PORT = int(os.getenv("SFTP_PORT", 22))
SFTP_USER = os.getenv("SFTP_USER")
SFTP_PASS = os.getenv("SFTP_PASS")