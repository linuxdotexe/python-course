"""
Day - 8

Object-Oriented Programming
"""

#* Defining a class
class Car:
    pass
    # def __init__(self, car_name):
    #     self.car = car_name

    # def details(self):
    #     print("Car Details:", self.car)


#* Creating an instance of a class (object)
# my_car = Car("nano")  # 'my_car' is an instance of the Car class
# my_car.details();
# exit()









#* Adding attributes in the initializer
class Car:
    def __init__(self, color, model):
        self.color = color     # instance attribute 'color'
        self.model = model     # instance attribute 'model'


#* Accessing instance attributes
# my_car = Car("red", "Sedan")
# print(my_car.color)  # Output: red
# print(my_car.model)  # Output: Sedan

# exit()









#* Defining a method
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self):  # defining a method 'drive'
        print(f"The {self.color} {self.model} is driving!")


#* Calling a method
# my_car = Car("blue", "SUV")
# my_car.drive()  # Output: The blue SUV is driving!

# exit()











#* Changing an attribute value inside a method
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        print("The car is", self.color)

    def repaint(self, new_color):
        self.color = new_color  # changing the 'color' attribute
        print(f"The car is now {self.color}!")


# my_car = Car("white", "SUV")
# my_car.repaint("black")  # Output: The car is now black!

# exit()










#* Class variable shared among all instances
class Car:
    wheels = 4  # class variable
    __wh = 3
    def __init__(self, color):
        self.color = color  # instance variable


car1 = Car("red")
car2 = Car("blue")

# print(car1.wheels)  # Output: 4
# print(car2.wheels)  # Output: 4
# print(car1.color)   # Output: red
# print(car2.color)   # Output: blue

# exit()











class Person:
    def __init__(self, name):
        self.name = name  # 'self.name' is an instance attribute


# p = Person("Alice")
# print(p.name)  # Output: Alice

# exit()








class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # '__balance' is private

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)  # Deposited: 500
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # This would throw an error due to private attribute

exit()










