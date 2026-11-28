# Linux Commands

The commands I reach for most often in the Bash shell. I learned them in the Google Cybersecurity Certificate (see [Course 4](../coursera-google-cybersecurity/courses/04-linux-and-sql.md)).

## Moving around and looking at files

| Command | What it does |
|---|---|
| `pwd` | Shows which directory I am in |
| `ls -la` | Lists everything in a directory, including hidden files, with permissions |
| `cd <dir>` | Moves into another directory (`cd ..` goes up one level) |
| `cat <file>` | Prints a whole file |
| `less <file>` | Lets me read a long file page by page |
| `head <file>` / `tail <file>` | Shows the first or last lines of a file |
| `tail -f <file>` | Follows a file as it grows, which is handy for logs |

## Searching

| Command | What it does |
|---|---|
| `grep "text" <file>` | Finds lines that contain some text |
| `grep -i "text" <file>` | Same, but ignores upper and lower case |
| `find / -name "file"` | Looks for a file by name, starting from `/` |
| `sort <file> \| uniq -c` | Counts how often each line appears. Sorting first matters, because `uniq` only counts repeated lines that are next to each other |

## Managing files

| Command | What it does |
|---|---|
| `mkdir <dir>` | Creates a directory |
| `touch <file>` | Creates an empty file |
| `cp <from> <to>` | Copies a file |
| `mv <from> <to>` | Moves or renames a file |
| `rm <file>` | Deletes a file. There is no recycle bin, so I double-check first |

## Users, permissions and help

| Command | What it does |
|---|---|
| `whoami` | Shows the user I am logged in as |
| `sudo <cmd>` | Runs one command with administrator rights |
| `chmod 640 <file>` | Changes who can read, write or run a file |
| `chown user:group <file>` | Changes the owner and group of a file |
| `man <cmd>` | Opens the manual for a command |

## System and network

| Command | What it does |
|---|---|
| `ps aux` | Lists running processes |
| `ss -tulpn` | Shows which ports are listening and which program owns them |
| `ping <host>` | Checks whether a host answers |
| `curl <url>` | Makes a web request from the terminal |

## How permissions work

A listing such as `-rw-r-----` has ten characters.

| Part | Example | Meaning |
|---|---|---|
| Type | `-` | A regular file (`d` would be a directory) |
| Owner | `rw-` | The owner can read and write |
| Group | `r--` | The group can only read |
| Others | `---` | Everyone else has no access |

Each permission has a number: read is 4, write is 2 and execute is 1. Add them up for each group. So `chmod 640` gives the owner 6 (read and write), the group 4 (read) and others 0.

This is also **least privilege** in practice: give each person only the access they need.
