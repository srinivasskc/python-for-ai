class Dog:
    def __init__(self,name,breed="None"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Bark!!!")

class Cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color

sky = Dog(name="Sky",breed="Labrador")
sky.name
sky.breed


# Calling methods.
sky.bark()


# dog1 = Dog(name="Sky")
# This will throw error due to 1 argument missing.
# Instead we can make the parameter optional by breed="None"
dog1 = Dog(name="Skey")
dog1.name


cat = Cat("Julie","Brown")
cat.name
cat.color


