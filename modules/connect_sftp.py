import paramiko
from common.config import SFTP_HOST, SFTP_PORT, SFTP_USER, SFTP_PASS

def connect_sftp():
    """Opens an SFTP-only connection using Transport."""
    try:
        # Create the transport object (direct TCP + SSH handshake)
        transport = paramiko.Transport((SFTP_HOST, SFTP_PORT))

        # Auth without opening a normal SSH session
        transport.connect(username=SFTP_USER, password=SFTP_PASS)

        # Create an SFTP session directly
        sftp = paramiko.SFTPClient.from_transport(transport)

        print("Connected to SFTP!\n")
        return transport, sftp

    except Exception as e:
        print(f"SFTP connection error: {e}")
        return None, None