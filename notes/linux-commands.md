# Linux Commands (basics)

| Command | Purpose |
|---|---|
| `pwd` | Show current directory |
| `ls -la` | List files, including hidden, with permissions |
| `cd <dir>` | Change directory |
| `cat <file>` | Print file contents |
| `less <file>` | Read a long file page by page |
| `grep "text" <file>` | Search for text in a file |
| `find / -name "file"` | Find a file by name |
| `chmod 640 <file>` | Change file permissions |
| `chown user:group <file>` | Change file owner |
| `ps aux` | List running processes |
| `ss -tulpn` | Show listening ports |
| `ping <host>` | Test connectivity |
| `curl <url>` | Make an HTTP request |
| `tail -f <file>` | Follow a log file live |
| `sort \| uniq -c` | Count repeated lines |
| `sudo <cmd>` | Run a command as administrator |
| `man <cmd>` | Open the manual for a command |

## Permissions
`rwx` = read, write, execute. Example `-rw-r-----`: owner can read/write, group can read, others have no access.
