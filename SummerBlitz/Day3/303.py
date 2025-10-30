# -*- coding: utf-8 -*-
#💻 Exercises - Day 3 
age = 22
height = 177.5
comple_x = 1 +1j

#calculate area of traingle
def tri():
    b, h = int(input("base :")),int(input("height :"))
    print("area is :",str(b * h *(1/2)))
    
#tri()

#perimeter of trangle 
def triPer():
    a, b, c = int(input("side 1 :")),int(input("side 3 :")), int(input("side 2 :"))
    print("Perimeter is :",str(a+b+c))
    
#triPer()

def areaAndPerRec():
    l, h = int(input("length :")),int(input("width :"))
    print("area is :",str(l * h))
    print("perimeter is :",str(2*(l + h)))

#areaAndPerRec()

def circle():
    r = int(input("radius :"))
    pi = 3.14
    area = pi * r * r
    c = 2 * pi * r 
    print('area :',area)
    print('circumference :', c)
    
#circle()

def slope8():
    m = 10-2/ 6-2
    print('slope is :', m)
    print('is slope from 8 > 9 :', 2 > m)
#slope8()

def findingZeroX():
    x = 0
    y = 1
    while y != 0:
        y = 8*x + 9
        x -= 0.1
    print("x at zero is ", x)
    
"""findingZeroX() need fixing; Calculate the value of y (y = x2 + 6x + 9). Try to use different x values and figure out at what x value y is
going to be 0."""

def falsey():
    print("is python > dragon :", len("python") > len("dragon"))
    
#falsey()

def checkString():
    print("do they both have the word on? :", "on" in "python" and "on" in "dragon" )
    print("do they both not have the word on? :", "on" not in "python" and "on" not in "dragon" )
#checkString()

def checkParagraph():
    print("""
          Does this sentence have the word Jargon?
          
          I hope this course is not full of jargon.
          """,
          "jargon" in "I hope this course is not full of jargon.")
    
#checkParagraph()

#print(str(float(len("python"))))

def evenFinder(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
        
#evenFinder(2)

def misc():
    print("is the floor division of 7 by 3 is equal to the int converted value of 2.7", 7 // 3 == int(2.7))
    print("is type of ‘10’ is equal to type of 10", "10" == 10)
    print("is int(‘9.8’) is equal to 10", int("9.8") == 10)
    
#misc()

def ratePhour():
    h, r = int(input("hour ")), int(input("rate "))
    e = r * h
    print(e)
    
#ratePhour()

def secondsFromYears():
    y = int(input("years :"))
    s = y * 365.25 *24 *60 *60
    print(s)
    
#secondsFromYears()

def table():
    print("""
          1 1 1 1 1
          2 1 2 4 8
          3 1 3 9 27
          4 1 4 16 64
          5 1 5 25 125""")

#table()
"""
 CONGRATULATIONS ! 🎉 
"""
