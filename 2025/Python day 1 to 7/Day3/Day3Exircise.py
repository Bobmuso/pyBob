age = int(22)
height =float(175)
comp= complex( 1+2j)
slope = float(2.5)
M = float(3.0)

def areaTriangle(base, height):
    base = float(base)
    height = float(height)
    return (base * height) / 2

def perimeterTriangle(side1, side2, side3):
    sidea = float(side1)
    sideb = float(side2)
    sidec = float(side3)
    return "The perimeter of the triangle is " + str(sidea + sideb + sidec)

def rectangleArea(length, width):
    length = float(length)
    width = float(width)
    return length * width

def circle_area():
    radius = input('Enter the radius of the circle: ')
    radius = float(radius)
    pi = 3.14
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference
    
def slope():
    yVal = float(input("Enter the value of Y: "))
    M = float(input("Enter the value of M: "))
    C = float(input("Enter the value of C: "))
    X = float(input("Enter the value of X: "))
    print(M)
    return M

def Slope():
    y2= float(input("Enter the value of y2: "))
    y1= float(input("Enter the value of y1: "))
    x2= float(input("Enter the value of x2: "))
    x1= float(input("Enter the value of x1: "))
    slope = (y2 - y1) / (x2 - x1)
    print(slope)
    return slope

def slopeCompare(val1, val2):
    if val1 > val2:
        print("The first slope is greater than the second slope.")
    elif val1 < val2:
        print("The first slope is less than the second slope.")
    else:
        print("The two slopes are equal.")

m1 = slope()
print("and")
m2 = Slope()
print('also')
slopeCompare(m2, m1)

def calcY()
    Xval = float(input("Enter the value of X: "))   
    Yval = Xval**2 + 6(Xval) + 9
    print("The value of Y is: ", Yval)  
    


