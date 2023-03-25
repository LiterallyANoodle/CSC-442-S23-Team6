import sys 
import argparse

# formatting and usage # 
# -h or --help for help 
# -d or --decrypt for decrypting a message 
# -e or --encrypt for encrypting a message

# Linux Terminal 
# ex: python3 Vigenere.py -e YOUR_KEY 

# PowerShell(recommand) or Git Bash <-- some issue/bug when using git 
# python Vigenere.py -e YOUR_KEY

def Vigenere(text, key, mode):    
    result = ""
    keyIndex = 0
    for char in text: # iterate through all the characters
        if char.isalpha():
            keyChar = key[keyIndex % len(key)] # here's where we start looking through the key
            shift = ord(keyChar.upper()) - 65 #performing the shift via the key
            # variation based on case (upper or lower)
            if (mode == "encrypt"): 
                if char.isupper():
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                else:
                    result += chr((ord(char) + shift - 97) % 26 + 97)
                keyIndex += 1
            elif (mode == "decrypt"):
                if char.isupper():
                    result += chr((ord(char) - shift - 65) % 26 + 65)
                else:
                    result += chr((ord(char) - shift - 97) % 26 + 97)
                keyIndex += 1
        else:
            result += char
    return result

if (__name__ == "__main__"):
    # Parse command-line arguments
    parser = argparse.ArgumentParser(prog='Vigenere Cipher')
    parser.add_argument('-e', action='store_true', help='encrypt text')
    parser.add_argument('--encrypt', action='store_true', help='encrypt text')
    parser.add_argument('-d', action='store_true', help='decrypt text')
    parser.add_argument('--decrypt', action='store_true', help='decrypt text')
    parser.add_argument('key', help='key to use for encryption/decryption')
    args = parser.parse_args()


# Read input text from a file
    if not sys.stdin.isatty():
        # Input is being redirected from a file
        text = sys.stdin.read().strip()
        result = Vigenere(text, args.key, "decrypt")  
        print(result)
    elif (args.e or args.encrypt): 
        mode = ("encrypt")
        #input_prompt = ("Text to encrypt: ")
        text = input().strip()  
        result = Vigenere(text, args.key, mode)  
        print(result)
    else:
        mode = ("decrypt")
        #input_prompt = ("Text to decrypt: ")
        text = input().strip()  
        result = Vigenere(text, args.key, mode)  
        print(result)
        
