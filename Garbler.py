import random
def Garbler(base, x):
    hidden = []
    index = 0
    while(x > 0):
        randChar = random.randint(33, 126)
        randPlace = random.randint(1, 800)
        if(randPlace == 69):
            if(index < len(base)):
                hidden.append(base[index])
                index += 1
        else:
            if(randChar == 48):
                randChar -= 1
            elif(randChar == 49):
                randChar += 1
            hidden.append(chr(randChar))
            x -= 1
    final_text = ""
    for item in hidden:
        final_text += item
    f = open("HiddenText.txt", "w")
    f.write(final_text)
    f.close
            

text = input("Please enter your binary message: ")
base_binary = []
for char in text:
    if(char == '0' or char == '1'):
        base_binary.append(char)

garble_count = len(base_binary) * 1000
Garbler(base_binary, garble_count)
