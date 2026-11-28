<h1 align="center">Incident Report Analysis: NIST CSF</h1>

<p align="center"><i>Portfolio activity · Google Cybersecurity Certificate, Course 3</i></p>

<p align="center">
<img src="https://img.shields.io/badge/STATUS-COMPLETED-2EA44F?style=for-the-badge" alt="Status: Completed">
<img src="https://img.shields.io/badge/COURSE-NETWORKS-0A66C2?style=for-the-badge" alt="Course 3: Networks and Network Security">
<img src="https://img.shields.io/badge/TYPE-PORTFOLIO_ACTIVITY-E3A008?style=for-the-badge" alt="Type: Portfolio activity">
</p>

[← Back to all activities](../README.md)

---

## 📄 Document

[Incident report analysis (PDF)](incident-report-analysis.pdf)

---

## 📌 Overview

| | |
|---|---|
| **Goal** | Use the five functions of the NIST Cybersecurity Framework (CSF) to analyze a security incident |
| **Scenario** | A company providing web design, graphic design and social media marketing services to small businesses |
| **Incident** | An ICMP flood (a type of DoS attack) that made the internal network unavailable for 2 hours |
| **Root cause** | An unconfigured firewall with no rules to filter traffic |
| **Framework** | NIST CSF: Identify, Protect, Detect, Respond, Recover |

## 📝 Summary

An attacker flooded the company's network with a large number of ICMP packets. Because the firewall was not configured, the packets got in and the internal network was unavailable for 2 hours. The incident team blocked the incoming ICMP packets and took non-critical services offline, then restored the critical services. They found that the attack had come in through the unconfigured firewall.

## 🧩 NIST CSF analysis

| Function | What I found or recommend |
|---|---|
| **Identify** | The attack was a DoS attack using ICMP packets. The firewall had no rules, so the flood entered the network. Employees could not reach resources, and customers could have been affected indirectly |
| **Protect** | Set firewall rules that limit, block or rate-limit ICMP packets, check them regularly and update them for new threats. Check the firewall configuration before it goes into use. An IPS can filter unnecessary ICMP packets. Inform the IT team and employees about the attack |
| **Detect** | Monitor network traffic continuously. Install an IDS to spot suspicious ICMP packets, and use a SIEM tool to collect and analyze firewall logs |
| **Respond** | Contain the incident by taking non-critical services offline and restoring critical ones, block incoming ICMP packets and the attack's source, analyze the incident with firewall logs or a SIEM, and brief the team |
| **Recover** | Restore critical services first, then bring non-critical ones back safely using backups of data and configurations. Check firewall rules before the network is fully restored, then test and monitor. Review and improve the recovery plan after each incident |

## 💬 Reflection

If a firewall is not configured properly and has no rules, attacks such as DoS can happen, and they are hard to stop. The five functions of the NIST CSF give a step-by-step way to manage an incident. In the future, the firewall should be configured correctly and IDS and IPS systems should be installed.

## 💡 What I learned

This activity let me use the NIST CSF on a real kind of incident instead of only reading about it. The five functions gave me a clear order to think in, from understanding what happened to getting back to normal and preventing a repeat.

---

<sub>Part of the [Google Cybersecurity Certificate](../../README.md) notes, [Course 3](../../courses/03-networks-and-network-security.md). The scenarios and company names are fictional training material.</sub>
