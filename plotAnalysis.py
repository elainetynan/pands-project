# analysis.py
#
# Analysis of the Fisher’s Iris data set.
#
# Author: Elaine Tynan
# Start-date: 22/03/2022

#import numpy as np
#import pandas as pd
#import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

# The next comment (line 12) is to stop errors using df.loc
# pylint: disable=no-member

plotPath = './plots/'
dataPath = './data/'
statsPath= './summaryStats/'

def plotIrisGrps(df, xcol, ycol, title, fname, xlabel='', ylabel=''):
    thePath = plotPath+'scatter/'
    legendTitle = xcol + " by " + ycol
    # Plot 3 types of Iris - sepal dimensions
    # plt.subplots() is a function that returns a tuple containing a figure and axes object(s).
    # figsize sets the dimensions of the plot. A common size is 8x6 and looks good when I run it. 
    fig, ax = plt.subplots(figsize=(8,6))

    for n, grp in df.groupby('class'):
        ax.scatter(x=xcol, y =ycol, data=grp, label=n)
    ax.legend(title=legendTitle)
    plt.title(title)
    ax.set_xlabel(xcol, fontweight ='bold')
    ax.set_ylabel(ycol, fontweight ='bold')
    plt.savefig(thePath+fname)
    #plt.show()
    
    # Close all plots
    plt.close('all')

def doClustering(dataset, xcol, ycol, xcolIdx, ycolIdx):
    thePath = plotPath+'cluster/'
    title = xcol + " v " + ycol + ": Clustered"
    fname = "Cluster_" + xcol + "_" + ycol + ".png"

    subset = dataset.iloc[:,[xcolIdx,ycolIdx]]
    #print(subset)
    #print("~~~~~~~~~~~~~~~~~~~~~")
    # Do Clustering
    kmeans = KMeans(3) # an unsupervised machine learning technique used to identify clusters of data objects in a dataset. 
    kmeans.fit(subset) # Computes k-means clustering
    identified_clusters = kmeans.fit_predict(subset)
    #
    data_with_clusters = subset.copy()
    data_with_clusters['Clusters'] = identified_clusters 
    plt.scatter(data_with_clusters[xcol],data_with_clusters[ycol],c=data_with_clusters['Clusters'],cmap='rainbow')
    plt.title(title)
    #plt.show()
    plt.savefig(thePath+fname)
    
    # Close all plots
    plt.close('all')
    
# Bar Charts of summary statistics

def barChartSummaryStat(df, colName):
    thePath = plotPath+'barSummary/'+colName+"/"
    
    
    minDf = df.groupby('class', as_index=False)[colName].min()
    ax = minDf.plot.bar(x='class', y=colName, rot=0)
    plt.title("Min of "+colName)
    plt.savefig(thePath+colName+"min.png")

    meanDf = df.groupby('class', as_index=False)[colName].mean()
    ax = meanDf.plot.bar(x='class', y=colName, rot=0)
    plt.title("Mean of "+colName)
    plt.savefig(thePath+colName+"mean.png")
    
    maxDf = df.groupby('class', as_index=False)[colName].max()
    ax = maxDf.plot.bar(x='class', y=colName, rot=0)
    plt.title("Max of "+colName)
    plt.savefig(thePath+colName+"max.png")
    
    stdDf = df.groupby('class', as_index=False)[colName].std()
    ax = stdDf.plot.bar(x='class', y=colName, rot=0)
    plt.title("Standard Deviation of "+colName)
    plt.savefig(thePath+colName+"std.png")
    
    # Close all plots
    plt.close('all')

def generateSummaryStats(df):
    # Get all rows for each class of Iris, then generate summary statistics & save them to csv
    setosa = df.loc[df['class'] == 'Iris-setosa']
    setosaStats = setosa.describe()
    setosaStats.to_csv(statsPath+'setosaStats.csv')

    versicolor = df.loc[df['class'] == 'Iris-versicolor']
    versicolorStats = versicolor.describe()
    versicolorStats.to_csv(statsPath+'versicolorStats.csv')

    virginica = df.loc[df['class'] == 'Iris-virginica']
    virginicaStats = virginica.describe()
    virginicaStats.to_csv(statsPath+'virginicaStats.csv')

def boxPlots(df):
    thePath = plotPath+'boxPlots/'

    # Do boxplots using seaborn for the experience of using the different package

    plt.figure() # for a new plot to clear old information
    ax = sns.boxplot(x="class", y="petal length", data=df)
    plt.title("Petal Length")
    plt.savefig(thePath+"boxPlotPetalLength.png")
    
    plt.figure()
    ax = sns.boxplot(x="class", y="petal width", data=df)
    plt.title("Petal Width")
    plt.savefig(thePath+"boxPlotPetalWidth.png")
    
    plt.figure()
    ax = sns.boxplot(x="class", y="sepal length", data=df)
    plt.title("Sepal Length")
    plt.savefig(thePath+"boxPlotSepalLength.png")
    
    plt.figure()
    ax = sns.boxplot(x="class", y="sepal width", data=df)
    plt.title("Sepal Width")
    plt.savefig(thePath+"boxPlotSepalWidth.png")
    
    # Close all plots
    plt.close('all')