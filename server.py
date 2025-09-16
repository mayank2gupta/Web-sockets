import socket

s = socket.socket()
s.bind(('localhost', 12345))
print("I am waiting")
s.listen(1)
print("wait over")
conn, addr = s.accept()
print('Connected by', addr)
while True:
    rMsg = conn.recv(1024)
    rMsg = rMsg.decode("utf-8")
    if rMsg == "exit":
        conn.sendall(b"exit")
        break
    print('Client:', rMsg)
    sMsg = input('Server: ')
    sMsg = sMsg.encode()
    conn.sendall(sMsg)
    
conn.close()
