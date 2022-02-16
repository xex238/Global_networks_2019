# Работа с сокетами (приём данных)
import socket

sock = socket.socket()
#sock.bind(('127.0.0.1', 9090))
sock.bind(('127.0.0.1', 49100))
sock.listen(1)
conn, addr = sock.accept()

print ("connected:", addr)
print("conn = ", conn)
print("conn.recv(1024) = ", conn.recv(1024))

#while True:
#    data = conn.recv(1024)
#    if not data:
#        break
#    conn.send(data.upper())

conn.close()