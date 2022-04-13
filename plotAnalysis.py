# analysis.py
#
# Analysis of the Fisher’s Iris data set.
#
# Author: Elaine Tynan
# Start-date: 22/03/2022

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

# The next comment (line 12) is to stop errors using df.loc
# pylint: disable=no-member

plotPath = './plots/'
dataPath = './data/'

def plotIrisGrps(df, xcol, ycol, legendTitle, title, xlabel, ylabel, fname):
    # Plot 3 types of Iris - sepal dimensions
    # plt.subplots() is a function that returns a tuple containing a figure and axes object(s).
    # figsize sets the dimensions of the plot. A common size is 8x6 and looks good when I run it. 
    fig, ax = plt.subplots(figsize=(8,6))

    for n, grp in df.groupby('class'):
        ax.scatter(x=xcol, y =ycol, data=grp, label=n)
    ax.legend(title=legendTitle)
    plt.title(title)
    ax.set_xlabel(xlabel, fontweight ='bold')
    ax.set_ylabel(ylabel, fontweight ='bold')
    plt.savefig(plotPath+fname)
    #plt.show()

def doClustering(dataset, xcol, ycol, title, fname, xcolIdx, ycolIdx):
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
    plt.savefig(plotPath+fname)
    
# Next try histograms of the summary staatistics grouped by class