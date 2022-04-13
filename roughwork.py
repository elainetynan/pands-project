# analysis.py
#
# Analysis of the Fisher’s Iris data set.
#
# Author: Elaine Tynan
# Start-date: 22/03/2022

import pandas as pd
import plotAnalysis as pa


# The next comment (line 12) is to stop errors using df.loc
# pylint: disable=no-member

plotPath = './plots/'
dataPath = './data/'

irisFile = dataPath+"iris.data"

# Read in Irish data. There is no header in this file.
df = pd.read_csv(irisFile, header=None)
# Add column names
df.columns =['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

# Get all rows for Iris-setosa
setosa = df.loc[df['class'] == 'Iris-setosa']
# Get all rows for Iris-versicolor
versicolor = df.loc[df['class'] == 'Iris-versicolor']
# Get all rows for Iris-virginica
virginica = df.loc[df['class'] == 'Iris-virginica']

#print(setosa)
#print(versicolor)
#print(virginica)

# Summary statistics for setosa
stats = setosa.describe()
# Summary statistics for versicolor
stats = versicolor.describe()
# Summary statistics for virginica
stats = virginica.describe()
'''
print(stats)
print()
print(stats)
print()
print(stats)
print()
'''

# Do Clustering
pa.doClustering(df, 'sepal length', 'sepal width', "Sepal Length v Sepal Width: Clustered",
                "ClusterSepalLengthSepalWidth.png", 0, 1)
                
pa.doClustering(df, 'sepal length', 'petal length', "Sepal Length v Petal Lengt: Clustered",
                "ClusterSepalLengthPetalLength.png", 0, 2)
                
pa.doClustering(df, 'sepal length', 'petal width', "Sepal Length v Petal Width: Clustered",
                "ClusterSepalLengthPetalWidth.png", 0, 3)

pa.doClustering(df, 'sepal width', 'petal width', "Sepal Width v Petal Width: Clustered",
                "ClusterSepal WidthPetalWidth.png", 1, 3)

pa.doClustering(df, 'petal length', 'sepal width', "Petal Length v Sepal Width: Clustered",
                "ClusterPetalLengthSepalWidth.png", 2, 1)

pa.doClustering(df, 'petal length', 'petal width', "Petal Length v Petal Width: Clustered",
                "ClusterPetalLengthPetalWidth.png", 2, 3)


# Plot all 4 measurements against each other
pa.plotIrisGrps(df, 'sepal length', 'sepal width', "Sepal length by width","Iris Data Set",
                'Sepal Length', 'Sepal Width', "SepalLengthSepalWidth.png")
pa.plotIrisGrps(df, 'petal length', 'petal width', "Petal length by width","Iris Data Set",
                'Petal Length', 'Petal Width', "PetalLengthPetalWidth.png")
pa.plotIrisGrps(df, 'petal length', 'sepal length', "Petal length by Sepal length","Iris Data Set",
                'Petal Length', 'Sepal Length', "PetalLengthSepalLength.png")
pa.plotIrisGrps(df, 'petal width', 'sepal width', "Petal width by Sepal width","Iris Data Set",
                'Petal Width', 'Sepal Width', "PetalWidthSepalWidth.png")
pa.plotIrisGrps(df, 'petal width', 'sepal length', "Petal width by Sepal length","Iris Data Set",
                'Petal Width', 'Sepal Length', "PetalWidthSepalLength.png")
pa.plotIrisGrps(df, 'petal length', 'sepal width', "Petal length by Sepal width","Iris Data Set",
                'Petal Length', 'Sepal Width', "PetalLengthSepalWidth.png")


# Next try histograms of the summary statistics grouped by class
