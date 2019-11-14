import random
import time 

x = "Loading."
for i in range(0, 5):
    print(x)
    x += "."
    time.sleep(2) #waits for two seconds
print("Loaded")

an_Example_List = ["a" , "b" , "C", 'G'] #defines a list
print(random.choice(an_Example_List)) #prints a random item from the list
print(random.randrange(0, 5)) #prints a rand number 0-4

#variables 
x = "a value"

#Conditionals
if True:
    print("yep")

if True and False: # will output False
    print("if either side of an AND is false the output is false")
elif True:
    print("see above")
else:
    print("Why bother true is always true")
if True or False: # will output True
    print("if either side of an OR is true the output is true")

#loops
v = "This is a sample string"
for letter in v:
    print(letter)
    
for letter in range(0,len(v)): #does the same thing as the loop above
    print(v[letter])

for item in an_Example_List: # printed each item from the list on new lines
    print(item)

while True:
    print("Looped")
    break #ends a loop 

num = 5
while num > 0:
    print(num)
    num -= 1

def function_Name(number):
    return number * number
# def variable (any or no parameters):  
        #parameters are any data a function needs to run
    #return value        is how you pass data out of a function 
print(function_Name(5))

a_num = 65
print(chr(a_num))
b_value = ord("B")
print(b_value)

