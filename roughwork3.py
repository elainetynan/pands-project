# analysis.py
#
# Analysis of the Fisher’s Iris data set.
#
# Author: Elaine Tynan
# Start-date: 22/03/2022

import pandas as pd
import plotAnalysis as pa
import matplotlib.pyplot as plt

# The next comment (line 12) is to stop errors using df.loc
# pylint: disable=no-member

plotPath = './plots/'
dataPath = './data/'

irisFile = dataPath+"iris.data"

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
plt.hist(df3,3)
plt.show()
'''

# Read in Irish data. There is no header in this file.
df = pd.read_csv(irisFile, header=None)
# Add column names
df.columns =['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

allStats = df.groupby('class').describe().unstack(1)
#print(allStats)
'''
fig, ax = plt.subplots()
ax.hist(df[0])
#plt.figtext(0.1,0.5, df.describe().to_string())
#plt.figtext(0.75,0.5, df.describe().loc[['mean','std']].to_string())

'''
sepalStats = allStats.loc['sepal length']
meanStats = sepalStats.loc['mean']
maxStats = sepalStats.loc['max']
stdStats = sepalStats.loc['std']
#allStats.to_csv("summaryStats.csv")
#allStats.to_excel("summaryStats.xlsx")
#print(countStats)
'''
'''
mylabels = ['Setosa', 'Versicolor', 'Virginica']
#plt.pie(meanStats, labels = mylabels)
plt.pie(stdStats, labels = mylabels)

#plt.hist(meanStats)
#irises = ['Setosa', 'Versicolor', 'Virginica']
#plt.xticks(irises)
#plt.xlabel(irises, fontsize=16)

plt.show()
'''
'''