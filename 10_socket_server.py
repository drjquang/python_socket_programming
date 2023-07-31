import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

DISCONNECT_MESSAGE = '!DISCONNECTED'


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected')
    isConnected = True
    while isConnected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                isConnected = False
            print(f'[{addr}] {msg}')
            conn.send('MSG received'.encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f'[LISTENING] Server is listening on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONs] {threading.active_count() - 1}')


print('[STARTING] Server is starting ...')
start()
