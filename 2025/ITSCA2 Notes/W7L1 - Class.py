#Define class and instance
class Car:
    def __init__(self, brand, model, year): #properites of class
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car('Toyota', 'Supra', '1998')
car2 = Car('Honda', 'Civic', '1995')

print(car1.brand) #Toyota
print(car2.year) #1995

#__init__ method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person('Elis', 30)
person2 = Person('Bob', 25)

#Attributes and methods
"""
#Attribute - characteristics of object
#Method - behaviour of object
"""

class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(self.pi *(self.radius ** 2))

    def circumference(self):
        return round(2 * (self.pi * self.radius))

circ1 = Circle(5)
area1 = Circle.area()
circum1 = Circle.circumference()

#Special Methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'

v1 = Vector(3, 4)
v2 = Vector(1, 3)

res1 = v1 + v2
print(res1) # Vector(4, 7)

#Property function
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2* (self.width + self.height)

    @property
    def diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

rect1 = Rectangle(2, 3)
area1 = rect1.area  #6
peri1 = rect1.perimeter #10
diag1 = rect1.diagonal #3.605...

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def toFahrenheit(self):
        return (self.temperature * 9/5) + 32

    @property
    def temperature(self):
        print('Getting value...')
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print('Setting value...')
        if value < -273.15:
            raise ValueError('Temperature below -273.15 is not possible')
        self._temperature = value

c = Celsius()
c.temperature = 35
print(c.toFahrenheit())

class Account:
    def __init__(self, accountNum, balance = 0):
        self.accountNum = accountNum
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited: R{amount}. New balance: R{self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdraw: R{amount}. New balance: R{self.balance}')
        else:
            print('Insufficient funds')

    def getBalance(self):
        print(f'Current balance for account number, {self.accountNum}: R{self.balance}')