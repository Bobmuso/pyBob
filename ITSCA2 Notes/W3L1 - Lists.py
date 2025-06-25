# Creating lists
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(list1) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

list2 = ['a', 20.5, 7, False]
print(list2) # ['a', 20.5, 7, False]

list3 = [4, ['a', 20.5, 7, False]]
print(list3) # [4, ['a', 20.5, 7, False]]

list4 = list(range(5))
print(list4) # [0, 1, 2, 3, 4]

# Accessing Elements
l1 = list1[0]
print(l1) # a

l2 = list1[3]
print(l2) # d

l3 = list1[-1]
print(l3) # g

l4 = list1[-3]
print(l4) # e

l5 = list3[1]
print(l5) # ['a', 20.5, 7, False]

l6 = list3[1][2]
print(l6) # 7

# Slicing List
# listName[start:stop:step]
out1 = list1[0:-2]
print(out1) # ['a', 'b', 'c', 'd', 'e']

out2 = list1[0:5]
print(out2) #['a', 'b', 'c', 'd', 'e']

out3 = list1[0:4]
print(out3) # ['a', 'b', 'c', 'd']

out4 = list1[5:2]
print(out4) # [] can't have 1st position be greater than 2nd position

out5 = list1[::2]
print(out5) # ['a', 'c', 'e', 'g']

out6 = list1[::-1]
print(out6) # ['g', 'f', 'e', 'd', 'c', 'b', 'a']

out7 = list1[::-2]
print(out7) # ['g', 'e', 'c', 'a']

# List Comprehension
out8 = [x**2 for x in range(1,11)]
print(out8) # [1, 4, 9, 16, 25, 36, 48, 64, 81, 100]

# Altering List
list5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list5[2:3] = []
print(list5) # ['a', 'b', 'd', 'e', 'f', 'g']

list6 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list6[3:] = []
print(list6) # ['a', 'b', 'c']

list7 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list7[1:1] = ['u', 'z']
print(list7) # ['a', 'u', 'z', 'b', 'c', 'd', 'e', 'f', 'g']

# Zip function
list8 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
acsiiValue = [ord(char) for char in list8]
print(list8)
print(acsiiValue)
pairs = list(zip(list8, acsiiValue))
print(pairs) # [('a', 97), ('b', 98), ('c', 99), ('d', 100), ('e', 101), ('f', 102), ('g', 103)]
# print(ord('A')) # 65 (acsii value)

# List Method
"""
l.append(x) - appends item x to the end of the list l
l.count(x) - returns the number of times item x appears in list l
l.extend(m) - appends all the iterable m's item to the end of list l;
l += m - does the same thing as extend
l.index(x, start, end) - returns the index position of the leftover item x in list l 
(or in the start:end slice of l) otherwise will raise ValueError exception
l.insert(i, x) - insert item x in list l at position int i
l.pop() - returns and removes the last item in list l
l.pop(i) - returns and removes the item at position int i in list i
l.remove(x) - removes the 1st occurrence of item x in list l 
or raise ValueError exception if x not found
l.reverse() - reverse list l in-place
l.sort() - sorts list l in-place
"""

# Problem 1
list9 = [1, 2, 3, 4, 5, 6, 7, 8]
sum(list9)

# Problem 2
def countString(l):
    numString = 0
    for item in l:
        if len(item) >= 2 and item[0] == item[-1]:
            numString += 1
    return numString

l7 = ['efef', 'rgcr', '2462', 'wvfb', 'dvfghd', '2']
res1 = countString(l7)
print("Result:",res1)

# Tuples
tup1 = (1, 2, 3)
print(tup1[0]) # 1
print(tup1[2]) # 3
# tup1[0] = 5
# print(tup1) # Tuples don't support item assignment

# Tuple packing
tup2 = ("Bob", 32, "Rapper")
print(tup2) # ("Bob", 32, "Rapper")
# Tuple unpackage
tup3 = ("Marry", 43, "Nurse")
(name, age, job) = tup3
print(name,"who is age",age,"has a job as a:",job) # "Marry who is age 43 has a job as a: Nurse"

a = 100
b = 200
(a, b) = (b, a)
print("a =",a,"\nb =",b)

# Problem 3
coordinates = (13.4, 35.6, 85.2)
coordinatesPacked = 13.4, 35.6, 85.2
x, y, z = coordinates
sqrCoordinates = tuple(i**2 for i in coordinates)
print("Coordinates:", coordinates)
print("Packed coordinates:", coordinatesPacked)
print("Unpacked coordinates (x, y, z):", x, y, z)
print("Squared coordinates:", sqrCoordinates)

# Problem 4
l8 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l8.sort(key = lambda l: l[1])
print(l8) 