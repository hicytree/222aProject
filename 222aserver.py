import socket
import os
 
host = ''
port = 8000
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)
print("Waiting for connection...")
c, addr = s.accept()

os.system("wget -nv -p http://54.188.10.173/")

# while True:
#     x = c.recv(1024 * 1024)
#     if x:
#         c.send(x)
#     if not x:
#         c.close()
#         break

c.close()