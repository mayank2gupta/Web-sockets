import socket

s = socket.socket()
s.connect(('localhost', 12345))
while True:
    msg = input("Client: ")
    sMsg = msg.encode()
    s.sendall(sMsg)
    rMsg = s.recv(1024)
    rMsg = rMsg.decode("utf-8")
    if rMsg == "exit":
        s.sendall(b"exit")
        break
    print('Server:', rMsg)
s.close()