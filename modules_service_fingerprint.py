import socket

def fingerprint_services(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((host, port))
        sock.send(b"\n")
        banner = sock.recv(1024).decode(errors="ignore")
        sock.close()
        return banner.strip() if banner else "No banner"
    except Exception:
        return "Unknown or no response"