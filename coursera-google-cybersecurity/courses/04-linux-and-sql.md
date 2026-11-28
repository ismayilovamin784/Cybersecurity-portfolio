# Course 4: Tools of the Trade: Linux and SQL

[← Back to certificate overview](../README.md)

| | |
|---|---|
| **Status** | ✅ Completed |
| **Focus** | Using Linux in the Bash shell and querying databases with SQL |
| **Modules** | 4: Introduction to operating systems · The Linux operating system · Linux commands in the Bash shell · Databases and SQL |
| **Official page** | [Coursera](https://www.coursera.org/learn/linux-and-sql) |

## Big picture
Security analysts spend a lot of time in the command line and in databases. Linux is common on servers and security tools, and SQL lets an analyst pull exactly the records they need from a large data set, such as login or purchase records.

## Operating systems
An operating system sits between the hardware and the applications and manages memory, files, processes and devices. People talk to it through a **graphical user interface (GUI)** or a **command-line interface (CLI)**. The CLI is faster for repeated work and easier to automate.

## Linux
- Linux is open source and comes in many **distributions**, which package the same kernel with different tools.
- The **shell** is the program that takes typed commands and passes them to the operating system. **Bash** is the most common one.
- Linux is popular in security because it is flexible, free and used on many servers.

## Working in Bash
The most useful commands are collected in my [Linux commands](../../notes/linux-commands.md) note. They fall into a few groups:

| Group | Examples |
|---|---|
| Navigate | `pwd`, `ls`, `cd` |
| Read and search | `cat`, `less`, `head`, `tail`, `grep`, `find` |
| Manage files | `mkdir`, `touch`, `cp`, `mv`, `rm` |
| Users and permissions | `sudo`, `chmod`, `chown`, `useradd` |
| Get help | `man`, `--help` |

**Permissions:** a string like `-rwxr-x---` has ten characters. The first shows the file type. The next three are for the owner, then three for the group, then three for everyone else. Giving each person only the access they need is the **principle of least privilege** in practice.

## Databases and SQL
A **relational database** stores data in tables with rows and columns. A **primary key** identifies each row and a **foreign key** links a row to another table.

| SQL part | Purpose |
|---|---|
| `SELECT` | Choose the columns to return |
| `FROM` | Choose the table |
| `WHERE` | Filter rows |
| `AND`, `OR`, `NOT` | Combine or reverse filter conditions |
| `LIKE` with `%` | Match a pattern |
| `JOIN` | Combine rows from two tables that share a key |

A simple example with made-up table names:

```sql
SELECT employee_id, device_id
FROM employees
WHERE department = 'Finance' AND last_login < '2026-01-01';
```

Joins matter because the answer to a security question is often in two places, for example a table of devices and a table of employees.

## Activity in this course
My portfolio activity (⭐) from this course: [File Permissions in Linux](../activities/linux-file-permissions/). I checked a project directory with `ls -la` and fixed three permission problems with `chmod`.

## What I learned
I learned to move around Linux without a graphical interface, read files, search them and manage permissions. I also learned to write SQL queries that filter data and combine tables. These two skills show up in many entry-level security tasks, such as checking logs, looking for a suspicious login or finding which devices a user owns.
