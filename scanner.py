import socket


while True:

    target = input("Enter domain or IP: ").strip()

    if not target:
        print("Target cannot be empty.")
        print("--------------------------------")
        continue

    try:
        socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid domain or IP address.")
        print("--------------------------------")
        continue

    while True:
        try:
            start_port = int(input("Enter starting port: "))
            end_port = int(input("Enter ending port: "))

            if start_port < 1 or end_port < 1:
                print("Ports cannot be negative or 0.")
                continue

            if start_port > 65535 or end_port > 65535:
                print("Ports cannot be higher than 65535.")
                continue

            if start_port > end_port:
                print("Starting port cannot be greater than ending port.")
                continue

            break

        except ValueError:
            print("Please enter numbers only.")

    open_ports = []

    for port in range(start_port, end_port + 1):
        my_socket = socket.socket()
        my_socket.settimeout(0.5)

        try:
            my_socket.connect((target, port))
            open_ports.append(port)
        except (socket.timeout, socket.error):
            pass

        my_socket.close()

    print("\nScan finished.")
    print(f"Open ports: {len(open_ports)}")

    if open_ports:
        print("Open ports:", open_ports)
    else:
        print("No open ports found.")

    print("--------------------------------")