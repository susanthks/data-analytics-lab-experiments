# EXPERIMENT 5

# MATRIX MULTIPLICATION USING HADOOP MAPREDUCE

---

## AIM

To implement a **Matrix Multiplication program using the Hadoop MapReduce framework** and perform multiplication of two matrices stored as input data in HDFS.

---

# THEORY

## Matrix Multiplication

If matrix **A** has dimensions `m × n` and matrix **B** has dimensions `n × p`, their product **C = A × B** has dimensions `m × p`.

Each element is calculated using a row of A and a column of B:

```text
C[i][j] = Σ A[i][k] × B[k][j]
```

For example:

```text
A = [1 2]
    [3 4]

B = [5 6]
    [7 8]
```

Then:

```text
C[0][0] = (1×5) + (2×7) = 19
C[0][1] = (1×6) + (2×8) = 22
C[1][0] = (3×5) + (4×7) = 43
C[1][1] = (3×6) + (4×8) = 50
```

Therefore:

```text
C = [19 22]
    [43 50]
```

---

## MapReduce Workflow

```text
                  Input Matrix Data
                         |
                         v
                  +-------------+
                  |    Mapper   |
                  +-------------+
                         |
                         v
              Intermediate Key-Value
                    Pairs (i,j)
                         |
                         v
                 Shuffle and Sort
                         |
                         v
                  +-------------+
                  |   Reducer   |
                  +-------------+
                         |
                         v
                  C[i][j] Values
                         |
                         v
                   Final Matrix
```

---

# ALGORITHM

**Step 1:** Start HDFS and YARN services.

**Step 2:** Create Mapper, Reducer, and Driver Java programs.

**Step 3:** Store matrix elements in the required input format.

**Step 4:** Upload the input file to HDFS.

**Step 5:** For every element `A[i][k]`, the Mapper generates a record for every output column `j`.

**Step 6:** For every element `B[k][j]`, the Mapper generates a record for every output row `i`.

**Step 7:** Use `(i,j)` as the intermediate key.

**Step 8:** Hadoop performs Shuffle and Sort and groups values for the same output position.

**Step 9:** The Reducer matches A and B values having the same inner index `k`.

**Step 10:** Multiply corresponding values and add all products.

**Step 11:** Generate `C[i][j]`.

**Step 12:** Store and display the resulting matrix.

---

# PROCEDURE

## Step 1: Start Hadoop Services

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

## Step 2: Create the Project Directory

```bash
mkdir MatrixMultiplication
cd MatrixMultiplication
```

## Step 3: Create the Java Files

```bash
nano MapperClass.java
nano ReducerClass.java
nano MatrixMultiplication.java
```

Enter the programs from Section 6.

## Step 4: Create the Input File

```bash
nano input.txt
```

Enter:

```text
A,0,0,1
A,0,1,2
A,1,0,3
A,1,1,4
B,0,0,5
B,0,1,6
B,1,0,7
B,1,1,8
```

Verify:

```bash
cat input.txt
```

## Step 5: Compile

```bash
javac -classpath "$(hadoop classpath)" *.java
```

## Step 6: Create the JAR

```bash
jar cf matrixmultiplication.jar *.class
```

## Step 7: Create HDFS Input Directory

```bash
hdfs dfs -mkdir -p /matrix_input
```

## Step 8: Upload Input

```bash
hdfs dfs -put input.txt /matrix_input
```

Verify:

```bash
hdfs dfs -ls /matrix_input
hdfs dfs -cat /matrix_input/input.txt
```

## Step 9: Remove Previous Output

```bash
hdfs dfs -rm -r -skipTrash /matrix_output
```

Ignore the error if the directory does not exist.

## Step 10: Execute the MapReduce Job

```bash
hadoop jar matrixmultiplication.jar MatrixMultiplication /matrix_input /matrix_output
```

## Step 11: View Output

```bash
hdfs dfs -ls /matrix_output
hdfs dfs -cat /matrix_output/part-r-00000
```

Expected:

```text
0,0    19
0,1    22
1,0    43
1,1    50
```

> **Note:** This implementation is configured for the 2 × 2 matrices used in this experiment. For arbitrary dimensions, the matrix dimensions should be supplied dynamically.

---

# PROGRAM / SOURCE CODE

## Mapper — `MapperClass.java`

```java
import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MapperClass
        extends Mapper<Object, Text, Text, Text> {

    private Text outputKey = new Text();
    private Text outputValue = new Text();

    // Matrix dimensions for this experiment
    private static final int ROWS_A = 2;
    private static final int COLS_B = 2;

    public void map(Object key, Text value, Context context)
            throws IOException, InterruptedException {

        String[] parts = value.toString().split(",");

        if (parts.length != 4) {
            return;
        }

        String matrix = parts[0];
        int row = Integer.parseInt(parts[1]);
        int column = Integer.parseInt(parts[2]);
        double val = Double.parseDouble(parts[3]);

        if (matrix.equals("A")) {

            // A[i][k] contributes to every C[i][j]
            for (int j = 0; j < COLS_B; j++) {

                outputKey.set(row + "," + j);
                outputValue.set("A," + column + "," + val);

                context.write(outputKey, outputValue);
            }

        } else if (matrix.equals("B")) {

            // B[k][j] contributes to every C[i][j]
            for (int i = 0; i < ROWS_A; i++) {

                outputKey.set(i + "," + column);
                outputValue.set("B," + row + "," + val);

                context.write(outputKey, outputValue);
            }
        }
    }
}
```

## Reducer — `ReducerClass.java`

```java
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class ReducerClass
        extends Reducer<Text, Text, Text, Text> {

    private Text result = new Text();

    public void reduce(Text key, Iterable<Text> values,
            Context context)
            throws IOException, InterruptedException {

        Map<Integer, Double> matrixA = new HashMap<>();
        Map<Integer, Double> matrixB = new HashMap<>();

        for (Text value : values) {

            String[] parts = value.toString().split(",");

            if (parts.length != 3) {
                continue;
            }

            String matrix = parts[0];
            int index = Integer.parseInt(parts[1]);
            double val = Double.parseDouble(parts[2]);

            if (matrix.equals("A")) {
                matrixA.put(index, val);
            } else if (matrix.equals("B")) {
                matrixB.put(index, val);
            }
        }

        double sum = 0.0;

        // C[i][j] = Σ A[i][k] × B[k][j]
        for (Integer k : matrixA.keySet()) {

            if (matrixB.containsKey(k)) {
                sum += matrixA.get(k) * matrixB.get(k);
            }
        }

        if (sum == (long) sum) {
            result.set(String.valueOf((long) sum));
        } else {
            result.set(String.valueOf(sum));
        }

        context.write(key, result);
    }
}
```

## Driver — `MatrixMultiplication.java`

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class MatrixMultiplication {

    public static void main(String[] args)
            throws Exception {

        Configuration conf = new Configuration();

        Job job = Job.getInstance(
                conf,
                "Matrix Multiplication"
        );

        job.setJarByClass(MatrixMultiplication.class);

        job.setMapperClass(MapperClass.class);
        job.setReducerClass(ReducerClass.class);

        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        FileInputFormat.addInputPath(
                job, new Path(args[0])
        );

        FileOutputFormat.setOutputPath(
                job, new Path(args[1])
        );

        System.exit(
                job.waitForCompletion(true) ? 0 : 1
        );
    }
}
```

---


# OUTPUT

## Input Matrices

### Matrix A

```text
1  2
3  4
```

### Matrix B

```text
5  6
7  8
```

## MapReduce Output

```text
0,0    19
0,1    22
1,0    43
1,1    50
```

## Final Matrix

```text
C = [19 22]
    [43 50]
```

## Observation Table

| Output Element | Calculation | Result |
|---|---|---:|
| C[0][0] | `(1×5) + (2×7)` | 19 |
| C[0][1] | `(1×6) + (2×8)` | 22 |
| C[1][0] | `(3×5) + (4×7)` | 43 |
| C[1][1] | `(3×6) + (4×8)` | 50 |

---

# RESULT

The **Matrix Multiplication program was successfully implemented and executed using the Hadoop MapReduce framework**.

For the given matrices:

```text
A = [1 2]
    [3 4]

B = [5 6]
    [7 8]
```

the resulting matrix was:

```text
C = [19 22]
    [43 50]
```

The result was successfully generated in HDFS.

---

# CONCLUSION

This experiment demonstrated how Hadoop MapReduce can be used to perform distributed matrix multiplication.


---

# 11. VIVA QUESTIONS

1. What is matrix multiplication?
2. What condition must be satisfied for two matrices to be multiplied?
3. What is the dimension of the product matrix?
4. Why is matrix multiplication suitable for MapReduce?
5. What is the Mapper key in this experiment?
6. What does the Mapper generate for an element of Matrix A?
7. What does the Mapper generate for an element of Matrix B?
8. What is the role of Shuffle and Sort?
9. What does the Reducer calculate?
10. What is the common index `k`?
11. Why is `(i,j)` used as the intermediate key?
12. What happens if matrix dimensions are incompatible?
13. What is HDFS?
14. Why must the MapReduce output directory not already exist?
15. What is the role of the Driver program?
16. What are some applications of matrix multiplication?
17. What is the conventional time complexity of multiplying two `n × n` matrices?
18. How can this program be modified to support arbitrary matrix dimensions?

---

# 12. IMPORTANT COMMANDS – QUICK REFERENCE

```bash
# Start Hadoop
start-dfs.sh
start-yarn.sh

# Verify services
jps

# Create project
mkdir MatrixMultiplication
cd MatrixMultiplication

# Compile
javac -classpath "$(hadoop classpath)" *.java

# Create JAR
jar cf matrixmultiplication.jar *.class

# Create HDFS input directory
hdfs dfs -mkdir -p /matrix_input

# Upload input
hdfs dfs -put input.txt /matrix_input

# Display input
hdfs dfs -cat /matrix_input/input.txt

# Remove previous output
hdfs dfs -rm -r -skipTrash /matrix_output

# Execute MapReduce
hadoop jar matrixmultiplication.jar MatrixMultiplication /matrix_input /matrix_output

# List output
hdfs dfs -ls /matrix_output

# Display output
hdfs dfs -cat /matrix_output/part-r-00000
```

---

# 13. COMPLETE EXPERIMENT WORKFLOW

```text
                         Start
                           |
                           v
                 Start HDFS and YARN
                           |
                           v
                Create Project Directory
                           |
                           v
                    Define Matrices
                           |
                           v
                  Create Mapper Program
                           |
                           v
                  Create Reducer Program
                           |
                           v
                  Create Driver Program
                           |
                           v
                  Compile Java Programs
                           |
                           v
                      Create JAR
                           |
                           v
               Create HDFS Input Directory
                           |
                           v
                    Upload Matrix Data
                           |
                           v
                   Remove Old Output
                           |
                           v
                Execute MapReduce Job
                           |
                           v
                        Mapper
                           |
                           v
               Generate Intermediate
                    Key-Value Pairs
                           |
                           v
                   Shuffle and Sort
                           |
                           v
                       Reducer
                           |
                           v
                    Calculate C[i][j]
                           |
                           v
                      HDFS Output
                           |
                           v
                    Verify Matrix
                           |
                           v
                          End
```

---

# 14. KEY LEARNING OUTCOMES

After completing this experiment, students should be able to:

- Explain matrix multiplication.
- Identify compatible matrix dimensions.
- Implement matrix multiplication using MapReduce.
- Generate suitable Mapper key-value pairs.
- Understand the role of the common index `k`.
- Explain Shuffle and Sort.
- Implement aggregation in a Reducer.
- Store and retrieve matrix data using HDFS.
- Compile and package Java MapReduce programs.
- Execute and verify a Hadoop MapReduce job.

---

# 15. EXTENSION ACTIVITIES

1. Modify the program to accept matrix dimensions as command-line arguments.
2. Implement multiplication of `2 × 3` and `3 × 2` matrices.
3. Extend the program to support larger matrices.
4. Read Matrix A and Matrix B from separate HDFS files.
5. Compare MapReduce matrix multiplication with conventional Java matrix multiplication.
6. Measure execution time for different matrix sizes.
