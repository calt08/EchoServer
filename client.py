import socket
# AF_INET = IPV4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8080))

msg_to_send = input("insert your message: ")

# Send msg
s.send(bytes(msg_to_send, "utf-8"))

input("Press enter!")  # Just to make it wait

# Recieve msg
msg = s.recv(1024)  # buffer
print(msg.decode("utf-8"))
s.close()
