# Course 7: Automate Cybersecurity Tasks with Python

[← Back to certificate overview](../README.md)

| | |
|---|---|
| **Status** | ✅ Completed |
| **Focus** | Python basics and using Python to automate security tasks |
| **Modules** | 4: Introduction to Python · Write effective Python code · Work with strings and lists · Python in practice |
| **Official page** | [Coursera](https://www.coursera.org/learn/automate-cybersecurity-tasks-with-python) |

## Big picture
Many security tasks are repetitive, such as checking logs, comparing lists of addresses or formatting data. Python lets an analyst automate that work and focus on the parts that need judgment.

## Python basics
- **Variables** store values. Common data types are strings, integers, floats, booleans, lists, tuples and dictionaries.
- **Conditionals** (`if`, `elif`, `else`) make decisions.
- **Loops** (`for` and `while`) repeat an action.

## Writing effective code
- **Functions** package a task so it can be reused. They take **parameters** and can send a result back with `return`.
- **Modules and libraries** give ready-made code, so there is no need to write everything from scratch.
- Readable code uses clear names and comments, because other people, and my future self, have to understand it.

## Strings and lists
- Strings and lists can be **indexed** and **sliced** to pick out parts of them.
- Lists have methods to add, remove and search items.
- **Regular expressions** (the `re` module) find patterns in text, such as an IP address or an email address in a log.

## Python in practice
- **Files:** open a file, read its contents and parse it into a structure that the code can use.
- **Debugging:** syntax errors stop the program from running, while logic errors give wrong results, so I learned to read error messages and test step by step.

A small example of the kind of task this enables, with documentation IP addresses:

```python
allow_list = ["192.0.2.10", "198.51.100.7"]
log_ips = ["192.0.2.10", "203.0.113.45"]

for ip in log_ips:
    if ip not in allow_list:
        print("Review this address:", ip)
```

A related portfolio project is planned: [Project 3: Log Analysis with Python](../../projects/03-log-analysis-python/).

## What I learned
I learned the building blocks of Python and how they fit into real security work: reading a file, finding a pattern, making a decision and repeating it for every line. The most useful habit was debugging calmly, reading the error first instead of guessing.
