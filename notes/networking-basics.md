# Networking Basics

A quick reference for the networking ideas I use most. More detail is in [Course 3](../coursera-google-cybersecurity/courses/03-networks-and-network-security.md).

## The OSI model

Seven layers, from the top (what the user sees) to the bottom (the cable):

| Layer | Name | Example |
|---|---|---|
| 7 | Application | HTTP, DNS, SSH |
| 6 | Presentation | Encryption, data formats |
| 5 | Session | Opening and closing a conversation |
| 4 | Transport | TCP, UDP, ports |
| 3 | Network | IP addresses, routing |
| 2 | Data Link | MAC addresses, switches |
| 1 | Physical | Cables, Wi-Fi signals |

In practice the four-layer **TCP/IP model** is what real networks use. I mostly use the OSI model to describe where a problem is.

## TCP and UDP

| | TCP | UDP |
|---|---|---|
| Connection | Sets one up first with a three-way handshake (SYN, SYN-ACK, ACK) | None |
| Reliability | Checks that data arrives, in order | Best effort, no check |
| Speed | Slower | Faster |
| Typical use | Web, email, SSH | DNS queries, streaming, online games |

## Common ports

| Port | Service | Note |
|---|---|---|
| 21 | FTP | File transfer, not encrypted |
| 22 | SSH | Encrypted remote login |
| 23 | Telnet | Remote login, not encrypted, so avoid it |
| 25 | SMTP | Sending email |
| 53 | DNS | Turns names into IP addresses |
| 80 | HTTP | Web, not encrypted |
| 110 / 143 | POP3 / IMAP | Receiving email |
| 443 | HTTPS | Web, encrypted |
| 445 | SMB | Windows file sharing |
| 3389 | RDP | Windows remote desktop |

A port that is open and not needed is one more way in, so closing unused ports is an easy win for security.

## IP addresses

- **IPv4** has 32 bits (for example `192.0.2.10`) and **IPv6** has 128 bits.
- **Private ranges** are used inside a home or company network: `10.0.0.0/8`, `172.16.0.0/12` and `192.168.0.0/16`.
- **CIDR** notation shows the size of a network. `/24` means the first 24 bits are the network part, which is the mask `255.255.255.0` and gives 254 usable addresses.
- A **MAC address** identifies a network card on the local network. **ARP** is how a device finds the MAC address that belongs to an IP address.

## Key services

| Service | What it does |
|---|---|
| DNS | Translates names such as `example.com` into IP addresses. Common record types are A, AAAA, MX, CNAME and TXT |
| DHCP | Gives devices an IP address automatically when they join a network |
| NAT | Lets many private devices share one public IP address |
| Firewall | Allows or blocks traffic based on rules |
| VPN | Sends traffic through an encrypted tunnel |

## HTTP status codes

| Code | Meaning |
|---|---|
| 200 | OK |
| 301 / 302 | Redirect |
| 401 | Not logged in |
| 403 | Logged in, but not allowed |
| 404 | Not found |
| 500 / 503 | Server error or unavailable |
