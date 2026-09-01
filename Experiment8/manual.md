# Experiment 8: Factorial and Palindrome Check Using R

## Aim

Write an **R program** to:

1. Find the factorial of a given number.
2. Check whether a given number or string is a palindrome.

---


# Part A – Factorial of a Number

## 1. Theory

The **factorial** of a non-negative integer `n` is the product of all positive integers from `1` to `n`.

It is represented as:

\[
n! = n \times (n-1) \times (n-2) \times \cdots \times 2 \times 1
\]



## 2. Algorithm – Factorial

1. Start.
2. Read a number `n`.
3. Check whether `n` is negative.
4. If `n` is negative, display an appropriate message.
5. Otherwise, initialize `factorial = 1`.
6. Repeat from `1` to `n`.
7. Multiply the current value of `factorial` by the loop variable.
8. Display the factorial.
9. Stop.

---

## 3. R Program – Factorial

```r
n <- as.integer(readline(prompt = "Enter a non-negative integer: "))

if (n < 0) {
  cat("Factorial is not defined for negative numbers.\n")
} else {
  
  fact <- 1
  
  if (n > 0) {
    for (i in 1:n) {
      fact <- fact * i
    }
  }

  cat("Factorial of", n, "is", fact, "\n")
}
```

---

## 4. Sample Output

### Example 1

```text
Enter a non-negative integer: 5
Factorial of 5 is 120
```

### Example 2

```text
Enter a non-negative integer: 0
Factorial of 0 is 1
```

### Example 3

```text
Enter a non-negative integer: -4
Factorial is not defined for negative numbers.
```

---

# Part B – Palindrome Check

## 1. Theory

A **palindrome** is a number or sequence that reads the same from left to right and right to left.


---

## 2. Algorithm – Palindrome Check

1. Start.
2. Read a number or string.
3. Convert the input into a character sequence.
4. Reverse the sequence.
5. Compare the original sequence with the reversed sequence.
6. If both are equal, display "Palindrome".
7. Otherwise, display "Not a Palindrome".
8. Stop.

---

## 3. R Program – Palindrome Check

```r
input <- readline(prompt = "Enter a number or string: ")
characters <- strsplit(input, "")[[1]]

reversed_input <- paste(rev(characters), collapse = "")
if (input == reversed_input) {
  cat(input, "is a Palindrome.\n")
} else {
  cat(input, "is not a Palindrome.\n")
}
```

---

## 4. Sample Output

### Example 1

```text
Enter a number or string: 121
121 is a Palindrome.
```

### Example 2

```text
Enter a number or string: 1234
1234 is not a Palindrome.
```

### Example 3

```text
Enter a number or string: madam
madam is a Palindrome.
```

---

# Part C – Using User-Defined Functions

Functions make the program modular and reusable.

## 1. Factorial Function

```r
factorial_custom <- function(n) {
  
  if (n < 0) {
    return(NA)
  }
  
  fact <- 1
  
  if (n > 0) {
    for (i in 1:n) {
      fact <- fact * i
    }
  }
  
  return(fact)
}

n <- as.integer(readline(prompt = "Enter a number: "))


result <- factorial_custom(n)

if (is.na(result)) {
  cat("Factorial is not defined for negative numbers.\n")
} else {
  cat("Factorial of", n, "is", result, "\n")
}
```

---

## 2. Palindrome Function

```r
is_palindrome <- function(input) {
  
  characters <- strsplit(input, "")[[1]]
  
  reversed_input <- paste(
    rev(characters),
    collapse = ""
  )
  
  return(input == reversed_input)
}


input <- readline(prompt = "Enter a number or string: ")


if (is_palindrome(input)) {
  cat(input, "is a Palindrome.\n")
} else {
  cat(input, "is not a Palindrome.\n")
}
```

---

# Part D – Combined Program

The following program performs both operations in a single R program.

```r
# Experiment 8
# Factorial and Palindrome Check

# -------------------------------
# Factorial Function
# -------------------------------

find_factorial <- function(n) {
  
  if (n < 0) {
    return(NA)
  }
  
  fact <- 1
  
  if (n > 0) {
    for (i in 1:n) {
      fact <- fact * i
    }
  }
  
  return(fact)
}



check_palindrome <- function(input) {
  
  characters <- strsplit(input, "")[[1]]
  
  reversed_input <- paste(
    rev(characters),
    collapse = ""
  )
  
  return(input == reversed_input)
}


n <- as.integer(
  readline(prompt = "Enter a non-negative integer: ")
)

factorial_result <- find_factorial(n)

if (is.na(factorial_result)) {
  cat("Factorial is not defined for negative numbers.\n")
} else {
  cat("Factorial of", n, "is", factorial_result, "\n")
}


input <- readline(
  prompt = "Enter a number or string to check for palindrome: "
)

if (check_palindrome(input)) {
  cat(input, "is a Palindrome.\n")
} else {
  cat(input, "is not a Palindrome.\n")
}
```

---

# Sample Output

```text
Enter a non-negative integer: 6
Factorial of 6 is 720

Enter a number or string to check for palindrome: 12321
12321 is a Palindrome.
```

Another example:

```text
Enter a non-negative integer: 5
Factorial of 5 is 120

Enter a number or string to check for palindrome: robotics
robotics is not a Palindrome.
```

---


# Result

The R programs for:

1. **Finding the factorial of a number**, and
2. **Checking whether a number/string is a palindrome**

were successfully implemented and executed.

---
# Important R Functions Used

| Function | Purpose |
|---|---|
| `readline()` | Read input from the user |
| `as.integer()` | Convert input to integer |
| `if` | Conditional execution |
| `else` | Alternative condition |
| `for` | Repetition/looping |
| `function()` | Create a user-defined function |
| `return()` | Return a value from a function |
| `strsplit()` | Split a string into characters |
| `rev()` | Reverse a vector |
| `paste()` | Combine strings |
| `cat()` | Display formatted output |
| `is.na()` | Check for `NA` values |

---

# Key Concepts Learned

- Variables in R
- User input
- Type conversion
- Conditional statements
- `for` loops
- User-defined functions
- String manipulation
- Character vectors
- Logical comparison
- Returning values from functions

---

# Common Mistakes

### 1. Forgetting type conversion

`readline()` returns input as a character string. Therefore, for factorial calculation, convert it using:

```r
n <- as.integer(readline())
```

### 2. Incorrect factorial initialization

Use:

```r
fact <- 1
```

not:

```r
fact <- 0
```

because multiplying by zero would always produce zero.

### 3. Forgetting the zero case

Remember:

```text
0! = 1
```

### 4. Incorrect string reversal

For character-based palindrome checking, use:

```r
strsplit(input, "")[[1]]
```

before applying `rev()`.

### 5. Case sensitivity

The basic palindrome program treats uppercase and lowercase characters as different.

For example:

```text
Madam
```

will not be considered the same as:

```text
madam
```

unless the input is converted to a common case.

---

# Optional Extension

Modify the palindrome program so that it ignores:

- Uppercase/lowercase differences
- Spaces
- Special characters

For example:

```text
"A man a plan a canal Panama"
```

should be recognized as a palindrome after preprocessing.

Hint:

```r
input <- tolower(input)
input <- gsub("[^a-z0-9]", "", input)
```

---

# Exercises

1. Write an R program to calculate the factorial using a `while` loop.
2. Write a recursive R function to calculate factorial.
3. Write an R program to check whether a given number is a palindrome.
4. Modify the palindrome program to ignore case.
5. Modify the program to ignore spaces and special characters.
6. Write a function that checks whether multiple numbers are palindromes.
7. Write a program to calculate factorials for all numbers from 1 to 10.

---

# Viva Questions

### 1. What is factorial?

The factorial of a non-negative integer `n` is the product of all positive integers from `1` to `n`.

### 2. What is the value of 0!?

```text
0! = 1
```

### 3. Is factorial defined for negative integers?

No. The factorial operation in this experiment is defined for non-negative integers.

### 4. What is a palindrome?

A palindrome is a sequence that reads the same forwards and backwards.

### 5. Give two examples of palindromes.

```text
121
madam
```

### 6. What does `readline()` do?

It reads input from the user as a character string.

### 7. Why do we use `as.integer()`?

To convert character input into an integer.

### 8. What does `strsplit()` do?

It splits a string into smaller character elements.

### 9. What does `rev()` do?

It reverses the order of elements in a vector.

### 10. What is the purpose of `function()`?

It is used to define a user-defined function in R.

---



# Learning Outcome

After completing this experiment, students should be able to:

- Write basic R programs.
- Use loops and conditional statements.
- Define and call functions.
- Perform basic string manipulation.
- Solve simple computational problems using R.
- Apply fundamental R programming concepts to data-analytics-related tasks.

---

## References

- R Core Team, *An Introduction to R*.
- R Core Team, *R Language Definition*.
- R Documentation – `factorial()`, string manipulation, and basic programming constructs.
