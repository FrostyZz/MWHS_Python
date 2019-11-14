import random
from time import sleep
#===============================================================================
# class First_Class():
#     # Attributes
#         # Parts of an object
#         # Each instance of the object can set values for its attributes.
#     name = ""
#     
#     # Constructor
#         # runs when a new instance of the class is created.
#         # always will be named the same in Python.
#         # can take parameters but must take self
#     def __init__(self, a_Name):
#         self.name = a_Name # when using attributes self.attribute is the format.
#             
#     # Methods
#         # These are special functions that belong to an object.
#         # They are the stuff an object can do.
#         # They must take self as a parameter
#     def print_Name(self):
#         print("My name is " + self.name)
# 
# example_One = First_Class("JOHN CENA") # Make an instance of a class
# example_Two = First_Class("Jeff")
# 
# example_One.print_Name() # call a method tied to a class
# print(example_Two.name) # call to an attribute
# 
# example_Two.name = "New Name as an Example" # Reassign attribute
# print(example_Two.name)
# import random
# class Second_Class():
#     num = 0
#     
#     def __init__(self):
#         self.num = random.randrange(0,11) * random.randrange(0,6)
#     def print_Num(self):
#         print(self.num)
#         
# 
# Second_Example = Second_Class()
# Second_Example_Two = Second_Class()
# 
# Second_Example.print_Num()
# Second_Example_Two.print_Num()
#===============================================================================

class Fish():
    life = True
    hunger = 0
    cleanliness = 0
    daysAlive = 0
    name = ""
    
    def __init__(self, fish_name):
        self.name = fish_name
        self.hunger = random.randrange(50,101)
        self.cleanliness = random.randrange(1,11)

    def toString(self):
        value =  self.name + "\n\t" + "Cleanliness: " + str(self.cleanliness)
        value += "\n\t" + "Hunger: " + str(self.hunger)
        value += "\n\t" + "Days Alive: " + str(self.daysAlive)
        print(value)
        return value
    def feed_Fish(self):
        self.hunger += random.randrange(1,11)
        if self.hunger > 100:
            self.hunger = 100
        print(self.name + " was fed and now has " + str(self.hunger) + " hunger.")
    def clean_Tank(self):
        self.cleanliness += random.randrange(1,11)
        if self.cleanliness > 10:
            self.cleanliness = 10
        print(self.name + "'s tank was cleaned and is now " + str(self.cleanliness) + " clean.")
    def set_Alive(self):
        self.hunger -= random.randrange(1,11)
        self.cleanliness -= 1
        if self.life:
            if self.hunger <= 0:
                self.life = False
                print(self.name + " has starved. :(")
            elif self.cleanliness <= 0:
                self.life = False
                print(self.name + " has died due to a dirty tank. :(")
    def do_Stuff(self):
        #sleep(3) # gives time to read text
        if self.life:
            num = random.randrange(1,101)
            if num < 50:
                print(self.name + " did nothing.")
            elif num < 90:
                self.feed_Fish()
            else:
                self.clean_Tank()
            self.set_Alive()
            self.daysAlive +=1
            self.toString()
            sleep(3)
        else:
            print(self.name + " is floating upside down at the top of the tank. :(")
                    
myFish = Fish("Bubbles")
while myFish.life:
    myFish.do_Stuff()