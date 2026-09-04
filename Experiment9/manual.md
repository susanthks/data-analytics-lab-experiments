# EXPERIMENT 9  
## Variance, Covariance and Correlation Using R

### Aim

To write an R program to calculate:

1. Variance
2. Covariance
3. Correlation

---


##  Basic Concepts

### Variance

Variance tells us **how much the values of one variable are spread out**.

- Small variance → values are close together.
- Large variance → values are more spread out.

**R function:**

```r
var(x)
```

###  Covariance

Covariance tells us **how two variables change together**.

- Positive covariance → both generally increase together.
- Negative covariance → one increases while the other decreases.
- Near-zero covariance → little linear co-movement.

**R function:**

```r
cov(x, y)
```

###  Correlation

Correlation tells us the **strength and direction of a linear relationship** between two variables.

The value of correlation is always between:

```text
-1 and +1
```

| Correlation | Meaning |
|---|---|
| +1 | Perfect positive relationship |
| Close to +1 | Strong positive relationship |
| Around 0 | Little/no linear relationship |
| Close to -1 | Strong negative relationship |
| -1 | Perfect negative relationship |

**R function:**

```r
cor(x, y)
```

### Easy way to remember

```text
Variance
   ↓
Spread of ONE variable

Covariance
   ↓
Direction of relationship between TWO variables

Correlation
   ↓
Strength + direction of linear relationship
```

---

# Example Dataset

Consider the following student data:

| Student | Study Hours | Marks |
|---|---:|---:|
| A | 2 | 50 |
| B | 3 | 60 |
| C | 4 | 70 |
| D | 5 | 80 |
| E | 6 | 90 |

We will use **Study Hours** and **Marks** for our experiment.

---

# Program 1 – Calculate Variance

### R Program

```r
# Variance

marks <- c(60, 70, 80, 90, 100)

variance <- var(marks)

cat("Variance =", variance)
```

### Output

```text
Variance = 250
```

### Interpretation

The variance of the marks is **250**.

---

# Program 2 – Calculate Covariance

### R Program

```r
# Covariance

hours <- c(2, 3, 4, 5, 6)
marks <- c(50, 60, 70, 80, 90)

covariance <- cov(hours, marks)

cat("Covariance =", covariance)
```

### Output

```text
Covariance = 12.5
```

### Interpretation

The covariance is positive.

Therefore:

```text
Study Hours ↑  →  Marks ↑
```

The two variables tend to increase together.

---

# Program 3 – Calculate Correlation

### R Program

```r
# Correlation

hours <- c(2, 3, 4, 5, 6)
marks <- c(50, 60, 70, 80, 90)

correlation <- cor(hours, marks)

cat("Correlation =", correlation)
```

### Output

```text
Correlation = 1
```

### Interpretation

The correlation is **+1**.

Therefore, the data has a **perfect positive linear relationship**.

---

# Complete Program

The following program calculates all three measures.

```r
# Experiment 9
# Variance, Covariance and Correlation

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

### Output

```text
Variance of Study Hours = 2.5
Variance of Marks = 250
Covariance = 12.5
Correlation = 1
```

---

# Procedure

### Step 1
Open **RStudio**.

### Step 2
Create the data:

```r
hours <- c(2, 3, 4, 5, 6)
marks <- c(50, 60, 70, 80, 90)
```

### Step 3
Calculate variance:

```r
var(hours)
var(marks)
```

### Step 4
Calculate covariance:

```r
cov(hours, marks)
```

### Step 5
Calculate correlation:

```r
cor(hours, marks)
```

### Step 6
Observe and interpret the results.

---

# Important R Functions

| R Function | Purpose |
|---|---|
| `mean(x)` | Finds the mean |
| `var(x)` | Finds variance |
| `cov(x,y)` | Finds covariance |
| `cor(x,y)` | Finds correlation |
| `plot(x,y)` | Creates a graph |
| `print(x)` | Displays result |
| `cat()` | Displays formatted output |

---

# Example of Positive and Negative Correlation

## Positive Relationship

```r
x <- c(10, 20, 30, 40, 50)
y <- c(15, 25, 35, 45, 55)

cor(x, y)
```

Here, both variables increase together.

**Result:** Positive correlation.

---

## Negative Relationship

```r
x <- c(10, 20, 30, 40, 50)
y <- c(50, 40, 30, 20, 10)

cor(x, y)
```

Here, when `x` increases, `y` decreases.

**Result:** Negative correlation.

---

#  Correlation Matrix

When we have several numerical variables, we can find the correlation between every pair.

```r
students <- data.frame(
  StudyHours = c(2, 3, 4, 5, 6),
  Attendance = c(60, 65, 75, 85, 95),
  Marks = c(50, 60, 70, 80, 90)
)

cor(students)
```

The result is called a **correlation matrix**.

The diagonal values are always:

```text
1
```

because a variable has perfect correlation with itself.

---

# Scatter Plot

We can visually see the relationship between two variables.

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

### Observation

An upward pattern indicates a **positive relationship**.

---


# Result

The R program was successfully implemented to calculate:

- Variance
- Covariance
- Correlation

The results were used to understand the **spread and relationship between numerical attributes**.

---

# Viva Questions

### 1. What is variance?

Variance measures the spread of values around their mean.

### 2. Which function is used for variance?

```r
var()
```

### 3. What is covariance?

Covariance shows the direction in which two variables change together.

### 4. Which function is used for covariance?

```r
cov()
```

### 5. What is correlation?

Correlation measures the strength and direction of a linear relationship.

### 6. Which function is used for correlation?

```r
cor()
```

### 7. What is the range of correlation?

```text
-1 to +1
```

### 8. What does +1 correlation mean?

Perfect positive linear relationship.

### 9. What does -1 correlation mean?

Perfect negative linear relationship.

### 10. What does correlation close to zero mean?

Little or no linear relationship.

### 11. Does correlation imply causation?

No.

### 12. What is a correlation matrix?

It shows the correlation between multiple numerical variables.

---

# Student Exercises

### Exercise 1

Calculate the variance of:

```text
10, 20, 30, 40, 50
```

---

### Exercise 2

Find the covariance between:

```text
X = 10, 20, 30, 40, 50
Y = 15, 25, 35, 45, 55
```

---

### Exercise 3

Calculate the correlation between:

```text
X = 10, 20, 30, 40, 50
Y = 50, 40, 30, 20, 10
```

---

### Exercise 4

Create the following student dataset:

- Study Hours
- Attendance
- Assignment Marks
- Exam Marks

Calculate:

1. Variance of each attribute.
2. Covariance matrix.
3. Correlation matrix.

---

### Exercise 5

Create a scatter plot between:

```text
Study Hours vs Exam Marks
```

Observe whether the relationship is positive or negative.

---

# Quick Revision

```text
VARIANCE
↓
Spread of ONE variable
↓
R function: var()

COVARIANCE
↓
Direction of joint variation
between TWO variables
↓
R function: cov()

CORRELATION
↓
Strength + direction
of a LINEAR relationship
↓
R function: cor()
↓
Range: -1 to +1
```

## Essential R Commands

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
cor(data)
```

```r
cov(data)
```

---

# Learning Outcome

After completing this experiment, students should be able to:

- Calculate variance using R.
- Calculate covariance using R.
- Calculate correlation using R.
- Interpret positive and negative relationships.
- Generate a correlation matrix.
- Create a simple scatter plot.
- Apply these concepts to a small dataset.

---

# Common Mistakes

### Mistake 1: Using text instead of numbers

Wrong:

```r
names <- c("Anu", "Arun", "Rahul")

var(names)
```

Use numerical data for variance, covariance, and correlation.

---

### Mistake 2: Different number of observations

The two variables should normally contain corresponding observations.

Correct:

```r
x <- c(1, 2, 3, 4)
y <- c(10, 20, 30, 40)
```

---

### Mistake 3: Confusing covariance and correlation

Remember:

```text
Covariance → Direction

Correlation → Strength + Direction
```

Correlation is always between:

```text
-1 and +1
```

---

### Mistake 4: Correlation does not mean causation

```text
Correlation ≠ Causation
```

A strong correlation does not prove that one variable causes another.

---

