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

# Read in Irish data. There is no header in this file. Then add column names
df = pd.read_csv(irisFile, header=None)
df.columns =['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

# Do Clustering for all 4 measurements against each other for each class
pa.doClustering(df, 'sepal length', 'sepal width', 0, 1)
pa.doClustering(df, 'sepal length', 'petal length', 0, 2)
pa.doClustering(df, 'sepal length', 'petal width', 0, 3)
pa.doClustering(df, 'sepal width', 'petal width', 1, 3)
pa.doClustering(df, 'petal length', 'sepal width', 2, 1)
pa.doClustering(df, 'petal length', 'petal width', 2, 3)

# Plot all 4 measurements against each other for each class
pa.plotIrisGrps(df, 'sepal length', 'sepal width', "Iris Data Set", "SepalLengthSepalWidth.png")
pa.plotIrisGrps(df, 'petal length', 'petal width', "Iris Data Set", "PetalLengthPetalWidth.png")
pa.plotIrisGrps(df, 'petal length', 'sepal length', "Iris Data Set", "PetalLengthSepalLength.png")
pa.plotIrisGrps(df, 'petal width', 'sepal width', "Iris Data Set", "PetalWidthSepalWidth.png")
pa.plotIrisGrps(df, 'petal width', 'sepal length', "Iris Data Set", "PetalWidthSepalLength.png")
pa.plotIrisGrps(df, 'petal length', 'sepal width', "Iris Data Set", "PetalLengthSepalWidth.png")

# Do bar charts of summary statistics of each measurement
pa.barChartSummaryStat(df, 'sepal length')
pa.barChartSummaryStat(df, 'sepal width')
pa.barChartSummaryStat(df, 'petal length')
pa.barChartSummaryStat(df, 'petal width')

# Generate Summary statistics in csv format
pa.generateSummaryStats(df)

# Do boxplots
pa.boxPlots(df)

# Do Andrews Plot/Curve
pa.doAndrewsCurves(df)

# Do 3D plots
pa.do3dPlots(df, 'sepal length', 'sepal width', 'petal width')
pa.do3dPlots(df, 'petal length', 'petal width', 'sepal width')
pa.do3dPlots(df, 'sepal length', 'sepal width', 'petal length')
pa.do3dPlots(df, 'petal length', 'petal width', 'sepal length')