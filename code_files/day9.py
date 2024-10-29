"""
Day - 9

OOP - 2
"""
# * ENCAPSULATION
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

# acc = Account("Alice", 1000)
# acc.deposit(500)
# print(acc.get_balance())

# exit()

# * INHERITANCE
class Vehicle:
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):  # Single inheritance
    def move(self):
        return "Car is driving"

# car = Car()
# print(car.move())

# exit()

# * POLYMORPHISM
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

# animal_sound(Dog())
# animal_sound(Cat())

# exit()

# * METHOD OVERRIDING
class Bird:
    def fly(self):
        return "Bird flies"

class Penguin(Bird):
    def fly(self):
        return "Penguin can't fly"

# penguin = Penguin()
# print(penguin.fly()) # output = ?

# exit()

# * SPECIAL METHODS
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1)
print(v2)
print(v1 + v2)
exit()
