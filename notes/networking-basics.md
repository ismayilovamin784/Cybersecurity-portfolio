# Networking Basics

## OSI model (7 layers)
7 Application · 6 Presentation · 5 Session · 4 Transport · 3 Network · 2 Data Link · 1 Physical

## TCP vs UDP
| | TCP | UDP |
|---|---|---|
| Connection | Yes (3-way handshake: SYN, SYN-ACK, ACK) | No |
| Reliability | Reliable, ordered | Best effort |
| Typical use | Web, email, SSH | DNS queries, streaming, gaming |

## Common ports
| Port | Service |
|---|---|
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 25 | SMTP |
| 3389 | RDP |

## HTTP status codes
2xx success · 3xx redirect · 4xx client error (403 forbidden, 404 not found) · 5xx server error

## Key ideas
- **DNS** translates names to IP addresses
- **DHCP** assigns IP addresses automatically
- **NAT** lets many private devices share one public IP
