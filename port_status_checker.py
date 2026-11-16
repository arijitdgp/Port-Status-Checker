import socket


def check_port(host, port, timeout=3):
    """Return whether TCP port is open or closed on the given host."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))

        if result == 0:
            return "OPEN"
        return "CLOSED or FILTERED"

    except socket.gaierror:
        return "ERROR: Hostname could not be resolved."
    except (ValueError, OverflowError):
        return "ERROR: Invalid port number. Enter a value from 1 to 65535."
    except socket.timeout:
        return "CLOSED or FILTERED (connection timed out)"
    except OSError as error:
        return f"ERROR: {error}"


def main():
    print("========== Port Status Checker ==========")

    host = input("Enter hostname or IP address: ").strip()

    if not host:
        print("Error: Hostname or IP address cannot be empty.")
        return

    try:
        port = int(input("Enter port number (1-65535): ").strip())
        if not 1 <= port <= 65535:
            print("Error: Port number must be between 1 and 65535.")
            return
    except ValueError:
        print("Error: Please enter a valid integer port number.")
        return

    status = check_port(host, port)
    print(f"\nHost: {host}")
    print(f"Port: {port}")
    print(f"Status: {status}")
    print("==========================================")


if __name__ == "__main__":
    main()
