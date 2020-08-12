import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 8080))
print("Listening on port 8080")
print()
s.listen(5)

while True:
    clientsocket, adress = s.accept()
    print(f"Connected to {adress}")
    msg = clientsocket.recv(1024)  # buffer
    msgData = msg.decode("utf-8")

    print("Recieved:" + msgData)
    print("Sending text...")
    clientsocket.send(msg)
    print("Text Sent!")
