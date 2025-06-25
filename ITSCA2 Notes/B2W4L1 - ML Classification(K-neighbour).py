import numpy as np #operations
import matplotlib.pyplot as plt #plotting
import pandas as pd #dataframes
from sklearn.model_selection import train_test_split #split into train and test dataset
from sklearn.neighbors import KNeighborsClassifier #group with closest value
from sklearn.preprocessing import StandardScaler #normalize parameter
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix #format of model

colNames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
df = pd.read_csv("Iris 1.csv", names = colNames, header = 0)
print(df.head())

x = df.iloc[:, :-1] #features, take all rows, not header
y = df.iloc[:,4] #target, take all rows, only need first 4

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 42)
print(xTrain[:5]) #train dataset
print(yTrain[:5])
print(xTest[:5])#test dataset
print(yTest[:5])

#normailze to make calc easier/uniform
scaler = StandardScaler()
scaler.fit(xTrain)
xTrain = scaler.transform(xTrain)
xTest = scaler.transform(xTest)
print(xTrain[:5])
print(xTest[:5])

#Doing calc for model
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(xTrain, yTrain)

#Make perdiction of test model to check accuary of model
yPred = knn.predict(xTest)
print(yPred[:5])
print(yTest[:5])

#Get accuracy of model
accuracy = accuracy_score(yTest, yPred)
print(f"\nAccuracy : {accuracy}") #Can multiple by 100 to get percentage

#Check which is right and wrong from accuracy
confMatrix = confusion_matrix(yTest, yPred)
print(confMatrix)

#Give report of classification
classReport = classification_report(yTest, yPred)
print(classReport)

plt.figure(figsize = (8, 6))
plt.imshow(confMatrix, interpolation = 'nearest', cmap = plt.cm.Blue)
plt.colorbar() #legend
tickMarks = np.arange(3)
species = ['Iris-setosa', 'Iris-versiolor', 'Iris-virginica']
plt.xticks(tickMarks, species, rotation = 45)
plt.yticks(tickMarks, species)
plt.tight_layout()
plt.show()

