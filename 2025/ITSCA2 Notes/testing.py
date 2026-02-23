def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

a = [56, 22, 74, 64, 25, 3, 58]
b = bubbleSort(a)
print(b)

def merge(s1, s2, s):
    i = j = 0
    while i + j < len(s):
        if j == len(s2) or (i < len(s1) and s1[i] < s1[j]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[i + j] = s1[j]
            j += 1

def mergeSort(s):
    n = len(s)
    if n < 2:
        return
    mid = n / 2
    s1 = s[0:mid]
    s2 = s[mid:n]
    mergeSort(s1)
    mergeSort(s2)
    merge(s1, s2, s)