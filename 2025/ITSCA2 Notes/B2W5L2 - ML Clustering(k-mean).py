import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()
df = pd.DataFrame(data = iris.data, columns = iris.feature_names)
print(df.head())

"""
colNames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'species']
df = pd.read_csv('Iris1.csv', names = colNames, header = 0)
print(df.head())
"""

labelMapping = {'Iris-setosa' : 0, 'Iris-versicolor' : 1, 'Iris-virginica' : 2}
df['species'] = df['species'].map(labelMapping)

x = df.iloc[:, :-1].values #copy all rows, copy all columns except last

scaler = StandardScaler()
scaler.fit(x)
x = scaler.transform(x)

kmeans = KMeans(n_clusters = 3, random_state = 11)
kmeans.fit(x)
df['predSpecies'] = kmeans.labels_ #give us clusters, unspecific which cluster for which species
df['predSpecies'] = np.choose(kmeans.labels_, [2, 0, 1]).astype(np.int64)
print('\n Data with Cluster/Species Labels: ')
print(kmeans.labels_)
print(df.head(20))

accuracy = accuracy_score(df['species'], df['predSpecies'])
classReport = classification_report(df['species'], df['predSpecies'])
confMatrix = confusion_matrix(df['species'], df['predSpecies'])
print(f'\nAccuracy: {accuracy}') #Accuracy as pencentage
print(f'\nClassification Report: \n{classReport}')
print(f'\nConfusion Matrix: \n{confMatrix}') #Gives grip to show much where misplaced

plt.figure(figsize =(10, 7))
colorMap = np.array(['red', 'blue', 'purple'])

plt.subplots(2, 2, 1) # 4 graphs on screen (2x2) and plot in pos 1
plt.scatter(df['sepal-length'], df['sepal-width'], color = colorMap[df['species']], marker = 'o')
plt.xlabel('sepal-length')
plt.ylabel('sepal-width')
plt.title('Sepal Actual')

plt.subplots(2, 2, 2) # 4 graphs on screen (2x2) and plot in pos 2
plt.scatter(df['sepal-length'], df['sepal-width'], color = colorMap[df['predSpecies']], marker = 'o')
plt.xlabel('sepal-length')
plt.ylabel('sepal-width')
plt.title('Sepal Predicted')

plt.subplots(2, 2, 3) # 4 graphs on screen (2x2) and plot in pos 3
plt.scatter(df['petal-length'], df['petal-width'], color = colorMap[df['species']], marker = 'o')
plt.xlabel('petal-length')
plt.ylabel('petal-width')
plt.title('Petal Actual')

plt.subplots(2, 2, 4) # 4 graphs on screen (2x2) and plot in pos 4
plt.scatter(df['petal-length'], df['petal-width'], color = colorMap[df['predSpecies']], marker = 'o')
plt.xlabel('petal-length')
plt.ylabel('petal-width')
plt.title('Petal Predicted')

#Elbow method
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist, pdist

iris = load_iris
x = iris.data

k = range(1, 11)

kM = [KMeans(n_clusters = eachK).fit(x) for eachK in k]
centriods = [eachK.cluster_centers_ for eachK in kM]
dK = [cdist(x) for eachC in centriods]
cIndex = [np.argmin(eachD, axis = 1) for eachD in dK]
dist = [np.argmin(eachD, axis = 1) for eachD in dK]
avgWithinSS = [sum(eachD)/x.shape[0] for eachD in dist]
wcss = [sum(eachD ** 2)/x.shape[0] for eachD in dist]

plt.figure(figsize = (10, 4))
plt.subplots()
plt.ylabel('Error Margin')
plt.xlabel('Number of Clusters')
plt.plot(k, avgWithinSS, 'b*-')