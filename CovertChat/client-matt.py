from socket import * 
from sys import stdout
from time import time 

# function translates deltas back into bits 
def read_covert(deltas, cutoff=0.25, slice_size=7):

    # deltas to bits
    bits = []
    for d in deltas:
        if d > cutoff:
            bits.append('1')
        else:
            bits.append('0')

    # slice bits
    char_bits = []
    bits_length = range(len(bits)//slice_size)
    for i in bits_length:
        char_bits.append("".join(bits[:slice_size]))
        bits = bits[slice_size:]

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
    # test server is 138.47.99.64
    # port 31337
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
        print("DELTAS ------------->", deltas)
        print("DELTAS LEN --------->", len(deltas))

    cutoff = 0.07
    slice_size = 8
    covert_message = read_covert(deltas, cutoff, slice_size)
    print(covert_message)

    return deltas

# test to find the average timing over many iterations 
# this helps in finding the cutoff point 
def average_test():
    deltass = []
    avgs = []
    for i in range(3): # send 5 requests for a message 
        deltass.append(main())

    # align by columns instead of rows in the matrix 
    columns = []
    for i in range(len(deltass[0])):
        column = []
        for row in deltass:
            column.append(row[i])
        columns.append(column)

    print("DELTASS --->", deltass)
    print("COLUMNS --->", columns)

    # average every column 
    for col in columns:
        avgs.append(round(sum(col)/len(col), 3))

    print("AVGS ------>", avgs)

if __name__ == "__main__":
    DEBUG = True
    AVG_TEST = False

    if AVG_TEST:
        average_test()
    else:
        main()
    