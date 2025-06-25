import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('weather1.csv')

#View regression
df.plot(x = 'MinTemp', y = 'MaxTemp', style = 'o')
plt.title('MinTemp vs MaxTemp')
plt.ylabel('MaxTemp')
plt.xlabel('MinTemp')
plt.show()

#Check for bell curve
plt.figure(figsize = (10, 6))
plt.hist(df['MaxTemp'], bins = 20, color = 'blue', edgecolor = 'black')
plt.title('Distribution of MaxTemp')
plt.ylabel('MaxTemp')
plt.xlabel('MinTemp')
plt.show()

#Check missing values
df = df[['MinTemp', 'MaxTemp']]
print('Missing values')
print(df.isnull().sum())

#Drop na values
df = df.dropna()

x = df[['MinTemp']].values
y = df[['MaxTemp']].values

#Create model
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 0.2, random_state = 42)


lr = LinearRegression()
#Train model
lr.fit(xTrain, yTrain)

#Make prediction
yPred = lr.predict(xTest)
print('Prediction of 1st 5 rows')
print(yPred)
print('Actual 1st 5 rows')
print(yTest)

#get model parameters
print('\nIntercept on y-axis')
print(lr.intercept_)
print('\ncoefficient on x')
print(lr.coef_)

mse = mean_squared_error(yTest, yPred)
r2 = r2_score(yTest, yPred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

#DataSet pred vs actual
dfActualVSPred = pd.DataFrame({'Actual' : yTest.flatten(), 'Predicted' : yPred.flatten()})
print(dfActualVSPred)

dfActualVSPred = dfActualVSPred.head(25)
dfActualVSPred.plot(kind = 'bar', figsize = (16, 10))
plt.show()

plt.figure(figsize = (10, 6))
plt.scatter(xTest, yTest, color = 'blue', label = 'Actual Max Temp')
plt.plot(xTest, yPred, color = 'red', label = 'Predicted Max Temp')
plt.xlabel('Min Temp')
plt.ylabel('Max Temp')
plt.legend()
plt.show()