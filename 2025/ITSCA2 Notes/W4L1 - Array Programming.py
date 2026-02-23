# Array Orientated Programming with NumPy
import numpy as np

# Vectors and matrix
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3],[4, 5, 6]]) # matrix = rows and columns
vector1 = np.array([1, 2, 3, 4, 5]) # vector = 1 row or 1 column
vector2 = np.array([6, 7, 8, 9, 10])
shp1 = np.shape(vector1) # (5,)

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7 ,8, 9]]) # have same amount of columns
shp2 = np.shape(matrix1) # (3, 3)

# Vector Operations
# Addition
vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([6, 7, 8, 9, 10])
result = vector1 + vector2 # [7, 9, 11, 13, 15]
# Multiplication
result = vector1 * vector2 # [6, 14, 24, 36, 50]
# Matrix Operations
# Additions
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
matrix2 = np.array([[1, 2, 23],
                    [44, 11, 6],
                    [7, 0, 39]])
result = matrix1 + matrix2
"""[[ 2  4 26]
    [48 16 12]
    [14  8 48]]"""

# Multiplication
# Element by element multiplication
result = matrix1 * matrix2
"""[[  1   4  69]
    [176  55  36]
    [ 49   0 351]]"""
# Standard matrix multiplication
result = np.dot(matrix1, matrix2)
"""[[110  24 152]
    [266  63 356]
    [422 102 560]]"""

# Indexing and slicing
vector1 = np.array([1, 2, 3, 4, 5])
r1 = vector1[0] # 1
r2 = vector1[2] # 3
r3 = vector1[1:] # [2 3 4 5]

matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
res1 = matrix1[0,0] # 1
res2 = matrix1[1:] # every row from row 1
"""[4, 5, 6],
   [7, 8, 9]"""
res3 = matrix1[1] # [4 5 6] only row 1
res4 = matrix1[:1] # [1 2 3] every row before row 1
res5 = matrix1[1:3,:] # from row 1 to the row before 3 (row 2) and everything in those rows
"""[4, 5, 6],
   [7, 8, 9]"""
res6 = matrix1[1:3,1:3] # from row 1 to the row before 3 (row 2) and from column 1 to the column before 3 (column 2)
"""[5, 6],
   [8, 9]"""
# Change elements
vector2[0] = 100 # [100 7 8 9 10]
matrix2[:2] = [0, 0, 0]
"""[1, 2, 0],
   [44, 11, 0],
   [7, 0, 0]"""

#Linear Algebra Operations
#matrix1T = np.transpose(matrix1)
"""[[1 4 7]
    [2 5 8]
    [3 6 9]]"""

#matrix1Inv = np.linalg.inv(matrix1)
#print(matrix1Inv)

#matrix1Det = np.linalg.det(matrix1)
#print(matrix1Det)

# Solving linear system

A = np.array([[1, 2], [3, 4]])
b = np.array([1,4])
c = np.linalg.solve(A, b) # [ 2.  -0.5]

# Array attributes

matrix1.dtype # int32

# Function to contstruct arrays
zeroArray = np.zeros((4,4))
"""[[0. 0. 0. 0.]
    [0. 0. 0. 0.]
    [0. 0. 0. 0.]
    [0. 0. 0. 0.]]"""
fillArray = np.full((4,4),3)
"""[[3 3 3 3]
    [3 3 3 3]
    [3 3 3 3]
    [3 3 3 3]]"""
onesArray = np.ones((4,4))
#print(5*onesArray)
"""[[5. 5. 5. 5.]
    [5. 5. 5. 5.]
    [5. 5. 5. 5.]
    [5. 5. 5. 5.]]"""
linespaceArray = np.linspace(0, 1, 5) # [0.  0.25  0.5  0.75  1.]
randomArray = np.random.rand(2, 3)
"""[[0.58550813 0.16511798 0.04140661]
    [0.92699644 0.34006796 0.66342943]]"""

#Reshaping and Stacking Arrays
arr1 = np.array([0, 1, 2, 3, 4, 5])
reshape1 = np.reshape(arr1, (6,1)) # total size of reshape should equal the size of array
"""[[0]
    [1]
    [2]
    [3]
    [4]
    [5]]"""
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
vStackArray = np.vstack((arr1, arr2)) # order matters
"""[[1 2]
    [3 4]
    [5 6]
    [7 8]]"""
hStackArray = np.hstack((arr1, arr2))
"""[[1 2 5 6]
    [3 4 7 8]]"""

# Array Functions

matr = np.array([[1, 2], [3, 4]])
totalSum = np.sum(matr) # 10
rowSum = np.sum(matr, axis = 0) # [4  6]
columnSum = np.sum(matr, axis = 1) # [3  7]
avg = np.mean(matr) # 2.5
maxVal = np.max(matr) # 4
minVal = np.min(matr) # 1

# Problem 1
arr1 = np.array([0, 1, 2, 3, 4, 5, 6])
newInt = 7
appendArr = np.append(arr1, newInt) # [0 1 2 3 4 5 6 7]

# Problem 2
arr1 = np.array([0, 1, 2, 3, 4, 5, 6])
flippedArr = np.flip(arr1) # [6 5 4 3 2 1 0]

# Problem 3
arr1 = np.array([0, 1, 2, 3, 4, 5, 6])
last3Val = arr1[-3:] # [4 5 6]

# Problem 4
arr1 = np.array([0, 1, 2, 3, 4, 5, 6])
target_item = 3
if target_item in arr1:
    index = np.where(arr1 == target_item)
    print("Item found in the list")
    newArr = np.delete(arr1, index) # [0 1 2 4 5 6]
else:
    print("Item not found in the list")

# Problem 5
x = np.array([1,1,1,2,2,2,5,25,1,1])
unique, counts = np.unique(x, return_counts=True)
print(np.asarray((unique, counts)).T)
"""[[ 1  5]
    [ 2  3]
    [ 5  1]
    [25  1]]"""