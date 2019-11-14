# Loop is a repeated behavior until some condition is met.

# while (the loop to use when you don't know how many times something runs)

# while loop w/ counter.
#===============================================================================
# num = 0 # initialized variable
# while num < 5: # termination point
#     print(num) 
#     num+=1 # increment
# 
# password = input("What is the password?\n").lower()
# while password != "correct":
#     password = input("What is the password?\n").lower()
# print("Correct.")
#===============================================================================

#===============================================================================
# word = ""
# wordTwo = "something"
# index = 0
# while len(word) < len(wordTwo):
#     word += wordTwo[index]
#     index += 1
#     print(word)
#===============================================================================
    
#===============================================================================
# var = input("Just type something.\n")
# while var != "something":
#     if var == "A":
#         break # exits the innermost loop.
#     print("Wrong.")
#     var = input("Just type something.\n")
#===============================================================================

# for loops
    # for loops should be used when you know how many times youll run.
        # or when you're going through a collection

for i in range(0,5): # for variable in range(num,end num): -- *doesnt include end*
   print(i) 
   
var = "Stuff"
for i in range(0,len(var)):
    print(var[i])