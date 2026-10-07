# Project 4: Security Audit for Botium Toys

**Status:** ✅ Completed · **Source:** Google Cybersecurity Certificate (Coursera), Course 2 · **Scenario:** fictional company

## Goal
Act as an entry-level security analyst doing an internal IT audit for a fictional toy company, Botium Toys. I reviewed the company's assets and security situation, checked which security controls and compliance practices are in place, and recommended improvements.

## What I did
1. Read the scope, goals and risk assessment of the audit.
2. Reviewed the company's assets and the main risks to them.
3. Completed a **controls assessment checklist** (14 controls).
4. Completed a **compliance checklist** for PCI DSS, GDPR and SOC.
5. Wrote recommendations for the IT manager.

## Controls assessment

| Control | In place? | Why |
|---|---|---|
| Least privilege | No | All employees can access internal data, including customer data |
| Disaster recovery plans | No | No plans exist |
| Password policies | No | A policy exists, but its requirements are too weak |
| Separation of duties | No | Not implemented |
| Firewall | Yes | Blocks traffic based on defined security rules |
| Intrusion detection system (IDS) | No | Not installed |
| Backups | No | No backups of critical data |
| Antivirus software | Yes | Installed and monitored regularly |
| Manual monitoring of legacy systems | No | Done, but without a regular schedule or clear intervention steps |
| Encryption | No | Credit card data is not encrypted |
| Password management system | No | No central system to enforce password rules |
| Locks (office, store, warehouse) | Yes | Sufficient locks in place |
| CCTV | Yes | Up to date and working |
| Fire detection and prevention | Yes | Working systems in place |

## Compliance assessment

| Standard | Best practice | Met? |
|---|---|---|
| PCI DSS | Only authorized users can access card data | No |
| PCI DSS | Card data is handled in a secure environment | No |
| PCI DSS | Encryption protects card transactions and data | No |
| PCI DSS | Secure password management | No |
| GDPR | E.U. customer data is kept private and secure | No |
| GDPR | Plan to notify E.U. customers within 72 hours of a breach | Yes |
| GDPR | Data is classified and inventoried | No |
| GDPR | Privacy policies and processes are enforced | Yes |
| SOC | User access policies are established | No |
| SOC | Sensitive data (PII/SPII) is confidential | No |
| SOC | Data integrity is ensured | Yes |
| SOC | Data is available to authorized users | No |

## Main findings
The biggest risks are weak access control (everyone can reach sensitive data), no encryption of card data, no backups or disaster recovery plan, and no IDS. Physical security (locks, CCTV, fire systems) and basic network protection (firewall, antivirus) are in good shape.

## My recommendations
1. **Least privilege and separation of duties:** give employees access only to the data they need for their job, especially customer and card data.
2. **Stronger passwords and MFA:** use a central password manager, require complex passwords and enable multi-factor authentication.
3. **Encryption and detection:** encrypt data at rest and in transit (needed for PCI DSS and GDPR), install an IDS, and prepare disaster recovery plans and backups.

## Completed checklist
[Controls and compliance checklist (PDF)](botium-controls-and-compliance-checklist.pdf)

## What I learned
In this project I learned how a security audit works step by step: first define the scope and goals, then look at the company's assets and risks, and then check each control and compliance requirement with evidence from the report. I learned that controls come in different kinds (administrative, technical and physical) and that they work together, so one missing control can leave a gap even when others are strong. What surprised me most was that Botium Toys had good physical security and basic protection like a firewall and antivirus, but weak protection for the data itself: no encryption, no backups and too much employee access to customer data. This showed me that a few weak controls can create problems for several rules at once, like PCI DSS, GDPR and SOC. Finally, I practiced turning my findings into clear recommendations, starting with the most important ones: limiting access, using strong passwords with MFA, and encrypting and backing up data.

> This is a training scenario. Botium Toys is a fictional company.
