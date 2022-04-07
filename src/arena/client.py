import socket

PORT = 5050
FORMAT = 'utf-8'
localsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def initiate():
    while True:
        try:
            HOST = input("Host: ")
            localsocket.connect((HOST,PORT))
            break
        except socket.gaierror:
            print("Host is not available!")
    print("Successfully connected.")
    while True:
        msg = input("[You]: ")
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (64 - len(send_length))
        localsocket.send(send_length)
        localsocket.send(message)

        if msg == "!DISCONNECT":
            print("Exiting match..")
            break

        msg_length = localsocket.recv(64).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = localsocket.recv(msg_length).decode(FORMAT)

            print(f"[{HOST}]: {msg}")
