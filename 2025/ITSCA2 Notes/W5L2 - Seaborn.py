#Data Visualisation
"""
1. histogram of passengers ages
2. bar plot of survival rate by gender
3. scatter plot between passengers ages, fares paid, coloured by survival stats
4. box plot of distribution of fares to different passenger classes
"""
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic.head()) # quick summary of dataset

fig, axes = plt.subplots(2, 2, figsize = (15, 15)) # 2x2 = 4 plots, figsize is size of plots

sns.histplot(data = titanic, x = 'age', ax = axes[0, 0])
axes[0, 0].set_title('Histogram')

sns.barplot(data = titanic, x = 'sex', y = 'survived', ax = axes[0, 1])
axes[0, 1].set_title('Bar Plot')

sns.scatterplot(data = titanic, x = 'age', y = 'fare', hue = 'survived', ax = axes[1, 0])
axes[1, 0].set_title('Scatter Plot')

sns.boxplot(data = titanic, x = 'class', y = 'fare', ax = axes[1, 1])
axes[1, 1].set_title('Box Plot')

fig.savefig('TitanicDataPlot.png', dpi = 123)