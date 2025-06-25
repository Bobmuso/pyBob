#File Manipulation
"""
'r' - read file / error if not exist
'a' - append file / create if not exist
'w' - write file / create if not exist
'x' - create file / erroe if exist
"""
import csv

data = [{'name' : 'John', 'age' : 30, 'city' : 'Pretoria'},
        {'name' : 'Elis', 'age' : 25, 'city' : 'CapeTown'},
        {'name' : 'Mark', 'age' : 42, 'city' : 'Durban'}]

#if file is in same location as program otherwise you need filepath
filePath = 'exampleText1.txt'

#Write to file
with open(filePath, 'w') as file:
    file.write('Name\tAge\tCity\n') # without \n it will not move to next line
    for eachRow in data:
        file.write(f'{eachRow['name']}\t{eachRow['age']}\t{eachRow['city']}\n')

#Read file
with open(filePath, 'r') as file:
    content = file.read()

#Unpack file line into variables
with open(filePath, 'r') as file:
    line = file.readline()
    name, age, city = line.split('\t')

# print(name.strip()) removes any whitespaces

#Unpack line by line
nameList = []
ageList = []
cityList = []

with open(filePath, 'r') as file:
    lines = file.readlines()
    for eachLine in lines:
        name, age, city = eachLine.split('\t')
        nameList.append(name)
        ageList.append(age)
        cityList.append(city)

for i in range(len(nameList)):
    print(nameList[i])
    print(ageList[i])
    print(cityList[i])

"""
OR
with open(filePath, 'r') as file:
    lines = file.readlines()
    for eachLine in lines:
        name, age, city = eachLine.split('\t')
        print(f'{name:<11}{age:<11}{city:<11}')
"""

#Update variable in file
ageIndex = 1
with open(filePath, 'r') as file:
    lines = file.readlines() #copies lines in variable

i = 0
for eachLine in lines:
    if 'Elis' in eachLine: #looking through lines to find 'Elis'
        lineContent = eachLine.split('\t') # ['Elis', 25, 'CapeTown']
        lineContent[ageIndex] = 27 # ['Elis', 27, 'CapeTown']
        lines[i] = '\t'.join(lineContent) #Change line number i to lineContent
    i += 1 # move to next i

with open(filePath, 'w') as file:
    file.writelines(lines) # write new lines into file

#JSON file
import json
data = {'records':[{'name' : 'John', 'age' : 30, 'city' : 'Pretoria'}, #records acts as table name
                   {'name' : 'Elis', 'age' : 25, 'city' : 'CapeTown'},
                   {'name' : 'Mark', 'age' : 42, 'city' : 'Durban'}]}
filePath = 'exampleData.json'

#Write to json
with open(filePath, 'w') as file:
    json.dump(data, file)

#Read from json
with open(filePath, 'r') as file:
    data1 = json.load(file)

print(data1) # print same data as data variable
print(data1['records'][0]) # {'name' : 'John', 'age' : 30, 'city' : 'Pretoria'}

# Numpy method
import numpy as np

data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

filePath = 'data.txt'

np.savetxt(filePath, data, fmt = '%d', delimiter = ',') #store txt using json approach
dataRead = np.loadtxt(filePath, dtype = int, demlimiter = ',')
"""
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
"""
#Working on CSV files with Error handling
import csv
filePath = 'test.csv'

dataToWrite = [['John', 30, 'Pretoria'],
        ['Elis', 25, 'CapeTown'],
        ['Mark', 42, 'Durban']]

try:
    with open(filePath, 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(dataToWrite)
    print('Data written successfully to', filePath)
except Exception as e:
    print('An error occurred while to csv file:', e)

#Reading csv file with Error handling
try:
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        dataRead = list(reader)
    print('Data successfully read from', filePath)
    for eachRow in dataRead:
        print(eachRow)

except FileNotFoundError:
    print('File not found')

except Exception as e:
    print('An error occurred while reading csv file:', e)