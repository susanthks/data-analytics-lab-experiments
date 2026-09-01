# EXPERIMENT 6

# IMPLEMENTATION OF PIG LATIN SCRIPTS FOR SORT, GROUP, JOIN, PROJECT AND FILTER OPERATIONS

---

##  AIM

To implement and execute **Pig Latin scripts** to perform **SORT, GROUP, JOIN, PROJECT, and FILTER** operations on datasets using Apache Pig.

---

## REQUIREMENTS

### Hardware Requirements

- Computer/Laptop
- Minimum 4 GB RAM recommended
- Sufficient storage for Hadoop and input datasets

### Software Requirements

| Software | Version |
|---|---|
| Operating System | Ubuntu Linux 24.04 LTS |
| Java | JDK 8 or Hadoop-compatible JDK |
| Apache Hadoop | 3.4.0 |
| Apache Pig | 0.17.0 |
| HDFS | Configured |
| YARN | Configured |

> **Note:** Verify Apache Pig and Hadoop compatibility with the versions installed in the laboratory.

---

## THEORY

### Apache Pig

Apache Pig is a high-level data-flow platform used for processing and analyzing large datasets on Hadoop. Its scripting language is called **Pig Latin**.

Instead of writing a complete Java MapReduce program, users can express data-processing operations using Pig Latin operators.

Basic workflow:

```text
LOAD → TRANSFORM → DUMP / STORE
```

### Important Pig Latin Operators

#### FILTER

Selects records satisfying a condition.

```pig
result = FILTER relation BY condition;
```

#### PROJECT

Selects required fields using `FOREACH ... GENERATE`.

```pig
result = FOREACH relation GENERATE field1, field2;
```

#### SORT

Sorts records using `ORDER BY`.

```pig
result = ORDER relation BY field DESC;
```

#### GROUP

Groups records having the same value.

```pig
result = GROUP relation BY field;
```

Aggregate functions such as `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX` can then be applied.

#### JOIN

Combines two relations using a common field.

```pig
result = JOIN relation1 BY field1,
               relation2 BY field2;
```

---

## DATASETS

### Students Dataset

Create `students.csv`:

```text
101,Anoop,CS,85
102,Anjali,EC,78
103,Arun,CS,92
104,Meera,ME,67
105,Nithin,EC,88
106,Reshma,CS,74
107,Rahul,ME,81
108,Swetha,EC,95
```

Schema:

```text
student_id,name,department,mark
```

### Departments Dataset

Create `departments.csv`:

```text
CS,Computer Science
EC,Electronics and Communication
ME,Mechanical Engineering
```

Schema:

```text
department_code,department_name
```

---

## ALGORITHM

### Part A – SORT

1. Load the student dataset.
2. Define the schema.
3. Sort students by marks.
4. Display the sorted relation.

### Part B – GROUP

1. Load the student dataset.
2. Group students by department.
3. Count students in each department.
4. Display the result.

### Part C – JOIN

1. Load the students dataset.
2. Load the departments dataset.
3. Join both relations using department code.
4. Project the required fields.
5. Display the result.

### Part D – PROJECT

1. Load the student dataset.
2. Select required fields using `FOREACH ... GENERATE`.
3. Display the projected relation.

### Part E – FILTER

1. Load the student dataset.
2. Apply a condition on marks.
3. Select students with marks greater than or equal to 80.
4. Display the result.

---

## 6. PROCEDURE

### Step 1: Start Hadoop Services

```bash
start-dfs.sh
start-yarn.sh
jps
```

Expected services include:

```text
NameNode
DataNode
SecondaryNameNode
ResourceManager
NodeManager
Jps
```

### Step 2: Create Project Directory

```bash
mkdir PigExperiment6
cd PigExperiment6
```

### Step 3: Create Input Files

```bash
nano students.csv
```

Enter:

```text
101,Anoop,CS,85
102,Anjali,EC,78
103,Arun,CS,92
104,Meera,ME,67
105,Nithin,EC,88
106,Reshma,CS,74
107,Rahul,ME,81
108,Swetha,EC,95
```

Create the departments file:

```bash
nano departments.csv
```

Enter:

```text
CS,Computer Science
EC,Electronics and Communication
ME,Mechanical Engineering
```

### Step 4: Create HDFS Input Directory

```bash
hdfs dfs -mkdir -p /pig_input
```

### Step 5: Upload Files

```bash
hdfs dfs -put students.csv /pig_input
hdfs dfs -put departments.csv /pig_input
```

Verify:

```bash
hdfs dfs -ls /pig_input
```

Display:

```bash
hdfs dfs -cat /pig_input/students.csv
hdfs dfs -cat /pig_input/departments.csv
```

---

# PIG LATIN PROGRAMS

## SORT

Create:

```bash
nano sort.pig
```

```pig
students = LOAD '/pig_input/students.csv'
           USING PigStorage(',')
           AS (
               id:int,
               name:chararray,
               dept:chararray,
               mark:int
           );

sorted_students = ORDER students BY mark DESC;

DUMP sorted_students;
```

Execute:

```bash
pig -x mapreduce sort.pig
```

Expected output:

```text
(108,Swetha,EC,95)
(103,Arun,CS,92)
(105,Nithin,EC,88)
(101,Anoop,CS,85)
(107,Rahul,ME,81)
(102,Anjali,EC,78)
(106,Reshma,CS,74)
(104,Meera,ME,67)
```

---

## GROUP

Create:

```bash
nano group.pig
```

```pig
students = LOAD '/pig_input/students.csv'
           USING PigStorage(',')
           AS (
               id:int,
               name:chararray,
               dept:chararray,
               mark:int
           );

grouped_students = GROUP students BY dept;

dept_count = FOREACH grouped_students
             GENERATE
                 group AS department,
                 COUNT(students) AS student_count;

DUMP dept_count;
```

Execute:

```bash
pig -x mapreduce group.pig
```

Expected output:

```text
(CS,3)
(EC,3)
(ME,2)
```

> The order of groups may vary unless an explicit `ORDER BY` is used.

---

## JOIN

Create:

```bash
nano join.pig
```

```pig
students = LOAD '/pig_input/students.csv'
           USING PigStorage(',')
           AS (
               id:int,
               name:chararray,
               dept:chararray,
               mark:int
           );

departments = LOAD '/pig_input/departments.csv'
              USING PigStorage(',')
              AS (
                  dept_code:chararray,
                  dept_name:chararray
              );

joined_data = JOIN students BY dept,
                    departments BY dept_code;

result = FOREACH joined_data
         GENERATE
             students::id AS id,
             students::name AS name,
             students::dept AS department,
             departments::dept_name AS department_name,
             students::mark AS mark;

DUMP result;
```

Execute:

```bash
pig -x mapreduce join.pig
```

Expected output:

```text
(101,Anoop,CS,Computer Science,85)
(102,Anjali,EC,Electronics and Communication,78)
(103,Arun,CS,Computer Science,92)
(104,Meera,ME,Mechanical Engineering,67)
(105,Nithin,EC,Electronics and Communication,88)
(106,Reshma,CS,Computer Science,74)
(107,Rahul,ME,Mechanical Engineering,81)
(108,Swetha,EC,Electronics and Communication,95)
```

---

## PROJECT

Create:

```bash
nano project.pig
```

```pig
students = LOAD '/pig_input/students.csv'
           USING PigStorage(',')
           AS (
               id:int,
               name:chararray,
               dept:chararray,
               mark:int
           );

projected_students = FOREACH students
                     GENERATE name, dept, mark;

DUMP projected_students;
```

Execute:

```bash
pig -x mapreduce project.pig
```

Expected output:

```text
(Anoop,CS,85)
(Anjali,EC,78)
(Arun,CS,92)
(Meera,ME,67)
(Nithin,EC,88)
(Reshma,CS,74)
(Rahul,ME,81)
(Swetha,EC,95)
```

---

## FILTER

Create:

```bash
nano filter.pig
```

```pig
students = LOAD '/pig_input/students.csv'
           USING PigStorage(',')
           AS (
               id:int,
               name:chararray,
               dept:chararray,
               mark:int
           );

high_scorers = FILTER students BY mark >= 80;

DUMP high_scorers;
```

Execute:

```bash
pig -x mapreduce filter.pig
```

Expected output:

```text
(101,Anoop,CS,85)
(103,Arun,CS,92)
(105,Nithin,EC,88)
(107,Rahul,ME,81)
(108,Swetha,EC,95)
```

---

# COMBINED PIG LATIN SCRIPT

Create:

```bash
nano experiment6.pig
```

```pig
-- Load students
students = LOAD '/pig_input/students.csv'
           USING PigStorage(',')
           AS (
               id:int,
               name:chararray,
               dept:chararray,
               mark:int
           );

-- Load departments
departments = LOAD '/pig_input/departments.csv'
              USING PigStorage(',')
              AS (
                  dept_code:chararray,
                  dept_name:chararray
              );

-- FILTER
filtered = FILTER students BY mark >= 80;

-- PROJECT
projected = FOREACH filtered
            GENERATE name, dept, mark;

-- SORT
sorted = ORDER projected BY mark DESC;

-- GROUP
grouped = GROUP students BY dept;

dept_count = FOREACH grouped
             GENERATE
                 group AS department,
                 COUNT(students) AS student_count;

-- JOIN
joined = JOIN students BY dept,
              departments BY dept_code;

joined_projected = FOREACH joined
                   GENERATE
                       students::id AS id,
                       students::name AS name,
                       students::dept AS department,
                       departments::dept_name AS department_name,
                       students::mark AS mark;

DUMP sorted;
DUMP dept_count;
DUMP joined_projected;
```

Execute:

```bash
pig -x mapreduce experiment6.pig
```

---

# STORING OUTPUT IN HDFS

Instead of `DUMP`, results can be stored using `STORE`.

Example:

```pig
STORE sorted INTO '/pig_output/sorted'
USING PigStorage(',');
```

Remove a previous output directory if required:

```bash
hdfs dfs -rm -r -skipTrash /pig_output
```

Verify:

```bash
hdfs dfs -ls /pig_output/sorted
hdfs dfs -cat /pig_output/sorted/part-*
```

---

#  OUTPUT SUMMARY

| Operation | Pig Latin Operator | Purpose |
|---|---|---|
| Sort | `ORDER BY` | Sort records |
| Group | `GROUP BY` | Group records with the same key |
| Join | `JOIN` | Combine two relations |
| Project | `FOREACH ... GENERATE` | Select required fields |
| Filter | `FILTER` | Select records satisfying a condition |

---

# OBSERVATION TABLE

| Sl. No. | Operation | Input Relation | Condition / Key | Expected Result |
|---:|---|---|---|---|
| 1 | Sort | Students | `mark DESC` | Students sorted by marks |
| 2 | Group | Students | `dept` | Students grouped by department |
| 3 | Join | Students + Departments | `dept = dept_code` | Student and department details combined |
| 4 | Project | Students | `name, dept, mark` | Selected fields displayed |
| 5 | Filter | Students | `mark >= 80` | High-scoring students displayed |

---

# RESULT

The required **Pig Latin scripts were successfully implemented and executed** to perform:

- Sorting
- Grouping
- Joining
- Projection
- Filtering

on the given datasets using Apache Pig and Hadoop.

---

# 13. CONCLUSION

This experiment demonstrated Apache Pig as a high-level data-flow platform for processing datasets on Hadoop.



# 14. VIVA QUESTIONS

1. What is Apache Pig?
2. What is Pig Latin?
3. Why is Pig used with Hadoop?
4. What is a relation in Pig?
5. What is the purpose of the `LOAD` operator?
6. What is the difference between `DUMP` and `STORE`?
7. What is the purpose of `FILTER`?
8. What is projection in Pig?
9. Which Pig operator is used for projection?
10. What is the purpose of `ORDER BY`?
11. What is the difference between `GROUP` and `ORDER BY`?
12. What is the purpose of `JOIN`?
13. What is a schema in Pig?
14. What is `PigStorage(',')`?
15. What is the purpose of the `group` field after a `GROUP` operation?
16. Which aggregate functions can be used with grouped data?
17. Can Pig process large datasets stored in HDFS?
18. What is the difference between Pig Latin and Java MapReduce?
19. What is the purpose of `-x mapreduce`?
20. What happens if the output directory already exists during `STORE`?
21. What is the difference between an inner join and an outer join?
22. Why are aliases used in Pig Latin?
23. What is a `FOREACH` statement?
24. How can multiple Pig operations be combined into a single script?
25. What are the advantages of using Pig for big-data processing?

---

# 15. IMPORTANT COMMANDS – QUICK REFERENCE

```bash
# Start Hadoop
start-dfs.sh
start-yarn.sh

# Verify services
jps

# Create project
mkdir PigExperiment6
cd PigExperiment6

# Create HDFS input directory
hdfs dfs -mkdir -p /pig_input

# Upload files
hdfs dfs -put students.csv /pig_input
hdfs dfs -put departments.csv /pig_input

# List files
hdfs dfs -ls /pig_input

# Display input
hdfs dfs -cat /pig_input/students.csv
hdfs dfs -cat /pig_input/departments.csv

# Run Pig scripts
pig -x mapreduce sort.pig
pig -x mapreduce group.pig
pig -x mapreduce join.pig
pig -x mapreduce project.pig
pig -x mapreduce filter.pig

# Run combined script
pig -x mapreduce experiment6.pig

# Remove previous output
hdfs dfs -rm -r -skipTrash /pig_output

# View stored output
hdfs dfs -ls /pig_output
hdfs dfs -cat /pig_output/*/part-*
```

---

# 16. COMPLETE EXPERIMENT WORKFLOW

```text
                         START
                           |
                           v
                  Start Hadoop Services
                           |
                           v
                    Create Input Data
                           |
                           v
                    Upload to HDFS
                           |
                           v
                       LOAD Data
                           |
              +------------+------------+
              |            |            |
              v            v            v
           FILTER       PROJECT       SORT
              |            |            |
              +------------+------------+
                           |
                           v
                         GROUP
                           |
                           v
                          JOIN
                           |
                           v
                    DUMP / STORE
                           |
                           v
                     View Results
                           |
                           v
                          END
```

---

# 17. KEY LEARNING OUTCOMES

After completing this experiment, students should be able to:

- Explain Apache Pig and Pig Latin.
- Load structured datasets into Pig.
- Apply filtering and projection operations.
- Sort large datasets.
- Group records based on a key.
- Join multiple datasets.
- Use aggregate functions with grouped relations.
- Store processed data in HDFS.
- Execute Pig Latin scripts in Hadoop MapReduce mode.
- Differentiate Pig Latin operations from traditional MapReduce programming.

---

# 18. EXTENSION ACTIVITIES

1. Modify the `FILTER` operation to select students with marks between 70 and 90.
2. Sort students by name in ascending order.
3. Group students by department and calculate the average mark.
4. Find the maximum and minimum mark in each department.
5. Perform a join between three datasets.
6. Perform a left outer join and full outer join.
7. Store each operation's output in a separate HDFS directory.
8. Create a Pig script that finds the number of students in each department whose marks are above 80.
9. Compare the Pig implementation with an equivalent MapReduce Java program.
10. Experiment with a larger dataset and observe the execution behavior.

---

# 19. LAB RECORD CHECKLIST

- [ ] Hadoop services started successfully.
- [ ] Input files created.
- [ ] Input files uploaded to HDFS.
- [ ] `sort.pig` executed successfully.
- [ ] `group.pig` executed successfully.
- [ ] `join.pig` executed successfully.
- [ ] `project.pig` executed successfully.
- [ ] `filter.pig` executed successfully.
- [ ] Outputs verified.
- [ ] Screenshots of important commands/results captured.
- [ ] Result and conclusion recorded.
- [ ] Viva questions reviewed.

---
