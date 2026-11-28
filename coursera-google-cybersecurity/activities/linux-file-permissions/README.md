<h1 align="center">File Permissions in Linux</h1>

<p align="center"><i>Portfolio activity · Google Cybersecurity Certificate, Course 4</i></p>

<p align="center">
<img src="https://img.shields.io/badge/STATUS-COMPLETED-2EA44F?style=for-the-badge" alt="Status: Completed">
<img src="https://img.shields.io/badge/COURSE-LINUX_AND_SQL-0A66C2?style=for-the-badge" alt="Course 4: Linux and SQL">
<img src="https://img.shields.io/badge/TYPE-PORTFOLIO_ACTIVITY-E3A008?style=for-the-badge" alt="Type: Portfolio activity">
</p>

[← Back to all activities](../README.md)

---

## 📄 Document

[File permissions in Linux (PDF)](file-permissions-in-linux.pdf)

---

## 📌 Overview

| | |
|---|---|
| **Goal** | Check and fix file and directory permissions so that each one matches the access it should have |
| **Scenario** | A research team needs the permissions in its project directory to follow the organization's rules |
| **Tools** | Linux Bash shell, `ls -la` and `chmod` |
| **Principle** | Least privilege: give each person only the access they need |

## 🔍 Step 1: Check the current permissions

I listed the project directory with `ls -la`. The `-l` option gives a detailed listing and `-a` includes hidden files. The directory contained one hidden file (`.project_x.txt`), one directory (`drafts`) and four other project files.

## 🧩 Reading the permissions string

The first column of the listing is a 10-character string.

| Characters | Meaning |
|---|---|
| 1st | File type: `d` is a directory, `-` is a regular file |
| 2nd to 4th | What the **user** (the owner) can do: read `r`, write `w`, execute `x` |
| 5th to 7th | What the **group** can do |
| 8th to 10th | What **other** users can do. This means everyone who is not the owner and not in the group |

A hyphen in any position means that permission is not given. For example, `project_t.txt` has `-rw-rw-r--`. It is a regular file, the user and the group can read and write it, other users can only read it, and nobody can execute it.

## 🛠️ Step 2: Change the permissions

| File or directory | Rule from the organization | Command | Result |
|---|---|---|---|
| `project_k.txt` | Other users must not have write access | `chmod o-w project_k.txt` | Write access removed for other users. This was the only file where they had it |
| `.project_x.txt` (hidden, archived) | Nobody may write to it, but the user and group can still read it | `chmod u-w`, `chmod g-w` and `chmod g+r` on the file | Read-only for the user and the group |
| `drafts` (directory) | Only the user `benjamin` may access it | `chmod g-x drafts` | The group's execute permission is removed. Only `benjamin` can enter the directory |

How the options work: `u` is the user, `g` is the group and `o` is other users. `+` adds a permission and `-` removes it. After each change I ran `ls -la` again to confirm that it worked.

## 📝 Summary

I checked the permissions with `ls -la`, then used `chmod` three times to match the access the organization wanted: removed write access for other users on `project_k.txt`, made `.project_x.txt` read-only for the user and group, and removed execute permission from the group on the `drafts` directory.

## 💡 What I learned

This activity made file permissions practical for me. I learned to read the permissions string quickly, to change only the permission that is wrong, and to check the result afterwards. It also showed me why permissions matter for security: a file that is writable by everyone, or a directory that the wrong group can open, is an easy gap to fix once you know where to look.

---

<sub>Part of the [Google Cybersecurity Certificate](../../README.md) notes, [Course 4](../../courses/04-linux-and-sql.md). The directory, files and user names are training material.</sub>
