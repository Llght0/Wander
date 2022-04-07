import socket

PORT = 5050
FORMAT = 'utf-8'
localsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def initiate():
    try:
        SERVER = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        while True:
            try:
                SERVER = input("Localhost address could not be resolved automatically. Please enter address.\n")
                socket.inet_aton(SERVER)
                break
            except socket.gaierror:
                print("Invalid address!")

    localsocket.bind((SERVER, PORT))
    localsocket.listen()

    print(f"Hosting at: {SERVER}")

    while True:
        print("Waiting for player to join...")
        conn, addr = localsocket.accept()
        print(f"{addr} has joined.")

        while True:
            msg_length = conn.recv(64).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)

                if msg == "!DISCONNECT" or msg == "!QUIT":
                    break

                print(f"[{addr}]: {msg}")

                msg = input("[You]: ")
                message = msg.encode(FORMAT)
                msg_length = len(message)
                send_length = str(msg_length).encode(FORMAT)
                send_length += b' ' * (64 - len(send_length))
                conn.send(send_length)
                conn.send(message)

        conn.close()