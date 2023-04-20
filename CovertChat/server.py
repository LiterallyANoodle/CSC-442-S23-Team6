from socket import *
from time import sleep 

# function creates a list of intervals to use 
def chopping_time(covert_message):

    # convert to bytes-like objects 
    str_encode = covert_message.encode()
    # str_bytes = []
    deltas = []
    for byte in str_encode:
        if DEBUG:
            print(bin(byte))
        # str_bytes.append(b)

        # convert bits into timings 
        # d > 0.25 returns a 1 
        # d <= 0.25 returns a 0 
        byte_clean = bin(byte)[2:]
        if DEBUG:
            print(byte, byte_clean)
        for bit in byte_clean:
            # if DEBUG:
            #     print(bit)
            if bit == '1':
                deltas.append(0.35)
            else:
                deltas.append(0.1)

    if DEBUG:
        print(deltas)

    return deltas

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
        message = "This is my message. My message is very long. My message is so long, in fact, that you could probably hide another much smaller message within it.\n"
        covert_message = "Secret"

        deltas = chopping_time(covert_message)

        # send one letter at a time
        for i in range(len(message)): 
            c.send(message[i].encode())
            try:
                sleep(deltas[i])
            except:
                sleep(0.1)

        # end and cleanup 
        c.send("EOF".encode())
        print("Message sent...")
    
    # cleanup
    c.close()

if __name__ == "__main__": 
    DEBUG = False
    main()