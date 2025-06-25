#Linear Search (unsorted array)
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

array = [17, 31, 52, 19, 41, 34, 76, 11, 28, 92]
target = 34
index = linearSearch(array, target)

"""if index != -1:
    print(f'{target} is found at index {index}')
else:
    print(f'{target} not found in array')"""

#BinarySearch (sorted array)
def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif target > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

array = [4, 8, 19, 25, 34, 39, 45, 48, 66, 75, 89, 95]
target = 75
index = binarySearch(array, target)

"""if index != -1:
    print(f'{target} is found at index {index}')
else:
    print(f'{target} not found in array')"""

#Selection Sort
def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

array = [23, 78, 45, 8, 32, 56]
sortedArray = selectionSort(array)
print(sortedArray)

def revSelectionSort(arr):
    for i in range(len(arr)):
        maxIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[maxIndex]:
                maxIndex = j
        arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
    return arr

array = [23, 78, 45, 8, 32, 56]
sortedArray = revSelectionSort(array)
print(sortedArray)

#Insertion Sort
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        nextElement = arr[i]
        while j >= 0 and arr[j] > nextElement:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = nextElement
    return arr

array = [10, 18, 25, 30, 23, 17, 45, 35]
sortedArray = insertionSort(array)
print(sortedArray)

def revInsertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        nextElement = arr[i]
        while j >= 0 and arr[j] < nextElement:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = nextElement
    return arr
array = [10, 18, 25, 30, 23, 17, 45, 35]
sortedArray = revInsertionSort(array)
print(sortedArray)

#Merge Sort
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(left, right):
    merged = []
    leftIndex = rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            merged.append(left[leftIndex])
            leftIndex += 1
        else:
            merged.append(right[rightIndex])
            rightIndex += 1
    while leftIndex < len(left):
        merged.append(left[leftIndex])
        leftIndex += 1
    while rightIndex < len(right):
        merged.append(right[rightIndex])
        rightIndex += 1
    return merged

array = [17, 31, 52, 19, 41, 34, 76, 11]
sortedArray = mergeSort(array)
print(sortedArray)

def revMergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = revMergeSort(left)
    right = revMergeSort(right)
    return revMerge(left, right)

def revMerge(left, right):
    merged = []
    leftIndex = rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] > right[rightIndex]:
            merged.append(left[leftIndex])
            leftIndex += 1
        else:
            merged.append(right[rightIndex])
            rightIndex += 1
    while leftIndex < len(left):
        merged.append(left[leftIndex])
        leftIndex += 1
    while rightIndex < len(right):
        merged.append(right[rightIndex])
        rightIndex += 1
    return merged

array = [17, 31, 52, 19, 41, 34, 76, 11]
sortedArray = revMergeSort(array)
print(sortedArray)