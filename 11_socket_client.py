import socket
import pickle

DISCONNECT_MESSAGE = '!DISCONNECTED'
HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
SERVER = '172.168.98.20' # change this when move to new location
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(FORMAT))


send("Client sends hello to server")
send(DISCONNECT_MESSAGE)

