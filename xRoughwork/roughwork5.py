# analysis.py
#
# Analysis of the Fisher’s Iris data set.
#
# Author: Elaine Tynan
# Start-date: 22/03/2022

import pandas as pd
import plotAnalysis as pa
import matplotlib.pyplot as plt
import numpy as np

# The next comment (line 12) is to stop errors using df.loc
# pylint: disable=no-member

plotPath = './plots/'
dataPath = './data/'

irisFile = dataPath+"iris.data"

# Read in Irish data. There is no header in this file.
df = pd.read_csv(irisFile, header=None)
# Add column names
df.columns =['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

### Summary stats

# Get all rows for Iris-setosa then get summary statistics for setosa
setosa = df.loc[df['class'] == 'Iris-setosa']
setostaStats = setosa.describe()
# Get all rows for Iris-versicolor then get summary statistics for versicolor
versicolor = df.loc[df['class'] == 'Iris-versicolor']
versicolorStats = versicolor.describe()
# Get all rows for Iris-virginica then get summary statistics for Iris-virginica
virginica = df.loc[df['class'] == 'Iris-virginica']
virginicaStats = virginica.describe()

'''
#print(df)
print(setostaStats)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(versicolorStats)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(virginicaStats)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
'''
### End Summary stats

def barChartSummaryStat(colName):
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

'''
sepalLenMean = df.groupby('class', as_index=False)['sepal length'].mean()
print(sepalLenMean)
##X = list(df.iloc[:, 0])
#Y = list(df.iloc[:, 1])
#plt.bar(x='sepal length', height, tick_label=['Iris-setosa','Iris-versicolor','Iris-virginica'])
ax = sepalLenMean.plot.bar(x='class', y='sepal length', rot=0)
plt.show()
'''
barChartSummaryStat('sepal length')

'''
myData = [['Iris-setosa', 5.006],['Iris-versicolor', 5.936],['Iris-virginica', 6.588]]
#df2 = pd.DataFrame(myData,columns=['Class', 'Mean'])
df2 = pd.DataFrame(myData)
df2.columns = ['class','mean']
df2.set_index('class')
print(df2)
print("~~~~~~~~~~~~~~~~")
#df3 = df2.pivot(index = '', columns='Class',values='Mean')
df3 = df2.transpose()
df3.columns = df3.iloc[0] 
df3 = df3[1:]
print(df3)
print("~~~~~~~~~~~~~~~~")

#ax = df3.plot.bar(x='mean', y='class',rot=0)
#plt.show()
'''

