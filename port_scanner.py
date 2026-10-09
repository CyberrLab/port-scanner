
import socket
from datetime import datetime


def scan_port(target, port, timeout=0.5):
    """Check whether a TCP port is accepting connections."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        return result == 0


def main():
    target = "127.0.0.1"  # Scan only your own computer
    ports = [22, 80, 135, 443, 445, 3306, 5000, 8000, 8080]

    print("=== Python TCP Port Scanner ===")
    print(f"Target: {target} (your own computer)")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 40)

    open_ports = []

    for port in ports:
        if scan_port(target, port):
            open_ports.append(port)
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED or FILTERED")

    print("-" * 40)
    print(f"Scan complete. Open ports found: {len(open_ports)}")


if __name__ == "__main__":
    main()
