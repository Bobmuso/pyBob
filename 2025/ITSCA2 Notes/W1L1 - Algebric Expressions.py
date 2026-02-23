#Algebric Expressions
def isRoot(x):
    fx = (x**2) - (0.25*x) + 5
    if fx == 0:
        return True
    else:
        return False

x = 2.3
ans = isRoot(x)
print(ans)

def testAlgExp1(a, b, c):
    leftSide = round((a+b)/c)
    rightSide = round((a/c) + (b/c))
    if leftSide == rightSide:
        return True
    else:
        return False

def testAlgExp2(a, b, c, d):
    leftSide = round((a/c) + (b/d))
    rightSide = round(((a*d) + (b*c))/(c*d))
    if leftSide == rightSide:
        return True
    else:
        return False

def testAlgExp3(a, b, c, d):
    leftSide = round((a/c) * (b/d))
    rightSide = round((a*b)/(c*d))
    if leftSide == rightSide:
        return True
    else:
        return False

def testAlgExp4(a, b, c, d):
    leftSide = round((a/b) / (c/d))
    middle = round((a/b) * (d/c))
    rightSide = round((a*d) / (b*c))
    if (leftSide == rightSide) and (middle == leftSide):
        return True
    else:
        return False


a = 1
b = 2
c = 3
d = 4

fx1 = testAlgExp1(a, b, c)
print(fx1)
fx2 = testAlgExp2(a, b, c, d)
print(fx2)
fx3 = testAlgExp3(a, b, c, d)
print(fx3)
fx4 = testAlgExp4(a, b, c, d)
print(fx4)

e = 32 > 8
print(e)

