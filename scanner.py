import socket
import subprocess

COMMON_PORTS = [22, 80, 443]

def ping_host(ip):
    try:
        output = subprocess.check_output(
            ["ping", "-c", "1", ip],
            stderr=subprocess.DEVNULL
        )
        return True
    except subprocess.CalledProcessError:
        return False

def scan_ports(ip):
    open_ports = []
    for port in COMMON_PORTS:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        s.close()
    return open_ports

def main():
    network = input("Enter network (example: 192.168.1.): ")

    print("\n Scanning network...\n")
    report = []

    for i in range(1, 11):
        ip = network + str(i)
        if ping_host(ip):
            ports = scan_ports(ip)
            print(f"Host Alive: {ip} | Open Ports: {ports}")
            report.append(f"{ip} | Open Ports: {ports}")
        else:
            print(f" Host Down: {ip}")

    with open("outputs/report.txt", "w") as f:
        for line in report:
            f.write(line + "\n")

    print("\n Scan complete. Report saved to outputs/report.txt")

if __name__ == "__main__":
    main()
