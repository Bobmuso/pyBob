import datetime
import math #Builtin functions

nums = [1, 2, 3, 5, 7, 9]
maxNum = max(nums) # 9
minNum = min(nums) # 1
print("Maximum:",maxNum) # Maximum: 9
print("Minimum:",minNum) # Minimum: 1

num1 = 23
sqrRoot = math.sqrt(num1) # using builtin function
print("Square root of",num1,"is:",sqrRoot) # Square root of 23 is: 4.8

# Functions in math
num2 = -10
absVal = abs(num2)
print(absVal) # 10

# Passing Argument
def printList(items):
    for each_item in items:
        print(each_item) # apples\n bananas\n pears\n orange
fruits = ["apples", "bananas", "pears", "orange"]
printList(fruits)

# Changing Argument
def subtract1(x1, x2):
    z = x1 - x2 # 10 - 20 = -10
    x2 = 100
    return z
a = 20
result1 = subtract1(10, a)
print(result1) # -10
print(a) # 20

def subtract2(x):
    z = x[0] - x[1]
    x[1] = 100
    return z
b = [10,20]
result2 = subtract2(b)
print(result2)

# Accessing Variables Outside the Local Namespace
a = 10
def multiply(x):
    return a*x

result3 = multiply(7)
print("Multiplication result:", result3) # Multiplication result: 70

# Default Values
def greet(name = "Alex"):
    print("Hello,", name)
greet()
greet("Steve")

# Variable Number of Arguments
def sumVal(*args): # allows you to add many agruments as needed
    sumV = 0
    for eachVal in args:
        sumV += eachVal
    return sumV

result4 = sumVal(6, 7, 8, 9)
print("Sum of values:",result4)

# Return Values
def power(x, exp = 2):
    return x**exp
  # y = x*2  all code in the function after the 1st 'return' will not be executed
  # return y

result5 = power(2)
result6 = power(4, 3)

print(result5) # 4
print(result6) # 8

# Recursive Functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
x1 = 5
result7 = factorial(x1)
print("Factorial of",x1,"is:",result7)

# Anonymous Functions
mul = lambda x,y,:x*y

print(mul(2,2)) # 4

# Decorators
def square(x):
    return x**2

a = square(4)
print(a) # 16

sq = square
b = sq(4)
print(b) # 16

# Wrapper function
# Scenario 1 & 2
def greetDec1(func):
    def wrapper1():
         result8 = func()
         return print(result8,"how are you?")
    return wrapper1

@greetDec1 # allows you to use greetDec1 without mentioning it, as seen below
def greet1():
    return "Hello, Alice"

# g = greetDec(greet)
g = greet1() # Hello, Alice how are you (even though you didn't mention greetDec1)

# Scenario 3
def greetDec2(func):
    def wrapper2(*args, **kwargs):
         result9 = func(*args, **kwargs) + "how are you?"
         caps = result9.upper()
         return caps
    return wrapper2

@greetDec2
def greet2(name):
    return "Hello, "+ name

h = greet2("Sam")
print(h) # HELLO, SAM HOW ARE YOU?

# Problem1

def evenOrOdd(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"

x2 = 5
result10 = evenOrOdd(x2)
print(result10) # Odd

# Problem2

x3 = 32
result11 = math.sqrt(x3)
print(result11)

# Problem3

now = datetime.datetime.now()
print(now)