## Normalizer

### About

**Normalizer** is a Python tool designed to automate the handling of files received via SFTP.

It downloads files from a remote server, decompresses `.gz` archives, cleans and standardizes text content, and outputs only normalized data ready for integration with other systems.

This project was built to replace a daily manual workflow, reducing operational effort and minimizing human error.

---

### What it does

- Connects to an SFTP server using environment variables  
- Downloads files from the last 24 hours  
- Automatically decompresses `.gz` files  
- Cleans and normalizes text data  
- Keeps only processed output files  
- Can run on a daily schedule or inside Docker  
- Exposes normalized files through a simple HTTP server  

---

### Stack

- Python 3  
- Paramiko (SFTP)  
- python-dotenv  
- gzip / shutil / os  
- Docker (optional)

---

### Running locally

```bash
git clone https://github.com/DigSix/normalizer
cd normalizer

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

```.env
SFTP_HOST=your.server.com
SFTP_PORT=22
SFTP_USER=username
SFTP_PASS=password
```

```bash
python main.py hh mm  #First run, 6 hours intervals.
```
