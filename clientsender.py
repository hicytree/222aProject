import socket
import random
from tqdm import tqdm
 
host = '52.12.185.223'
port = 8000
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while (True):
    try:
        x = s.recv(1024)
        if not x:
            s.close()
            break
    except socket.error as e:
        s.close()
        break

# iterations = int(2**20/1024)
# for i in tqdm(range(iterations)):
#     rand = str(random.randint(0, 9))
#     a = rand * 1024 * 1024
#     b = a.encode('utf-8')
#     s.send(b)
#     s.recv(1024 * 1024)