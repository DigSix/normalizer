import paramiko
import socket
from common.config import SFTP_HOST, SFTP_PORT, SFTP_USER, SFTP_PASS

def connect_sftp():
    """Opens an SFTP-only connection using Transport with proper timeouts."""
    try:
        # Create a TCP socket with timeout
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(50)
        sock.connect((SFTP_HOST, SFTP_PORT))

        # Create the SSH transport using this socket
        transport = paramiko.Transport(sock)
        transport.banner_timeout = 50
        transport.auth_timeout = 50

        # Connect using username + password
        transport.connect(username=SFTP_USER, password=SFTP_PASS)

        # Create SFTP session
        sftp = paramiko.SFTPClient.from_transport(transport)

        print("Connected to SFTP!\n")
        return transport, sftp

    except Exception as e:
        print(f"SFTP connection error: {e}")
        return None, None
