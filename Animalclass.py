class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed, weight):
        super().__init__(name, age)
        self.breed = breed
        self.weight = weight

class Cat(Animal):
    def __init__(self, name, age, color, gender):
        super().__init__(name, age)
        self.color = color
        self.gender = gender

# Example usage
my_dog = Dog("Luna", 5, "Red Healer", 60)
print(f"My dog's name is {my_dog.name}, he is {my_dog.age} years old, and weighs {my_dog.weight} pounds.")
my_cat = Cat("Chapo", 3, "gray", "female")
print(f"My cat's name is {my_cat.name}, she is {my_cat.age} years old, and has {my_cat.color} fur.")
