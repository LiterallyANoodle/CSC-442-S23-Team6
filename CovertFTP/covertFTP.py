from ftplib import FTP

def count_permission_bits(listing): 
    
    raw_perms = []
    for line in listing:
        raw_perms.append(line[:11])

    print(raw_perms)

if __name__ == "__main__":
    
    # Variables 
    HOST = '138.47.99.64'
    PORT = 21
    USER = 'anonymous'
    PASS = ''
    METHOD = True # True indicates 7 bit mode and False indicates 10 bit mode 

    # Gather information from server
    ftp = FTP()
    ftp.connect(host=HOST, port=PORT)
    ftp.login(user=USER, passwd=PASS)
    ftp.retrlines('LIST')
    ftp.quit()
    
    print(files)

    # count_permission_bits(listing)

    
