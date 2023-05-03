import sys
import itertools 

# open the key file and read (rb means read byte)
with open("key2", "rb") as f:
    key = bytearray(f.read())

# take the message from stdin
message = sys.stdin.buffer.read()

# XOR encryption/decryption
res = bytearray(len(message))

# handle cases where the key is not the same size as the message
if (len(key) != len(message)):
    key_iter = itertools.cycle(key) # the iterator that repeats the key
    for i in range(len(message)):
        res[i] = message[i] ^ next(key_iter) # use next() to get the next element from the key iterator
else:
    for i in range(len(message)):
        res[i] = message[i] ^ key[i % len(key)]

# write to stdout or a file (w means write, obvi)
if len(sys.argv) > 1:
    with open(sys.argv[1], "wb") as f:
        f.write(res)
else:
    sys.stdout.buffer.write(res)
