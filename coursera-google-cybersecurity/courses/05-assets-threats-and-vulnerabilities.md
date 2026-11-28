# Course 5: Assets, Threats, and Vulnerabilities

[← Back to certificate overview](../README.md)

| | |
|---|---|
| **Status** | ✅ Completed |
| **Focus** | Protecting assets, finding weaknesses and thinking like an attacker |
| **Modules** | 4: Introduction to asset security · Protect organizational assets · Vulnerabilities in systems · Threats to asset security |
| **Official page** | [Coursera](https://www.coursera.org/learn/assets-threats-and-vulnerabilities) |

## Big picture
This course goes deeper into the ideas from Courses 1 and 2. It asks three questions: what do we need to protect, how do we protect it, and where could it be attacked? It ends with threat modeling, a structured way to think about attacks before they happen.

## Introduction to asset security
- **Asset classification** means sorting assets by how sensitive they are, for example public, internal, confidential and restricted. The class decides how much protection an asset needs.
- A **risk** is scored by how likely it is and how severe the impact would be.
- The **NIST Cybersecurity Framework** gives a common structure for managing these decisions.
- Cloud services made asset security harder, because data now lives outside the company's own buildings.

## Protecting assets
| Topic | In my words |
|---|---|
| Security controls | Safeguards that reduce risk. They can be administrative, technical or physical |
| Data lifecycle | Data is collected, stored, used, archived and finally destroyed. Each stage needs protection |
| Privacy and compliance | Laws and standards decide how personal data can be collected and handled |
| Encryption | Symmetric encryption uses one shared key. Asymmetric encryption uses a public and a private key |
| Public key infrastructure (PKI) | A system that proves a public key really belongs to who it claims |
| Hashing | A one-way function that turns data into a fixed value. It shows whether data was changed, and it supports non-repudiation |
| Authentication | Proves who you are. SSO and MFA make it easier and stronger |
| Authorization | Decides what you may do after you are verified |
| Accounting and auditing | Records user activity so it can be reviewed later |

The **principle of least privilege** appears again here: give people only the access they need.

## Vulnerabilities in systems
- **Vulnerability management** is a cycle of finding, assessing, fixing and checking weaknesses.
- **Defense in depth** uses several layers of protection, so one failed control does not expose everything.
- **CVE** entries give known vulnerabilities a public identifier, and the **OWASP Top 10** lists the most common web application risks.
- A **vulnerability assessment** is an internal review of systems. **Penetration testing** simulates a real attack to see what an attacker could reach.
- An **attack surface** is every point where an attacker could try to get in. Reducing it lowers risk.
- **Open source intelligence (OSINT)** uses public information. Attackers use it, and so can defenders.

## Threats to asset security
| Threat | What it is |
|---|---|
| Social engineering | Manipulating people instead of breaking technology |
| Phishing | Fake messages that steal information or spread malware, in several forms such as email, voice and text |
| Malware | Harmful software such as viruses, worms, ransomware and spyware |
| Cryptojacking | Secretly using someone's computer to mine cryptocurrency |
| Cross-site scripting (XSS) | Injecting malicious script into a trusted web page |
| Injection attacks | Sending malicious input, such as SQL, to a database or application |

**Threat modeling** looks at a system the way an attacker would. The course uses **PASTA** (Process for Attack Simulation and Threat Analysis), which has seven stages: define objectives, define the technical scope, break the application down, analyze threats, analyze vulnerabilities, model attacks, and analyze risk and impact.

## Practice topics in this course
Classifying assets on a home network, scoring risks by likelihood and severity, improving authentication and authorization for a small business, creating hash values, and applying the PASTA framework.

## What I learned
This was the course that made the attacker's point of view clear to me. I learned how to classify assets and why encryption, hashing and access control protect them, how vulnerabilities are found and managed, and how threats like phishing, malware and injection work. I also learned that threat modeling is a good habit: it is cheaper to think about how something could be attacked before it is built than after it is breached.
