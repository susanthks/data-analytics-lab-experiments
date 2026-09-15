# EXPERIMENT 11
# LOGISTIC REGRESSION USING R

## 1. AIM

To write an R program to implement **Logistic Regression** for classification using the given `creditcard.csv` dataset.

## 2. REQUIREMENTS

- R / RStudio
- `creditcard.csv` dataset
- Basic knowledge of R programming

## 3. THEORY

**Logistic Regression** is a supervised machine-learning technique used for predicting a **categorical outcome**.

It estimates the probability of an observation belonging to a class using the logistic (sigmoid) function:

**P(Y = 1) = 1 / (1 + e^(-z))**

where,

**z = β₀ + β₁X₁ + β₂X₂ + ... + βₙXₙ**

For this experiment:
- **Target:** `Class`
- **Predictors:** `V1`, `V2`, and `Amount`
- `Class = 0` → Non-fraud
- `Class = 1` → Fraud

A probability of **0.5 or above** is classified as Class 1; otherwise, it is classified as Class 0.

**Basic workflow:**

`Dataset → Preprocessing → Train/Test Split → Logistic Model → Prediction → Confusion Matrix → Accuracy`

## 4. ALGORITHM

1. Load the `creditcard.csv` dataset.
2. Convert `Class` into a factor.
3. Divide the dataset into training and testing sets.
4. Build a logistic regression model using `V1`, `V2`, and `Amount`.
5. Predict class probabilities for the test data.
6. Convert probabilities into predicted classes using a 0.5 threshold.
7. Generate the confusion matrix.
8. Calculate classification accuracy.

## 5. PROCEDURE

1. Place `creditcard.csv` in the R working directory.
2. Open R/RStudio and run the following program.
3. Load the dataset and convert the target variable into a factor.
4. Split the data into 80% training and 20% testing data.
5. Apply `glm()` with `family = binomial`.
6. Predict the test-set probabilities.
7. Convert probabilities into class labels.
8. Display the confusion matrix and accuracy.

## 6. PROGRAM / SOURCE CODE

```r
# Logistic Regression using R

# Load dataset
data <- read.csv("creditcard.csv")

# Convert target variable to factor
data$Class <- factor(data$Class)

# Split data into training and testing sets
set.seed(123)
index <- sample(1:nrow(data), 0.8 * nrow(data))

train <- data[index, ]
test  <- data[-index, ]

# Build logistic regression model
model <- glm(
  Class ~ V1 + V2 + Amount,
  data = train,
  family = binomial
)

# Display model summary
summary(model)

# Predict probabilities
prob <- predict(model, test, type = "response")

# Convert probabilities into classes
pred <- ifelse(prob >= 0.5, 1, 0)

# Confusion matrix
cm <- table(
  Actual = test$Class,
  Predicted = pred
)

print(cm)

# Calculate accuracy
accuracy <- mean(
  pred == as.numeric(as.character(test$Class))
)

cat("Accuracy =", accuracy)
```

## 7. OUTPUT

The program displays:

1. **Logistic regression model summary**
2. **Confusion matrix**

Example format:

```text
             Predicted
Actual          0     1
    0        ...   ...
    1        ...   ...

Accuracy = ...
```

> **Note:** Exact output and accuracy may vary depending on the data split and R environment.

## 8. RESULT

Thus, the R program for implementing **Logistic Regression** was successfully executed using the given `creditcard.csv` dataset, and the predicted classes, confusion matrix, and classification accuracy were obtained.

## 9. VIVA QUESTIONS

1. What is Logistic Regression?
2. Why is Logistic Regression used for classification?
3. What is the sigmoid function?
4. What is the purpose of `glm()` in R?
5. Why is `family = binomial` used?
6. What is a confusion matrix?
7. What is the role of the 0.5 threshold?
8. What is the difference between training and testing data?

## 10. QUICK REFERENCE

| R Function | Purpose |
|---|---|
| `read.csv()` | Load CSV data |
| `factor()` | Convert variable to categorical |
| `sample()` | Select training observations |
| `glm()` | Build logistic regression model |
| `predict()` | Generate predictions |
| `table()` | Create confusion matrix |
| `mean()` | Calculate accuracy |


