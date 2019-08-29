#!/usr/bin/env python3
#Create a Class Animal

class Animal:
    #instance attribute: 
    #   species = None
    #   name

    def __init__(self, name):
        self.name =  name
        self.species = None
    
    def make_noise(self):
        print()

# animal = Animal("Test")
# animal.name == "Test"

class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "tiger"
    
    def make_noise(self):
        print("Roar")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "dog"
    
    def make_noise(self):
        print("Bark")

class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.species = "cow"

    def make_noise(self):
        print("Moo")

class Zoo:
    def __init__(self):
        self.animals = []

    def add(self, animal):
        self.animals.append(animal)
    
    def show_animals(self):
       
        for animal in self.animals:
            print(animal.name)
            animal.make_noise()
        
if __name__ == "__main__":
    mike = Tiger("Mike")
    molly = Dog("Molly")
    bessie = Cow("Bessie")

    zoo = Zoo()
    zoo.add(mike)
    zoo.add(molly)
    zoo.add(bessie)

    zoo.show_animals()
