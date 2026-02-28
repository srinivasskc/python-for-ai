# Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

# Child class - specific animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says bow..bow!"

class Cat(Animal):
    def bite(self):
        return f"{self.name} is biting!"

# Create a dog - using positional argument
my_dog = Dog("sky")
# Or with named argument
my_dog2 = Dog(name="Max")

# Dog can do animal things (inherited)
print(my_dog.eat())    # Buddy is eating
print(my_dog.sleep())  # Buddy is sleeping

# Dog can also do dog things
print(my_dog.bark())   # Buddy says bow..bow!

#############
my_cat = Cat("Lille")
my_cat.eat()
my_cat.sleep()
my_cat.bite()
