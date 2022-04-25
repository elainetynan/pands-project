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
from pandas.plotting import andrews_curves

# Import Library for loading & splitting data & creating Decision tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# The next comment (line 12) is to stop errors using df.loc
# pylint: disable=no-member

dataPath = './data/'

def doDecisionTree(df):
    ds = load_iris()
    # Extract Measurements
    x = ds.data

    # Extract Class Labels (target)
    y = ds.target

    # Creating Training and Test datasets
    x_train, x_test, y_train, y_test = train_test_split(x,y, random_state = 50, test_size = 0.25)

    # Creating Decision Tree Classifier
    clf = DecisionTreeClassifier()
    clf.fit(x_train,y_train)

    # Predict Accuracy Score
    y_pred = clf.predict(x_test)
    #print("Train data accuracy:",accuracy_score(y_true = y_train, y_pred=clf.predict(x_train)))
    #print("Test data accuracy:",accuracy_score(y_true = y_test, y_pred=y_pred))
    print(y_pred)