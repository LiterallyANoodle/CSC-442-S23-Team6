def TranSeven(Arr, x):
    index = 0
    word = []
    for i in range(int(x)): #This will iterate for length / 7 times to handle each character
        ASCII = 0 #This will become the ASCII value of the character after processing
        addTo = 64 #This starts at 64 since that is the value of the 1st bit in a 7-bit sequence
        for j in range(0,7):
            curr = Arr[index]
            if(curr == "1"):
                ASCII += addTo
            addTo = addTo/2
            index += 1
        character = chr(int(ASCII))
        word.append(character)
    answer = ""
    for f in word:
        answer += f
    print(answer)

def TranEight(Arr, x):
    index = 0
    word = []
    for i in range(int(x)):
        ASCII = 0
        addTo = 128
        for j in range(0,8):
            curr = Arr[index]
            if(curr == "1"):
                ASCII += addTo
            addTo = addTo/2
            index += 1
        character = chr(int(ASCII))
        word.append(character)
    answer = ""
    for f in word:
        answer += f
    print(answer)

testStr = "01100111011011110010000001110100011010010110110101100101"
charArr = [char for char in testStr]

l = len(charArr)
a = l/7
b = l/8

if(l%7 == 0 and l%8 == 0):
    TranSeven(charArr, a)
    TranEight(charArr, b)
elif(l%7 == 0):
    TranSeven(charArr, a)
elif(l%8 == 0):
    TranEight(charArr, b)
else:
    print("Invalid length of binary.")
