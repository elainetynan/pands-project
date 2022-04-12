# analysis.py
#
# Analysis of the Fisher’s Iris data set.
#
# Author: Elaine Tynan
# Start-date: 22/03/2022

import pandas as pd
import matplotlib.pyplot as plt

# The next comment (line 12) is to stop errors using df.loc
# pylint: disable=no-member

irisFile = "iris.data"

# Read in Irish data. There is no header in this file.
df = pd.read_csv(irisFile, header=None)

# Add column names
df.columns =['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

# Get all rows for Iris-setosa
setosa = df.loc[df['class'] == 'Iris-setosa']
#print(setosa)

# Get all rows for Iris-versicolor
versicolor = df.loc[df['class'] == 'Iris-versicolor']
#print(versicolor)

# Get all rows for Iris-virginica
virginica = df.loc[df['class'] == 'Iris-virginica']
#print(virginica)

# Summary statistics for setosa
stats = setosa.describe()
print(stats)
print()

# Summary statistics for versicolor
stats = versicolor.describe()
print(stats)
print()

# Summary statistics for virginica
stats = virginica.describe()
print(stats)
print()

# Plot 3 types of Iris - sepal dimensions
# plt.subplots() is a function that returns a tuple containing a figure and axes object(s).
# figsize sets the dimensions of the plot. A common size is 8x6 and looks good when I run it. 
fig, ax = plt.subplots(figsize=(8,6))

for n, grp in df.groupby('class'):
    ax.scatter(x='sepal length', y ='sepal width', data=grp, label=n)
ax.legend(title="Sepal length by width")
plt.title("Iris Data Set")
ax.set_xlabel('Sepal Length', fontweight ='bold')
ax.set_ylabel('Sepal Width', fontweight ='bold')
plt.savefig("SepalLengthSepalWidth.png")
#plt.show()

# Plot 3 types of Iris - petal dimensions
fig, ax = plt.subplots(figsize=(8,6))

for n, grp in df.groupby('class'):
    ax.scatter(x='petal length', y ='petal width', data=grp, label=n)
ax.legend(title="Petal length by width")
plt.title("Iris Data Set")
ax.set_xlabel('Petal Length', fontweight ='bold')
ax.set_ylabel('Petal Width', fontweight ='bold')
plt.savefig("PetalLengthPetalWidth.png")
#plt.show()

# Plot 3 types of Iris - petal length by sepal length
fig, ax = plt.subplots(figsize=(8,6))

for n, grp in df.groupby('class'):
    ax.scatter(x='petal length', y ='sepal length', data=grp, label=n)
ax.legend(title="Petal length by Sepal length")
plt.title("Iris Data Set")
ax.set_xlabel('Petal Length', fontweight ='bold')
ax.set_ylabel('Sepal Length', fontweight ='bold')
plt.savefig("PetalLengthSepalLength.png")
#plt.show()

# Plot 3 types of Iris - petal width by sepal width
fig, ax = plt.subplots(figsize=(8,6))

for n, grp in df.groupby('class'):
    ax.scatter(x='petal width', y ='sepal width', data=grp, label=n)
ax.legend(title="Petal width by Sepal width")
plt.title("Iris Data Set")
ax.set_xlabel('Petal Width', fontweight ='bold')
ax.set_ylabel('Sepal Width', fontweight ='bold')
plt.savefig("PetalWidthSepalWidth.png")
#plt.show()

# Plot 3 types of Iris - petal width by sepal width
fig, ax = plt.subplots(figsize=(8,6))

for n, grp in df.groupby('class'):
    ax.scatter(x='petal width', y ='sepal length', data=grp, label=n)
ax.legend(title="Petal width by Sepal length")
plt.title("Iris Data Set")
ax.set_xlabel('Petal Width', fontweight ='bold')
ax.set_ylabel('Sepal Length', fontweight ='bold')
plt.savefig("PetalWidthSepalLength.png")
#plt.show()

# Plot 3 types of Iris - petal width by sepal width
fig, ax = plt.subplots(figsize=(8,6))

for n, grp in df.groupby('class'):
    ax.scatter(x='petal length', y ='sepal width', data=grp, label=n)
ax.legend(title="Petal length by Sepal width")
plt.title("Iris Data Set")
ax.set_xlabel('Petal Length', fontweight ='bold')
ax.set_ylabel('Sepal Width', fontweight ='bold')
plt.savefig("PetalLengthSepalWidth.png")
#plt.show()

# Next try histograms of the summary staatistics grouped by class