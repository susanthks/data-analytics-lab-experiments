# Experiment10: Linear Regression and Prediction in R

## Aim

Write an R program to perform **linear regression** and use the fitted regression model to make predictions.

---

## Objective

To understand how to:

- Create a dataset in R.
- Fit a simple linear regression model.
- Obtain the regression equation.
- Predict the dependent variable for new input values.
- Visualize the observed data and regression line.

---

## Software Required

- R
- RStudio (recommended)

---

## Theory

### What is Linear Regression?

Linear regression is a supervised learning/statistical technique used to model the relationship between a **dependent variable** and one or more **independent variables**.

For simple linear regression, the relationship is represented as:

$$
y = b_0 + b_1x
$$

where:

- $y$ = dependent variable
- $x$ = independent variable
- $b_0$ = intercept
- $b_1$ = slope/coefficient

The fitted model is commonly written as:

$$
\hat{y} = b_0 + b_1x
$$

Here, $\hat{y}$ represents the predicted value of the dependent variable.

### Example

Suppose we want to predict a student's **exam score** based on the number of **hours studied**.

- Independent variable ($x$): Hours Studied
- Dependent variable ($y$): Exam Score

The regression model learns the relationship between these two variables from the given observations.

---

## R Function Used

The main function used for linear regression in R is:

```r
lm()
```

Syntax:

```r
model <- lm(y ~ x, data = dataset)
```

The `~` symbol specifies the relationship between the dependent and independent variables.

To display the complete model summary:

```r
summary(model)
```

To make predictions:

```r
predict(model, newdata = data.frame(x = new_value))
```

---

## Algorithm

1. Start the program.
2. Create or load the dataset containing independent and dependent variables.
3. Store the data in an R data frame.
4. Fit a linear regression model using `lm()`.
5. Display the model summary.
6. Extract the intercept and slope of the regression equation.
7. Create new input values for which predictions are required.
8. Use `predict()` to calculate the predicted values.
9. Display the predictions.
10. Plot the original observations and fitted regression line.
11. Stop the program.

---

## R Program

```r
# Linear Regression and Prediction in R

# Step 1: Create the dataset
data <- data.frame(
  Hours_Studied = c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
  Exam_Score = c(35, 40, 45, 50, 55, 60, 65, 70, 75, 80)
)

# Step 2: Display the dataset
print(data)

# Step 3: Build the linear regression model
model <- lm(Exam_Score ~ Hours_Studied, data = data)

# Step 4: Display the model summary
print(summary(model))

# Step 5: Display the regression coefficients
print(coef(model))

# Step 6: Create new values for prediction
new_data <- data.frame(
  Hours_Studied = c(2.5, 5.5, 7.5, 11)
)

# Step 7: Make predictions
predictions <- predict(model, newdata = new_data)

# Step 8: Display prediction results
result <- data.frame(
  Hours_Studied = new_data$Hours_Studied,
  Predicted_Score = predictions
)

print(result)

# Step 9: Plot the original data
plot(
  data$Hours_Studied,
  data$Exam_Score,
  main = "Linear Regression: Hours Studied vs Exam Score",
  xlab = "Hours Studied",
  ylab = "Exam Score",
  pch = 19
)

# Step 10: Add regression line
abline(model, lwd = 2)
```

---

## Explanation of the Program

### 1. Creating the Dataset

```r
data <- data.frame(
  Hours_Studied = c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
  Exam_Score = c(35, 40, 45, 50, 55, 60, 65, 70, 75, 80)
)
```

A data frame is created with two columns:

- `Hours_Studied` — independent variable
- `Exam_Score` — dependent variable

---

### 2. Building the Regression Model

```r
model <- lm(Exam_Score ~ Hours_Studied, data = data)
```

The `lm()` function fits a linear regression model.

The expression:

```text
Exam_Score ~ Hours_Studied
```

means that we are predicting `Exam_Score` using `Hours_Studied`.

---

### 3. Viewing the Model Summary

```r
summary(model)
```

The summary provides important information such as:

- Regression coefficients
- Standard error
- t-value
- p-value
- Residual information
- R-squared value
- Adjusted R-squared value

---

### 4. Obtaining the Regression Equation

The coefficients can be obtained using:

```r
coef(model)
```

For this sample dataset, the fitted relationship is approximately:

$$
\hat{y} = 30 + 5x
$$

Therefore, if a student studies for 6 hours:

$$
\hat{y} = 30 + 5(6) = 60
$$

So the predicted exam score is approximately **60**.

---

### 5. Making Predictions

New values are stored in a data frame:

```r
new_data <- data.frame(
  Hours_Studied = c(2.5, 5.5, 7.5, 11)
)
```

Predictions are generated using:

```r
predictions <- predict(model, newdata = new_data)
```

The `predict()` function uses the fitted regression model to estimate the dependent variable for the supplied input values.

---

### 6. Visualizing the Regression Model

The original observations are plotted using:

```r
plot(
  data$Hours_Studied,
  data$Exam_Score
)
```

The regression line is added using:

```r
abline(model)
```

The graph helps us visually understand how well the linear model represents the observed data.

---

## Sample Output

### Dataset

```text
   Hours_Studied Exam_Score
1             1         35
2             2         40
3             3         45
4             4         50
5             5         55
6             6         60
7             7         65
8             8         70
9             9         75
10           10         80
```

### Regression Coefficients

```text
(Intercept)     30
Hours_Studied    5
```

Hence, the regression equation is:

$$
\hat{y} = 30 + 5x
$$

### Prediction Table

For the given new input values, the model predicts approximately:

```text
  Hours_Studied Predicted_Score
1          2.5            42.5
2          5.5            57.5
3          7.5            67.5
4         11.0            85.0
```

> **Note:** The prediction for 11 hours is an example of **extrapolation**, because the training data only contains values from 1 to 10 hours. Predictions outside the observed range should be interpreted carefully.

---

## Expected Graph

The graph should contain:

- Individual data points representing the observed values.
- A straight regression line passing through the data.
- X-axis: Hours Studied.
- Y-axis: Exam Score.

The points in this example lie exactly on a straight line, so the fitted regression line will pass through all observations.

---

## Important R Commands

| Command | Purpose |
|---|---|
| `data.frame()` | Creates a data frame |
| `lm()` | Fits a linear regression model |
| `summary()` | Displays detailed model information |
| `coef()` | Extracts model coefficients |
| `predict()` | Makes predictions using the model |
| `plot()` | Creates a scatter plot |
| `abline()` | Adds a regression line to a plot |

---

## Result

Thus, the R program for **linear regression and prediction** was successfully implemented. The linear regression model was fitted using `lm()`, and predictions for new input values were obtained using `predict()`.

---

## Viva Questions

1. What is linear regression?
2. What is the difference between dependent and independent variables?
3. What does the `lm()` function do in R?
4. What does the `~` symbol represent in an R regression formula?
5. What is the meaning of the intercept?
6. What is the meaning of the slope/coefficient?
7. What is the purpose of `summary(model)`?
8. Which R function is used to make predictions?
9. What is the difference between interpolation and extrapolation?
10. What does R-squared indicate in a regression model?
11. Why do we use a data frame for `newdata` with `predict()`?
12. What is the purpose of `abline(model)`?

---

## Exercise

Modify the program to:

1. Create a dataset containing **Years of Experience** and **Salary**.
2. Fit a linear regression model to predict salary from experience.
3. Predict the salary for employees having 2, 5, and 8 years of experience.
4. Plot the observations and regression line.
5. Display the regression equation and model summary.

