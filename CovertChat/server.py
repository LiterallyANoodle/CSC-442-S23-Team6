from socket import *
from time import sleep 

port = 1337

s = socket(AF_INET, SOCK_STREAM)
s.bind(("", port))

s.listen(0)
print("Server is listening...") 

c, addr = s.accept()

message = "Some message...\n"

for i in message: 
    c.send(i.encode())
    sleep(0.1)

c.send("EOF".encode())
print("Message sent...")
c.close()
