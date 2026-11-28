<h1 align="center">Network Traffic Analysis: DNS and ICMP</h1>

<p align="center"><i>Hands-on activity · Google Cybersecurity Certificate, Course 3</i></p>

<p align="center">
<img src="https://img.shields.io/badge/STATUS-COMPLETED-2EA44F?style=for-the-badge" alt="Status: Completed">
<img src="https://img.shields.io/badge/COURSE-NETWORKS-0A66C2?style=for-the-badge" alt="Course 3: Networks and Network Security">
<img src="https://img.shields.io/badge/TYPE-HANDS--ON_ACTIVITY-555555?style=for-the-badge" alt="Type: Hands-on activity">
</p>

[← Back to all activities](../README.md)

---

## 📄 Document

[Cybersecurity incident report: network traffic analysis (PDF)](network-traffic-analysis-incident-report.pdf)

---

## 📌 Overview

| | |
|---|---|
| **Goal** | Find out why a website could not be reached, using a DNS and ICMP traffic log |
| **Tool** | `tcpdump` capture |
| **Result** | DNS queries to UDP port 53 were refused, so the site could not load |
| **Course topic** | Reading network traffic and network protocols |

## 🔎 What the log showed

When a user types the website address into a browser, the first step is a **DNS lookup**. The computer sends a UDP packet to the DNS server on port 53 to ask for the site's IP address.

| Entry | Detail |
|---|---|
| Query | From `192.51.100.15` (the client) to `203.0.113.2` (the DNS server), UDP port 53 |
| Reply | No DNS answer. An ICMP error came back instead: `udp port 53 unreachable` |
| Repeats | The same pair of entries appears three times, at 13:24, 13:26 and 13:28 |

The ICMP error came from the DNS server's own address. That means the server is online and reachable, but nothing on it accepts traffic on UDP port 53. Without an IP address, the browser cannot make the HTTPS request, so the page never loads. The website itself is not the problem.

## 🧭 Analysis and likely causes

Customers reported a "destination port unreachable" error, and the first log entry was at 13:24. I visited the site, got the same error and captured the traffic with `tcpdump`. Every DNS query was answered by an ICMP unreachable message.

Most likely causes:
1. The DNS service on `203.0.113.2` has stopped or is misconfigured.
2. A firewall rule is rejecting traffic on port 53.

A flood against the DNS server is possible, but unlikely. An overloaded server usually just times out, and here a clear error message came back every time.

**Next steps:** check whether the DNS service is running on the server, check the firewall rules for port 53, and test whether the site also fails from a different network. The security team was informed and the site was still down at the time of the report.

## 💡 What I learned

I learned to follow a request step by step through a log: DNS first, then the web connection. I also learned that the exact error message is a clue. An ICMP "port unreachable" points to a closed port or a blocking rule, while a plain timeout points more toward overload.

---

<sub>Part of the [Google Cybersecurity Certificate](../../README.md) notes, [Course 3](../../courses/03-networks-and-network-security.md). The scenarios and company names are fictional training material.</sub>
