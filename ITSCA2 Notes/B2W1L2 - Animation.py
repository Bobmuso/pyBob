#Animation Process
"""
Import Libraries
Create Fig and Axes
Define Data and Initial Plot
Define Update Function
Create Animation
Display Animation
Optional Settings
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
xData = np.linspace(0, 2 * np.pi, 100)
yData = np.sin(xData)
line, = ax.plot(xData, yData)

#Shift to the right
def update(frame):
    line.set_ydata(np.sin(xData - frame/10))
    return line

#Shift to the left
"""
def update(frame): 
    line.set_ydata(np.sin(xData + frame/10))
    return line
"""

anim = animation.FuncAnimation(fig, func = update, frames = range(100), interval = 50)
plt.show()

"Close image to save resources"

#Yield Function
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def swap(A, i, j):
    if i != j:
        A[i], A[j] = A[j], A[i]

def insertionSort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            swap(A, j, j-1)
            j -= 1
            yield A

def selectionSort(A):
    if len(A) == 1:
        return
    for i in range(len(A)):
        minInd = i
        for j in range(i, len(A)):
            if A[j] < A[minInd]:
                minInd = j
            yield A
        swap(A, i, minInd)
        yield A

N = int(input('Enter numberof random integers to sort: '))
selAlgText = "Enter sorting algorithm \n(i)insertion\n(s)selection\nInput:"
selAlg = input(selAlgText)

A = [x + 1 for x in range(N)]
random.seed(time.time())
random.shuffle(A)

if selAlg == 'i':
    title = 'Insertion Sort'
    genFunc = insertionSort(A)
else:
    title = 'Selection Sort'
    genFunc = selectionSort(A)

fig, ax = plt.subplots()
ax.set_title(title)

barRects = ax.bar(range(len(A)), A, align = 'edge')
ax.set_ylim(0, N)
ax.set_xlim(0, N)

iteration = [0]
def updateFig(A, rects, interation):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    interation[0] + 1

anim = animation.FuncAnimation(fig, func = updateFig, fargs = (barRects, iteration),
                               frames = genFunc, interval = 1, repeat = False, cache_frame_data = False)

plt.show()