# Experiment 10: Linear Regression and Prediction Using CSV Dataset

## Aim

To write an R program to read a sample dataset from a CSV file using `read.csv()`, perform multiple linear regression, analyze the regression model, and make predictions using the fitted model.

---

## Objective

The objectives of this experiment are to:

1. Read an external CSV dataset into R.
2. Understand the structure of a dataset.
3. Display and summarize the imported data.
4. Perform multiple linear regression using `lm()`.
5. Interpret regression coefficients.
6. Evaluate the regression model using `summary()`.
7. Make predictions for new observations using `predict()`.
8. Visualize the relationship between advertising expenditure and sales.

---

# Dataset Description

The dataset used in this experiment contains information about advertising expenditure and corresponding sales.

The uploaded CSV dataset contains **200 observations** and the following four variables:

| Variable | Description | Role |
|---|---|---|
| `TV` | Advertising expenditure through TV | Independent variable |
| `Radio` | Advertising expenditure through Radio | Independent variable |
| `Newspaper` | Advertising expenditure through Newspaper | Independent variable |
| `Sales` | Resulting sales | Dependent variable |

The first few records of the dataset are:

```text
     TV  Radio  Newspaper  Sales
1  230.1   37.8       69.2   22.1
2   44.5   39.3       45.1   10.4
3   17.2   45.9       69.3   12.0
4  151.5   41.3       58.5   16.5
5  180.8   10.8       58.4   17.9
6    8.7   48.9       75.0    7.2
```

These values are taken directly from the uploaded CSV file.

---

# Theory

## 1. What is Linear Regression?

Linear regression is a statistical technique used to study the relationship between a dependent variable and one or more independent variables.

It can be used for:

- Understanding relationships between variables
- Estimating the effect of independent variables
- Predicting future or unknown values

---

## 2. Simple Linear Regression

When there is only one independent variable, it is called **simple linear regression**.

The general equation is:

\[
Y = \beta_0 + \beta_1X
\]

where:

- `Y` = dependent variable
- `X` = independent variable
- `β₀` = intercept
- `β₁` = regression coefficient/slope

---

## 3. Multiple Linear Regression

When there are two or more independent variables, it is called **multiple linear regression**.

The general equation is:

\[
Y = \beta_0 + \beta_1X_1 + \beta_2X_2 + \beta_3X_3 + \cdots + \beta_nX_n
\]

For the current dataset:

\[
Sales = \beta_0 + \beta_1(TV) + \beta_2(Radio) + \beta_3(Newspaper)
\]

Here:

- `Sales` is the dependent variable.
- `TV` is the first independent variable.
- `Radio` is the second independent variable.
- `Newspaper` is the third independent variable.

---

# R Functions Used

| Function | Purpose |
|---|---|
| `read.csv()` | Reads a CSV file |
| `print()` | Displays data |
| `head()` | Displays first few records |
| `tail()` | Displays last few records |
| `str()` | Displays the structure of the dataset |
| `summary()` | Provides summary statistics/model summary |
| `lm()` | Creates a linear regression model |
| `coef()` | Extracts regression coefficients |
| `predict()` | Generates predictions |
| `plot()` | Creates a graph |
| `abline()` | Adds a regression line |
| `getwd()` | Displays the current working directory |

---

# Program

## Step 1: Read the CSV Dataset

Save the CSV file as:

```text
Advertising.csv
```

Then use:

```r
data <- read.csv("Advertising.csv")
```

The `read.csv()` function imports the CSV file into R as a data frame.

---

## Step 2: Display the Dataset

```r
print(data)
```

This displays all the observations in the R console.

---

## Step 3: Display the First Few Records

```r
head(data)
```

Expected output:

```text
     TV Radio Newspaper Sales
1 230.1  37.8      69.2  22.1
2  44.5  39.3      45.1  10.4
3  17.2  45.9      69.3  12.0
4 151.5  41.3      58.5  16.5
5 180.8  10.8      58.4  17.9
6   8.7  48.9      75.0   7.2
```

---

## Step 4: Display the Structure

```r
str(data)
```

This helps us understand:

- Number of observations
- Number of variables
- Variable names
- Data types

The dataset contains numerical variables for `TV`, `Radio`, `Newspaper`, and `Sales`.

---

## Step 5: Display Summary Statistics

```r
summary(data)
```

This provides:

- Minimum
- First quartile
- Median
- Mean
- Third quartile
- Maximum

for each numerical variable.

For the uploaded dataset, there are **200 observations**. The approximate ranges are:

| Variable | Minimum | Maximum | Mean |
|---|---:|---:|---:|
| TV | 0.7 | 296.4 | 147.04 |
| Radio | 0.0 | 49.6 | 23.26 |
| Newspaper | 0.3 | 114.0 | 30.55 |
| Sales | 1.6 | 27.0 | 15.13 |

---

# Step 6: Create the Multiple Linear Regression Model

```r
model <- lm(Sales ~ TV + Radio + Newspaper, data = data)
```

The `lm()` function is used to create a linear regression model.

The expression:

```text
Sales ~ TV + Radio + Newspaper
```

means:

> Predict `Sales` using `TV`, `Radio`, and `Newspaper`.

---

# Step 7: Display the Model Summary

```r
summary(model)
```

The model summary provides important information such as:

- Regression coefficients
- Standard errors
- t-values
- p-values
- Residual information
- R-squared
- Adjusted R-squared
- F-statistic

---

# Step 8: Display the Regression Coefficients

```r
coef(model)
```

For the uploaded dataset, the fitted model is approximately:

```text
(Intercept)     4.625124
TV              0.054446
Radio           0.107001
Newspaper       0.000336
```

Therefore, the regression equation is approximately:

\[
Sales = 4.6251 + 0.05445(TV) + 0.10700(Radio) + 0.00034(Newspaper)
\]

---

# Interpretation of the Regression Equation

## Intercept

The intercept is approximately:

```text
4.6251
```

This represents the predicted sales when the expenditure on TV, Radio, and Newspaper is zero.

---

## TV Coefficient

The coefficient of TV is approximately:

```text
0.05445
```

This means that, holding Radio and Newspaper expenditure constant, an increase of one unit in TV advertising expenditure is associated with an increase of approximately `0.05445` units in predicted sales.

---

## Radio Coefficient

The coefficient of Radio is approximately:

```text
0.10700
```

This means that, holding TV and Newspaper expenditure constant, an increase of one unit in Radio advertising expenditure is associated with an increase of approximately `0.10700` units in predicted sales.

---

## Newspaper Coefficient

The coefficient of Newspaper is approximately:

```text
0.00034
```

This indicates that the estimated contribution of Newspaper advertising to sales is very small in this fitted model after accounting for TV and Radio expenditure.

---

# Step 9: Check Model Performance

The coefficient of determination, `R²`, can be obtained using:

```r
summary(model)$r.squared
```

For this dataset:

```text
R-squared ≈ 0.9026
```

Therefore, approximately **90.26% of the variation in Sales is explained by the three advertising variables in this fitted model**.

This indicates a strong overall relationship between the predictors and sales for this dataset.

---

# Step 10: Create New Data for Prediction

Suppose we want to predict sales for three new advertising plans:

| TV | Radio | Newspaper |
|---:|---:|---:|
| 100 | 20 | 20 |
| 150 | 30 | 30 |
| 200 | 40 | 40 |

Create the new dataset in R:

```r
new_data <- data.frame(
  TV = c(100, 150, 200),
  Radio = c(20, 30, 40),
  Newspaper = c(20, 30, 40)
)
```

---

# Step 11: Make Predictions

```r
predictions <- predict(model, newdata = new_data)
```

The `predict()` function uses the trained regression model to estimate sales for the new observations.

---

# Step 12: Display Prediction Results

```r
result <- data.frame(
  new_data,
  Predicted_Sales = predictions
)

print(result)
```

The predicted values are approximately:

```text
   TV Radio Newspaper Predicted_Sales
1 100    20        20          12.216
2 150    30        30          16.012
3 200    40        40          19.808
```

Therefore:

| TV | Radio | Newspaper | Predicted Sales |
|---:|---:|---:|---:|
| 100 | 20 | 20 | 12.216 |
| 150 | 30 | 30 | 16.012 |
| 200 | 40 | 40 | 19.808 |

---

# Step 13: Visualize TV Advertising and Sales

Although the model uses three independent variables, we can visualize the relationship between one predictor and the dependent variable.

For example, TV advertising versus Sales:

```r
plot(
  data$TV,
  data$Sales,
  main = "TV Advertising vs Sales",
  xlab = "TV Advertising",
  ylab = "Sales",
  pch = 19
)
```

---

# Step 14: Add a Regression Line

For visualization of the direct relationship between TV and Sales, create a simple regression model:

```r
simple_model <- lm(Sales ~ TV, data = data)
```

Then add the regression line:

```r
abline(simple_model, lwd = 2)
```

Complete visualization:

```r
plot(
  data$TV,
  data$Sales,
  main = "TV Advertising vs Sales",
  xlab = "TV Advertising",
  ylab = "Sales",
  pch = 19
)

simple_model <- lm(Sales ~ TV, data = data)

abline(simple_model, lwd = 2)
```

---

# Complete R Program

The complete program is given below.

```r
# Experiment 10
# Multiple Linear Regression and Prediction
# Using a CSV Dataset

# Step 1: Read the CSV file
data <- read.csv("Advertising.csv")

# Step 2: Display the dataset
print(data)

# Step 3: Display the first few records
head(data)

# Step 4: Display the structure of the dataset
str(data)

# Step 5: Display summary statistics
summary(data)

# Step 6: Build the multiple linear regression model
model <- lm(
  Sales ~ TV + Radio + Newspaper,
  data = data
)

# Step 7: Display the model summary
summary(model)

# Step 8: Display regression coefficients
print(coef(model))

# Step 9: Display R-squared value
print(summary(model)$r.squared)

# Step 10: Create new data for prediction
new_data <- data.frame(
  TV = c(100, 150, 200),
  Radio = c(20, 30, 40),
  Newspaper = c(20, 30, 40)
)

# Step 11: Make predictions
predictions <- predict(
  model,
  newdata = new_data
)

# Step 12: Display prediction results
result <- data.frame(
  new_data,
  Predicted_Sales = predictions
)

print(result)

# Step 13: Plot TV advertising vs Sales
plot(
  data$TV,
  data$Sales,
  main = "TV Advertising vs Sales",
  xlab = "TV Advertising",
  ylab = "Sales",
  pch = 19
)

# Step 14: Add a simple regression line
simple_model <- lm(Sales ~ TV, data = data)

abline(
  simple_model,
  lwd = 2
)
```

---

# Important: Working Directory

The CSV file must be available in the R working directory if only the filename is provided.

Check the current working directory using:

```r
getwd()
```

For example:

```text
[1] "C:/Users/Student/Documents/R_Lab"
```

Place:

```text
Advertising.csv
```

inside that folder.

You can also specify the complete path:

```r
data <- read.csv("C:/Users/Student/Documents/R_Lab/Advertising.csv")
```

On Linux:

```r
data <- read.csv("/home/student/R_Lab/Advertising.csv")
```

---

# Understanding the Complete Workflow

The experiment follows the following data analytics workflow:

```text
             CSV Dataset
                  |
                  v
             read.csv()
                  |
                  v
             Data Frame
                  |
          +-------+-------+
          |       |       |
          v       v       v
        head()  str()  summary()
                  |
                  v
             lm() Model
                  |
                  v
           Model Evaluation
                  |
                  v
             predict()
                  |
                  v
          Predicted Sales
                  |
                  v
          Visualization
```

---

# Result

The CSV dataset was successfully imported into R using `read.csv()`.

A multiple linear regression model was developed using:

```text
TV
Radio
Newspaper
```

to predict:

```text
Sales
```

The fitted model was approximately:

\[
Sales = 4.6251 + 0.05445(TV) + 0.10700(Radio) + 0.00034(Newspaper)
\]

The model achieved an R² value of approximately:

\[
R^2 = 0.9026
\]

Predictions were successfully generated for new advertising expenditure values using the `predict()` function.

---

# Viva Questions

## 1. What is a CSV file?

CSV stands for **Comma-Separated Values**. It is a text-based format used to store tabular data.

## 2. Which function is used to read a CSV file in R?

```r
read.csv()
```

## 3. What does `read.csv()` return?

It normally returns the CSV data as a **data frame**.

## 4. What is the purpose of `head()`?

It displays the first few observations of a dataset.

## 5. What is the purpose of `str()`?

It displays the structure and data types of the dataset.

## 6. What is multiple linear regression?

It is a regression technique involving one dependent variable and two or more independent variables.

## 7. Which R function is used to create a linear regression model?

```r
lm()
```

## 8. What does this expression mean?

```r
Sales ~ TV + Radio + Newspaper
```

It means that `Sales` is predicted using `TV`, `Radio`, and `Newspaper`.

## 9. Which function is used to make predictions?

```r
predict()
```

## 10. What is R²?

R², or the coefficient of determination, indicates the proportion of variation in the dependent variable explained by the regression model.

## 11. What is the approximate R² value obtained in this experiment?

Approximately:

```text
0.9026
```

or:

```text
90.26%
```

## 12. What is the dependent variable in this experiment?

```text
Sales
```

## 13. What are the independent variables?

```text
TV
Radio
Newspaper
```

## 14. Why do we use `newdata` in `predict()`?

`newdata` provides new values of the independent variables for which predictions are required.

## 15. What is the purpose of `abline()`?

It is used to add a straight line, such as a regression line, to an existing plot.

---

# Exercises for Students

### Exercise 1

Modify the program to predict sales for:

```text
TV = 120
Radio = 25
Newspaper = 30
```

### Exercise 2

Predict sales for:

```text
TV = 250
Radio = 45
Newspaper = 50
```

### Exercise 3

Create a scatter plot of:

```text
Radio vs Sales
```

### Exercise 4

Create a scatter plot of:

```text
Newspaper vs Sales
```

### Exercise 5

Find the R² value of a simple regression model:

```r
lm(Sales ~ TV, data = data)
```

and compare it with the multiple regression model.

### Exercise 6

Use `cor()` to calculate the correlation between the variables:

```r
cor(data)
```

---

# Files Required

The experiment requires the following files:

```text
Experiment10/
│
├── manual.md.md
│
├── Advertising.csv
│
└── program.R
```

The `Advertising.csv` file should contain the exact dataset supplied for this experiment.

---

# Learning Outcomes

After completing this experiment, students will be able to:

- Import external datasets into R.
- Work with CSV files.
- Understand data frames.
- Inspect and summarize datasets.
- Build simple and multiple linear regression models.
- Interpret regression coefficients.
- Evaluate a regression model using R².
- Generate predictions using `predict()`.
- Create basic regression visualizations.
- Understand a basic real-world data analytics workflow.
