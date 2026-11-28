<h1 align="center">Cybersecurity Incident Report: SYN Flood</h1>

<p align="center"><i>Hands-on activity · Google Cybersecurity Certificate, Course 3</i></p>

<p align="center">
<img src="https://img.shields.io/badge/STATUS-COMPLETED-2EA44F?style=for-the-badge" alt="Status: Completed">
<img src="https://img.shields.io/badge/COURSE-NETWORKS-0A66C2?style=for-the-badge" alt="Course 3: Networks and Network Security">
<img src="https://img.shields.io/badge/TYPE-HANDS--ON_ACTIVITY-555555?style=for-the-badge" alt="Type: Hands-on activity">
</p>

[← Back to all activities](../README.md)

---

## 📄 Document

[Cybersecurity incident report (PDF)](cybersecurity-incident-report-syn-flood.pdf)

---

## 📌 Overview

| | |
|---|---|
| **Goal** | Identify the type of attack behind a website connection error and explain how it breaks the website |
| **Evidence** | Network logs showing the web server overloaded with SYN requests |
| **Result** | A likely DoS attack, specifically a SYN flood |
| **Course topic** | Network intrusions (Denial of Service) |

## 🔎 Finding

The connection error is probably caused by a **denial of service (DoS) attack**. The logs show the web server overloaded with SYN packet requests until it stops responding. This pattern is called **SYN flooding**.

## ⚙️ How the attack breaks the website

Every normal connection to a web server starts with a TCP three-way handshake.

| Step | Packet | What happens |
|---|---|---|
| 1 | SYN | The visitor asks to connect |
| 2 | SYN-ACK | The server agrees and reserves resources for the visitor |
| 3 | ACK | The visitor confirms, and the connection opens |

In a SYN flood, the attacker sends a huge number of SYN packets. The server tries to reserve resources for every request, so its resources run out. Real visitors can no longer open a connection, and they see a timeout message in their browser.

## 💡 What I learned

This activity showed me how a normal TCP handshake can be turned into a weakness. I learned to connect what the logs show (many SYN requests and a server that stops answering) with the real effect on a visitor (a timeout). It also made the difference between a DoS attack and a normal traffic spike clearer.

---

<sub>Part of the [Google Cybersecurity Certificate](../../README.md) notes, [Course 3](../../courses/03-networks-and-network-security.md). The scenarios and company names are fictional training material.</sub>
