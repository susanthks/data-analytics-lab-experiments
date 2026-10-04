from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator

# Create Spark session
spark = SparkSession.builder \
    .appName("Experiment15-Clustering") \
    .getOrCreate()

# Load dataset
data = spark.read.csv(
    "data.csv",
    header=True,
    inferSchema=True
)

# Select features
feature_columns = ["feature1", "feature2"]

# Convert features into a vector
assembler = VectorAssembler(
    inputCols=feature_columns,
    outputCol="features"
)

dataset = assembler.transform(data)

# Create K-Means model
kmeans = KMeans(
    k=3,
    seed=1,
    featuresCol="features",
    predictionCol="prediction"
)

# Train the model
model = kmeans.fit(dataset)

# Make predictions
predictions = model.transform(dataset)

# Display results
predictions.select(
    *feature_columns,
    "prediction"
).show()

# Display cluster centers
print("Cluster Centers:")
for center in model.clusterCenters():
    print(center)

# Evaluate using Silhouette score
evaluator = ClusteringEvaluator(
    featuresCol="features",
    predictionCol="prediction"
)

silhouette = evaluator.evaluate(predictions)

print("Silhouette Score =", silhouette)

spark.stop()
