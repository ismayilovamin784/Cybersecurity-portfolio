<h1 align="center">Security Incident Report: Brute Force and Malware</h1>

<p align="center"><i>Hands-on activity · Google Cybersecurity Certificate, Course 3</i></p>

<p align="center">
<img src="https://img.shields.io/badge/STATUS-COMPLETED-2EA44F?style=for-the-badge" alt="Status: Completed">
<img src="https://img.shields.io/badge/COURSE-NETWORKS-0A66C2?style=for-the-badge" alt="Course 3: Networks and Network Security">
<img src="https://img.shields.io/badge/TYPE-HANDS--ON_ACTIVITY-555555?style=for-the-badge" alt="Type: Hands-on activity">
</p>

[← Back to all activities](../README.md)

---

## 📄 Document

[Security incident report (PDF)](security-incident-report.pdf)

---

## 📌 Overview

| | |
|---|---|
| **Goal** | Identify the network protocol involved, document the incident and recommend one fix |
| **Tool** | `tcpdump` capture in a sandbox |
| **Result** | A compromised website caused by a brute force attack on a default admin password |
| **Recommendation** | Two-factor authentication (2FA) |

## 🌐 Protocol involved

DNS was used to find the site. The browser asked the DNS server for the IP address of the website, then sent a `GET / HTTP/1.1` request. The malicious file was delivered through **HTTP** at the application layer, so HTTP is the main protocol in this incident.

## 🗒️ Incident timeline

| Step | What happened |
|---|---|
| 1 | A former employee guessed passwords until he found the admin password, which is a **brute force** attack |
| 2 | He added his own JavaScript to the website, which asked visitors to download a file, and then changed the admin password |
| 3 | A few hours later, customers wrote to the helpdesk: they had to download a file, were then sent to a fake copy of the website, and their computers slowed down |
| 4 | The owner could not log in because the password had been changed, so he contacted the hosting provider |
| 5 | The company's analysts opened the site in a sandbox and ran `tcpdump`. They downloaded the file and saw the browser redirected to a different website, `greatrecipesforme.com`, which contained malware |
| 6 | The logs showed the order of requests: DNS for the real site, HTTP request, file download, then a new DNS request and HTTP request for the fake site |
| 7 | A senior analyst confirmed the compromise by finding the added JavaScript in the source code |

## 🔎 Cause

The admin password was still the **default** one, and there was no control to stop repeated login attempts, so the attacker found it easily.

## ✅ Recommendation

Use **two-factor authentication (2FA)**. Even if someone guesses or learns the password, they would also need the code sent to the account owner's phone. In this incident, 2FA would have stopped the attacker from reaching the admin panel.

## 💡 What I learned

This activity showed me how one weak password can lead to a chain of problems: a hacked site, harmed customers and a lot of cleanup work. I also learned how to read a packet capture in order (DNS, then HTTP, then the redirect) to rebuild what happened.

---

<sub>Part of the [Google Cybersecurity Certificate](../../README.md) notes, [Course 3](../../courses/03-networks-and-network-security.md). The scenarios and company names are fictional training material.</sub>
