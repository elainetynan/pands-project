# pands-project
Project for Programming and Scripting project.


Introduction
~~~~~~~~~~~~
After reading the project spec (Beatty, 2022) I read the UC Irvine Machine Learning Repository information on the Iris Data Set (Fisher, 1936), the link given in the project brief. This led me to the relevant papers but none of the links given worked for me, so I proceeded to do an online search for each of the papers. The first site I came across, from mirlab (Jyh-Shing, 1996), was remarkably similar to the initial link given but additionally it had some interesting graphs. The graphs were very helpful in understanding what data was being stored and how it was being used to distinguish between the different types of Iris flowers. It also gave me ideas on what kinds of analysis I should be doing for this project.

At the initial stages of this project, I found the prospect of doing analysis on plants daunting as I am the opposite of green-fingered (I often refer to myself as black-fingered) and my gardening knowledge is sparse, at best. On looking at this initial page from mirilab, I am hopefully that gardening knowledge will not be an issue and that I can simply treat the data as I would any raw data.

On further inspection of the mirilab web page it is a page from an online book about Data Clustering and Pattern recognition, which at an early stage seems like it could be helpful in this project.


The Iris Data Set
~~~~~~~~~~~~~~~~~
The Iris dataset is famous as the dataset used in a paper in 1936 by R.A Fisher. The paper titled 'The Use of Multiple Measurements in Taxonomic Problems' includes fifty samples of data on three different species of the Iris Flower. Each Flower had the following information recorded about it: Sepal length in cm, Sepal width in cm, Petal length in cm, petal width in cm and class, where class is either 'Iris-setosa', 'Iris-versicolor' or 'Iris-virginica'.
One flower species (Iris-setosa) is linearly separable from the other two, while the other two are not linearly separable from each other. Data can be classed as linearly separable if a line can be drawn anywhere on the plane that will have all the data objects from one dataset at one side of it and all the datasets from the other dataset at the other side.This is shown extensively in research of the Iris dataset and is clear in the analyses I consequently carried out.
The Iris dataset became a typical example for statistical analysis and machine learning. The fact that the data only contains two clusters (Iris Setosa in one cluster and Iris Versicolor with Iris Virginica in the other cluster) means it is not a good example for cluster analysis but inversely is a good example of the differences between supervised and unsupervised techniques in data mining as Iris Versicolor and Iris Virginica is not separable without further species information that Fisher used (Wikipedia, 2022). The analyses I carried out has backed this up.



Instructions for running code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Call the analysis.py python program. the plotAnalysis.py must be in the same folder as the analysis.py file
The following directory and file must exist:
./data - containing the Iris data set called 'iris.data'

The following empty directories must exist:
./summaryStats
./plots
./plots/barSummary
./plots/cluster
./plots/scatter
./plots/scatter3D

Plotly.Express and kaleido must be installed and can be doe so as follows:
pip install plotly==5.7.0
pip install kaleido



Analysis
~~~~~~~~
Based on the analysis I have concluded the below information.


Scatter Graphs

In the scatter graph of Sepal Length v Sepal Width it shows that the class Setosa has smaller sepal lengths but larger sepal widths than the other two class of Iris. The remaining two class of Iris are very much overlapping but in general the class Versicolor has a shorter and slightly narrower sepal than the class Virginica.

The scatter graph of Petal Length v Petal Width shows that the class Setosa has shorter and narrower petals than the other two class of Iris.
The class Versicolor is both shorter and narrower than the class Virginica, which has the longest and widest petals of all 3.

The remaining four scatter graphs (Petal Length v Sepal Length, Petal Length v Sepal Width, Petal Width v Sepal Length, Petal Width v Sepal Width) all show similar patterns where Iris Setosa clearly has the shortest and widest sepals and shortest and narrowest petals while the other two Irises are closer in size with the Versicolor having shorter and narrower petals and sepals than Virginica.


Cluster Plots

The cluster plots again show a clear difference between Iris Setosa and the other two class of Iris. Again, the Iris Setosa is smaller than the other two class of Iris is both length and width. In most cases using K-means clustering there is a clear distinction between Iris Setosa and the remaining two Iris class which makes it linearly separable from them. This is not true for Iris Versicolor and Iris Virginica.


Box plots

In all instances of the box plots (plotting the sepal length, sepal width, petal length and sepal width) it is clear that the Iris Setosa is smallest, Iris Virginica is largest and Iris versicolor is in the middle although it is closer in all dimensions to Iris Virginica than to Iris Setosa.


Bar Charts

The Bar charts for the min, max mean and standard deviation of all four measurements reinforce what the other visualisations show, again that Iris Setosa is clearly the smallest in all areas except the sepal width. the Iris Virginica is the largest with Iris Versicolor being in the middle. This is true, even for standard deviation.
In the case of sepal width Iris Setosa is the widest with Iris Virginica being the narrowest and Iris Versicolor being in the middle.


Andrews Curve

The Andrews surce show the 3 class of Iris. It show a large proportion ove overlap between Iris Virginica and Iris Versicolor. It also shows Iris Virginica having the largest values, for the most part while Iris Setosa has the smallest values for the most part, towards the end and beginning Iris Setosa has larger values which would correspond to it having wider sepals. The reason why it is larger at the start and end is because the Andrews curve is version of the radar chart which is circular in nature, we could essentially join the end of the plot with the beginning of it.


Summary Statistics

The summary statistics is a quick look at the same information that is shown in the box plots


3D Scatter Plots

The 3D scatter plots showed very similar data to the scatter plots but presented them in a visually more striking way. Again Iris-setosa is smallest in petal length and width as well as sepal length, but has wider sepals. Iris-versicolor falls in the middle in all measurements but closer to Iris-virginica, which is the largest in all measurements except the sepal width.



Conclusion
~~~~~~~~~~
My initial trepidation of analysing data related to gardening was certainly unfounded. The Iris data set is clearly another set of data with categorical and continuous data.
At this stage of the course, we have not covered data analyses in much detail. This was a good exercise to get us initiated into real data analytics, although I’m sure there will be a lot more to come.
When researching the dataset, it is clear that it is widely used and has been researched and analysed to a great degree. With that in mind I have only scratched the surface and have certainly not revealed any ground-breaking revelations.
What I have concluded is that Iris Setosa is clearly quite different to the other 2 classes of Iris. If one were to calculate the average area of the petals of all 3 class of Iris (there is no formula to calculate the surface area of an irregular shape), it is clear that the Iris Setosa would have the smallest petal surface area. The same can not be said for the sepal as the Iris Setosa sepal width is the largest, which would clearly make it difficult to differentiate form the Iris Versicolor and Iris Virginica based on surface area. In saying that, when looking at the individual dimensions (length and width) of the sepal, it is clearly different to the other two.
While Iris Setosa is clearly different, the same cannot be said for Iris Virginica and Iris Versicolor. On close examination the Iris Versicolor is smaller but there is quite an overlap which would make it difficult to decide if an Iris were an Iris Versicolor or Iris Virginica based on measurements alone.
Pictures of the three classes of Iris again back up the findings of my (and many others) analysis that the Iris Setosa is indeed quite different to the other two, which are quite similar, especially in size. 



Diary
~~~~~

11/04/2022
~~~~~~~~~~
I researched how to do a scatter plot of two columns grouped by another column value using matplotlib and found a way that would allow me to add the three classes of lilies to one plot using a for loop here: https://stackoverflow.com/questions/21800004/pandas-for-loop-on-a-group-by

I also found a way to set the Axes labels here: https://www.geeksforgeeks.org/matplotlib-axes-axes-set_xlabel-in-python/


12/04/2022
~~~~~~~~~~
On researching the Iris dataset, I came across a method of clustering that has been used in the analysis of the dataset over the year. The K-Mean Clustering is a technique to identify clusters of data in a dataset. K-means clustering in Python is considered to be reasonably straightforward. (Arvai, 2019)
Clustering is a method to separate data into groups/clusters. Clusters can be defined as groups of data that are more similar to each other than to data in other clusters in the dataset. K-means clustering is a type of Partitional Clustering. this means that all data objects are part of only one cluster and there is no overlapping between clusters, each cluster must have at least one data object. (Arvai, 2019)
I found easy to follow and well explained information on how to use K-means cluster in python. The steps involved in calculating the K-means as per Pranshu (2021) can be outlined as follows:
    Step-1: Select the value for K, the number of clusters to be formed.
    Step-2: Select random K points as centroids.
    Step-3: Assign all data points based on their distance from the centroids (closest centroid).
    Step-4: Set a new centroid of each cluster.
    Step-5: Repeat step no.3, reassigns each datapoint to the new closest centroid.
    Step-6: If any reassignment occurs, then go to step-4 otherwise end
Pranshu (2021) also outlined some easy-to-follow python code.

Some other code I researched was the use of loc and iloc in dataframes. These had been covered in our classes, but I needed more in-depth knowledge when using them. I found useful information at https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html  and https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html. Also following on from the information I found on K-means Clustering I wanted a little more knowledge of the structure of the function which I found here: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html


19/04/2022
~~~~~~~~~~
Based on the summary statistics that are generated by the dataframe.describe() function I decided to generate bar charts from the statistics. The format of the summary statistics was inconvenient, and it made more sense to generate the statistics individually for each measurement grouped by class. This gave be a dataframe for each measurement and also for each statistic, e.g., for Iris-setosa I has four dataframes (min, mean, max & standard deviation) for each measurement. I did not save these as I also generated the summary statistics for each class using the above mentioned dataframe.describe() function. I did save these summary statistics to csv files. I generated and saved the bar charts using the dataframe.groupby() function and the individual statistical functions. as per the example on https://datascienceparichay.com/article/pandas-groupby-minimum/ and then tried replacing 'min' with the various different statistics I required.
There were different ways to generate bar charts I tried the matplotlib.pyplot.bar() function as per https://www.geeksforgeeks.org/how-to-plot-bar-graph-in-python-using-csv-file/ but found the dataframe.plot.bar() function worked better for what I needed to do as per https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html

I also did some tidying up and moved code that was no longer being used from the analysis.py program file. I put some of the tasks into functions which I stored in plotAnalysis.py and call them in analysis.py as it is neater and easier to use and follow.
The analysis.py file is now essentially a series of calls to functions while the plotAnalysis.py file is a series of functions. I think later in the process I will rename plotAnalysis.py to something more meaningful.


20/04/2022
~~~~~~~~~~
I put in the function to create four boxplots, one for each of the four measurements, all grouped by Iris class. This is a good visualisation of the Min, Max, 1st, 2nd and 3rd quartiles of each class of Iris mased on the four measurements. This new function is called by the analysis.py program. 
I saw this as an opportunity to use the Seaborn package as all the rest of my plots have been using matplotlib. I did research on how to do this and found an especially useful article on Python Data Visualisations on https://www.kaggle.com/code/benhamner/python-data-visualizations Initially when I created these plots seaborn was plotting all the figures on top of one another, so I did research to find how to prevent this and came across a stackoverflow query at this link: https://stackoverflow.com/questions/36018681/stop-seaborn-plotting-multiple-figures-on-top-of-one-another
I had been getting a warning about having more than twenty plots opened (even though I was saving the plots and not showing them, they were in fact ‘open’) so I did research into how I could prevent this. I did not want to simply supress the warning as the warning message suggested as I felt if the plots were ‘open’ this could be a memory issue. I found a solution on stackoverflow, where I could close all plots with one command and called this at the end of every function that created multiple plots at this link: https://stackoverflow.com/questions/21884271/warning-about-too-many-open-figures.


25/04/2022
~~~~~~~~~~
Today I found an interesting data visualisation called the Andrews Plot, or in Python the andrews_curve (Yashi, 2021). This can be used to find outliers in data but more importantly in the case of the Iris-dataset, it can be used “as a technique for classifying observations into groups”, (Spencer, 2003). Spencer (2003) goes on to explain how the Andrews plot will produce similar curves for data in groups with similar patterns for grouped data. The plot created from the Iris dataset clearly shows the 3 groups and how the data differs and also overlaps.
I also did some research on decision tress but decided not to use them. For my level of knowledge in data analyses so far, I felt it did not add any value to my analyses of the Iris Dataset.


27/04/2022
~~~~~~~~~~
I decided to include £d scatter graphs to my analysis. This involved installing both plotly.express which needed to be installed. This was good experience is using a new package that I had never heard of as well as installing packages. To save the plot using Plotly express I also needed to install kaleido (instruction given for installing both above). The 3D scatter graphs are a little more complicated to use compared to regular scatter graphs but that is to be expected. Good code samples and information was supplied by the Portylu website (2022). I had also looked at various other ways of doing them such as Bedre (2022) and Devakumar (2020) showed but I wanted to try a new package as well as the fact that the using plotly made the code quite simple.



References
~~~~~~~~~~

Arvai, K. (2019), K-Means Clustering in Python: A Practical Guide. Available at:
https://realpython.com/k-means-clustering-python/ (Accessed: 12 April 2022)

Beatty, A. (2022), PROJECT: Programming and Scripting. Available at: https://learnonline.gmit.ie/pluginfile.php/547122/mod_label/intro/Project.pdf?time=1646300056436 (Accessed: 22 March 2022)

Bedre, R. (2022), Create scatter plots using Python (matplotlib pyplot.scatter). Available at: https://www.reneshbedre.com/blog/scatter-plot-matplotlib.html (Accessed: 27 April 2022)

Data Science Parichay (2021), Minimum Value in Each Group – Pandas Groupby. Available at: https://datascienceparichay.com/article/pandas-groupby-minimum/ (Accessed: 19 April 2022)

Devakumar, K. P. (2020), Plotly Express 3D Scatter Plot - Iris Data. Available at: https://www.kaggle.com/code/imdevskp/plotly-express-3d-scatter-plot-iris-data/notebook (Accessed 27 April 2022)

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science. Available at: https://archive.ics.uci.edu/ml/datasets/iris
(Accessed: 22 March 2022)

Fisher R.A. (1936), The use of multiple Measurements in Taxonomic Problems. Available at: https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x (Accessed: 12 April 2022)

Hamner, B. (2017), Python Data Visualizations. Available at: https://www.kaggle.com/code/benhamner/python-data-visualizations (Accessed: 20 April 2022)

Jyh-Shing Roger Jang (1996), Data Clustering and Pattern Recognition. available at http://mirlab.org/jang/books/dcpr/ (Accessed: 22 March 2022)

Pranshu, (2021), K Means Clustering Simplified in Python. Available at: https://www.analyticsvidhya.com/blog/2021/04/k-means-clustering-simplified-in-python/ (Accessed: 12 April 2022)

Plotly (2022), 3D Scatter Plots in Python. Available at: https://plotly.com/python/3d-scatter-plots/ (Accessed: 27 April 2022)
  
Spencer N.H. (2003), Investigating Data with Andrews Plots. Social Science Computer Review. Available at: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.608.6250&rep=rep1&type=pdf (Accessed: 25 April 2022)

Yashi S. (2021), Analyzing Decision Tree and K-means Clustering using Iris dataset. Available at: https://www.analyticsvidhya.com/blog/2021/06/analyzing-decision-tree-and-k-means-clustering-using-iris-dataset/ (Accessed: 25 April 2022)
  

Wikipedia (2022), Iris flower data set. Available at: https://en.wikipedia.org/wiki/Iris_flower_data_set (Accessed: 12 April 2022)



Other References read but not used directly in the project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Duda, & Hart, P. E. (1973), Pattern classification and scene analysis. Wiley. Available at: https://www.cs.toronto.edu/~rgrosse/courses/csc321_2018/tutorials/tut2.pdf (Accessed: 12 April 2022)

Hamner, B. Jatana, V. Swain, A (2016) Iris Species. Available at: https://www.kaggle.com/datasets/uciml/iris (Accessed: 12 April 2022)

Pedregosa et al (2011),Scikit-learn: Machine Learning in Python, K-means clustering. JMLR 12, pp. 2825-2830, 2011. Available at: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html (Accessed: 12 April 2022)
