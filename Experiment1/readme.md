# Experiment 1: Installation and Configuration of Hadoop & HDFS File Management

## Aim

To install and configure Apache Hadoop in a Linux environment, explore the Hadoop Distributed File System (HDFS), and perform basic file management operations using Hadoop shell commands.

---

## Learning Objectives

After completing this experiment, students will be able to:

- Understand the Hadoop ecosystem.
- Install and configure Apache Hadoop.
- Verify Hadoop installation.
- Start and stop Hadoop services.
- Understand the Hadoop Distributed File System (HDFS).
- Execute commonly used Hadoop shell commands.
- Perform file and directory management in HDFS.
- Compare HDFS commands with traditional Linux file system commands.

---

## Software Requirements

| Software | Version |
|----------|---------|
| Ubuntu Linux | 22.04 LTS (or later) |
| Java JDK | 8 or above |
| Apache Hadoop | 3.x |
| SSH | Installed |
| Terminal | Ubuntu Terminal |

---

## Theory

### What is Hadoop?

Apache Hadoop is an open-source framework designed for distributed storage and processing of large datasets across clusters of computers. It uses the Hadoop Distributed File System (HDFS) for storage and MapReduce for parallel data processing.

### Core Components of Hadoop

- **HDFS (Hadoop Distributed File System):** Distributed storage system.
- **YARN (Yet Another Resource Negotiator):** Resource management and job scheduling.
- **MapReduce:** Parallel data processing framework.
- **Hadoop Common:** Common libraries and utilities required by Hadoop modules.

### HDFS Architecture

```text
                +----------------------+
                |       Client         |
                +----------+-----------+
                           |
                           |
                   +-------v-------+
                   |   NameNode    |
                   +-------+-------+
                           |
      ---------------------------------------------
      |                    |                      |
+-----v------+      +------v------+       +-------v------+
| DataNode 1 |      | DataNode 2  |       | DataNode 3   |
+------------+      +-------------+       +--------------+
```

The **NameNode** manages metadata, while **DataNodes** store the actual data blocks.

---

## Installation Steps

### Step 1: Update Ubuntu

```bash
sudo apt update
sudo apt upgrade
```

### Step 2: Install Java

```bash
sudo apt install openjdk-11-jdk
```

Verify installation:

```bash
java -version
```

### Step 3: Download Hadoop

```bash
wget https://downloads.apache.org/hadoop/common/hadoop-3.x.x/hadoop-3.x.x.tar.gz
```

Extract the archive:

```bash
tar -xvf hadoop-3.x.x.tar.gz
```

Move Hadoop to the installation directory:

```bash
sudo mv hadoop-3.x.x /usr/local/hadoop
```

### Step 4: Configure Environment Variables

Open the Bash configuration file:

```bash
nano ~/.bashrc
```

Add the following lines:

```bash
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

Reload the configuration:

```bash
source ~/.bashrc
```

### Step 5: Verify Hadoop Installation

```bash
hadoop version
```

---

## Starting Hadoop

### Format the NameNode

```bash
hdfs namenode -format
```

### Start HDFS

```bash
start-dfs.sh
```

### Verify Running Services

```bash
jps
```

Expected output:

```text
NameNode
DataNode
SecondaryNameNode
Jps
```

---

## Hadoop Shell Commands

### Display Hadoop Version

```bash
hadoop version
```

### Create a Directory

```bash
hdfs dfs -mkdir /lab
```

Create nested directories:

```bash
hdfs dfs -mkdir -p /lab/experiment1/input
```

### List Files and Directories

```bash
hdfs dfs -ls /
```

Recursive listing:

```bash
hdfs dfs -ls -R /
```

### Upload a File to HDFS

```bash
hdfs dfs -put sample.txt /lab
```

or

```bash
hdfs dfs -copyFromLocal sample.txt /lab
```

### Display File Contents

```bash
hdfs dfs -cat /lab/sample.txt
```

### Download a File from HDFS

```bash
hdfs dfs -get /lab/sample.txt
```

or

```bash
hdfs dfs -copyToLocal /lab/sample.txt
```

### Rename a File

```bash
hdfs dfs -mv /lab/sample.txt /lab/data.txt
```

### Copy a File

```bash
hdfs dfs -cp /lab/data.txt /lab/backup.txt
```

### Delete a File

```bash
hdfs dfs -rm /lab/data.txt
```

Delete a directory recursively:

```bash
hdfs dfs -rm -r /lab
```

### Check Disk Usage

```bash
hdfs dfs -du /lab
```

### Count Files and Directories

```bash
hdfs dfs -count /lab
```

### Display HDFS Report

```bash
hdfs dfsadmin -report
```

---

## File Management Tasks

### Task 1: Create a Directory

```bash
hdfs dfs -mkdir /DataAnalytics
```

### Task 2: Create a Subdirectory

```bash
hdfs dfs -mkdir /DataAnalytics/Input
```

### Task 3: Upload a File

```bash
hdfs dfs -put student.txt /DataAnalytics/Input
```

### Task 4: Verify the Uploaded File

```bash
hdfs dfs -ls /DataAnalytics/Input
```

### Task 5: Display the File Contents

```bash
hdfs dfs -cat /DataAnalytics/Input/student.txt
```

### Task 6: Rename the File

```bash
hdfs dfs -mv /DataAnalytics/Input/student.txt /DataAnalytics/Input/data.txt
```

### Task 7: Copy the File

```bash
hdfs dfs -cp /DataAnalytics/Input/data.txt /DataAnalytics/Input/backup.txt
```

### Task 8: Download the File

```bash
hdfs dfs -get /DataAnalytics/Input/data.txt
```

### Task 9: Delete the Backup File

```bash
hdfs dfs -rm /DataAnalytics/Input/backup.txt
```

### Task 10: Delete the Directory

```bash
hdfs dfs -rm -r /DataAnalytics
```

---

## Expected Outcome

Upon successful completion of this experiment, students will be able to:

- Install and configure Apache Hadoop.
- Start and verify Hadoop services.
- Understand the HDFS architecture.
- Execute common Hadoop shell commands.
- Perform file and directory operations in HDFS.
- Manage data stored in Hadoop Distributed File System.

---

## Viva Questions

1. What is Apache Hadoop?
2. What is HDFS?
3. What are the core components of Hadoop?
4. What is the role of the NameNode?
5. What is the function of a DataNode?
6. What is YARN?
7. What is the purpose of MapReduce?
8. How do you upload a file to HDFS?
9. How do you delete a directory in HDFS?
10. Differentiate between the Linux file system and HDFS.

---

## Conclusion

This experiment introduced the installation and configuration of Apache Hadoop and demonstrated the use of HDFS shell commands for managing files and directories. Students gained practical experience with the Hadoop environment, providing a strong foundation for future experiments involving distributed storage and big data processing.
