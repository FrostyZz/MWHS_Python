import random

#===============================================================================
# # Math Operators
# print(5 + 5)
# print(5 - 5)
# print(5 * 5)
# print(5 / 5)
# print(5 % 5) # % = Modulus (Remainder)
# # Math Operators
#===============================================================================

#print(random.randrange(0,10)) # randRange(start,end) -- doesnt include end.

#===============================================================================
# num = random.randrange(0,4)
# if num == 0:
#     print("Option 1")
# elif num == 1:
#     print("Option 2")
# elif num == 2:
#     print("Option 3")
# else:
#     print("Option 4")
#===============================================================================

#===============================================================================
 choice = input("Rock, Paper, or Scissors? \n")
 choice = choice.lower()
 num = random.randrange(0,3)
 if num == 0:
     print("Rock")
     if choice == "rock":
         print("Tie.")
     elif choice == "paper":
         print("You Lose.")
     else:
         print("You Win.")
 elif num == 1:
     print("Paper")
     if choice == "rock":
         print("You Lose.")
     elif choice == "paper":
         print("Tie")
     else:
         print("You Win.")
 else:
     print("Scissors")
     if choice == "rock":
         print("You Win.")
     elif choice == "paper":
         print("You Lose.")
     else:
         print("Tie")
#===============================================================================\

