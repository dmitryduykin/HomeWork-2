import socket
import os

sock = socket.socket()
sock.bind(('localhost', 8000))
sock.listen(1)

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024).decode("utf-8")
    print ("Data: " + data)

    res = data.split('\n')[0].split(' ')[1]
    path = './' + res

    if not os.path.isfile(path):
            path = './index.html'

    file = open(path, 'rb')
    conn.send("""HTTP/1.1 200 OK\n\n\n""".encode() + file.read())
    conn.send(file.read())
    file.close()
conn.close()
sock.close()