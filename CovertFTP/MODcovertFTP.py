from ftplib import FTP
from sys import * 

def count_permission_bits(listing): 
    
    binaries = []
    
    # 7 bit mode
    if METHOD:
        for line in listing:
            raw_perms = line[:10]
            if raw_perms[:3] == "---":
                raw_perms = raw_perms.replace("-", "0")
                # print(raw_perms)
                raw_perms = raw_perms.replace("d", "1")     # using replace like this is super lazy lol
                raw_perms = raw_perms.replace("r", "1")
                raw_perms = raw_perms.replace("w", "1")
                raw_perms = raw_perms.replace("x", "1")
                binaries.append(raw_perms)
    # 10 bit mode
    else:
        for line in listing:
            raw_perms = line[:10]
            raw_perms = raw_perms.replace("-", "0")
            # print(raw_perms)
            raw_perms = raw_perms.replace("d", "1")
            raw_perms = raw_perms.replace("r", "1")
            raw_perms = raw_perms.replace("w", "1")
            raw_perms = raw_perms.replace("x", "1")
            binaries.append(raw_perms)

    if DEBUG:
        print(binaries)

    return binaries

def seven_decode(binaries):
    
    # make slices of 7 
    slices = []
    chars = []
    for b in binaries:
        slices.append(b[3:])
        chars.append(chr(int(b[3:], 2)))

    # make the converted char list into string 
    covert_message = ''.join(chars)

    if DEBUG:
        print(slices)
        print(chars)
        print(covert_message)

    return covert_message

def ten_decode(binaries):
    
    # combine everything into one long string 
    totality = ''
    for b in binaries:
        totality += b

    if DEBUG:
        print(totality)
        print(len(totality))

    # then divide into 7 bit slices
    slices = []
    chars = []
    while len(totality) >= 7:
        slices.append(totality[:7])
        chars.append(chr(int(totality[:7], 2)))
        totality = totality[7:]

    # make the converted char list into string 
    covert_message = ''.join(chars)

    if DEBUG:
        print(slices)
        print(chars)
        print(covert_message)

    # double check the bits are all still there, sanity check
    if DEBUG:
        test = ''
        for b in slices:
            test += b 
        print("test is ")
        print(len(test))

    return covert_message


if __name__ == "__main__":
    
    # Variables 
    # Timo FTP is 138.47.99.64 on port 21
    DEBUG = True
    HOST = '138.47.99.64'
    PORT = 21
    USER = 'anonymous'
    PASS = ''
    DIRECTORY = '/10'
    USE_PASSIVE = True
    METHOD = False # True indicates 7 bit mode and False indicates 10 bit mode 

    # Gather information from server
    ftp = FTP()
    ftp.connect(host=HOST, port=PORT)
    ftp.login(user=USER, passwd=PASS)
    ftp.set_pasv(USE_PASSIVE)
    ftp.cwd(DIRECTORY)
    listing = []
    ftp.dir(listing.append)
    ftp.quit()
    
    if DEBUG:
        print(listing)

    # convert perms into binary
    binaries = count_permission_bits(listing)

    if METHOD:
        seven_decode(binaries)
    else:
        ten_decode(binaries)

    
