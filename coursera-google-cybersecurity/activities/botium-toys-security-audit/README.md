<h1 align="center">Security Audit: Botium Toys</h1>

<p align="center"><i>Internal IT security audit for a fictional company · Google Cybersecurity Certificate, Course 2</i></p>

<p align="center">
<img src="https://img.shields.io/badge/STATUS-COMPLETED-2EA44F?style=for-the-badge" alt="Status: Completed">
<img src="https://img.shields.io/badge/COURSE-PLAY_IT_SAFE-0A66C2?style=for-the-badge" alt="Course 2: Play It Safe">
<img src="https://img.shields.io/badge/SCENARIO-FICTIONAL-555555?style=for-the-badge" alt="Fictional scenario">
</p>

<p align="center">
<a href="../../../README.md">← Back to portfolio</a>
&nbsp;·&nbsp;
<a href="botium-controls-and-compliance-checklist.pdf">📄 Controls and compliance checklist (PDF)</a>
</p>

---

## 📌 Overview

| | |
|---|---|
| **Role** | Entry-level security analyst (training scenario) |
| **Company** | Botium Toys, a fictional toy company |
| **Type** | Internal security audit: controls assessment and compliance review |
| **Frameworks** | NIST CSF, PCI DSS, GDPR, SOC type 1 and type 2 |
| **Deliverables** | Completed controls and compliance checklist, recommendations for the IT manager |
| **Source** | Google Cybersecurity Certificate (Coursera), Course 2: Play It Safe: Manage Security Risks |

## 🎯 Goal

Act as an entry-level security analyst and review the security posture of Botium Toys. I looked at the company's assets and risks, checked which security controls and compliance practices are in place, and recommended improvements that the IT manager could present to stakeholders.

## 🧭 Approach

1. Read the audit scope, goals and risk assessment.
2. Reviewed the company's assets and the main risks to them.
3. Completed a **controls assessment checklist** (14 controls).
4. Completed a **compliance checklist** for PCI DSS, GDPR and SOC (12 best practices).
5. Summarized the findings and wrote prioritized recommendations.

## 📊 Results at a glance

| Area | Items reviewed | In place / met | Missing / not met |
|---|---|---|---|
| Security controls | 14 | 5 | 9 |
| Compliance best practices | 12 | 3 | 9 |

**Strong:** physical security (locks, CCTV, fire systems) and basic protection (firewall, antivirus).
**Weak:** protection of the data itself: access control, encryption, backups and recovery planning.

## 🔐 Controls assessment

| Control | Type | In place? | Finding |
|---|---|---|---|
| Least privilege | Administrative | ❌ No | All employees can access internal data, including customer data |
| Disaster recovery plans | Administrative | ❌ No | No plans exist |
| Password policies | Administrative | ❌ No | A policy exists, but its requirements are too weak |
| Separation of duties | Administrative | ❌ No | Not implemented |
| Firewall | Technical | ✅ Yes | Blocks traffic based on defined security rules |
| Intrusion detection system (IDS) | Technical | ❌ No | Not installed |
| Backups | Technical | ❌ No | No backups of critical data |
| Antivirus software | Technical | ✅ Yes | Installed and monitored regularly |
| Manual monitoring of legacy systems | Administrative | ❌ No | Done, but without a regular schedule or clear intervention steps |
| Encryption | Technical | ❌ No | Credit card data is not encrypted |
| Password management system | Technical | ❌ No | No central system to enforce password rules |
| Locks (office, store, warehouse) | Physical | ✅ Yes | Sufficient locks in place |
| CCTV | Physical | ✅ Yes | Up to date and working |
| Fire detection and prevention | Physical | ✅ Yes | Working systems in place |

<sub>Control types: **administrative** controls are policies and procedures, **technical** controls are tools and systems, **physical** controls protect buildings and equipment.</sub>

## 📋 Compliance assessment

| Standard | Best practice | Met? |
|---|---|---|
| PCI DSS | Only authorized users can access card data | ❌ No |
| PCI DSS | Card data is handled in a secure environment | ❌ No |
| PCI DSS | Encryption protects card transactions and data | ❌ No |
| PCI DSS | Secure password management | ❌ No |
| GDPR | E.U. customer data is kept private and secure | ❌ No |
| GDPR | Plan to notify E.U. customers within 72 hours of a breach | ✅ Yes |
| GDPR | Data is classified and inventoried | ❌ No |
| GDPR | Privacy policies and processes are enforced | ✅ Yes |
| SOC | User access policies are established | ❌ No |
| SOC | Sensitive data (PII/SPII) is confidential | ❌ No |
| SOC | Data integrity is ensured | ✅ Yes |
| SOC | Data is available to authorized users | ❌ No |

## 🔎 Main findings

The biggest risks are:

- **Weak access control:** everyone can reach sensitive data, including customer and card information.
- **No encryption** of credit card data.
- **No backups or disaster recovery plan,** so a failure or attack could cause serious data loss.
- **No intrusion detection system (IDS),** so suspicious activity may go unnoticed.

A few weak controls affect several rules at once. For example, missing encryption and access control put Botium Toys out of line with PCI DSS, GDPR and SOC at the same time.

## ✅ Recommendations

| Priority | Recommendation | Why it matters |
|---|---|---|
| 1 | **Least privilege and separation of duties:** give employees access only to the data they need for their job, especially customer and card data | Reduces insider risk and supports PCI DSS, GDPR and SOC |
| 2 | **Stronger passwords and MFA:** use a central password manager, require complex passwords and enable multi-factor authentication | Protects accounts from takeover and supports PCI DSS |
| 3 | **Encryption and detection:** encrypt data at rest and in transit, install an IDS, and prepare backups and disaster recovery plans | Protects data and speeds up detection and recovery |

## 💡 What I learned

In this project I learned how a security audit works step by step: first define the scope and goals, then look at the company's assets and risks, and then check each control and compliance requirement with evidence from the report. I learned that controls come in different kinds (administrative, technical and physical) and that they work together, so one missing control can leave a gap even when others are strong.

What surprised me most was that Botium Toys had good physical security and basic protection like a firewall and antivirus, but weak protection for the data itself: no encryption, no backups and too much employee access to customer data. This showed me that a few weak controls can create problems for several rules at once, like PCI DSS, GDPR and SOC.

Finally, I practiced turning my findings into clear recommendations, starting with the most important ones: limiting access, using strong passwords with MFA, and encrypting and backing up data.

---

<sub>This is a training scenario from the Google Cybersecurity Certificate. Botium Toys is a fictional company.</sub>
