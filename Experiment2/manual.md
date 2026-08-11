# EXPERIMENT 2

# IMPLEMENTING WORD COUNT USING MAPREDUCE

---

## 1. AIM

To implement a **Word Count program using the Hadoop MapReduce framework** to determine the number of occurrences of each word in a given input text file.

---

## 2. REQUIREMENTS

### 2.1 Hardware Requirements

- Computer/Laptop
- Minimum 4 GB RAM recommended
- Sufficient storage for Hadoop installation and HDFS data

### 2.2 Software Requirements

| Software | Version |
|---|---|
| Operating System | Ubuntu Linux 24.04 LTS |
| Java | JDK 8 or Hadoop-compatible JDK |
| Apache Hadoop | 3.4.0 |
| HDFS | Configured and running |
| YARN | Configured and running |

---

## 3. THEORY

### 3.1 Introduction to MapReduce

**MapReduce** is a distributed programming model used by Apache Hadoop to process large datasets.

A MapReduce application primarily consists of:

1. **Mapper**
2. **Shuffle and Sort**
3. **Reducer**

The input data is divided into smaller portions and processed by Mapper tasks. The intermediate results are then grouped and sorted by Hadoop before being passed to Reducer tasks.

---

### 3.2 Mapper

The **Mapper** processes the input data and produces intermediate key-value pairs.

For a Word Count application, each word is emitted with a value of `1`.

For example:

```text
Input:
Hadoop is powerful
```

Mapper output:

```text
(Hadoop, 1)
(is, 1)
(powerful, 1)
```

---

### 3.3 Shuffle and Sort

The **Shuffle and Sort** phase is handled by the Hadoop framework.

During this phase:

- Intermediate Mapper output is collected.
- Records having the same key are grouped together.
- Keys are sorted.
- Grouped key-value pairs are passed to the Reducer.

Example:

```text
Mapper Output:

(Hadoop,1)
(is,1)
(Hadoop,1)
(is,1)
```

After Shuffle and Sort:

```text
(Hadoop,[1,1])
(is,[1,1])
```

---

### 3.4 Reducer

The **Reducer** receives a key and a list of values and performs the required aggregation.

For Word Count:

```text
(Hadoop,[1,1])
```

is reduced to:

```text
(Hadoop,2)
```

Thus, the Reducer calculates the total number of occurrences of each word.

---

### 3.5 Word Count Example

Consider the following input:

```text
Hadoop is big data
Hadoop is fast
Big data is useful
```

The Mapper generates word-count pairs. The Mapper used in this experiment converts words to lowercase.

After Shuffle and Sort:

```text
big     [1,1]
data    [1,1]
fast    [1]
hadoop  [1,1]
is      [1,1,1]
useful  [1]
```

The Reducer generates:

```text
big      2
data     2
fast     1
hadoop   2
is       3
useful   1
```

---

### 3.6 MapReduce Workflow

```text
                 Input File
                      |
                      v
              +---------------+
              |    Mapper     |
              +---------------+
                      |
                      v
        Intermediate Key-Value Pairs
                      |
                      v
              Shuffle and Sort
                      |
                      v
              +---------------+
              |    Reducer    |
              +---------------+
                      |
                      v
                Final Output
```

---

## 4. ALGORITHM

### Algorithm: Word Count Using Hadoop MapReduce

**Step 1:** Start Hadoop HDFS and YARN services.

**Step 2:** Create a project directory named `WordCount`.

**Step 3:** Create the Mapper class.

**Step 4:** Create the Reducer class.

**Step 5:** Create the Driver class.

**Step 6:** Create the input text file.

**Step 7:** Compile the Java source files using the Hadoop classpath.

**Step 8:** Create a JAR file containing the compiled class files.

**Step 9:** Create an input directory in HDFS.

**Step 10:** Upload the input text file to HDFS.

**Step 11:** Execute the MapReduce job by specifying the HDFS input and output directories.

**Step 12:** List the HDFS output directory.

**Step 13:** Display the generated word-count output.

**Step 14:** Verify the word frequencies with the original input.

---

# 5. PROCEDURE

## Step 1: Open the Terminal

Press:

```text
Ctrl + Alt + T
```

to open the Ubuntu terminal.

---

## Step 2: Start Hadoop Services

Start HDFS:

```bash
start-dfs.sh
```

Start YARN:

```bash
start-yarn.sh
```

Verify the running Hadoop services:

```bash
jps
```

Expected output is similar to:

```text
NameNode
DataNode
SecondaryNameNode
ResourceManager
NodeManager
Jps
```

> **Note:** The exact list of processes may vary depending on the Hadoop configuration.

---

## Step 3: Create the Project Directory

Create a directory named `WordCount`:

```bash
mkdir WordCount
```

Move into the directory:

```bash
cd WordCount
```

---

## Step 4: Create the Mapper File

Create the Mapper source file:

```bash
nano MapperClass.java
```

Enter the Mapper program given in **Section 6.1**.

Save the file:

```text
Ctrl + O
Enter
```

Exit:

```text
Ctrl + X
```

---

## Step 5: Create the Reducer File

Create the Reducer source file:

```bash
nano ReducerClass.java
```

Enter the Reducer program given in **Section 6.2**.

Save:

```text
Ctrl + O
Enter
```

Exit:

```text
Ctrl + X
```

---

## Step 6: Create the Driver File

Create the Driver source file:

```bash
nano WordCount.java
```

Enter the Driver program given in **Section 6.3**.

Save:

```text
Ctrl + O
Enter
```

Exit:

```text
Ctrl + X
```

---

## Step 7: Create the Input File

Create the input file:

```bash
nano input.txt
```

Enter:

```text
Hadoop is big data
Hadoop is fast
Big data is useful
```

Save:

```text
Ctrl + O
Enter
```

Exit:

```text
Ctrl + X
```

---

## Step 8: Verify the Project Files

Run:

```bash
ls
```

The directory should contain:

```text
MapperClass.java
ReducerClass.java
WordCount.java
input.txt
```

Display the input:

```bash
cat input.txt
```

Expected:

```text
Hadoop is big data
Hadoop is fast
Big data is useful
```

---

## Step 9: Compile the Java Files

Compile the Java source files using the Hadoop classpath:

```bash
javac -classpath "$(hadoop classpath)" *.java
```

After successful compilation, verify:

```bash
ls
```

The following `.class` files should be present:

```text
MapperClass.class
ReducerClass.class
WordCount.class
```

> **Troubleshooting:** If Java compatibility or `class file version` errors are displayed, check the installed Java version using:
>
> ```bash
> java -version
> ```
>
> and ensure that the Java version is compatible with the installed Hadoop environment.

---

## Step 10: Create the JAR File

Create the JAR file:

```bash
jar cf wordcount.jar *.class
```

Verify:

```bash
ls
```

The project directory should now contain:

```text
MapperClass.java
MapperClass.class
ReducerClass.java
ReducerClass.class
WordCount.java
WordCount.class
input.txt
wordcount.jar
```

---

## Step 11: Create the HDFS Input Directory

Create the input directory:

```bash
hdfs dfs -mkdir -p /input
```

Verify:

```bash
hdfs dfs -ls /
```

---

## Step 12: Upload the Input File to HDFS

Upload `input.txt` to HDFS:

```bash
hdfs dfs -put input.txt /input
```

Verify:

```bash
hdfs dfs -ls /input
```

Expected:

```text
input.txt
```

Display the file from HDFS:

```bash
hdfs dfs -cat /input/input.txt
```

---

## Step 13: Remove Previous Output Directory

Before executing the MapReduce job, ensure that `/output` does not already exist.

If it exists, remove it:

```bash
hdfs dfs -rm -r -skipTrash /output
```

> **Important:** Hadoop generally requires the MapReduce output directory to be absent before a job is executed.

If `/output` does not exist, an error may be displayed. This can be ignored.

---

## Step 14: Execute the MapReduce Job

Run:

```bash
hadoop jar wordcount.jar WordCount /input /output
```

The arguments are:

| Argument | Description |
|---|---|
| `wordcount.jar` | MapReduce application JAR |
| `WordCount` | Driver class |
| `/input` | HDFS input directory |
| `/output` | HDFS output directory |

The execution follows:

```text
Input
  |
  v
Mapper
  |
  v
Shuffle and Sort
  |
  v
Reducer
  |
  v
HDFS Output
```

Wait until the job completes successfully.

---

## Step 15: Verify the Output Directory

List the output directory:

```bash
hdfs dfs -ls /output
```

Expected files include:

```text
_SUCCESS
part-r-00000
```

---

## Step 16: Display the Output

Run:

```bash
hdfs dfs -cat /output/part-r-00000
```

Expected output:

```text
big     2
data    2
fast    1
hadoop  2
is      3
useful  1
```

> **Note:** The spacing between the word and count may vary depending on the terminal display.

---

# 6. PROGRAM / SOURCE CODE

## 6.1 Mapper Program — `MapperClass.java`

```java
import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MapperClass
        extends Mapper<Object, Text, Text, IntWritable> {

    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(Object key, Text value, Context context)
            throws IOException, InterruptedException {

        String[] words = value.toString().split("\\s+");

        for (String w : words) {
            word.set(w.toLowerCase());
            context.write(word, one);
        }
    }
}
```

### Description

The Mapper:

1. Reads each input line.
2. Splits the line into words.
3. Converts each word to lowercase.
4. Emits `(word, 1)` for every word.

---

## 6.2 Reducer Program — `ReducerClass.java`

```java
import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class ReducerClass
        extends Reducer<Text, IntWritable, Text, IntWritable> {

    public void reduce(Text key, Iterable<IntWritable> values,
            Context context)
            throws IOException, InterruptedException {

        int sum = 0;

        for (IntWritable value : values) {
            sum += value.get();
        }

        context.write(key, new IntWritable(sum));
    }
}
```

### Description

The Reducer:

1. Receives each word as a key.
2. Receives all associated count values.
3. Adds the values.
4. Writes the final word count.

---

## 6.3 Driver Program — `WordCount.java`

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCount {

    public static void main(String[] args) throws Exception {

        Configuration conf = new Configuration();

        Job job = Job.getInstance(conf, "Word Count");

        job.setJarByClass(WordCount.class);

        job.setMapperClass(MapperClass.class);

        job.setReducerClass(ReducerClass.class);

        job.setOutputKeyClass(Text.class);

        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(
                job, new Path(args[0]));

        FileOutputFormat.setOutputPath(
                job, new Path(args[1]));

        System.exit(
                job.waitForCompletion(true) ? 0 : 1
        );
    }
}
```

### Description

The Driver:

- Configures the MapReduce job.
- Specifies the Mapper.
- Specifies the Reducer.
- Specifies input and output paths.
- Starts the MapReduce execution.

---

# 7. OUTPUT

## 7.1 Input

The input file `input.txt` contains:

```text
Hadoop is big data
Hadoop is fast
Big data is useful
```

---

## 7.2 HDFS Input

Command:

```bash
hdfs dfs -cat /input/input.txt
```

Output:

```text
Hadoop is big data
Hadoop is fast
Big data is useful
```

---

## 7.3 MapReduce Execution

Command:

```bash
hadoop jar wordcount.jar WordCount /input /output
```

The Hadoop framework processes the input through:

```text
Mapper → Shuffle and Sort → Reducer
```

---

## 7.4 HDFS Output

Command:

```bash
hdfs dfs -cat /output/part-r-00000
```

Output:

```text
big     2
data    2
fast    1
hadoop  2
is      3
useful  1
```

---

## 7.5 Observation Table

| Sl. No. | Word | Frequency |
|---:|---|---:|
| 1 | big | 2 |
| 2 | data | 2 |
| 3 | fast | 1 |
| 4 | hadoop | 2 |
| 5 | is | 3 |
| 6 | useful | 1 |

---

# 8. RESULT

The **Word Count program was successfully implemented using the Hadoop MapReduce framework**. The input text file was stored in HDFS, processed through the Mapper, Shuffle and Sort, and Reducer stages, and the frequency of each word was successfully generated in the HDFS output directory.

---

# 9. CONCLUSION

The experiment provided practical knowledge of implementing a basic MapReduce application using Java and Apache Hadoop.

The experiment demonstrated:

- Creation of a Mapper.
- Creation of a Reducer.
- Configuration using a Driver program.
- Compilation using Hadoop libraries.
- Creation of a JAR file.
- Uploading input data to HDFS.
- Execution of a MapReduce job.
- Retrieval and verification of the output.

Thus, the experiment helped in understanding the fundamental workflow of **Hadoop MapReduce-based distributed data processing**.

---

# 10. VIVA QUESTIONS

### 1. What is Hadoop MapReduce?

MapReduce is a distributed programming model used by Hadoop to process large datasets in parallel.

### 2. What are the major stages of MapReduce?

The major stages are:

- Map
- Shuffle and Sort
- Reduce

### 3. What is the function of the Mapper?

The Mapper processes input data and generates intermediate key-value pairs.

### 4. What is the output of the Mapper in Word Count?

The Mapper generates:

```text
(word, 1)
```

for every word.

### 5. What is the function of the Reducer?

The Reducer receives grouped values for each key and performs aggregation to generate the final result.

### 6. What happens during Shuffle and Sort?

Hadoop groups intermediate records having the same key and sorts the keys before passing them to the Reducer.

### 7. Why is Word Count commonly used to demonstrate MapReduce?

Word Count is a simple application that clearly demonstrates the complete MapReduce processing workflow.

### 8. What is a key-value pair?

A key-value pair consists of a key and its associated value.

Example:

```text
(hadoop, 1)
```

### 9. What is HDFS?

HDFS stands for **Hadoop Distributed File System** and is the distributed storage system used by Hadoop.

### 10. Why should the output directory not already exist?

Hadoop normally requires the output directory to be absent before a MapReduce job starts to prevent overwriting existing output.

### 11. What is the purpose of the Driver program?

The Driver configures and submits the MapReduce job and specifies the Mapper, Reducer, input path, and output path.

### 12. What is the purpose of a JAR file?

A JAR file packages the compiled Java classes required to execute the MapReduce application.

### 13. What is `IntWritable`?

`IntWritable` is Hadoop's serializable wrapper for an integer value.

### 14. What is `Text` in Hadoop?

`Text` is Hadoop's writable type used to represent text/string data.

### 15. What is the purpose of `hdfs dfs -put`?

It copies a local file into HDFS.

Example:

```bash
hdfs dfs -put input.txt /input
```

### 16. What is the purpose of `hdfs dfs -cat`?

It displays the contents of a file stored in HDFS.

### 17. What does the command `hadoop jar` do?

It executes a Hadoop MapReduce application packaged in a JAR file.

---

# 11. IMPORTANT COMMANDS – QUICK REFERENCE

```bash
# Start Hadoop services
start-dfs.sh
start-yarn.sh

# Verify Hadoop services
jps

# Create project
mkdir WordCount
cd WordCount

# Compile Java files
javac -classpath "$(hadoop classpath)" *.java

# Create JAR
jar cf wordcount.jar *.class

# Create HDFS input directory
hdfs dfs -mkdir -p /input

# Upload input file
hdfs dfs -put input.txt /input

# Display HDFS input
hdfs dfs -cat /input/input.txt

# Remove previous output
hdfs dfs -rm -r -skipTrash /output

# Execute MapReduce job
hadoop jar wordcount.jar WordCount /input /output

# List output
hdfs dfs -ls /output

# Display output
hdfs dfs -cat /output/part-r-00000
```

---

# 12. COMPLETE EXPERIMENT WORKFLOW

```text
                Start
                  |
                  v
        Start HDFS and YARN
                  |
                  v
        Create WordCount Folder
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
          Create input.txt
                  |
                  v
          Compile Java Files
                  |
                  v
          Create JAR File
                  |
                  v
       Create HDFS /input Folder
                  |
                  v
       Upload input.txt to HDFS
                  |
                  v
       Remove Existing /output
                  |
                  v
       Execute MapReduce Job
                  |
                  v
              Mapper
                  |
                  v
        Shuffle and Sort
                  |
                  v
              Reducer
                  |
                  v
          HDFS /output
                  |
                  v
        part-r-00000
                  |
                  v
          Verify Word Count
                  |
                  v
                 End
```

---

## 13. KEY LEARNING OUTCOMES

After completing this experiment, the student should be able to:

- Explain the MapReduce programming model.
- Differentiate between Mapper and Reducer.
- Explain the Shuffle and Sort phase.
- Develop a basic Java MapReduce application.
- Compile and package a Hadoop application.
- Work with input and output data in HDFS.
- Execute a MapReduce job.
- Interpret MapReduce output.
