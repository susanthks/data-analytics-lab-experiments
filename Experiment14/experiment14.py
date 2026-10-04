from pyspark.sql import SparkSession
from pyspark.sql.functions import min, max

# Create Spark Session
spark = SparkSession.builder \
    .appName("ObservationAnalysis") \
    .getOrCreate()

# Read the CSV dataset
df = spark.read.csv(
    "observations.csv",
    header=True,
    inferSchema=True
)

# Display the dataset
print("Dataset:")
df.show()

# Display the schema
print("Schema:")
df.printSchema()

# i) Count total number of observations
total_observations = df.count()

# ii) Count number of distinct years
number_of_years = df.select("Year").distinct().count()

# iii) Find oldest and newest year
year_range = df.select(
    min("Year").alias("Oldest_Year"),
    max("Year").alias("Newest_Year")
).first()

# Display results
print("\n--- Results ---")
print("Total number of observations:", total_observations)
print("Number of years:", number_of_years)
print("Oldest year:", year_range["Oldest_Year"])
print("Newest year:", year_range["Newest_Year"])

# Stop Spark Session
spark.stop()
