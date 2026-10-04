# Experiment 14: Spark Program for Dataset Observation Analysis

## Aim

To implement a Spark program to:

1. Count the total number of observations included in the dataset.
2. Count the number of years over which observations have been made.
3. Display the oldest and the newest year of observation.

## Software Requirements

- Apache Spark
- PySpark
- Python 3.x
- Jupyter Notebook / VS Code / Terminal
- CSV dataset containing a **Year** column

## Theory

Apache Spark is a distributed data-processing framework designed to process large datasets efficiently.

In this experiment, PySpark is used to load a dataset and perform basic analysis on the year of observation.

The following operations are performed:

### 1. Total Number of Observations

The total number of records in the dataset can be obtained using:

```python
df.count()
```

### 2. Number of Years

The number of distinct years represented in the dataset can be found using:

```python
df.select("Year").distinct().count()
```

### 3. Oldest and Newest Year

The oldest year is obtained using `min()` and the newest year using `max()`:

```python
from pyspark.sql.functions import min, max

df.select(min("Year"), max("Year")).show()
```

> **Note:** If your dataset uses a different column name such as `year`, `Year_Observed`, or `Observation_Year`, replace `Year` in the program accordingly.

---

## Dataset

Use a CSV dataset containing observations recorded over different years.

### Example Dataset

Save the following data as `observations.csv`:

```csv
Year,Observation
2000,Observation 1
2001,Observation 2
2001,Observation 3
2002,Observation 4
2005,Observation 5
2010,Observation 6
2010,Observation 7
2015,Observation 8
2020,Observation 9
2020,Observation 10
```

For this sample dataset:

- Total observations = 10
- Number of distinct years = 7
- Oldest year = 2000
- Newest year = 2020

---

## Procedure

1. Install and configure Apache Spark and PySpark.
2. Create or obtain the required CSV dataset.
3. Make sure the dataset contains a year column.
4. Start a Spark session.
5. Read the CSV dataset into a Spark DataFrame.
6. Display the dataset and verify the column names.
7. Count the total number of observations.
8. Find the number of distinct years.
9. Find the oldest year.
10. Find the newest year.
11. Display the results.

---

## Program

Create a file named `experiment14.py`.



Run the program using:

```bash
spark-submit experiment14.py
```

If PySpark is being used directly:

```bash
python3 experiment14.py
```

---

## Expected Output

```text
Dataset:
+----+-------------+
|Year|  Observation|
+----+-------------+
|2000|Observation 1|
|2001|Observation 2|
|2001|Observation 3|
|2002|Observation 4|
|2005|Observation 5|
|2010|Observation 6|
|2010|Observation 7|
|2015|Observation 8|
|2020|Observation 9|
|2020|Observation 10|
+----+-------------+

--- Results ---
Total number of observations: 10
Number of years: 7
Oldest year: 2000
Newest year: 2020
```

---

## Explanation of the Program

### Create Spark Session

```python
spark = SparkSession.builder \
    .appName("ObservationAnalysis") \
    .getOrCreate()
```

Creates a Spark session required to perform Spark operations.

### Read Dataset

```python
df = spark.read.csv(
    "observations.csv",
    header=True,
    inferSchema=True
)
```

Reads the CSV file into a Spark DataFrame.

- `header=True` treats the first row as column names.
- `inferSchema=True` automatically identifies suitable data types.

### Count Observations

```python
total_observations = df.count()
```

Returns the total number of rows in the DataFrame.

### Count Distinct Years

```python
number_of_years = df.select("Year").distinct().count()
```

The `distinct()` function removes duplicate years and `count()` counts the remaining unique years.

### Find Oldest and Newest Years

```python
df.select(
    min("Year").alias("Oldest_Year"),
    max("Year").alias("Newest_Year")
).first()
```

- `min("Year")` returns the oldest year.
- `max("Year")` returns the newest year.

---

## Result

The Spark program was successfully implemented to:

- Count the total number of observations.
- Count the number of distinct years of observation.
- Identify the oldest year of observation.
- Identify the newest year of observation.

## Viva Questions

1. What is Apache Spark?
2. What is PySpark?
3. What is a Spark DataFrame?
4. What is the purpose of `SparkSession`?
5. What does the `count()` function do?
6. Why is `distinct()` used in this experiment?
7. What is the difference between `count()` and `distinct().count()`?
8. What is the purpose of `min()`?
9. What is the purpose of `max()`?
10. What is the use of `inferSchema=True`?
11. What is the difference between an RDD and a DataFrame?
12. Why should the Spark session be stopped after completing the program?
