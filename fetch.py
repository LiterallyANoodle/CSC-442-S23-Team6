
from ftplib import FTP

# FTP server details
IP = "138.47.99.64"
PORT = 21
USER = "anonymous"
PASSWORD = ""
DIRECTORY = "/"
METHOD = 10 # 7 or 10
USE_PASSIVE = True # set to False if the connection times out

def sevenBit(line):

    chCounter = 0
    letter = ""
    for ch in line:
        if chCounter > 2 and chCounter < 10:
            if ch == "-":
                letter = letter + "0"
            else:
                letter = letter + "1"
        chCounter += 1
    letter = chr(int(letter,2))
    return letter

def tenBit(line):
    chCounter = 0
    letter = ""
    for ch in line:
        if chCounter < 10:
            if ch == "-":
                letter = letter + "0"
            else:
                letter = letter + "1"
        chCounter += 1
    letter = chr(int(letter,2))
    return letter

# connect and login to the FTP server (if anonymous type anonymous and hit enter)
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files (ls -l)
ftp.cwd(DIRECTORY)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

covertM = ""

if METHOD == 10:
    for f in files:
        covertM = covertM + tenBit(f)
elif METHOD == 7:

        # 7 bit method
    checkDash = "---"
    for f in files: # check if the first 3 permissions are dashes, if not then move on
        check3 = ""  

        for ch in f: # for every character in the line
            if len(check3) >= 3:
                if check3 == checkDash:
                    covertM = covertM + sevenBit(f) # call sevenBit function given the line of output
                    break
                else:
                    break
            
            check3 = check3 + ch

print(covertM)
