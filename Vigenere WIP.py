import sys 
import argparse

# formatting and usage # 
# -h or --help for usage 
# -d or --decrypt for decrypting a message 
# -e or --encrypt for encrypting a message
# -k or --key for entering your secret key that you want to use 

# Linux Terminal 
# ex: python3 Vigenere.py -e -k SECRETKEY 

# PowerShell or Git Bash 
# python Vigenere.py -e -k SECRETKEY

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
    parser = argparse.ArgumentParser(description='Vigenere cipher')
    parser.add_argument('-e', '--encrypt', action='store_true', help='encrypt text')
    parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt text')
    parser.add_argument('-k', '--key', required=True, help='key to use for encryption/decryption')
    args = parser.parse_args()

    # Read input text from a file
    if not sys.stdin.isatty():
        # Input is being redirected from a file
        text = sys.stdin.read().strip()
    else:
        # Get input text from the user
        text = input("Enter text to encrypt/decrypt: ").strip()
    

    # Apply the Vigenere cipher to the input text
    if (args.encrypt):
        result = Vigenere(text, args.key, "encrypt")
    else: 
        result = Vigenere(text, args.key, "decrypt")
    print(result)

