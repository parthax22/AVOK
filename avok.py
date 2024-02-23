import socket
import threading
import ipaddress



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

def scan_host(target_host, start_port, end_port):
    print(f"[*] Scanning {target_host}...")
    for port in range(start_port, end_port + 1):
        scan_port(target_host, port)

def display_host_info(host):
    try:
        host_ip = socket.gethostbyname(host)
        print(f"[*] Domain: {host}")
        print(f"[*] IP Address: {host_ip}")
        return host_ip
    except socket.gaierror:
        print("[!] Could not resolve hostname")
        return None

def main():
    print("\033[91m" + r"""
 $$$$$$\  $$\    $$\  $$$$$$\  $$\   $$\ 
$$  __$$\ $$ |   $$ |$$  __$$\ $$ | $$  |
$$ /  $$ |$$ |   $$ |$$ /  $$ |$$ |$$  / 
$$$$$$$$ |\$$\  $$  |$$ |  $$ |$$$$$  /  
$$  __$$ | \$$\$$  / $$ |  $$ |$$  $$<   
$$ |  $$ |  \$$$  /  $$ |  $$ |$$ |\$$\  
$$ |  $$ |   \$  /    $$$$$$  |$$ | \$$\ 
\__|  \__|    \_/     \______/ \__|  \__|
                   
                      𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚍 𝚋𝚢 𝚊𝚟𝚢𝚊𝚢𝚜𝚎𝚌
                                         
    """ + "\033[0m")
    target_hosts = input("Enter the target host to scan: ").split(',')
    start_port = int(input("Enter the starting port (default=1): ") or 1)
    end_port = int(input("Enter the ending port (default=1024): ") or 1024)

    for host in target_hosts:
        host = host.strip()
        print("\n" + "="*50)
        print(f"[^] Target Host: {host}")
        print("="*50)
        ip_address = display_host_info(host)
        if ip_address:
            try:
                ipaddress.IPv4Address(ip_address)
                scan_host(ip_address, start_port, end_port)
            except ipaddress.AddressValueError:
                print("[!] Invalid IPv4 address.")
                continue

if __name__ == "__main__":
    main()
