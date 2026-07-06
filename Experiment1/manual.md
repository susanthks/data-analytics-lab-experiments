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
| Ubuntu Linux | 24.04 LTS |
| Java JDK | 8 or above |
| Apache Hadoop | 3.4.0|
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
```

### Step 2: Install Java

```bash
sudo apt install openjdk-8-jdk
```

Verify the installation:

```bash
java -version
```

---
### Step 3: Install SSH

SSH is crucial for secure communication between nodes in a Hadoop cluster. It enables secure data transfer, remote administration, and coordination among distributed components, ensuring the integrity and confidentiality of the system.

The command to install SSH on Ubuntu is:

```bash
sudo apt install ssh
sudo apt-get install pdsh
```

### Step 4: Create a Dedicated Hadoop User

Create a new user named `hadoop`:

```bash
sudo adduser hadoop
```

Add the user to the sudo group:

```bash
sudo usermod -aG sudo hadoop
```

Switch to the Hadoop user:

```bash
su - hadoop
```

Verify the current user:

```bash
whoami
```

Expected output:

```text
hadoop
```

---

### Step 5: Configure SSH

Create an SSH key for the ‘hadoop’ user without a password to enable easy and secure access.


Generate an SSH key:

```bash
ssh-keygen -t rsa
```
<img width="720" height="453" alt="image" src="https://github.com/user-attachments/assets/976ad1c6-008c-4c8d-8bf8-54b0c2e17a8a" />

Transfer the generated public key to the authorized keys file and set permissions to ensure secure access.

### Step 6: Set Permission

```bash
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys 
chmod 640 ~/.ssh/authorized_keys
```
<img width="720" height="60" alt="image" src="https://github.com/user-attachments/assets/d3390613-8b2e-4516-b2a3-2314d20cdb63" />

Test SSH login:

```bash
ssh localhost
```

Exit the SSH session:

```bash
exit
```

---
### Step 7: Switch user Hadoop

```bash
su — hadoop
```
<img width="720" height="69" alt="image" src="https://github.com/user-attachments/assets/3753de1c-9fb2-4cb6-a4a9-374e02288c4c" />

---

### Step 8: Download Hadoop

Download the Hadoop package:

```bash
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.4.0/hadoop-3.4.0.tar.gz
```

Extract the archive:

```bash
tar -xvzf hadoop-3.4.0.tar.gz
```

Rename the extracted directory:

```bash
mv hadoop-3.4.0 hadoop
```

---

### Step 9: Configure Environment Variables

Edit the Bash configuration file:

```bash
nano ~/.bashrc
```

Add the following lines:

```bash
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export HADOOP_HOME=/home/hadoop/hadoop
export HADOOP_INSTALL=$HADOOP_HOME
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export HADOOP_YARN_HOME=$HADOOP_HOME
export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin
export HADOOP_OPTS=”-Djava.library.path=$HADOOP_HOME/lib/native”
```
<img width="720" height="449" alt="image" src="https://github.com/user-attachments/assets/90aaa79c-dbab-47fa-bdf4-15fd6868f017" />


Reload the configuration:

```bash
source ~/.bashrc
```
Open the Hadoop environment variable file in the nano text editor:

```bash
nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh
```
---
In the opened file, locate the line with “export JAVA_HOME” and configure it:

```bash
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```
<img width="720" height="449" alt="image" src="https://github.com/user-attachments/assets/e6bbdbed-027c-49ad-b691-5e32c71380d8" />

### Step 9: Configuring Hadoop

```bash
cd hadoop/
```

Open core-site.xml to configure the Hadoop file system. Update “fs.defaultFS” with your system hostname:

```bash
nano $HADOOP_HOME/etc/hadoop/core-site.xml
```

Add the following lines to the file:

```bash
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://localhost:9000</value>
    </property>
</configuration>
```
Open hdfs-site.xml to configure Namenode and Datanode directories:

```bash
nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```

Add the following lines to the file:

```bash
configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:///home/hadoop/hadoopdata/hdfs/namenode</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:///home/hadoop/hadoopdata/hdfs/datanode</value>
    </property>
 </configuration>
```


Verify the environment variables:

```bash
echo $HADOOP_HOME
```

---

### Step 10: Verify Hadoop Installation

```bash
hadoop version
```

---

### Step 11: Format the NameNode

```bash
hdfs namenode -format
```

---

### Step 12: Start HDFS

```bash
start-dfs.sh
```

Verify the running services:

```bash
jps
```

### Expected output:

```text
NameNode
DataNode
SecondaryNameNode
Jps
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
---

## Result

Apache Hadoop was successfully installed and configured in a Linux environment using a dedicated **hadoop** user account. Hadoop services were started successfully, and HDFS shell commands were executed to create directories, upload, download, copy, rename, and delete files. The successful execution of these commands verified that the Hadoop Distributed File System (HDFS) was functioning correctly.

---

## Conclusion

In this experiment, students learned how to install and configure Apache Hadoop, create a dedicated Hadoop user, configure passwordless SSH, and verify the Hadoop environment. They also gained hands-on experience with the Hadoop Distributed File System (HDFS) by performing various file management operations using Hadoop shell commands. This experiment provides the foundational knowledge required for subsequent experiments involving HDFS, MapReduce, Hive, Pig, and other Hadoop ecosystem components.

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
