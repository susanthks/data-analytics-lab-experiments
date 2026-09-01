# EXPERIMENT 7

# IMPLEMENTATION OF DATABASE OPERATIONS USING HIVE

---

## AIM

To implement and execute **database operations using Apache Hive**, including database creation, table creation, data insertion, data retrieval, filtering, sorting, grouping, aggregation, updating, and deletion using HiveQL.

---

## REQUIREMENTS

### Hardware Requirements

- Computer/Laptop
- Minimum 4 GB RAM recommended
- Sufficient storage for Hadoop and Hive

### Software Requirements

| Software | Version |
|---|---|
| Operating System | Ubuntu Linux 24.04 LTS |
| Java | JDK 8 or Hadoop-compatible JDK |
| Apache Hadoop | 3.4.0 |
| Apache Hive | 3.x / compatible version |
| HDFS | Configured |
| YARN | Configured |

> **Note:** Hive versions and commands may vary depending on the Hive installation used in the laboratory.

---

## THEORY

### What is Apache Hive?

Apache Hive is a data warehouse infrastructure built on top of Hadoop. It provides a SQL-like language called **HiveQL (Hive Query Language)** for querying and analyzing large datasets stored in Hadoop.

Hive allows users to perform database-style operations without writing MapReduce programs manually.

### HiveQL

HiveQL supports operations such as:

- Creating databases
- Creating tables
- Loading data
- Inserting records
- Selecting records
- Filtering records
- Sorting records
- Grouping records
- Aggregate functions
- Altering tables
- Dropping tables
- Dropping databases

Basic workflow:

```text
Create Database
      |
      v
Create Table
      |
      v
Load / Insert Data
      |
      v
Query Data
      |
      v
Process / Analyze Data
```

---

## DATABASE AND TABLE OPERATIONS

The following operations are implemented:

1. Create database
2. Show databases
3. Use database
4. Create table
5. Show tables
6. Describe table
7. Insert data
8. Load data
9. Select data
10. Filter data
11. Sort data
12. Group data
13. Aggregate data
14. Alter table
15. Drop table
16. Drop database

---

## ALGORITHM

1. Start HDFS and YARN services.
2. Start Hive or Beeline.
3. Create a Hive database.
4. Select the database using `USE`.
5. Create a student table with appropriate fields.
6. Insert or load student records.
7. Display records using `SELECT`.
8. Filter records using `WHERE`.
9. Sort records using `ORDER BY`.
10. Group records using `GROUP BY`.
11. Apply `COUNT()`, `AVG()`, `MAX()`, and `MIN()`.
12. Modify the table using `ALTER TABLE`.
13. Drop the table and database after completing the experiment.

---

## 6. PROCEDURE

### Step 1: Start Hadoop Services

```bash
start-dfs.sh
start-yarn.sh
jps
```

Expected services:

```text
NameNode
DataNode
SecondaryNameNode
ResourceManager
NodeManager
Jps
```

### Step 2: Start Hive

Depending on the installation:

```bash
hive
```

or:

```bash
beeline
```

If HiveServer2 is configured, Beeline can be used.

---

## CREATE AND SELECT DATABASE

### Display Databases

```sql
SHOW DATABASES;
```

### Create Database

```sql
CREATE DATABASE IF NOT EXISTS college;
```

### Select Database

```sql
USE college;
```

Verify:

```sql
SELECT current_database();
```

---

## CREATE TABLE

```sql
CREATE TABLE students (
    id INT,
    name STRING,
    department STRING,
    mark INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

Display tables:

```sql
SHOW TABLES;
```

Describe the table:

```sql
DESCRIBE students;
```

Expected schema:

```text
id           int
name         string
department   string
mark         int
```

---

## INSERT DATA

```sql
INSERT INTO TABLE students VALUES
(101,'Anoop','CS',85),
(102,'Anjali','EC',78),
(103,'Arun','CS',92),
(104,'Meera','ME',67),
(105,'Nithin','EC',88),
(106,'Reshma','CS',74),
(107,'Rahul','ME',81),
(108,'Swetha','EC',95);
```

> If the installed Hive version does not support multi-row `INSERT ... VALUES`, insert records individually or use the `LOAD DATA` method below.

---

## LOAD DATA FROM A FILE

Create:

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

Load it using:

```sql
LOAD DATA LOCAL INPATH '/path/to/students.csv'
INTO TABLE students;
```

Replace the path with the actual location.

> Use either `INSERT` or `LOAD DATA` to populate the table. Do not use both unless duplicate records are intentionally required.

---

## SELECT OPERATIONS

### Display All Records

```sql
SELECT * FROM students;
```

Expected:

```text
101  Anoop    CS  85
102  Anjali   EC  78
103  Arun     CS  92
104  Meera    ME  67
105  Nithin   EC  88
106  Reshma   CS  74
107  Rahul    ME  81
108  Swetha   EC  95
```

### Select Specific Columns

```sql
SELECT name, department, mark
FROM students;
```

---

## FILTER USING WHERE

Students scoring 80 or more:

```sql
SELECT *
FROM students
WHERE mark >= 80;
```

Expected:

```text
101  Anoop    CS  85
103  Arun     CS  92
105  Nithin   EC  88
107  Rahul    ME  81
108  Swetha   EC  95
```

Students from CS:

```sql
SELECT *
FROM students
WHERE department = 'CS';
```

---

## SORT USING ORDER BY

```sql
SELECT *
FROM students
ORDER BY mark DESC;
```

Expected order:

```text
108  Swetha   EC  95
103  Arun     CS  92
105  Nithin   EC  88
101  Anoop    CS  85
107  Rahul    ME  81
102  Anjali   EC  78
106  Reshma   CS  74
104  Meera    ME  67
```

---

## GROUP BY

```sql
SELECT department, COUNT(*) AS student_count
FROM students
GROUP BY department;
```

Expected:

```text
CS  3
EC  3
ME  2
```

---

## AGGREGATE FUNCTIONS

### Count

```sql
SELECT COUNT(*) AS total_students
FROM students;
```

Expected:

```text
8
```

### Average

```sql
SELECT AVG(mark) AS average_mark
FROM students;
```

Expected:

```text
82.5
```

### Maximum

```sql
SELECT MAX(mark) AS highest_mark
FROM students;
```

Expected:

```text
95
```

### Minimum

```sql
SELECT MIN(mark) AS lowest_mark
FROM students;
```

Expected:

```text
67
```

### Department-wise Average

```sql
SELECT department, AVG(mark) AS average_mark
FROM students
GROUP BY department;
```

Expected approximately:

```text
CS  83.67
EC  87.00
ME  74.00
```

---

## DISTINCT

```sql
SELECT DISTINCT department
FROM students;
```

Expected:

```text
CS
EC
ME
```

---

## LIMIT

```sql
SELECT *
FROM students
LIMIT 5;
```

---

##  ALTER TABLE

### Rename Table

```sql
ALTER TABLE students
RENAME TO student_details;
```

Verify:

```sql
SHOW TABLES;
```

Rename back:

```sql
ALTER TABLE student_details
RENAME TO students;
```

### Add Column

```sql
ALTER TABLE students
ADD COLUMNS (email STRING);
```

Verify:

```sql
DESCRIBE students;
```

> Existing records may contain `NULL` for the newly added column.

---

## DROP TABLE

```sql
DROP TABLE IF EXISTS students;
```

Verify:

```sql
SHOW TABLES;
```

---

## DROP DATABASE

If the database is empty:

```sql
DROP DATABASE IF EXISTS college;
```

If tables remain:

```sql
DROP DATABASE college CASCADE;
```

Verify:

```sql
SHOW DATABASES;
```

---

## COMPLETE HIVEQL PROGRAM

Create:

```bash
nano experiment7.hql
```

```sql
CREATE DATABASE IF NOT EXISTS college;

USE college;

DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INT,
    name STRING,
    department STRING,
    mark INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

INSERT INTO TABLE students VALUES
(101,'Anoop','CS',85),
(102,'Anjali','EC',78),
(103,'Arun','CS',92),
(104,'Meera','ME',67),
(105,'Nithin','EC',88),
(106,'Reshma','CS',74),
(107,'Rahul','ME',81),
(108,'Swetha','EC',95);

SHOW TABLES;

DESCRIBE students;

SELECT * FROM students;

SELECT name, department, mark
FROM students
WHERE mark >= 80;

SELECT *
FROM students
ORDER BY mark DESC;

SELECT department, COUNT(*) AS student_count
FROM students
GROUP BY department;

SELECT
    department,
    AVG(mark) AS average_mark,
    MAX(mark) AS highest_mark,
    MIN(mark) AS lowest_mark
FROM students
GROUP BY department;

SELECT DISTINCT department
FROM students;

SELECT *
FROM students
LIMIT 5;
```

---

## EXECUTE THE HIVE SCRIPT

Hive CLI:

```bash
hive -f experiment7.hql
```

Beeline:

```bash
beeline -f experiment7.hql
```

The exact command depends on the installed Hive environment.

---

## OUTPUT

### Table Data

```text
101  Anoop    CS  85
102  Anjali   EC  78
103  Arun     CS  92
104  Meera    ME  67
105  Nithin   EC  88
106  Reshma   CS  74
107  Rahul    ME  81
108  Swetha   EC  95
```

### Filter Output

```text
101  Anoop    CS  85
103  Arun     CS  92
105  Nithin   EC  88
107  Rahul    ME  81
108  Swetha   EC  95
```

### Group Output

```text
CS  3
EC  3
ME  2
```

### Aggregate Output

```text
Total Students = 8
Average Mark   = 82.5
Highest Mark   = 95
Lowest Mark    = 67
```

---

## OBSERVATION TABLE

| Sl. No. | Operation | HiveQL Statement | Expected Result |
|---:|---|---|---|
| 1 | Create Database | `CREATE DATABASE` | Database created |
| 2 | Create Table | `CREATE TABLE` | Table created |
| 3 | Insert Data | `INSERT INTO` | Records inserted |
| 4 | Select | `SELECT` | Records displayed |
| 5 | Filter | `WHERE` | Matching records displayed |
| 6 | Sort | `ORDER BY` | Sorted records |
| 7 | Group | `GROUP BY` | Department-wise groups |
| 8 | Aggregate | `COUNT`, `AVG`, `MAX`, `MIN` | Statistical results |
| 9 | Distinct | `DISTINCT` | Unique departments |
| 10 | Alter | `ALTER TABLE` | Table schema modified |
| 11 | Drop Table | `DROP TABLE` | Table removed |
| 12 | Drop Database | `DROP DATABASE` | Database removed |

---

## RESULT

The **database operations using Apache Hive were successfully implemented and executed** using HiveQL.

The experiment demonstrated database creation, table creation, data insertion, data retrieval, filtering, sorting, grouping, aggregation, alteration, and deletion operations on data stored in the Hadoop environment.

---

## 26. CONCLUSION

This experiment provided practical experience with **Apache Hive and HiveQL**. Students learned how Hive provides an SQL-like interface for processing large datasets in Hadoop without directly writing Java MapReduce programs.

---

## 27. VIVA QUESTIONS

1. What is Apache Hive?
2. What is HiveQL?
3. Why is Hive used with Hadoop?
4. What is a Hive database?
5. What is a Hive table?
6. What is the purpose of the `USE` command?
7. What is the difference between `SHOW DATABASES` and `SHOW TABLES`?
8. What is the purpose of `DESCRIBE`?
9. What is the purpose of `LOAD DATA`?
10. What is the difference between `INSERT` and `LOAD DATA`?
11. What is the purpose of the `WHERE` clause?
12. What is the purpose of `ORDER BY`?
13. What is the purpose of `GROUP BY`?
14. What are aggregate functions in Hive?
15. What is the use of `COUNT()`?
16. What is the use of `AVG()`?
17. What is the difference between `WHERE` and `HAVING`?
18. What is `DISTINCT`?
19. What is the purpose of `ALTER TABLE`?
20. How can a Hive table be deleted?
21. How can a Hive database be deleted?
22. What is `ROW FORMAT DELIMITED`?
23. What is `FIELDS TERMINATED BY ','`?
24. What is the difference between Hive and a traditional RDBMS?
25. Does Hive replace a traditional OLTP database?
26. What is the role of HDFS in Hive?
27. What is the Hive Metastore?
28. What is the difference between managed and external tables?
29. What is Beeline?
30. What are the advantages of Hive for big-data analytics?

---

## IMPORTANT COMMANDS – QUICK REFERENCE

### Hadoop

```bash
start-dfs.sh
start-yarn.sh
jps
```

### Hive

```bash
hive
```

or:

```bash
beeline
```

### Database

```sql
SHOW DATABASES;
CREATE DATABASE IF NOT EXISTS college;
USE college;
DROP DATABASE IF EXISTS college;
```

### Table

```sql
SHOW TABLES;
DESCRIBE students;
DROP TABLE IF EXISTS students;
```

### Queries

```sql
SELECT * FROM students;

SELECT * FROM students
WHERE mark >= 80;

SELECT *
FROM students
ORDER BY mark DESC;

SELECT department, COUNT(*)
FROM students
GROUP BY department;
```

### Execute Script

```bash
hive -f experiment7.hql
```

or:

```bash
beeline -f experiment7.hql
```

---

## COMPLETE EXPERIMENT WORKFLOW

```text
                         START
                           |
                           v
                  Start Hadoop Services
                           |
                           v
                       Start Hive
                           |
                           v
                  Create Hive Database
                           |
                           v
                     USE Database
                           |
                           v
                    Create Table
                           |
                           v
                  Insert / Load Data
                           |
                           v
                    SELECT Data
                           |
              +------------+------------+
              |            |            |
              v            v            v
           FILTER        SORT         GROUP
              |            |            |
              +------------+------------+
                           |
                           v
                     AGGREGATE
                           |
                           v
                    ALTER TABLE
                           |
                           v
                     DROP TABLE
                           |
                           v
                   DROP DATABASE
                           |
                           v
                          END
```

---

## KEY LEARNING OUTCOMES

After completing this experiment, students should be able to:

- Explain Apache Hive and HiveQL.
- Create and manage Hive databases.
- Create Hive tables with appropriate schemas.
- Insert and load data into Hive tables.
- Retrieve data using `SELECT`.
- Filter data using `WHERE`.
- Sort data using `ORDER BY`.
- Group data using `GROUP BY`.
- Perform aggregation using `COUNT`, `AVG`, `MAX`, and `MIN`.
- Modify table structures using `ALTER TABLE`.
- Delete tables and databases.
- Execute HiveQL scripts.
- Understand the role of Hive in Hadoop-based data analytics.

---

## EXTENSION ACTIVITIES

1. Create a second table named `departments`.
2. Insert department information into the table.
3. Perform an inner join between `students` and `departments`.
4. Calculate department-wise average marks.
5. Find the student with the highest mark.
6. Find the number of students scoring above 80 in each department.
7. Create an external Hive table using the same dataset.
8. Compare managed and external tables.
9. Load a larger CSV dataset into Hive.
10. Compare equivalent SQL queries with HiveQL queries.
11. Use `HAVING` to display departments whose average mark is greater than 80.
12. Create a partitioned table and compare it with a non-partitioned table.

---

