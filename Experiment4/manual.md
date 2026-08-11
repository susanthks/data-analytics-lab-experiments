# EXPERIMENT 4

# REMOVING STOP WORDS FROM TEXT FILES USING MAPREDUCE

---

## 1. AIM

To implement a **Hadoop MapReduce program to remove stop words from the given text files** and generate a filtered text output containing only meaningful words.

---

# 2. REQUIREMENTS

## 2.1 Hardware Requirements

- Computer/Laptop
- Minimum 4 GB RAM recommended
- Sufficient storage for Hadoop and HDFS data

## 2.2 Software Requirements

| Software | Version |
|---|---|
| Operating System | Ubuntu Linux 24.04 LTS |
| Java | JDK 8 or Hadoop-compatible JDK |
| Apache Hadoop | 3.4.0 |
| HDFS | Configured and running |
| YARN | Configured and running |

---

# 3. THEORY

## 3.1 Introduction

Text data often contains words that occur frequently but provide little useful information for analysis. Such words are called **stop words**.

Examples of common English stop words are:

```text
a
an
the
is
are
was
were
and
or
of
to
in
on
for
with
by
```

Stop-word removal is a common preprocessing technique used in:

- Natural Language Processing
- Text Mining
- Information Retrieval
- Search Engines
- Document Classification
- Sentiment Analysis
- Machine Learning

---

## 3.2 What are Stop Words?

Stop words are commonly occurring words that are usually removed during text preprocessing because they may contribute little semantic information to a particular analysis.

For example:

```text
Input:
Hadoop is a framework for big data processing.

After removing stop words:
Hadoop framework big data processing
```

Here:

```text
is
a
for
```

are treated as stop words.

> **Note:** The exact list of stop words depends on the application. In this experiment, a predefined list of common English stop words is used.

---

## 3.3 MapReduce Approach

The stop-word removal process can be implemented using the Mapper.

The Mapper:

1. Reads each input line.
2. Splits the line into words.
3. Converts each word to lowercase for comparison.
4. Checks whether the word belongs to the stop-word list.
5. Ignores the word if it is a stop word.
6. Emits the remaining words.

The Reducer receives the remaining words and writes them to the output.

---

## 3.4 Example

Consider:

```text
Hadoop is a framework for big data.
```

The Mapper examines each word:

| Word | Stop Word? | Action |
|---|---|---|
| Hadoop | No | Keep |
| is | Yes | Remove |
| a | Yes | Remove |
| framework | No | Keep |
| for | Yes | Remove |
| big | No | Keep |
| data | No | Keep |

Filtered result:

```text
Hadoop framework big data
```

---

## 3.5 MapReduce Workflow

```text
                  Input Text File
                         |
                         v
                  +-------------+
                  |    Mapper   |
                  +-------------+
                         |
                         v
              Check Stop-Word List
                    /        \
                  Yes         No
                   |           |
                   v           v
                Remove       Keep
                               |
                               v
                        Shuffle and Sort
                               |
                               v
                         +-----------+
                         |  Reducer  |
                         +-----------+
                               |
                               v
                       Filtered Output
```

---

# 4. ALGORITHM

### Algorithm: Stop-Word Removal Using MapReduce

**Step 1:** Start HDFS and YARN services.

**Step 2:** Create a project directory.

**Step 3:** Define a list of common English stop words.

**Step 4:** Create the Mapper program.

**Step 5:** Read the input text line by line.

**Step 6:** Split each line into individual words.

**Step 7:** Normalize each word for comparison by converting it to lowercase.

**Step 8:** Check whether the word exists in the stop-word list.

**Step 9:** If the word is a stop word, discard it.

**Step 10:** Otherwise, emit the word from the Mapper.

**Step 11:** The Shuffle and Sort phase groups the Mapper output.

**Step 12:** The Reducer writes the remaining words.

**Step 13:** Compile and package the Java program.

**Step 14:** Upload the input text file to HDFS.

**Step 15:** Execute the MapReduce job.

**Step 16:** Display and verify the filtered output.

---

# 5. PROCEDURE

## Step 1: Start Hadoop Services

Start HDFS:

```bash
start-dfs.sh
```

Start YARN:

```bash
start-yarn.sh
```

Verify:

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

---

## Step 2: Create the Project Directory

```bash
mkdir StopWordRemoval
cd StopWordRemoval
```

---

## Step 3: Create the Mapper Program

Create:

```bash
nano MapperClass.java
```

Enter the Mapper program given in **Section 6.1**.

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

## Step 4: Create the Reducer Program

Create:

```bash
nano ReducerClass.java
```

Enter the Reducer program given in **Section 6.2**.

Save and exit.

---

## Step 5: Create the Driver Program

Create:

```bash
nano RemoveStopWords.java
```

Enter the Driver program given in **Section 6.3**.

Save and exit.

---

## Step 6: Create the Input File

Create:

```bash
nano input.txt
```

Enter the following sample text:

```text
Hadoop is a framework for big data processing.
The Hadoop framework is used for processing large datasets.
MapReduce is a programming model for processing data.
```

Save and exit.

---

## Step 7: Verify the Project Files

Run:

```bash
ls
```

Expected:

```text
MapperClass.java
ReducerClass.java
RemoveStopWords.java
input.txt
```

Display the input:

```bash
cat input.txt
```

---

## Step 8: Compile the Java Programs

Compile:

```bash
javac -classpath "$(hadoop classpath)" *.java
```

Verify:

```bash
ls
```

The following class files should be generated:

```text
MapperClass.class
ReducerClass.class
RemoveStopWords.class
```

> **Note:** If a Java class-file compatibility error occurs, verify the installed Java version using `java -version` and ensure that it is compatible with the Hadoop installation.

---

## Step 9: Create the JAR File

```bash
jar cf stopword.jar *.class
```

Verify:

```bash
ls
```

---

## Step 10: Create the HDFS Input Directory

```bash
hdfs dfs -mkdir -p /stopword_input
```

Verify:

```bash
hdfs dfs -ls /
```

---

## Step 11: Upload the Input File to HDFS

```bash
hdfs dfs -put input.txt /stopword_input
```

Verify:

```bash
hdfs dfs -ls /stopword_input
```

Display the file:

```bash
hdfs dfs -cat /stopword_input/input.txt
```

---

## Step 12: Remove Previous Output Directory

Hadoop requires the MapReduce output directory to be absent before running the job.

Remove any previous output:

```bash
hdfs dfs -rm -r -skipTrash /stopword_output
```

If the directory does not exist, the error can be ignored.

---

## Step 13: Execute the MapReduce Job

Run:

```bash
hadoop jar stopword.jar RemoveStopWords /stopword_input /stopword_output
```

The arguments are:

| Argument | Description |
|---|---|
| `stopword.jar` | MapReduce application JAR |
| `RemoveStopWords` | Driver class |
| `/stopword_input` | HDFS input directory |
| `/stopword_output` | HDFS output directory |

---

## Step 14: Check the Output Directory

```bash
hdfs dfs -ls /stopword_output
```

Expected:

```text
_SUCCESS
part-r-00000
```

---

## Step 15: Display the Output

```bash
hdfs dfs -cat /stopword_output/part-r-00000
```

Expected output will contain the words after stop-word removal.

For example:

```text
Hadoop
framework
big
data
processing
Hadoop
framework
used
processing
large
datasets
MapReduce
programming
model
processing
data
```

> **Note:** The exact order of the output depends on the MapReduce key sorting and the input split structure. The output may contain one word per line.

---

# 6. PROGRAM / SOURCE CODE

## 6.1 Mapper Program — `MapperClass.java`

```java
import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MapperClass
        extends Mapper<Object, Text, Text, Text> {

    private final Set<String> stopWords = new HashSet<>(
        Arrays.asList(
            "a", "an", "the",
            "is", "are", "was", "were",
            "and", "or",
            "of", "to", "in", "on",
            "for", "with", "by",
            "from", "at", "as",
            "be", "this", "that",
            "it", "its",
            "has", "have", "had",
            "will", "would",
            "can", "could",
            "should", "do", "does", "did"
        )
    );

    private Text outputKey = new Text();
    private Text outputValue = new Text();

    public void map(Object key, Text value, Context context)
            throws IOException, InterruptedException {

        String line = value.toString();

        String[] words = line.split("\\s+");

        for (String word : words) {

            word = word.replaceAll(
                    "^[^a-zA-Z]+|[^a-zA-Z]+$",
                    ""
            );

            if (word.isEmpty()) {
                continue;
            }

            String lowerWord = word.toLowerCase();

            if (!stopWords.contains(lowerWord)) {

                outputKey.set(lowerWord);
                outputValue.set(word);

                context.write(outputKey, outputValue);
            }
        }
    }
}
```

### Description

The Mapper:

1. Reads each line.
2. Splits it into words.
3. Removes leading and trailing punctuation.
4. Converts the word to lowercase for stop-word comparison.
5. Checks the stop-word set.
6. Discards stop words.
7. Emits non-stop words.

---

## 6.2 Reducer Program — `ReducerClass.java`

```java
import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class ReducerClass
        extends Reducer<Text, Text, Text, Text> {

    private Text output = new Text();

    public void reduce(Text key, Iterable<Text> values,
            Context context)
            throws IOException, InterruptedException {

        for (Text value : values) {
            output.set(value.toString());
            context.write(key, output);
        }
    }
}
```

### Description

The Reducer receives the remaining words from the Mapper and writes them to the output.

The key is the normalized lowercase word, while the value contains the original word.

For example:

```text
hadoop    Hadoop
framework framework
```

The output key is used by Hadoop for sorting.

---

## 6.3 Driver Program — `RemoveStopWords.java`

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class RemoveStopWords {

    public static void main(String[] args) throws Exception {

        Configuration conf = new Configuration();

        Job job = Job.getInstance(
                conf,
                "Remove Stop Words"
        );

        job.setJarByClass(RemoveStopWords.class);

        job.setMapperClass(MapperClass.class);

        job.setReducerClass(ReducerClass.class);

        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        FileInputFormat.addInputPath(
                job,
                new Path(args[0])
        );

        FileOutputFormat.setOutputPath(
                job,
                new Path(args[1])
        );

        System.exit(
                job.waitForCompletion(true) ? 0 : 1
        );
    }
}
```

---

# 7. OUTPUT

## 7.1 Input

```text
Hadoop is a framework for big data processing.
The Hadoop framework is used for processing large datasets.
MapReduce is a programming model for processing data.
```

---

## 7.2 Stop Words Removed

For this experiment, words such as the following are removed:

```text
is
a
the
for
and
of
to
in
on
with
```

---

## 7.3 Filtered Output

Command:

```bash
hdfs dfs -cat /stopword_output/part-r-00000
```

Sample output:

```text
big    big
data   data
data   data
datasets datasets
framework framework
framework framework
Hadoop Hadoop
Hadoop Hadoop
large large
MapReduce MapReduce
model model
processing processing
processing processing
processing processing
programming programming
used used
```

The output is sorted by the normalized key.

---

## 7.4 Cleaner Final Text

The significant words extracted from the input are:

```text
Hadoop framework big data processing
Hadoop framework used processing large datasets
MapReduce programming model processing data
```

---

## 7.5 Observation

| Input Word | Stop Word? | Result |
|---|:---:|---|
| Hadoop | No | Retained |
| is | Yes | Removed |
| a | Yes | Removed |
| framework | No | Retained |
| for | Yes | Removed |
| big | No | Retained |
| data | No | Retained |
| processing | No | Retained |
| the | Yes | Removed |
| used | No | Retained |
| large | No | Retained |
| datasets | No | Retained |
| MapReduce | No | Retained |
| programming | No | Retained |
| model | No | Retained |

---

# 8. RESULT

The **MapReduce program for removing stop words from the given text file was successfully implemented and executed using Apache Hadoop**.

The Mapper identified and removed predefined stop words, while the remaining meaningful words were processed by the Reducer and stored in the HDFS output directory.

---

# 9. CONCLUSION

This experiment demonstrated the use of Hadoop MapReduce for **text preprocessing and stop-word removal**.

The experiment provided practical understanding of:

- Text preprocessing.
- Stop-word identification.
- Mapper-based filtering.
- Key-value pair generation.
- Shuffle and Sort.
- Reducer processing.
- HDFS input and output.
- Execution of a Java MapReduce application.

Stop-word removal is an important preprocessing step in many **Natural Language Processing and Big Data analytics applications**.

---

# 10. VIVA QUESTIONS

### 1. What are stop words?

Stop words are frequently occurring words that are often removed during text preprocessing because they may provide limited useful information for a particular analysis.

### 2. Give some examples of stop words.

Examples include:

```text
a, an, the, is, are, and, of, to, in, for
```

### 3. What is the objective of this experiment?

To remove predefined stop words from text files using Hadoop MapReduce.

### 4. Which MapReduce phase performs the stop-word filtering?

The **Mapper** performs the stop-word filtering.

### 5. Why is stop-word removal useful?

It can reduce unnecessary textual information and simplify subsequent text-processing tasks.

### 6. What happens to a word if it is found in the stop-word set?

The Mapper discards it and does not emit it.

### 7. What happens to a word that is not a stop word?

The Mapper emits it for further MapReduce processing.

### 8. Why are words converted to lowercase?

Lowercase conversion allows words such as `The` and `the` to be compared consistently against the stop-word list.

### 9. What is the purpose of the stop-word `HashSet`?

A `HashSet` provides an efficient way to check whether a word belongs to the predefined stop-word collection.

### 10. Why is punctuation removed?

Removing leading and trailing punctuation prevents words such as:

```text
"data,"
```

from being treated differently from:

```text
data
```

### 11. What is the role of the Reducer in this program?

The Reducer receives the words that survived the Mapper's stop-word filtering and writes the final output.

### 12. Can stop-word removal be performed entirely in the Mapper?

Yes. Since stop-word removal is a filtering operation, the actual removal can be performed entirely in the Mapper. A Reducer is included in this experiment to demonstrate the complete MapReduce workflow.

### 13. Why can the Reducer be avoided for a filtering-only application?

If no aggregation or grouping is required, the Mapper can directly write the filtered records. This can be implemented using a Map-only job.

### 14. What is HDFS?

HDFS stands for **Hadoop Distributed File System** and provides distributed storage for Hadoop.

### 15. Why must the output directory not already exist?

Hadoop normally does not allow a MapReduce job to overwrite an existing output directory.

### 16. What command uploads a file to HDFS?

```bash
hdfs dfs -put input.txt /stopword_input
```

### 17. What command displays the HDFS output?

```bash
hdfs dfs -cat /stopword_output/part-r-00000
```

### 18. What are some applications of stop-word removal?

- Text mining
- Search engines
- Document classification
- Sentiment analysis
- Information retrieval
- Natural Language Processing
- Text clustering

---

# 11. IMPORTANT COMMANDS – QUICK REFERENCE

```bash
# Start Hadoop services
start-dfs.sh
start-yarn.sh

# Verify Hadoop services
jps

# Create project
mkdir StopWordRemoval
cd StopWordRemoval

# Compile
javac -classpath "$(hadoop classpath)" *.java

# Create JAR
jar cf stopword.jar *.class

# Create HDFS input directory
hdfs dfs -mkdir -p /stopword_input

# Upload input file
hdfs dfs -put input.txt /stopword_input

# Display input
hdfs dfs -cat /stopword_input/input.txt

# Remove previous output
hdfs dfs -rm -r -skipTrash /stopword_output

# Execute MapReduce
hadoop jar stopword.jar RemoveStopWords /stopword_input /stopword_output

# List output
hdfs dfs -ls /stopword_output

# Display output
hdfs dfs -cat /stopword_output/part-r-00000
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
              Create Project Directory
                         |
                         v
                 Create Stop-Word Set
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
                    Create Input File
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
                 Upload Input to HDFS
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
                Check Stop-Word List
                     /         \
                   Yes          No
                    |            |
                    v            v
                 Remove        Keep
                                  |
                                  v
                         Shuffle and Sort
                                  |
                                  v
                              Reducer
                                  |
                                  v
                           HDFS Output
                                  |
                                  v
                           Verify Result
                                  |
                                  v
                                 End
```

---

# 13. KEY LEARNING OUTCOMES

After completing this experiment, the student should be able to:

- Define stop words and explain their importance.
- Implement stop-word filtering using Hadoop MapReduce.
- Create and use a stop-word collection.
- Perform text preprocessing in a Mapper.
- Generate and process Hadoop key-value pairs.
- Understand the role of Shuffle and Sort.
- Implement a Reducer for filtered data.
- Store and retrieve data using HDFS.
- Compile, package, and execute a Java MapReduce application.
- Explain applications of stop-word removal in NLP and Big Data Analytics.

---

# 14. EXTENSION ACTIVITY

Modify the program to:

1. Read the stop-word list from a separate file stored in HDFS.
2. Remove punctuation from all words.
3. Perform stemming after stop-word removal.
4. Calculate the frequency of the remaining words.
5. Compare the number of words before and after stop-word removal.
6. Implement the same task using a **Map-only job** and compare it with the Mapper-Reducer implementation.
