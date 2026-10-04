# Nmap Cheat Sheet

> Only scan systems you own or have explicit permission to scan.

| Command | Purpose |
|---|---|
| `nmap <target>` | Default scan of the top 1000 ports |
| `nmap -sn <network>` | Host discovery only (no port scan) |
| `nmap -p 22,80,443 <target>` | Scan specific ports |
| `nmap -p- <target>` | Scan all 65535 ports |
| `nmap -sV <target>` | Detect service versions |
| `nmap -sC <target>` | Run default scripts |
| `nmap -O <target>` | Guess the operating system |
| `nmap -A <target>` | Aggressive: OS, version, scripts, traceroute |
| `nmap -T4 <target>` | Faster timing |
| `nmap -oN scan.txt <target>` | Save output to a file |

## Port states
- **open**: a service is listening
- **closed**: reachable, nothing listening
- **filtered**: a firewall blocks the probe
