#Experiment 15: Implement Clustering Techniques Using Spark

## Aim

To implement clustering techniques using Apache Spark and analyze the resulting clusters.

## Requirements

Apache Spark

Scala or PySpark

Java Development Kit (JDK)

Python (for PySpark)

Sample dataset

## Theory

Clustering is an unsupervised machine-learning technique used to group similar data points into clusters. Spark MLlib provides scalable clustering algorithms that can process large datasets efficiently.

Common clustering techniques available in Spark include:

K-Means: Partitions data into k clusters by minimizing the distance between data points and their cluster centers.

Bisecting K-Means: A hierarchical approach that repeatedly divides clusters into two groups.

Gaussian Mixture Model (GMM): Represents clusters as a mixture of Gaussian probability distributions.

In this experiment, K-Means clustering is implemented using Spark MLlib.

## Procedure

Install and configure Apache Spark.

Start a Spark application or open a PySpark shell.

Import the required Spark ML libraries.

Load the dataset into a Spark DataFrame.

Select the relevant features for clustering.

Use VectorAssembler to combine the features into a single feature vector.

Create a K-Means model and specify the number of clusters (k).

Train the model using the feature vectors.

Predict the cluster assigned to each data point.

Display the cluster centers and predictions.

Evaluate the clustering using an appropriate metric such as Silhouette score.

## PySpark Implementation

refer

```python
spark_program.py
```

## Sample Dataset

The data.csv file can contain:

feature1,feature2
1.0,1.5
1.2,1.8
1.1,1.3
5.0,5.5
5.2,5.8
4.8,5.1
9.0,1.0
9.2,1.3
8.8,0.8

## Expected Output

The program displays the cluster assigned to each data point and the cluster centers.

Example:

+--------+--------+----------+
|feature1|feature2|prediction|
+--------+--------+----------+
|     1.0|     1.5|         0|
|     1.2|     1.8|         0|
|     5.0|     5.5|         1|
|     5.2|     5.8|         1|
|     9.0|     1.0|         2|
|     9.2|     1.3|         2|
+--------+--------+----------+

Cluster Centers:
[...]
[...]
[...]

Silhouette Score = ...


The exact cluster numbers and centers may vary because cluster labels are assigned by the algorithm.

## Result

Thus, clustering was successfully implemented using Apache Spark K-Means, and the data points were grouped into clusters based on their feature similarity. The quality of the clustering was evaluated using the Silhouette score.

## Viva Questions

What is clustering?

What is the difference between supervised and unsupervised learning?

What is K-Means clustering?

Why is the value of k required in K-Means?

What is the role of VectorAssembler in Spark ML?

What is a cluster center?

What is the Silhouette score?

Name other clustering algorithms available in Spark.

What are the advantages of using Spark for clustering?

What happens if an inappropriate value of k is selected?
