# Nmap Cheat Sheet

Nmap scans a network to find devices, open ports and the services running on them.

> **Only scan systems you own or have clear, written permission to scan.** Scanning other people's systems can be illegal. I plan to practice only in my own home lab and on training platforms.

## Common options

| Command | What it does |
|---|---|
| `nmap <target>` | Default scan of the 1000 most common ports |
| `nmap -sn <network>` | Finds which hosts are up, without scanning ports |
| `nmap -p 22,80,443 <target>` | Scans only the ports I list |
| `nmap -p- <target>` | Scans all 65535 ports |
| `nmap -sV <target>` | Detects the version of each service |
| `nmap -sC <target>` | Runs the default scripts |
| `nmap -O <target>` | Guesses the operating system |
| `nmap -A <target>` | Aggressive: OS, versions, scripts and traceroute together |
| `nmap -T4 <target>` | Scans faster, but is noisier and easier to notice |
| `nmap -oN scan.txt <target>` | Saves the results to a text file |

## What the port states mean

| State | Meaning |
|---|---|
| open | A service is listening and answering |
| closed | The port can be reached, but nothing is listening |
| filtered | A firewall is blocking the probe, so Nmap cannot tell |

Nmap also reports mixed states such as `open|filtered` when it cannot decide.

## How I read a result

1. Which ports are open? Each one is a possible way in.
2. Which service and version is behind each port? Old versions often have known vulnerabilities.
3. Does the service need to be reachable at all? If not, close it or block it with a firewall.

This is the defender's view of a scan: find out what an attacker would see before they do.
