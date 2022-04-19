# pands-project
Project for Programming and Scripting project.


Introduction
~~~~~~~~~~~~
After reading the project spec (Beatty, 2022) I read the UC Irvine Machine Learning Repository information on the Iris Data Set (Fisher, 1936), the link given in the project brief. This lead me to the relevant papers but none of the links given worked for me, so I proceeded to do an online search for each of the papers. The first site I came across, from mirlab (Jyh-Shing, 1996), was very similar to the initial link given but additionally it had some very interesting graphs. The graphs were very helpful in understanding what data was stored and how it was being used to distinguish between the different types of Iris flowers. It also gave me some ideas on what kinds of analysis I should be doing for this project.
At the initial stages of this project I found the prospect of doing analysis on plants daunting as I am the opposite of green-fingered (I often refer to myself as black-fingered) and my gardening knowledge is sparse, at best. On looking at this initial page from mirilab, I am hopefully that garedening knowledge will not be an issue and that I can simply treat the data as I would any raw data.

On further inspection of the mirilab web page it appears to be a page from an online book about Data Clustering and Pattern recognition, which at an early stage seems like it could be helpful in this project.


The Iris Data Set
~~~~~~~~~~~~~~~~~
The Iris dataset is famous as the dataset used in a paper in 1936 by R.A Fisher. The paper
titled 'The Use od Multiple Measurements in Taxonomic Problems' includes 50 samples of data on 3 different species of the Iris Flower. Each Flower had the following information recorded about it: Sepal length in cm, Sepal width in cm, Petal length in cm, petal width in cm and class, where class is either 'Iris-setosa', 'Iris-versicolor' or 'Iris-virginica'.
One flower species is linearly seperable from the other 2, while the other two are not linearly sepearable from each other. Data can be classesd as linearly seperable if a line can be drawn anywhere on the plane that will have all the data objects from one datset at one side of it and all the datasets from the other dataset at the other side.

Instructions
~~~~~~~~~~~~
Call the analysis.py python program. the plotAnalysis.py must be in the same folder as the analysis.py file
The following directory and file must exist:
./data - containing the Iris data set called 'iris.data'

The following empty directories must exist:
./summaryStats
./plots
./plots/barSummary
./plots/cluster
./plots/scatter



Diary
~~~~~

11/04/2022
~~~~~~~~~~
I researched how to do a scatter plot of 2 columns grouped by another column value using matplot lib and found a way that would allow me add the 3 classes of lilies to one plot using a for loop here: https://stackoverflow.com/questions/21800004/pandas-for-loop-on-a-group-by

I also found a way to set the Axes labels here: https://www.geeksforgeeks.org/matplotlib-axes-axes-set_xlabel-in-python/



12/04/2022
~~~~~~~~~~
On researching the Iris Dataset itself I came accross a method of clustering that has been used in the analysis of the dataset over the year. The K-Mean Clustering is a technique to identify clusters of data in a dataset. K-means clustering in Python is considered to be reasonably straightforward. (Arvai, 2019)
Clustering is a method to deparate data into groups/clusters. Clusters can be defined as groups of data that are more similar to each other than to data in other clusters in the dataset. K-means clustering is a type of Partitional Clustering. this means that all data objects are part of only one cluster and there is no overlapping between clusters, each cluster must have at least one data object. (Arvai, 2019)
I found some very easy to follow and well explained information on how to use K-means cluster in python. The steps involved in calculating the K-means as per Pranshu (2021) can be outlined as follows:
    Step-1: Select the value for K,  the number of clusters to be formed.
    Step-2: Select random K points as centroids.
    Step-3: Assign all data points based on their distance from the centroids (closest centroid).
    Step-4: Set a new centroid of each cluster.
    Step-5: Repeat step no.3, reassigns each datapoint to the new closest centroid.
    Step-6: If any reassignment occurs, then go to step-4 otherwise end
Pranshu (2021) also outlined some easy tpo follow python code.

Some other code I researched was the use of loc and iloc in dataframnes. These had been covered in our classes but I needed mire indepth knowledge when using them. I found useful information at https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html  and https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html. Also following on from the information I found on K-means Clustering I wanted a little more knowledge of the structure of the function which I found here: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html



19/04/2022
~~~~~~~~~~
Based on the summaryt statistics that are generated by the dataframe.describe() function I decided to generate some bar charts from the statistics. The format of the summary statistics was inconvenient and it made more sense to generate the statistics indivisually for each measurement grouped by class. This gave be a dataframe for each measurement and also for each statistic, e.g for Iris-setosa I has 4 dataframes (min, mean, max & standard deviation) for each measurement. I did not save these as I also generated the summary statistics for each class using the above mentioned dataframe.descibe() function. I did save these summary statistics to csv files. I generated and saved the bar charts using the dataframe.groupby() function and the individual statistc functions. as per the example on https://datascienceparichay.com/article/pandas-groupby-minimum/ and then tried replacing 'min' with the various different statistics I required.
There were a few different ways to generate bar charts I tried the matplotlib.pyplot.bar() function as per https://www.geeksforgeeks.org/how-to-plot-bar-graph-in-python-using-csv-file/ but found the dataframe.plot.bar() function worked better for what I needed to do as per https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html

I also did some tidy up and moved code that was no longer being used form the analysis.py program file. I put some of the tasks into functions which I stored in plotAnalysis.py and call them in analysis.py as it is neater and easier to use and follow.
The analysis.py file is now esentially a series of calls to functions while the plotAnalysis.py file is a series of functions. I thik later in the process i will rename plotAnalysis.py to something more meaningful.



References
~~~~~~~~~~

Arvai, K. (2019), K-Means Clustering in Python: A Practical Guide. Available at:
https://realpython.com/k-means-clustering-python/ (Accessed: 12 April 2022)

Beatty, A. (2022), PROJECT: Programming and Scripting. Available at: https://learnonline.gmit.ie/pluginfile.php/547122/mod_label/intro/Project.pdf?time=1646300056436 (Accessed: 22 March 2022)

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science. Available at: https://archive.ics.uci.edu/ml/datasets/iris (Accessed: 22 March 2022)

Fisher R.A. (1936), The use of multiple Measurements in Taxonomic Problems. Available at: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x (Accessed: 12 April 2022)

Jyh-Shing Roger Jang (1996), Data Clustering and Pattern Recognition. available at http://mirlab.org/jang/books/dcpr/. (Accessed: 22 March 2022)

Pranshu, (2021), K Means Clustering Simplified in Python. Available at: https://www.analyticsvidhya.com/blog/2021/04/k-means-clustering-simplified-in-python/ (Accessed: 12 April 2022)



Possibly


Duda, & Hart, P. E. (1973), Pattern classification and scene analysis. Wiley. Available at: 

https://www.cs.toronto.edu/~rgrosse/courses/csc321_2018/tutorials/tut2.pdf

K-means clustering

https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html



Iris DataSet
https://www.kaggle.com/datasets/uciml/iris Accesed: 12 April 2022
