# EXPERIMENT 9 – CALCULATING VARIANCE, COVARIANCE AND CORRELATION USING R

## AIM

To write an R program to calculate the **variance, covariance, and correlation** of numerical attributes.

---

## THEORY

### 1. Variance

Variance measures how much the values of a variable are spread around its mean.

- A **small variance** indicates that the values are close to the mean.
- A **large variance** indicates that the values are more widely spread.

In R, variance is calculated using:

```r
var(x)
```

### 2. Covariance

Covariance measures the direction in which two variables change together.

- **Positive covariance:** both variables tend to increase together.
- **Negative covariance:** one variable tends to increase when the other decreases.
- **Covariance close to zero:** there may be little linear relationship.

In R:

```r
cov(x, y)
```

### 3. Correlation

Correlation measures the **strength and direction of the linear relationship** between two variables.

The correlation coefficient ranges from **-1 to +1**.

In R:

```r
cor(x, y)
```

### Correlation Interpretation

| Correlation Value | Interpretation |
|---:|---|
| +1 | Perfect positive correlation |
| +0.7 to +0.99 | Strong positive correlation |
| +0.3 to +0.69 | Moderate positive correlation |
| 0 to +0.29 | Weak positive correlation |
| 0 | No linear correlation |
| -0.29 to 0 | Weak negative correlation |
| -0.69 to -0.3 | Moderate negative correlation |
| -0.99 to -0.7 | Strong negative correlation |
| -1 | Perfect negative correlation |

> **Note:** Correlation indicates association, but correlation alone does not necessarily imply causation.

---

# ALGORITHM

1. Start R or RStudio.
2. Enter the numerical data.
3. Store the values in R vectors.
4. Calculate the variance of each variable using `var()`.
5. Calculate covariance using `cov()`.
6. Calculate correlation using `cor()`.
7. Display the calculated values.
8. Interpret the results.
9. Stop.

---

# PROCEDURE

### Step 1: Open RStudio

Open **RStudio** and create a new R script.

### Step 2: Enter the Dataset

Use the following sample data:

| Study Hours | Marks |
|---:|---:|
| 2 | 50 |
| 3 | 60 |
| 4 | 70 |
| 5 | 80 |
| 6 | 90 |

Enter the data in R:

```r
hours <- c(2, 3, 4, 5, 6)
marks <- c(50, 60, 70, 80, 90)
```

### Step 3: Calculate Variance

```r
var(hours)
var(marks)
```

### Step 4: Calculate Covariance

```r
cov(hours, marks)
```

### Step 5: Calculate Correlation

```r
cor(hours, marks)
```

### Step 6: Verify the Results

Observe the values displayed in the R console and interpret the relationship between study hours and marks.

---

# PROGRAM / SOURCE CODE

```r
# Experiment 9
# Variance, Covariance and Correlation

# Data
hours <- c(2, 3, 4, 5, 6)
marks <- c(50, 60, 70, 80, 90)

# Variance
variance_hours <- var(hours)
variance_marks <- var(marks)

# Covariance
covariance <- cov(hours, marks)

# Correlation
correlation <- cor(hours, marks)

# Display results
cat("Variance of Study Hours =", variance_hours, "\n")
cat("Variance of Marks =", variance_marks, "\n")
cat("Covariance =", covariance, "\n")
cat("Correlation =", correlation, "\n")
```

---

# OUTPUT

Expected output:

```text
Variance of Study Hours = 2.5
Variance of Marks = 250
Covariance = 12.5
Correlation = 1
```

---

# RESULT ANALYSIS

The calculated values are:

| Measure | Variable / Pair | Value |
|---|---|---:|
| Variance | Study Hours | 2.5 |
| Variance | Marks | 250 |
| Covariance | Study Hours and Marks | 12.5 |
| Correlation | Study Hours and Marks | 1 |

### Interpretation

- The variance of study hours is **2.5**, indicating the spread of study hours around their mean.
- The variance of marks is **250**, indicating the spread of marks around their mean.
- The covariance is **12.5**, which is positive. Therefore, study hours and marks tend to increase together.
- The correlation is **1**, indicating a **perfect positive linear relationship** in this sample dataset.

---

# CORRELATION MATRIX

A correlation matrix can be used when more than two numerical variables are available.

Example:

```r
data <- data.frame(
  StudyHours = c(2, 3, 4, 5, 6),
  Attendance = c(70, 75, 80, 85, 90),
  Marks = c(50, 60, 70, 80, 90)
)

cor(data)
```

The output will contain the correlation coefficient between every pair of variables.

---

# VISUALIZATION

A scatter plot can be used to visualize the relationship between study hours and marks.

```r
plot(
  hours,
  marks,
  main = "Study Hours vs Marks",
  xlab = "Study Hours",
  ylab = "Marks",
  pch = 19
)
```

### Expected Observation

The points will form an increasing straight-line pattern because the sample data has a perfect positive correlation.

---

# RESULT

The R program was successfully executed to calculate the **variance, covariance, and correlation** of numerical data.

---

# CONCLUSION

Variance describes the spread of an individual variable, covariance describes the direction in which two variables change together, and correlation describes the strength and direction of their linear relationship. R provides simple built-in functions such as `var()`, `cov()`, and `cor()` for performing these calculations efficiently.

---

# IMPORTANT R FUNCTIONS

| Function | Purpose | Example |
|---|---|---|
| `var()` | Calculates variance | `var(hours)` |
| `cov()` | Calculates covariance | `cov(hours, marks)` |
| `cor()` | Calculates correlation | `cor(hours, marks)` |
| `data.frame()` | Creates a data frame | `data.frame(hours, marks)` |
| `plot()` | Creates a plot | `plot(hours, marks)` |
| `cat()` | Displays formatted output | `cat("Result =", x)` |

---

# COMMON ERRORS

### Error 1: Different vector lengths

Incorrect:

```r
hours <- c(2, 3, 4, 5)
marks <- c(50, 60, 70)
```

The two variables should normally contain the same number of observations when calculating covariance or correlation.

### Error 2: Using non-numerical data

Functions such as `var()`, `cov()`, and `cor()` require suitable numerical data.

### Error 3: Missing values

If the dataset contains missing values, specify an appropriate missing-value handling method when required.

Example:

```r
cor(x, y, use = "complete.obs")
```

---

# VIVA QUESTIONS

1. What is variance?
2. What is the purpose of `var()` in R?
3. What is covariance?
4. What does a positive covariance indicate?
5. What does a negative covariance indicate?
6. What is correlation?
7. What is the range of a correlation coefficient?
8. What does a correlation of `+1` indicate?
9. What does a correlation of `-1` indicate?
10. What is the difference between covariance and correlation?
11. Does correlation imply causation? Explain.
12. Which R function is used to calculate a correlation matrix?

---

# LABORATORY EXERCISES

### Exercise 1

Create two vectors representing:

- Number of study hours
- Examination marks

Calculate their:

- Variance
- Covariance
- Correlation

### Exercise 2

Create two vectors representing:

- Temperature
- Electricity consumption

Calculate the covariance and correlation.

### Exercise 3

Create a data frame containing:

- Study Hours
- Attendance
- Marks

Generate the correlation matrix using `cor()`.

### Exercise 4

Create a scatter plot showing the relationship between two numerical variables.

### Exercise 5

Use your own dataset and identify:

1. The variable with the highest variance.
2. A pair of variables with positive correlation.
3. A pair of variables with negative correlation, if available.

---

# QUICK REFERENCE

```r
# Variance
var(x)

# Covariance
cov(x, y)

# Correlation
cor(x, y)

# Correlation Matrix
cor(data)

# Scatter Plot
plot(x, y)
```

---

# LEARNING OUTCOMES

After completing this experiment, students should be able to:

- Understand the concept of variance.
- Calculate variance using R.
- Understand covariance between two variables.
- Calculate covariance using R.
- Understand the strength and direction of correlation.
- Calculate correlation using R.
- Generate and interpret a correlation matrix.
- Visualize relationships between numerical variables using scatter plots.
- Interpret statistical results in a simple data-analysis context.

---

