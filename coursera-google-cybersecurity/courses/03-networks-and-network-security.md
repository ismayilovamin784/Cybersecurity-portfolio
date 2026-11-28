# Course 3: Connect and Protect: Networks and Network Security

[← Back to certificate overview](../README.md)

| | |
|---|---|
| **Status** | ✅ Completed |
| **Focus** | How networks work, how they get attacked and how to harden them |
| **Modules** | 4: Network architecture · Network operations · Secure against network intrusions · Security hardening |
| **Official page** | [Coursera](https://www.coursera.org/learn/networks-and-network-security) |

## Big picture
To protect a network, you first need to know how data travels through it. This course starts with network design, moves to the devices and protocols that keep traffic flowing, then looks at the attacks that target them and finishes with ways to make systems harder to break.

## Network architecture
Data moves through layers, and each layer has its own job. The **TCP/IP model** has four layers and is the one used in practice. The **OSI model** has seven layers and is mostly used to describe where a problem happens. My short reference is in [networking basics](../../notes/networking-basics.md).

| TCP/IP layer | What it does | Examples |
|---|---|---|
| Application | Gives programs access to the network | HTTP, HTTPS, DNS, SSH |
| Transport | Moves data between devices and tracks ports | TCP, UDP |
| Internet | Adds IP addresses and finds a route | IP, ICMP |
| Network access | Sends the actual bits over cables or Wi-Fi | Ethernet, Wi-Fi |

- **IP addresses** identify devices on a network. IPv4 uses 32 bits and IPv6 uses 128 bits, which gives far more addresses.
- **Cloud networks** and **software-defined networks** move much of the network from physical hardware into software that can be configured and scaled quickly.

## Network operations
| Tool or idea | In my words |
|---|---|
| Firewall | Allows or blocks traffic based on rules. A stateful firewall also remembers active connections |
| VPN | Creates an encrypted tunnel over a public network. WireGuard and IPSec are two common VPN protocols |
| Proxy server | Sits between users and the internet and can filter, hide or cache requests |
| Security zones | Splits a network into areas with different trust levels, for example an outside zone, a DMZ and an internal zone |
| Subnetting and CIDR | Splits one network into smaller ones. CIDR notation such as `/24` shows how many bits belong to the network part |
| Wireless security | Protocols improved over time from WEP to WPA, WPA2 and WPA3, with stronger encryption each time |

## Network intrusions
| Attack | What happens |
|---|---|
| Denial of Service (DoS) | One source floods a target so real users cannot reach it |
| Distributed DoS (DDoS) | The same flood, sent from many devices at once |
| Packet sniffing | An attacker captures traffic to read data that is not encrypted |
| IP spoofing | An attacker fakes a trusted IP address. Variants include on-path, replay and smurf attacks |

I also learned to read basic `tcpdump` output. Each line shows a timestamp, the source and destination, and flags that describe the packet, which helps to spot a flood or a strange connection.

## Security hardening
Hardening means reducing the ways a system can be attacked.
- **Operating system hardening:** keep systems patched, use a secure baseline configuration, remove services that are not needed and enforce strong passwords and MFA.
- **Network hardening:** filter ports, limit who can reach which resources, encrypt traffic and review firewall rules regularly.
- **Cloud hardening:** the provider and the customer share responsibility, so the customer still has to configure access and settings safely.
- **Brute force attacks** are slowed down by strong passwords, MFA and limits on login attempts.

## Activities in this course
Five hands-on activities came from this course. The last one is a portfolio activity (⭐).

| Activity | What it shows |
|---|---|
| [Cybersecurity Incident Report: SYN Flood](../activities/network-attack-analysis-syn-flood/) | Spotting a DoS attack and explaining how it abuses the TCP handshake |
| [Network Traffic Analysis: DNS and ICMP](../activities/network-traffic-analysis-dns-icmp/) | Reading a `tcpdump` log to find why a website could not be reached |
| [Security Incident Report: Brute Force and Malware](../activities/security-incident-report-brute-force/) | Documenting a compromised website and recommending 2FA |
| [Security Risk Assessment: Network Hardening](../activities/security-risk-assessment-hardening/) | Choosing firewall, password and MFA hardening measures |
| ⭐ [Incident Report Analysis: NIST CSF](../activities/incident-report-analysis-nist-csf/) | Applying the five NIST CSF functions to an ICMP flood |

## What I learned
This course connected the theory from the first two courses to real infrastructure. I learned how data moves across the TCP/IP layers, what firewalls, VPNs, proxies and security zones are for, and how common attacks such as DoS and IP spoofing work. The most useful idea for me was hardening: many attacks succeed because a system was left with default settings or unneeded services, so good basic configuration blocks a lot of them.
