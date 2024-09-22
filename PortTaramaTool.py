import socket


def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 1 saniyelik zaman aşımı
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} açık")
            open_ports.append(port)
        sock.close()
    return open_ports


def main():
    ip = input("IP adresini girin: ")

    # Port aralığı: 1-1000
    start_port = 1
    end_port = 1000

    print(f"{ip} adresinde {start_port}-{end_port} aralığındaki portları tarıyor...")
    open_ports = scan_ports(ip, start_port, end_port)

    if not open_ports:
        print("Açık port bulunamadı.")
    else:
        print(f"Açık portlar: {open_ports}")


if __name__ == "__main__":
    main()

