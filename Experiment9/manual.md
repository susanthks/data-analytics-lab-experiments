# Experiment 9: Variance, Covariance and Correlation Using R

## Aim

Write an **R program to calculate variance, covariance, and correlation between different types of attributes**.

---

## Objectives

After completing this experiment, students will be able to:

- Understand variance as a measure of data dispersion.
- Calculate the variance of an attribute using R.
- Understand covariance between two attributes.
- Calculate covariance using R.
- Understand correlation between two numerical attributes.
- Calculate Pearson correlation using R.
- Interpret positive, negative, and zero correlation.
- Use built-in statistical functions in R.
- Analyze relationships between attributes in a dataset.

---

## Software Requirements

- R
- RStudio (recommended)
- Windows / Linux / macOS

### Verify R Installation

Open the R console or terminal and execute:

```r
R --version
```

---

# 1. Introduction

Statistical measures are essential in **Data Analytics** because they help us understand the characteristics and relationships within a dataset.

In this experiment, three important statistical measures are studied:

1. **Variance**
2. **Covariance**
3. **Correlation**

These measures are useful for understanding:

- How much an attribute varies.
- Whether two attributes vary together.
- The strength and direction of the relationship between two attributes.

For example, consider a dataset containing:

- Hours studied
- Marks obtained
- Attendance percentage

We can use variance to understand the spread of marks and correlation to determine whether study hours and marks are related.

---

# 2. Variance

## 2.1 Definition

**Variance** measures how far the values in a dataset are spread from their mean.

A small variance indicates that the values are close to the mean.

A large variance indicates that the values are widely distributed around the mean.

For a sample:

\[
s^2 = \frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}
\]

where:

- \(x_i\) = individual observation
- \(\bar{x}\) = sample mean
- \(n\) = number of observations
- \(s^2\) = sample variance





---

## 2.2 Example

Consider the following marks:

```text
60, 70, 80, 90, 100
```

The mean is:

```text
80
```

The values are distributed around the mean.

Variance quantifies this dispersion.

---

## 2.3 Variance in R

R provides the built-in `var()` function.

### Syntax

```r
var(x)
```

where `x` is a numeric vector.

### Example

```r
marks <- c(60, 70, 80, 90, 100)

variance <- var(marks)

print(variance)
```

### Expected Output

```text
[1] 250
```

---

# 3. Covariance

## 3.1 Definition

**Covariance** measures the direction in which two variables change together.

If two variables tend to increase together, their covariance is positive.

If one variable tends to increase while the other decreases, their covariance is negative.

A covariance close to zero indicates little linear co-movement.

For sample data:

\[
Cov(X,Y)=
\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{n-1}
\]

---

## 3.2 Interpretation of Covariance

| Covariance | General Interpretation |
|---|---|
| Positive | Variables tend to increase together |
| Negative | One variable tends to increase when the other decreases |
| Approximately zero | Little linear co-movement |

**Important:** The magnitude of covariance depends on the units of the variables, so covariance values from differently scaled variables are not directly comparable.

---

## 3.3 Covariance in R

R provides the `cov()` function.

### Syntax

```r
cov(x, y)
```

### Example

```r
hours <- c(2, 3, 4, 5, 6)
marks <- c(50, 60, 70, 80, 90)

covariance <- cov(hours, marks)

print(covariance)
```

### Expected Output

```text
[1] 12.5
```

The positive covariance indicates that the two attributes tend to increase together.

---

# 4. Correlation

## 4.1 Definition

**Correlation** measures the **strength and direction of a linear relationship** between two numerical variables.

The Pearson correlation coefficient is represented by:

\[
r =
\frac{Cov(X,Y)}
{\sqrt{Var(X)Var(Y)}}
\]

The correlation coefficient lies between:

\[
-1 \leq r \leq 1
\]

---

## 4.2 Interpretation

| Correlation | Interpretation |
|---:|---|
| +1 | Perfect positive linear correlation |
| +0.7 to +1 | Strong positive correlation |
| +0.3 to +0.7 | Moderate positive correlation |
| Around 0 | Little/no linear correlation |
| -0.3 to -0.7 | Moderate negative correlation |
| -0.7 to -1 | Strong negative correlation |
| -1 | Perfect negative linear correlation |

These ranges are only general guidelines; interpretation depends on the context.

---

## 4.3 Correlation in R

R provides the `cor()` function.

### Syntax

```r
cor(x, y)
```

### Example

```r
hours <- c(2, 3, 4, 5, 6)
marks <- c(50, 60, 70, 80, 90)

correlation <- cor(hours, marks)

print(correlation)
```

### Expected Output

```text
[1] 1
```

This indicates a perfect positive linear relationship in this illustrative dataset.

---

# 5. Difference Between Variance, Covariance and Correlation

| Measure | Purpose | Number of Variables | Range |
|---|---|---:|---:|
| Variance | Measures spread of one variable | 1 | 0 to infinity |
| Covariance | Measures direction of joint variation | 2 | No fixed range |
| Correlation | Measures strength and direction of linear relationship | 2 | -1 to +1 |

### Easy way to remember

```text
Variance
   ↓
Spread of ONE attribute

Covariance
   ↓
Direction of relationship between TWO attributes

Correlation
   ↓
Strength + direction of linear relationship between TWO attributes
```

---

# 6. R Program – Calculate Variance

```r
# Experiment 9
# Calculate variance of an attribute

marks <- c(60, 70, 80, 90, 100)

variance <- var(marks)

cat("Variance of marks =", variance, "\n")
```

### Output

```text
Variance of marks = 250
```

---

# 7. R Program – Calculate Covariance

```r
# Experiment 9
# Calculate covariance between two attributes

hours <- c(2, 3, 4, 5, 6)
marks <- c(50, 60, 70, 80, 90)

covariance <- cov(hours, marks)

cat("Covariance =", covariance, "\n")
```

### Output

```text
Covariance = 12.5
```

The positive value indicates that the two attributes tend to increase together.

---

# 8. R Program – Calculate Correlation

```r
# Experiment 9
# Calculate correlation between two attributes

hours <- c(2, 3, 4, 5, 6)
marks <- c(50, 60, 70, 80, 90)

correlation <- cor(hours, marks)

cat("Correlation =", correlation, "\n")
```

### Output

```text
Correlation = 1
```

The result indicates a perfect positive linear relationship for this example.

---

# 9. Complete R Program

The following program calculates **variance, covariance, and correlation** for attributes in the same dataset.

```r
# Experiment 9
# Variance, Covariance and Correlation

# Student dataset
hours <- c(2, 3, 4, 5, 6)
marks <- c(50, 60, 70, 80, 90)

# Calculate variance
variance_hours <- var(hours)
variance_marks <- var(marks)

# Calculate covariance
covariance <- cov(hours, marks)

# Calculate correlation
correlation <- cor(hours, marks)

# Display results
cat("Variance of Study Hours =", variance_hours, "\n")
cat("Variance of Marks =", variance_marks, "\n")
cat("Covariance =", covariance, "\n")
cat("Correlation =", correlation, "\n")
```

### Output

```text
Variance of Study Hours = 2.5
Variance of Marks = 250
Covariance = 12.5
Correlation = 1
```

---

# 10. Using Different Types of Attribute Relationships

To understand the measures better, consider three different cases.

## Case 1 – Positive Relationship

```r
x <- c(10, 20, 30, 40, 50)
y <- c(15, 25, 35, 45, 55)

cov(x, y)
cor(x, y)
```

Both variables increase together.

Expected interpretation:

```text
Positive covariance
Positive correlation
```

---

## Case 2 – Negative Relationship

```r
x <- c(10, 20, 30, 40, 50)
y <- c(50, 40, 30, 20, 10)

cov(x, y)
cor(x, y)
```

As `x` increases, `y` decreases.

Expected interpretation:

```text
Negative covariance
Negative correlation
```

---

## Case 3 – Weak/No Linear Relationship

```r
x <- c(1, 2, 3, 4, 5)
y <- c(3, 1, 5, 2, 4)

cov(x, y)
cor(x, y)
```

The variables do not show a strong linear pattern.

Expected interpretation:

```text
Covariance close to zero
Correlation close to zero
```

---

# 11. Correlation Matrix

When a dataset contains multiple numerical attributes, we can calculate the correlation between every pair of attributes.

Consider:

```r
students <- data.frame(
  StudyHours = c(2, 3, 4, 5, 6),
  Attendance = c(60, 65, 75, 85, 95),
  Marks = c(50, 60, 70, 80, 90)
)

cor(students)
```

The output is a correlation matrix.

```text
            StudyHours Attendance Marks
StudyHours       1.00       ...    ...
Attendance       ...        1.00   ...
Marks            ...        ...    1.00
```

The diagonal values are always:

```text
1
```

because every variable has perfect correlation with itself.

---

# 12. Covariance Matrix

Similarly, R can calculate the covariance between multiple numerical attributes.

```r
cov(students)
```

This produces a covariance matrix.

Example structure:

```text
            StudyHours Attendance Marks
StudyHours       ...        ...    ...
Attendance       ...        ...    ...
Marks            ...        ...    ...
```

Unlike correlation, covariance does not have a fixed range.

---

# 13. Visualization of Correlation

A scatter plot can help visualize the relationship between two numerical attributes.

```r
hours <- c(2, 3, 4, 5, 6)
marks <- c(50, 60, 70, 80, 90)

plot(
  hours,
  marks,
  main = "Study Hours vs Marks",
  xlab = "Study Hours",
  ylab = "Marks",
  pch = 19
)
```

A roughly upward-sloping pattern indicates a positive relationship.





---

# 14. Complete Data Analytics Example

## Student Performance Analysis

Consider the following dataset:

| Student | Study Hours | Attendance | Marks |
|---|---:|---:|---:|
| A | 2 | 60 | 50 |
| B | 3 | 65 | 60 |
| C | 4 | 75 | 70 |
| D | 5 | 85 | 80 |
| E | 6 | 95 | 90 |

### R Program

```r
# Student Performance Dataset

students <- data.frame(
  Student = c("A", "B", "C", "D", "E"),
  StudyHours = c(2, 3, 4, 5, 6),
  Attendance = c(60, 65, 75, 85, 95),
  Marks = c(50, 60, 70, 80, 90)
)

# Variance
cat("Variance of Study Hours:",
    var(students$StudyHours), "\n")

cat("Variance of Attendance:",
    var(students$Attendance), "\n")

cat("Variance of Marks:",
    var(students$Marks), "\n")

# Covariance
cat("\nCovariance between Study Hours and Marks:",
    cov(students$StudyHours, students$Marks), "\n")

cat("Covariance between Attendance and Marks:",
    cov(students$Attendance, students$Marks), "\n")

# Correlation
cat("\nCorrelation between Study Hours and Marks:",
    cor(students$StudyHours, students$Marks), "\n")

cat("Correlation between Attendance and Marks:",
    cor(students$Attendance, students$Marks), "\n")

# Correlation matrix
cat("\nCorrelation Matrix:\n")
print(cor(students[, 2:4]))
```

---

# 15. Important R Functions

| Function | Purpose | Example |
|---|---|---|
| `mean()` | Calculate mean | `mean(x)` |
| `var()` | Calculate sample variance | `var(x)` |
| `cov()` | Calculate covariance | `cov(x, y)` |
| `cor()` | Calculate correlation | `cor(x, y)` |
| `plot()` | Create a basic plot | `plot(x, y)` |
| `data.frame()` | Create data frame | `data.frame(x, y)` |
| `cat()` | Display output | `cat("Result")` |
| `print()` | Display object | `print(x)` |

---

# 16. Important Concepts to Remember

### Variance

Measures **how much one attribute varies**.

### Covariance

Measures **the direction of joint variation between two attributes**.

### Correlation

Measures **the strength and direction of a linear relationship between two attributes**.

### Important Relationship

Correlation is a standardized form of covariance:

\[
r =
\frac{Cov(X,Y)}
{\sqrt{Var(X)Var(Y)}}
\]

Therefore:

```text
Covariance → Direction
Correlation → Direction + Standardized Strength
```

---

# 17. Important Note About Correlation

Correlation does **not** imply causation.

For example, if two variables have a strong positive correlation, it does not necessarily mean that one variable causes the other.

```text
Correlation ≠ Causation
```

This is an important concept in Data Analytics.

---

# 18. Common Mistakes

## Mistake 1 – Using non-numeric data

Functions such as `var()`, `cov()`, and `cor()` require appropriate numeric data.

Incorrect:

```r
names <- c("Anu", "Arun", "Rahul")

var(names)
```

Use numerical attributes instead.

---

## Mistake 2 – Different vector lengths

The variables used for covariance/correlation should represent corresponding observations.

```r
x <- c(1, 2, 3, 4)
y <- c(10, 20, 30)
```

These vectors do not have matching lengths.

---

## Mistake 3 – Confusing covariance and correlation

Covariance does not have a fixed range.

Correlation always lies between:

```text
-1 and +1
```

---

## Mistake 4 – Assuming correlation means causation

A strong correlation does not prove that one variable causes another.

---

# 19. Algorithm

## Algorithm for Variance

1. Start.
2. Read a numerical attribute.
3. Calculate the mean.
4. Calculate deviations from the mean.
5. Square the deviations.
6. Calculate their average using the sample variance definition.
7. Display the variance.
8. Stop.

## Algorithm for Covariance

1. Start.
2. Read two numerical attributes.
3. Calculate the mean of both attributes.
4. Calculate deviations from their respective means.
5. Multiply corresponding deviations.
6. Calculate the sample covariance.
7. Display the covariance.
8. Stop.

## Algorithm for Correlation

1. Start.
2. Read two numerical attributes.
3. Calculate covariance.
4. Calculate the standard deviation of both attributes.
5. Standardize covariance using the standard deviations.
6. Display the correlation coefficient.
7. Stop.

---

# 20. Result

The R program was successfully implemented to calculate:

- **Variance** of numerical attributes.
- **Covariance** between two numerical attributes.
- **Correlation** between two numerical attributes.

The experiment also demonstrated how these statistical measures can be applied to analyze relationships between attributes in a dataset.

---

# 21. Learning Outcomes

After completing this experiment, students should be able to:

- Calculate variance using R.
- Calculate covariance between attributes.
- Calculate Pearson correlation.
- Interpret positive and negative relationships.
- Generate correlation and covariance matrices.
- Use statistical functions available in R.
- Apply statistical measures to real-world datasets.
- Understand the importance of statistical analysis in Data Analytics.

---

# 22. Viva Questions

### 1. What is variance?

Variance measures the dispersion of observations around their mean.

### 2. Which R function is used to calculate variance?

```r
var()
```

### 3. What is covariance?

Covariance measures the direction of joint variation between two variables.

### 4. Which R function calculates covariance?

```r
cov()
```

### 5. What is correlation?

Correlation measures the strength and direction of a linear relationship between two variables.

### 6. Which R function calculates correlation?

```r
cor()
```

### 7. What is the range of Pearson correlation?

```text
-1 to +1
```

### 8. What does a correlation of +1 mean?

Perfect positive linear correlation.

### 9. What does a correlation of -1 mean?

Perfect negative linear correlation.

### 10. What does correlation close to zero indicate?

Little or no linear relationship.

### 11. Does covariance have a fixed range?

No.

### 12. What is the difference between covariance and correlation?

Covariance indicates the direction of joint variation, while correlation gives both direction and standardized strength of a linear relationship.

### 13. What is a correlation matrix?

A matrix showing pairwise correlations between multiple numerical variables.

### 14. What are the diagonal values of a correlation matrix?

They are `1`, because each variable has perfect correlation with itself.

### 15. Does correlation imply causation?

No.

---

# 23. Exercises

1. Write an R program to calculate the variance of the following data:

```text
10, 20, 30, 40, 50
```

2. Calculate the covariance between:

```text
X = 10, 20, 30, 40, 50
Y = 15, 25, 35, 45, 55
```

3. Calculate the correlation between two numerical attributes.

4. Create a student dataset containing:

- Study Hours
- Attendance
- Assignment Marks
- Exam Marks

Calculate the variance of each numerical attribute.

5. Generate a covariance matrix for the student dataset.

6. Generate a correlation matrix for the student dataset.

7. Create a scatter plot between Study Hours and Exam Marks.

8. Identify the attribute that has the strongest positive correlation with Exam Marks.

---

# 24. Quick Revision

```text
VARIANCE
↓
Measures spread of ONE variable
R function → var()

COVARIANCE
↓
Measures direction of joint variation
between TWO variables
R function → cov()

CORRELATION
↓
Measures strength + direction
of a LINEAR relationship
R function → cor()
Range → -1 to +1
```

### Essential R Syntax

```r
var(x)
```

```r
cov(x, y)
```

```r
cor(x, y)
```

```r
cor(data_frame)
```

```r
cov(data_frame)
```

---

# Conclusion

This experiment introduces three fundamental statistical concepts used in Data Analytics: **variance, covariance, and correlation**.

Using R, students can efficiently calculate these measures and use them to understand the **dispersion and relationships among numerical attributes**. These concepts form the foundation for exploratory data analysis, feature analysis, statistical modeling, and machine learning.