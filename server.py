# server.py
import http.server
import socketserver
import os
from common.config import FOLDER, PORT, IP


# change the directory to serve only the normalized files

def start_server():
    os.chdir(FOLDER)

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving normalized files at http://{IP}:{PORT}")
        httpd.serve_forever()
