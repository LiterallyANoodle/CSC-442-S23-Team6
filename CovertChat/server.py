from socket import *
from time import sleep 

def main():

    # server setup 
    port = 1337
    repeat = True

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("", port))

    # continuously send messages to connecting clients 
    while (repeat):
        s.listen(0)
        print("Server is listening...") 

        c, addr = s.accept()

        # my messages
        message = "Some message...\n"
        covert_message = "Secret"

        # send one letter at a time
        for i in message: 
            c.send(i.encode())
            sleep(0.1)

        # end and cleanup 
        c.send("EOF".encode())
        print("Message sent...")
    
    # cleanup
    c.close()

if __name__ == "__main__": 
    main()