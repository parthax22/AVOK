import socket
import threading
import ipaddress

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3389]

def scan_port(target_host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(f"[+] Port {port}/tcp is open")
        sock.close()
    except Exception as e:
        print(f"Error: {e}")

def scan_host(target_host, ports):
    print(f"[*] Scanning {target_host}...")
    for port in ports:
        threading.Thread(target=scan_port, args=(target_host, port)).start()

def display_host_info(host):
    try:
        host_ip = socket.gethostbyname(host)
        print(f"[*] Target Host: {host}")
        print(f"[*] IP Address: {host_ip}")
    except socket.gaierror:
        print("[!] Could not resolve hostname")

def main():
    target_hosts = input("Enter the target host(s) to scan (comma-separated for multiple hosts): ").split(',')
    start_port = int(input("Enter the starting port (press Enter for default 1): ") or 1)
    end_port = int(input("Enter the ending port (press Enter for default 1024): ") or 1024)

    for host in target_hosts:
        display_host_info(host.strip())
        ports = range(start_port, end_port + 1)
        scan_host(host.strip(), ports)

if __name__ == "__main__":
    main()
