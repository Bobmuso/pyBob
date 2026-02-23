import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.compose import ColumnTransformer #convert catergorical data to numberials
from sklearn.preprocessing import OneHotEncoder #show existence and non-existents of value in columns by creating new columns   (male = 0, 1 and female = 1, 0)
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential #build neutral network
from tensorflow.keras.layers import Dense #create input, hidden and output layer
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv('Churn_Modelling.csv')
pd.set_option('display.max_columns', None) #optional to display all columns
print(df.head())
df.isna().sum() #show number of emptpy values
df = df.dropna() #remove empty values
x = df.iloc[:, 3:-1].values #all rows, column except non relevent/target
y = df.iloc[:, -1].values #alls rows in last column
print(x)
print(y)

#merge info back into one column
le = LabelEncoder
x[:, 2] = le.fit_transform(x[:, 2])
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [1])], remainder = 'passthrough')
x = np.array(ct.fit_transform(x))

xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 0)

scaler = StandardScaler()
xTrain = scaler.fit_transform(xTrain)
xTest = scaler.fit_transform(xTest)

ann = Sequential()
ann.add(Dense(units = 6, activation = 'relu', input_dim = xTrain.shape[1]))
ann.add(Dense(units = 6, activation = 'relu'))
ann.add(Dense(units = 1,  activation = 'sigmoid'))
ann.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

ann.fit(xTrain, yTrain, batch_size = 32, epochs = 100)

yPred = (ann.predict(xTest) > 0.5).astype('int32')
print('\Classification report:')
print(classification_report(yTest, yPred))

confMatrix = confusion_matrix(yTest, yPred)
sns.heatmap(confMatrix, annot = True, fmt = 'd', cmap = 'Blues')
plt.title('Confusion Matrix')
plt.xlabel('predicted')
plt.ylabel('actual')
plt.show()