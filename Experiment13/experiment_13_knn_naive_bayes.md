# Experiment 13: KNN and Naive Bayes Classifier using R

## Aim

To implement **K-Nearest Neighbors (KNN)** and **Naive Bayes Classifier** using R and compare their classification results.

---

## Objectives

1. Understand the basic working of KNN classification.
2. Understand the working of a Naive Bayes classifier.
3. Implement both classifiers using R.
4. Predict the class of test data.
5. Evaluate the classification performance using a confusion matrix and accuracy.

---

## Software Requirements

- R
- RStudio (recommended)
- Required R packages:
  - `class` (for KNN)
  - `e1071` (for Naive Bayes)
  - `caret` (for data splitting and evaluation)

---

## Dataset

For this experiment, the built-in **Iris dataset** is used.

The Iris dataset contains measurements of iris flowers:

| Feature | Description |
|---|---|
| Sepal.Length | Sepal length |
| Sepal.Width | Sepal width |
| Petal.Length | Petal length |
| Petal.Width | Petal width |
| Species | Target class |

The target variable `Species` contains three classes: Setosa, Versicolor, and Virginica.

---

## Theory

### 1. K-Nearest Neighbors (KNN)

K-Nearest Neighbors is a non-parametric, instance-based supervised learning algorithm. It classifies a novel data point based on the majority vote of its **k nearest neighbors** in the feature space.

The distance between points is typically computed using the **Euclidean distance formula**:

$$d(p, q) = \sqrt{\sum_{i=1}^{n} (q_i - p_i)^2}$$

**Advantages:**
- Simple to understand and implement.
- No explicit training phase required ("lazy learner").
- Naturally handles multi-class classification problem variants.

---

### 2. Naive Bayes Classifier

The Naive Bayes classifier is a probabilistic machine learning model based on **Bayes' Theorem**. It is called *naive* because it assumes that all input features are completely independent of each other given the class variable.

The operational formula derived from Bayes' Theorem is:

$$P(C_k \vert{} x) = \frac{P(x \vert{} C_k) \cdot P(C_k)}{P(x)}$$

where:
- $P(C_k \vert{} x)$ = Posterior probability of class $C_k$ given predictors x.
- $P(x \vert{} C_k)$ = Likelihood of predictors given class.
- $P(C_k)$ = Prior probability of class.
- P(x) = Prior probability of predictor.

**Advantages:**
- Performs highly efficiently even with small data sizes.
- Extremely fast for both training and real-time predictions.
- Robust to irrelevant features.

---

## Procedure

1. Open RStudio.
2. Install and load the required packages (`class`, `e1071`, `caret`).
3. Load the Iris dataset.
4. Scale continuous features (highly recommended for numeric KNN stability).
5. Split the dataset into training and testing sets (80% training, 20% testing).
6. Train and execute predictions simultaneously using the KNN algorithm.
7. Generate the KNN confusion matrix and calculate performance metrics.
8. Train a Naive Bayes classifier on the training partition.
9. Predict the classes of the test data using the Naive Bayes model.
10. Calculate the confusion matrix and accuracy metrics for Naive Bayes.
11. Output a performance summary to compare classification results.

---

## R Program

### Step 1: Install and Load Packages

Run the following commands:

```r
install.packages("class")
install.packages("e1071")
install.packages("caret")
```

Load the packages:

```r
library(class)
library(e1071)
library(caret)
```

---

### Step 2: Load and Preprocess the Dataset

```r
data(iris)

# Normalize/Scale the numeric features for KNN stability
scaled_features <- scale(iris[, 1:4])
iris_scaled <- data.frame(scaled_features, Species = iris$Species)

head(iris_scaled)
```

---

### Step 3: Split the Dataset

Use 80% of the data for training and 20% for testing.

```r
set.seed(123)

index <- createDataPartition(iris_scaled$Species,
                              p = 0.80,
                              list = FALSE)

train_data <- iris_scaled[index, ]
test_data <- iris_scaled[-index, ]
```

---

# Part A: KNN Classifier

## Step 4: Run KNN Model & Predictions

Unlike other models, KNN combines training and prediction into a single execution step using the `knn()` function from the `class` package.

```r
# Separate predictors from target labels
train_x <- train_data[, 1:4]
test_x <- test_data[, 1:4]
train_y <- train_data$Species

# Run KNN classification (setting k = 3)
knn_pred <- knn(train = train_x, 
                test = test_x, 
                cl = train_y, 
                k = 3)

print(knn_pred)
```

---

## Step 5: Evaluate the KNN Model

```r
knn_cm <- confusionMatrix(knn_pred, test_data$Species)
print(knn_cm)

# Extract only the exact accuracy calculation
knn_accuracy <- knn_cm$overall["Accuracy"]
cat("KNN Accuracy:", round(knn_accuracy, 4), "
")
```

---

# Part B: Naive Bayes Classifier

## Step 6: Train the Naive Bayes Model

```r
nb_model <- naiveBayes(Species ~ ., data = train_data)
print(nb_model)
```

---

## Step 7: Make Predictions using Naive Bayes

```r
nb_pred <- predict(nb_model, test_data)
print(nb_pred)
```

---

## Step 8: Evaluate the Naive Bayes Model

```r
nb_cm <- confusionMatrix(nb_pred, test_data$Species)
print(nb_cm)

# Extract only the exact accuracy calculation
nb_accuracy <- nb_cm$overall["Accuracy"]
cat("Naive Bayes Accuracy:", round(nb_accuracy, 4), "
")
```

---

# Complete R Program

The following program can be executed as a single script.

```r
# Experiment 12
# KNN and Naive Bayes Classifier using R

# Install packages if required
# install.packages("class")
# install.packages("e1071")
# install.packages("caret")

library(class)
library(e1071)
library(caret)

# Load Iris dataset
data(iris)

# Normalize numeric properties for uniform scale tracking
scaled_features <- scale(iris[, 1:4])
iris_scaled <- data.frame(scaled_features, Species = iris$Species)

# Split dataset
set.seed(123)

index <- createDataPartition(
  iris_scaled$Species,
  p = 0.80,
  list = FALSE
)

train_data <- iris_scaled[index, ]
test_data <- iris_scaled[-index, ]

# -----------------------------
# KNN CLASSIFIER
# -----------------------------

train_x <- train_data[, 1:4]
test_x <- test_data[, 1:4]
train_y <- train_data$Species

# Train and Predict via KNN
knn_pred <- knn(train = train_x, 
                test = test_x, 
                cl = train_y, 
                k = 3)

# KNN confusion matrix
knn_cm <- confusionMatrix(knn_pred, test_data$Species)
print("--- KNN Confusion Matrix ---")
print(knn_cm)

# KNN accuracy
knn_accuracy <- knn_cm$overall["Accuracy"]


# -----------------------------
# NAIVE BAYES CLASSIFIER
# -----------------------------

# Train Naive Bayes
nb_model <- naiveBayes(Species ~ ., data = train_data)

# Naive Bayes prediction
nb_pred <- predict(nb_model, test_data)

# Naive Bayes confusion matrix
nb_cm <- confusionMatrix(nb_pred, test_data$Species)
print("--- Naive Bayes Confusion Matrix ---")
print(nb_cm)

# Naive Bayes accuracy
nb_accuracy <- nb_cm$overall["Accuracy"]


# -----------------------------
# COMPARISON
# -----------------------------

cat("\nModel Comparison\n")
cat("-------------------------\n")
cat("KNN Accuracy:         ", round(knn_accuracy, 4), "\n")
cat("Naive Bayes Accuracy: ", round(nb_accuracy, 4), "\n")
```

---

## Expected Output

```text
--- KNN Confusion Matrix ---
Confusion Matrix and Statistics
...

--- Naive Bayes Confusion Matrix ---
Confusion Matrix and Statistics
...

Model Comparison
-------------------------
KNN Accuracy:          0.xx
Naive Bayes Accuracy:  0.xx
```

---

## Comparison of KNN and Naive Bayes

| Feature | KNN | Naive Bayes |
|---|---|---|
| **Learning Type** | Instance-based (Lazy Learner) | Parametric (Eager Learner) |
| **Basic Strategy** | Proximity/Distance minimization | Probabilistic classification |
| **Assumptions** | Closer features mean closer labels | Independent input predictors |
| **Computation cost** | Expensive during inference steps | High training speed, low evaluation overhead |
| **Sensitivity to Scaling**| High (requires data standardization) | Minimal impact from range differences |

---

## Result

Thus, **KNN and Naive Bayes classifiers were successfully implemented using R** on the Iris dataset. The models were evaluated, test data was classified, confusion matrices were generated, and classification accuracy values were tracked and compared.

---

## Viva Questions

1. What is the fundamental difference between lazy learning and eager learning?
2. Why is data scaling/normalization critical before executing KNN?
3. How does selection of the parameter 'k' modify performance limits in KNN?
4. What happens if 'k' is given a value that matches the exact count of output classes?
5. Why is the Naive Bayes classifier explicitly designated as "naive"?
6. Explain Bayes' Theorem and its elements within classification problems.
7. How does Naive Bayes process a classification variable that is entirely missing from training subsets?
8. What is the operational distinction between data splitting components like training sets versus validation/testing sets?
9. How do you construct a Confusion Matrix, and how do you isolate model Accuracy?
10. Which model scales more reliably when dealing with highly expanded feature frameworks?

---

## Learning Outcome

After completing this experiment, students will be able to:

- Explain the mechanical processes defining KNN classification frameworks.
- Articulate probability rules underlying Naive Bayes structures.
- Format code structures implementing standardized KNN executions in R.
- Structure operations training Naive Bayes configurations.
- Parse complex prediction evaluations from Confusion Matrix outputs.
