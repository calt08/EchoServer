import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8080))
s.listen(5)

while True:
    clientsocket, adress = s.accept()
    print(f"Connected to {adress}")
    clientsocket.send(bytes("Welcome!", "utf-8"))
