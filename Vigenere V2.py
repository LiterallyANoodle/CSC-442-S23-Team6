import sys 
import argparse

# formatting and usage # 
# -h or --help for help 
# -d or --decrypt for decrypting a message 
# -e or --encrypt for encrypting a message

# Linux Terminal 
# ex: python3 Vigenere.py -e YOUR_KEY 

# PowerShell or Git Bash 
# python Vigenere.py -e YOUR_KEY

def Vigenere(text, key, mode): 
    result = ""
    key_index = 0
    # go through each character input 
    for character in text: 
        # check if character is a letter
        if character.isalpha(): 
            # apply the cipher to letter and checking input case sensitivity 
            if (mode == "encrypt"): 
                if (character.isupper()):
                    character = chr((ord(character.upper()) + ord(key[key_index].upper()) - 2 * ord('A')) % 26 + ord('A'))
                else: 
                    character = chr((ord(character.lower()) + ord(key[key_index].lower()) - 2 * ord('a')) % 26 + ord('a'))
            elif (mode == "decrypt"):
                if (character.isupper()):
                    character = chr((ord(character.upper()) - ord(key[key_index].upper()) + 26) % 26 + ord('A'))
                else:
                    character = chr((ord(character.upper()) - ord(key[key_index].upper()) + 26) % 26 + ord('a'))
            # move to the next letter in the key 
            key_index = (key_index + 1) % len(key)
        # add to result string 
        result += character
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
    elif (args.e or args.encrypt): 
        mode = ("encrypt")
        input_prompt = ("Text to encrypt: ")
        text = input(input_prompt).strip()  
        result = Vigenere(text, args.key, mode)  
        print(result)
    else:
        mode = ("decrypt")
        input_prompt = ("Text to decrypt: ")
        text = input(input_prompt).strip()  
        result = Vigenere(text, args.key, mode)  
        print(result)
        


