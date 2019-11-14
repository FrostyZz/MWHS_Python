import random
from builtins import str
from Tools.Scripts.svneol import possible_text_file
class Animal():
    species = ""
    cuteness = 0
    coolness = 0
    value = 0
    intelligence = 0
    
    def __init__(self, spec):
        self.species = spec
        
    def toString(self):
        print(self.species)
        print("Coolness: " + str(self.coolness))
        print("Cuteness: " + str(self.cuteness))
        print("Intelligence: " + str(self.intelligence))
        print("Value: " + str(self.value))
        print("----------")
        
    def sale(self, amount):
        if amount >= self.value and random.randrange(1,11) > 6:
            print("Adopted.")
            return True
        return False

class Dog(Animal):
    
    def __init__(self, spec):
        super().__init__(spec)
        self.intelligence = random.randrange(5,11)
        self.cuteness = random.randrange(3,7)
        self.coolness = random.randrange(1,5)
        self.value = self.coolness + self.cuteness + self.intelligence
        self.toString()

class Cat(Animal):
    def __init__(self, spec): # ayden sucks and he copies my code
        super().__init__(spec)
        self.intelligence = random.randrange(7,11)
        self.cuteness = random.randrange(4,9)
        self.coolness = random.randrange(1,3)
        self.value = self.coolness + self.cuteness + self.intelligence
        self.toString()
        
class Parrot(Animal):
    def __init__(self, spec):
        super().__init__(spec)
        self.intelligence = random.randrange(8,11)
        self.cuteness = random.randrange(1,3)
        self.coolness = random.randrange(4,11)
        self.value = self.coolness + self.cuteness + self.intelligence
        self.toString()
        
class Fish(Animal):
    def __init__(self, spec):
        super().__init__(spec)
        self.intelligence = 1
        self.cuteness = random.randrange(1,3)
        self.coolness = random.randrange(1,11)
        self.value = self.coolness + self.cuteness + self.intelligence
        self.toString()
        
doggo = Dog("Dog")
coggo = Fish("Fish")
poggo = Parrot("Parrot")
foggo = Cat("Cat")

animals = [doggo,coggo,poggo,foggo]
        
topValue = 0
best = Animal("Placeholder")
for pet in animals:
    if pet.value > topValue:
        topValue = pet.value
        best = pet
print("The most valuable animal is " + best.species + ".")

topCute = 0
best = Animal("Placeholder")
for pet in animals:
    if pet.cuteness > topCute:
        topCute = pet.cuteness
        best = pet
print("The cutest animal is " + best.species + ".")

topSmart = 0
best = Animal("Placeholder")
for pet in animals:
    if pet.intelligence > topSmart:
        topSmart = pet.intelligence
        best = pet
print("The smartest animal is " + best.species + ".")

topcool = 0
best = Animal("Placeholder")
for pet in animals:
    if pet.coolness > topcool:
        topcool = pet.coolness
        best = pet
print("The coolest animal is " + best.species + ".")
print("----------")
class Person():
    money = 0
    dislikes = ""
    name = ""
    possible_dislikes = ["Dog", "Cat", "Fish", "Parrot"]
    
    def __init__(self):
        self.name = self.name_me()
        self.dislikes = random.choice(self.possible_dislikes)
        self.money = random.randrange(7,16)
        
    def name_me(self):
        return input("What is this person's name?\n")    
    def choose_Pet(self, animals):
        while True:
            topValue = 0
            best = Animal("Placeholder")
            for pet in animals:
                if pet.value > topValue:
                    topValue = pet.value
                    best = pet
                if self.money >= topValue and pet.species != self.dislikes:
                    return best.species
                animals.remove(best)
                if len(animals) == 0:
                    return "No pet will work."
p = Person()
print(p.name + " has chosen " + p.choose_Pet(animals) + ".")