# Any time you repeat something more than once it is too much.

#===============================================================================
# def addThem(a,b):
#     return a + b
# 
# # def variableName(params):
# #    (code)
# #    return data
# # Parameters are any data the function needs to run.
# # return - passes data out of the function (you dont need return or params)
# 
# def sayHi():
#     print("Hi.")
# 
# sayHi()
# 
# def printDec(character):
#     print("Decimal: " + str(ord(character)))
#                         # str(param) turns the parameter into a string
#                         # ord(param) returns the ASCII value of the param.
#===============================================================================


def convertCharacter(character):
    num = ord(character)
    print("--------------------")
    print(character)
    print("Decimal: " + str(num))
    print("Binary: " + str(bin(num)))
    print("Hex: " + str(hex(num)))
    print("Octl: " + str(oct(num)))
# convertCharacter('f')

def convertString(theString):
    for i in range(0,len(theString)):
        convertCharacter(theString[i])

#convertString(input("Convert Input: \n"))

def totalString(a_String):
    total = 0
    for i in range(0,len(a_String)):
        total += ord(a_String[i])
    print(total)
    
totalString(input("Type a string: \n"))
