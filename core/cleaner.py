from modules.clean_old_files import clean_old_files
from common.config import NFOLDER, FOLDER, CLEAN_DATE

def cleaner():
    clean_old_files(NFOLDER, CLEAN_DATE)
    clean_old_files(FOLDER, CLEAN_DATE)