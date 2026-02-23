#Instance attribute
"""
Specific to instance in class
Defined within __init__
Each instance can have different values of the attributes
"""
#Class attribute
"""
Attribute shared amongs all instances in class
Defined outside of any method and accessed bt class itself (ClassName.attribute) or instances (self.attribute)
Change to attribute affects all instances using instance
"""

class Particle:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity

    def kineticEnergy(self):
        return 0.5 * self.mass * self.velocity ** 2

particle1 = Particle(0.01, 10)
particle2 = Particle(0.02, 15)

class Gas:
    gasConstant = 8.314

    @classmethod
    def idealGasLaw(cls, pressure, volume, temperature):
        return (pressure * volume)/(cls.gasConstant * temperature)

pressure1 = 101335
volume1 = 0.22414
temp1 = 273.15

moles = Gas.idealGasLaw(pressure1, volume1, temp1)

#Instance Method
"""
Method that operates on an instance of a class
Takes self as 1st parameter, which refers to method called
Method can access and modify instance attributes
"""
#Class Method
"""
Method that operates on the class itself rather than on a instance of the class
Takes cls as 1st parameter, which refers to class itself
Method can access and modify class attributes
"""

#Instance
class Converter1:
    def __init__(self, rate):
        self.rate = rate

    def metersToMiles1(self, meters):
        return meters * self.rate

conv1 = Converter1(0.000621371)
distMiles1 = conv1.metersToMiles1(1000)

#Class
class Converter2:
    rate = 0.000621371

    @classmethod
    def metersToMiles2(cls, meters):
        return meters * cls.rate

conv2 = Converter2()
distMiles2 = conv2.metersToMiles2(1000)

#Subclass & superclass
import math

class Shape:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f'This is a {self.name}.'

class Rectangle:
    def __init__(self, width, height):
        self.name = 'rectangle'
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.name = 'circle'
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

rect1 = Rectangle(4, 5)
circ1 = Circle(3)
info1 = rect1.info() # This is a rectangle

#Encapsulation (Private attribute)
class Vector:
    def __init__(self, components):
        self.__components = components

    def dotProducts(self, other):
        if len(self.__components) != len(other.__components):
            raise ValueError('Vector must have same dimensions')
        dotProductResult = 0
        for i in range(len(self.__components)):
            dotProductResult += self.__components[i] * other.__components[i]
        return dotProductResult

v1 = Vector([1, 2, 3, 4])
v2 = Vector([5, 6, 7 ,8])
print('Dot product of v1 and v2:', v1.dotProducts(v2))
#print('Components of v1:', v1.components) give error

#Class as decorator
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Logging the function call')
        return self.func(*args, **kwargs)

@Logger
def add(x, y):
    return x + y

print('Result:', add(3, 4))

import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        startTime = time.time()
        result = self.func(*args, **kwargs)
        endTime = time.time()
        print('Execution time:', endTime - startTime, 'secs')
        return result

def calcFactorial(n):
    if n == 0:
        return 1
    else:
        n * calcFactorial(n - 1)

print('Factorial:', calcFactorial(5))
