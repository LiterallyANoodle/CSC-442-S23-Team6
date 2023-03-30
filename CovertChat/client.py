from socket import * 
from sys import stdout
from time import time 

ip = "localhost"
port = 1337

s = socket(AF_INET, SOCK_STREAM)

s.connect((ip, port))

data = s.recv(4096).decode()

while (data.rstrip("\n") != "EOF"):
    stdout.write(data)
    stdout.flush()
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()
    delta = round(t1 - t0, 3)
    stdout.write(f" {delta}\n")

s.close()
