# analysis.py
#
# Analysis of the Fisher’s Iris data set.
#
# Author: Elaine Tynan
# Start-date: 12/04/2022

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

irisFile = dataPath+"iris.data"
df = pd.read_csv(irisFile, header=None)
df.columns =['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

'''
subset = df.iloc[:,0:2] # from column 0 up to but not including column 2
print(subset)
print("~~~~~~~~~~~~~~~~~")
'''
# Before Clustering
#subset.plot.scatter(x='sepal length', y ='sepal width', title="Before Clustering")
#plt.show(block=True)

def doClustering(dataset, xcol, ycol, title, fname, startCol, endCol):
    subset = dataset.iloc[:,startCol:endCol] 
    # Do Clustering
    kmeans = KMeans(3) # an unsupervised machine learning technique used to identify clusters of data objects in a dataset. 
    kmeans.fit(subset) # Computes k-means clustering
    identified_clusters = kmeans.fit_predict(subset)
    
    data_with_clusters = dataset.copy()
    data_with_clusters['Clusters'] = identified_clusters 
    plt.scatter(data_with_clusters[xcol],data_with_clusters[ycol],c=data_with_clusters['Clusters'],cmap='rainbow')
    plt.title(title)
    #plt.show()
    plt.savefig(plotPath+fname)


#subset = df.iloc[:,0:2] # from column 0 up to but not including column 2
#print(subset)
#print("~~~~~~~~~~~~~~~~~")
doClustering(df, 'sepal length', 'sepal width', "Sepal Length v Sepal Width: Clustered",
                "ClusterSepalLengthVWidth.png", 0, 2)

#subset = df.iloc[:,2:4] # from column 0 up to but not including column 2
#print(subset)
#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
doClustering(df, 'petal length', 'petal width', "Petal Length v Petal Width: Clustered",
                "ClusterPetalLengthVWidth.png", 2, 4)