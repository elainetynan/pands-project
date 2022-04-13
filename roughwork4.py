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

def describe_helper(series):
    splits = str(series.describe()).split()
    keys, values = "", ""
    for i in range(0, len(splits), 2):
        keys += "{:8}\n".format(splits[i])
        values += "{:>8}\n".format(splits[i+1])
    print("################")
    print(keys)
    print("~~~~~~~~~~~~~~~~")
    print(values)
    print("****************")
    return keys, values


#demo = np.random.uniform(0,10,100)
plt.hist(df, bins=9)
plt.figtext(.95, .49, describe_helper(pd.Series(df))[0], {'multialignment':'left'})
plt.figtext(1.05, .49, describe_helper(pd.Series(df))[1], {'multialignment':'right'})
plt.show()