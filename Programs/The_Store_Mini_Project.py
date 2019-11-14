
"""

Your Name Goes Here --> Chase Hall

"""


import random, time

class Animal():
    
    def __init__(self, spec):
        self.species = spec
        self.cuteness = 0
        self.intelligence = 0
        self.coolness = 0
        self.value = 0
    
    def toString(self):
        string = self.species + "\n\t" + "Cuteness:" + str(self.cuteness) + "\n\t"
        string += "Coolness:" + str(self.coolness) + "\n\t" 
        string += "Intelligence:" + str(self.intelligence) + "\n\t"
        string += "Value: $" + str(self.value)
        return string
    
    def calValue(self):
        self.value = self.intelligence + self.coolness + self.cuteness
        return self.value #########################################
    
class Dog(Animal):
    
    def __init__(self):
        super().__init__("Dog")
        self.cuteness = random.randrange(2, 6)
        self.intelligence = random.randrange(3 , 11)
        self.coolness = random.randrange( 2 , 7)
        self.value = self.calValue()

class Rat(Animal):
    
    def __init__(self):
        super().__init__("Rat")
        self.cuteness = random.randrange(1, 3)
        self.intelligence = random.randrange(2 , 10)
        self.coolness = random.randrange( 1 , 4)
        self.value = self.calValue()

class Cat(Animal):
    
    def __init__(self):
        super().__init__("Cat")
        self.cuteness = random.randrange(1, 11)
        self.intelligence = random.randrange(4 , 11)
        self.coolness = random.randrange( 1 , 4)
        self.value = self.calValue()

class Snake(Animal):
    
    def __init__(self):
        super().__init__("Snake")
        self.cuteness = random.randrange(1, 3)
        self.intelligence = random.randrange(1 , 4)
        self.coolness = random.randrange( 1 , 11)
        self.value = self.calValue()
        
class Macaw(Animal):
    
    def __init__(self):
        super().__init__("Macaw")
        self.cuteness = random.randrange(1, 4)
        self.intelligence = random.randrange(5 , 11)
        self.coolness = random.randrange( 3 , 11)
        self.value = self.calValue()
        
class Fish(Animal):
    
    def __init__(self):
        super().__init__("Fish")
        self.cuteness = random.randrange(1, 3)
        self.intelligence = random.randrange(1 , 3)
        self.coolness = random.randrange( 1 , 11)
        self.value = self.calValue()

class Unicorn(Animal):
    
    def __init__(self):
        super().__init__("Sprinkles the Magic Unicorn")
        self.cuteness = random.randrange(9, 11)
        self.intelligence = random.randrange(1 , 3)
        self.coolness = 11
        self.value = self.calValue()

animals = [Unicorn(), Dog(), Cat(), Rat(), Snake(), Fish() , Macaw()]

#print(animals[0].toString())

class Person():
    
    def __init__(self):
        self.name = self.set_Name()
        self.money = random.randrange(5, 26)
        self.dislikes = []
        self.set_Dislikes()
    
    def set_Name(self):
        names = ["Bob", "Tim", "Sam", "Sarah", "Stacy", "Amy", "Amber", "David", "Peter", "Amanda", "Tracy", "Taylor"]
        return random.choice(names)
        
    def set_Dislikes(self):
        animals = ["Macaw", "Dog", "Cat", "Fish", "Rat", "Unicorn", "Snake"]
        rand_Animals = []
        for i in range(0, random.randrange(1,4)):
            rand_Animals.append(random.choice(animals))
        self.dislikes = rand_Animals
    
    def find_Best_Value(self, animals):
        val = 0
        best = Animal("PlaceHolder")
        for ani in animals:
            if ani.value > val: 
                val = ani.value
                best = ani
        return best 
    
    def choose_Best(self, animals):
        while len(animals) > 0:
            best = self.find_Best_Value(animals)
            if best.species not in self.dislikes and best.value <= self.money:
                print( self.name + " chooses the " + best.species + ".")
                return best 
            animals.remove(best)
        print(self.name + " did not find any animals.")
        return None

#p = Person()
#p.choose_Best(animals)

class Store():
    def __init__(self):
        self.possible_Animals = ["Macaw", "Dog", "Cat", "Fish", "Rat", "Unicorn", "Snake"]
        self.inventory = {}
        self.animal_List = []
        self.money_Earned = 0
        self.animals_sold = 0
        self.animals_Unsold = 0
        self.build_Inventory()
        self.make_animal_List()
        
    def build_Inventory(self):
        """
        @self: This function randomly adds 10 animals to a dictionary object
        The value should be set to 0 for all animals.
        Set self.inventory = the dictionary 
        """
        Inventory = {}
        for i in range(0,10):
            animals = [Unicorn(), Dog(), Cat(), Rat(), Snake(), Fish() , Macaw()] 
            Inventory[random.choice(animals)] = 0
        self.inventory = Inventory
        #print(Inventory)# dev comment
        
    
    def make_animal_List(self):
        """
        @self: For every animal in the animal inventory dictionary,
        make a list of just the animals without the count.
        Set self.animal_List = the list created. 
        """
        animal_list = []
        for animals in self.inventory:
            animal_list.insert(0, animals)
        self.animal_List = animal_list
        
    def sell_Animal(self, person):
        """
        @self: call the Person class choose_best() on the self.animal_List
        if the function returns an animal, 
            add the animal value to the self.money_Earned
            add one to self.animals_sold
            remove the animal from the self.animal_List and self.inventory
        Call self.increment_Animals()
        """
        animal_chosen = person.choose_Best(self.animal_List)
        if animal_chosen != None:
            self.money_Earned += animal_chosen.value
            self.animals_sold += 1
            self.inventory.pop(animal_chosen)
            self.make_animal_List()
        self.increment_Animals()
        return animal_chosen
    
    def increment_Animals(self):
        """
        @self: for every animal in the self.inventory
            add one to the value of the animal in the dictionary 
            if the number > 10
                remove the animal from the self.inventory and self.animal_List
                add one to self.animals_Unsold
            Append new animals to the animal_List and inventory 
            until the len(animal_List) is 10
        """
        
        for  i in range(0, len(self.inventory)):
            if  i < len(self.inventory):
                self.make_animal_List()
                self.inventory[self.animal_List[i]] += 1
                if self.inventory[self.animal_List[i]] > 10:
                    del self.inventory[self.animal_List[i]]
                    self.animals_Unsold += 1
        self.make_animal_List()
        while len(self.animal_List) < 10:
                animals = [Unicorn(), Dog(), Cat(), Rat(), Snake(), Fish() , Macaw()] 
                rand_ani = random.choice(animals)
                self.inventory[rand_ani] = 0
                self.animal_List.append(rand_ani)
            
    def toString(self):
        """
        @self: Print the store stats including
            Current Animals
            money_Earned
            animals_sold
            animals_Unsold
        """
        animal_String = ""
        for ani in self.animal_List:
            animal_String += ani.species + " "
        print("Current Animals: " + animal_String)
        print("Money Earned: $" + str(self.money_Earned))
        print("Animals Sold: " + str(self.animals_sold))
        print("Animals not Sold: " + str(self.animals_Unsold))
        

def tester():
    the_Store = Store()
    while the_Store.animals_sold < 20 and the_Store.animals_Unsold < 40:
        the_Store.toString()
        the_Store.sell_Animal(Person())
        time.sleep(2) # sleep
    print("Final results:")
    the_Store.toString()   
    
tester()