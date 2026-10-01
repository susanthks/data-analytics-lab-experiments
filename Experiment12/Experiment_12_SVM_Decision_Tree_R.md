# Experiment 12: SVM and Decision Tree Classifier using R

## Aim

To implement **Support Vector Machine (SVM)** and **Decision Tree Classifier** using R and compare their classification results.

---

## Objectives

1. Understand the basic working of SVM classification.
2. Understand the working of a Decision Tree classifier.
3. Implement both classifiers using R.
4. Predict the class of test data.
5. Evaluate the classification performance using a confusion matrix and accuracy.

---

## Software Requirements

- R
- RStudio (recommended)
- Required R packages:
  - `e1071`
  - `rpart`
  - `rpart.plot`
  - `caret`

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

The target variable `Species` contains three classes:

- Setosa
- Versicolor
- Virginica

---

## Theory

### 1. Support Vector Machine (SVM)

Support Vector Machine is a supervised machine learning algorithm used mainly for classification and regression.

For classification, SVM finds an optimal **hyperplane** that separates different classes. The data points closest to the separating boundary are called **support vectors**.

For a linear classifier, the decision boundary can be represented as:

`w.x + b = 0`

where:

- `w` = weight vector
- `x` = input feature vector
- `b` = bias

SVM tries to maximize the margin between different classes.

**Advantages:**

- Works well with high-dimensional data.
- Effective when there is a clear separation between classes.
- Can use different kernels for non-linear classification.

---

### 2. Decision Tree

A Decision Tree is a supervised learning algorithm that classifies data by applying a sequence of decision rules.

Each internal node represents a condition on a feature, each branch represents an outcome of the condition, and each leaf represents the predicted class.

Example:

```text
              Petal.Length < 2.5?
                 /          \
               Yes           No
                |             |
             Setosa       Other class
```

Common criteria used for splitting include:

- Gini Index
- Entropy / Information Gain

**Advantages:**

- Easy to understand and interpret.
- Can be visualized as a tree.
- Requires little data preprocessing.

---

## Procedure

1. Open RStudio.
2. Install the required packages.
3. Load the Iris dataset.
4. Split the dataset into training and testing sets.
5. Train an SVM classifier.
6. Predict the classes of the test data.
7. Calculate the confusion matrix and accuracy.
8. Train a Decision Tree classifier.
9. Predict the classes of the test data.
10. Calculate the confusion matrix and accuracy.
11. Display the Decision Tree.
12. Compare the classification results.

---

## R Program

### Step 1: Install and Load Packages

Run the following commands:

```r
install.packages("e1071")
install.packages("rpart")
install.packages("rpart.plot")
install.packages("caret")
```

Load the packages:

```r
library(e1071)
library(rpart)
library(rpart.plot)
library(caret)
```

> **Note:** Package installation is required only once. If the packages are already installed, the `install.packages()` commands can be skipped.

---

### Step 2: Load the Dataset

```r
data(iris)

head(iris)
str(iris)
summary(iris)
```

---

### Step 3: Split the Dataset

Use 80% of the data for training and 20% for testing.

```r
set.seed(123)

index <- createDataPartition(iris$Species,
                              p = 0.80,
                              list = FALSE)

train_data <- iris[index, ]
test_data <- iris[-index, ]

dim(train_data)
dim(test_data)
```

---

# Part A: SVM Classifier

## Step 4: Train the SVM Model

```r
svm_model <- svm(
  Species ~ Sepal.Length + Sepal.Width +
    Petal.Length + Petal.Width,
  data = train_data,
  kernel = "linear"
)

print(svm_model)
```

---

## Step 5: Make Predictions using SVM

```r
svm_pred <- predict(svm_model, test_data)

print(svm_pred)
```

---

## Step 6: Evaluate the SVM Model

```r
svm_cm <- confusionMatrix(svm_pred, test_data$Species)

print(svm_cm)
```

Display only the accuracy:

```r
svm_accuracy <- svm_cm$overall["Accuracy"]

print(svm_accuracy)
```

---

# Part B: Decision Tree Classifier

## Step 7: Train the Decision Tree

```r
tree_model <- rpart(
  Species ~ Sepal.Length + Sepal.Width +
    Petal.Length + Petal.Width,
  data = train_data,
  method = "class"
)

print(tree_model)
```

---

## Step 8: Display the Decision Tree

```r
rpart.plot(tree_model,
           type = 3,
           extra = 104,
           fallen.leaves = TRUE)
```

The resulting tree shows the feature-based decisions used to classify the Iris flowers.

genui{"learning_viz":{"type_id":"DECISION_TREE_CLASSIFICATION_PATH","initial_values":{"x1":5.5,"x2":3.5}}}

---

## Step 9: Make Predictions using Decision Tree

```r
tree_pred <- predict(tree_model,
                     test_data,
                     type = "class")

print(tree_pred)
```

---

## Step 10: Evaluate the Decision Tree

```r
tree_cm <- confusionMatrix(tree_pred, test_data$Species)

print(tree_cm)
```

Display only the accuracy:

```r
tree_accuracy <- tree_cm$overall["Accuracy"]

print(tree_accuracy)
```

---

# Complete R Program

The following program can be executed as a single script.

```r
# Experiment 12
# SVM and Decision Tree Classifier using R

# Install packages if required
# install.packages("e1071")
# install.packages("rpart")
# install.packages("rpart.plot")
# install.packages("caret")

library(e1071)
library(rpart)
library(rpart.plot)
library(caret)

# Load Iris dataset
data(iris)

# Split dataset
set.seed(123)

index <- createDataPartition(
  iris$Species,
  p = 0.80,
  list = FALSE
)

train_data <- iris[index, ]
test_data <- iris[-index, ]

# -----------------------------
# SVM CLASSIFIER
# -----------------------------

svm_model <- svm(
  Species ~ Sepal.Length + Sepal.Width +
    Petal.Length + Petal.Width,
  data = train_data,
  kernel = "linear"
)

print(svm_model)

# SVM prediction
svm_pred <- predict(svm_model, test_data)

# SVM confusion matrix
svm_cm <- confusionMatrix(
  svm_pred,
  test_data$Species
)

print(svm_cm)

# SVM accuracy
svm_accuracy <- svm_cm$overall["Accuracy"]

cat("SVM Accuracy:",
    round(svm_accuracy, 4), "\n")


# -----------------------------
# DECISION TREE CLASSIFIER
# -----------------------------

tree_model <- rpart(
  Species ~ Sepal.Length + Sepal.Width +
    Petal.Length + Petal.Width,
  data = train_data,
  method = "class"
)

print(tree_model)

# Display decision tree
rpart.plot(
  tree_model,
  type = 3,
  extra = 104,
  fallen.leaves = TRUE
)

# Decision Tree prediction
tree_pred <- predict(
  tree_model,
  test_data,
  type = "class"
)

# Decision Tree confusion matrix
tree_cm <- confusionMatrix(
  tree_pred,
  test_data$Species
)

print(tree_cm)

# Decision Tree accuracy
tree_accuracy <- tree_cm$overall["Accuracy"]

cat("Decision Tree Accuracy:",
    round(tree_accuracy, 4), "\n")


# -----------------------------
# COMPARISON
# -----------------------------

cat("\nModel Comparison\n")
cat("-------------------------\n")
cat("SVM Accuracy: ",
    round(svm_accuracy, 4), "\n")

cat("Decision Tree Accuracy: ",
    round(tree_accuracy, 4), "\n")
```

---

## Expected Output

The program displays:

1. Structure and summary of the Iris dataset.
2. SVM model information.
3. SVM confusion matrix.
4. SVM classification accuracy.
5. Decision Tree model information.
6. Decision Tree visualization.
7. Decision Tree confusion matrix.
8. Decision Tree classification accuracy.

A typical output format is:

```text
SVM Accuracy: 0.xx

Decision Tree Accuracy: 0.xx

Model Comparison
-------------------------
SVM Accuracy:       0.xx
Decision Tree Accuracy: 0.xx
```

> The exact accuracy can vary depending on the training/testing split and model settings.

---

## Sample Confusion Matrix Format

The confusion matrix shows the number of correctly and incorrectly classified samples.

```text
             Prediction
Reference     Setosa  Versicolor  Virginica

Setosa          xx        0          0
Versicolor       0       xx          x
Virginica        0        x         xx
```

The diagonal values represent correctly classified samples.

---

## Comparison of SVM and Decision Tree

| Feature | SVM | Decision Tree |
|---|---|---|
| Learning type | Supervised | Supervised |
| Main use | Classification / Regression | Classification / Regression |
| Decision mechanism | Hyperplane / kernel | Feature-based rules |
| Interpretability | Moderate | High |
| Visualization | Less intuitive | Easy to visualize |
| Data preprocessing | May benefit from scaling | Usually less sensitive |
| Non-linear classification | Kernel functions | Tree-based splits |

---

## Result

Thus, **SVM and Decision Tree classifiers were successfully implemented using R** on the Iris dataset. The models were trained, test data was classified, confusion matrices were generated, and classification accuracy was calculated.

---

## Viva Questions

1. What is supervised learning?
2. What is SVM?
3. What is a hyperplane in SVM?
4. What are support vectors?
5. What is the purpose of a kernel in SVM?
6. What is a Decision Tree?
7. What is a root node?
8. What is a leaf node?
9. What is Gini Index?
10. What is entropy?
11. What is a confusion matrix?
12. How is classification accuracy calculated?
13. What is the difference between SVM and Decision Tree?
14. Why is the dataset divided into training and testing data?
15. Why is `set.seed()` used in the R program?

---

## Learning Outcome

After completing this experiment, students will be able to:

- Explain the basic concept of SVM classification.
- Explain the structure of a Decision Tree.
- Implement SVM using R.
- Implement Decision Tree classification using R.
- Generate predictions for test data.
- Evaluate classification models using a confusion matrix and accuracy.
