# Course 2: Play It Safe: Manage Security Risks

[← Back to certificate overview](../README.md)

| | |
|---|---|
| **Status** | ✅ Completed |
| **Focus** | Managing risk with frameworks and controls, and responding to incidents |
| **Modules** | 4: Security domains · Security frameworks and controls · Introduction to cybersecurity tools · Use playbooks to respond to incidents |
| **Official page** | [Coursera](https://www.coursera.org/learn/manage-security-risks) |

## Big picture
Risk management means finding what could go wrong, deciding how serious it is and reducing the damage.
- **Threat**: anything that could harm an asset
- **Vulnerability**: a weakness a threat can use
- **Risk**: the chance that an asset's confidentiality, integrity or availability is harmed
- **Risk mitigation**: having procedures ready to reduce the impact quickly

Threats can be **internal** (employees, vendors, partners) or **external** (outsiders). **Attack vectors** are the paths attackers use. **Ransomware** is one example: attackers lock data and demand payment.

## NIST Cybersecurity Framework: five functions
1. **Identify**: understand the risks to people, assets and data
2. **Protect**: put policies, training and tools in place
3. **Detect**: find possible incidents quickly through monitoring
4. **Respond**: contain and analyze incidents and improve afterwards
5. **Recover**: return systems to normal operation

## NIST Risk Management Framework: seven steps
Prepare → Categorize → Select → Implement → Assess → Authorize → Monitor

In short: get ready before a breach happens, sort systems by risk, choose and apply controls, check that the controls work, take responsibility for the remaining risk and keep watching. NIST also publishes **SP 800-53**, a detailed set of security controls used by U.S. federal systems.

## Access and data protection
- **Authentication** proves who you are; **authorization** decides what you may access.
- **Biometrics** use physical traits (like fingerprints) for authentication.
- **Encryption** turns readable data into an encoded form so only the right people can read it.

## Audits, posture and responsibility
- A **security audit** reviews controls, policies and procedures against a set of expectations.
- **Security posture** is how well an organization can defend its critical assets and adapt to change.
- **Business continuity** means staying productive through plans for disasters and recovery.
- **Shared responsibility**: everyone in an organization helps reduce risk.

## Monitoring and response tools
- **SIEM** tools collect and analyze logs. Examples in the course: **Splunk** (Cloud and Enterprise) and **Chronicle**.
- **SOAR** uses automation to respond to security events faster.
- **Playbooks** are step-by-step guides for handling a known type of incident.
- **Incident response** means quickly identifying an attack, containing the damage and fixing the effects.

## What I learned
In Course 2 I moved from basic ideas to how organizations manage risk. I learned the difference between a threat, a vulnerability and a risk, and how organizations use the NIST Cybersecurity Framework (identify, protect, detect, respond, recover) and the NIST Risk Management Framework to organize their security work. I also learned about access control (authentication and authorization), encryption, security audits and why security is a shared responsibility. Finally, I was introduced to SIEM tools (such as Splunk and Chronicle), SOAR, and playbooks that guide a team during incident response.

## Hands-on activity
In the hands-on activity I did a security audit for a fictional company, Botium Toys. I reviewed its assets and risks, completed a controls checklist and a compliance checklist (PCI DSS, GDPR and SOC), and wrote recommendations for the IT manager. This showed me how security controls connect to compliance rules and why access control, encryption and backups matter so much.

Full project: [Security Audit for Botium Toys](../activities/botium-toys-security-audit/)

## What was difficult or interesting
The NIST frameworks were the hardest at first because they have many steps and new terms. What interested me most was how SIEM tools and playbooks help analysts react to incidents in an organized way.
