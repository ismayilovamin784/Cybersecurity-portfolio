<h1 align="center">Security Risk Assessment: Network Hardening</h1>

<p align="center"><i>Hands-on activity · Google Cybersecurity Certificate, Course 3</i></p>

<p align="center">
<img src="https://img.shields.io/badge/STATUS-COMPLETED-2EA44F?style=for-the-badge" alt="Status: Completed">
<img src="https://img.shields.io/badge/COURSE-NETWORKS-0A66C2?style=for-the-badge" alt="Course 3: Networks and Network Security">
<img src="https://img.shields.io/badge/TYPE-HANDS--ON_ACTIVITY-555555?style=for-the-badge" alt="Type: Hands-on activity">
</p>

[← Back to all activities](../README.md)

---

## 📄 Document

[Security risk assessment report (PDF)](security-risk-assessment-report.pdf)

---

## 📌 Overview

| | |
|---|---|
| **Goal** | Choose hardening methods that would stop a data breach from happening again, and explain why |
| **Weaknesses found** | No firewall rules, shared passwords and a default admin password |
| **Recommended measures** | Firewall maintenance, password policies and multi-factor authentication (MFA) |
| **Course topic** | Security hardening |

## 🛠️ Recommended hardening measures

| # | Measure | Weakness it fixes | How it helps |
|---|---|---|---|
| 1 | **Firewall maintenance** | The company had no firewall rules, so all incoming traffic passed through | Rules filter malicious and unnecessary traffic. They must be reviewed and updated regularly and after each incident |
| 2 | **Password policies** | Employees shared passwords and the admin password was still the default | No sharing, one account per person and a changed admin password. Hashed and salted passwords are harder to crack, and longer passwords resist brute force. Following NIST advice, passwords do not need to be overly complex or changed often |
| 3 | **Multi-factor authentication (MFA)** | A stolen or guessed password was enough to get in | A second step such as an OTP, PIN, badge or fingerprint means a password alone is not enough |

## 🧭 Why these three together

- **MFA** adds a confirmation that goes to the account owner, so a found password is not enough. It also makes password sharing pointless, because the second check is not with another person.
- **Strong password rules** lead to longer passwords, so a brute force attack takes much longer. After too many wrong tries the account can be blocked.
- **Firewall checks** keep harmful traffic out and make sure earlier attacks cannot simply happen again.

Applied regularly and consistently, these measures make a repeat breach much harder.

## 💡 What I learned

I learned that hardening is mostly about closing simple gaps: rules that were never written, passwords that were never changed and accounts that were shared. I also learned that no single measure is enough, so layering them gives better protection.

---

<sub>Part of the [Google Cybersecurity Certificate](../../README.md) notes, [Course 3](../../courses/03-networks-and-network-security.md). The scenarios and company names are fictional training material.</sub>
