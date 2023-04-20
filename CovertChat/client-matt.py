from socket import * 
from sys import stdout
from time import time 

# function translates deltas back into bits 
def read_covert(deltas):

    # deltas to bits
    bits = []
    for d in deltas:
        if d > 0.25:
            bits.append('1')
        else:
            bits.append('0')

    # slice bits
    char_bits = []
    bits_length = range(len(bits)//7)
    for i in bits_length:
        char_bits.append("".join(bits[:7]))
        bits = bits[7:]

    if DEBUG:
        print(char_bits)

    # bit slices to ints 
    chars = []
    for char in char_bits:
        chars.append(int(char, 2))

    # remove any trailing 0's (ints)
    chars = [chr(item) for item in chars if item != 0 ]

    if DEBUG:
        print(chars)

    return "".join(chars)


def main():

    # connection setup 
    ip = "138.47.99.64"
    port = 31337

    s = socket(AF_INET, SOCK_STREAM)

    s.connect((ip, port))

    data = s.recv(4096).decode()
    deltas = []

    # retrieve data and covert message
    while (data.rstrip("\n") != "EOF"):
        stdout.write(data)
        stdout.flush()
        t0 = time()
        data = s.recv(4096).decode()
        t1 = time()
        delta = round(t1 - t0, 3)
        deltas.append(delta)
        # stdout.write(f" {delta}\n")

    s.close()

    if DEBUG:
        print(deltas)

    covert_message = read_covert(deltas)
    print(covert_message)


if __name__ == "__main__":
    DEBUG = False
    main()