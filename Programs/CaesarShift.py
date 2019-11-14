def getMessage():
    while True:
        message = input("What is your message? \n").lower()
        use_it = True
        for i in message: # this for loop looks at every character in the message.
            num = ord(i) # convert to decimal
            if (num >= 97 and num <= 122) or i == " ":
                continue
            else:
                use_it = False
        if use_it:
            return message
        print("The message must be only lower case letters and spaces.")

def getShift():
    return int(input("How many shifts should the message perform? \n"))

def performShift():
    finalEncrypt = ""
    message = getMessage()
    shift = getShift()
    for i in message:
        num = ord(i)
        if i == " ":
            finalEncrypt += " "
        else:
            num += shift
            if num > 122:
                num -= 97
                num %= 26
                num += 97
            finalEncrypt += chr(num)
    print("Encrypted Message:")
    print(finalEncrypt)
    
performShift()