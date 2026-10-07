# Google Cybersecurity Certificate (Coursera)

My notes in my own words. I do not publish quiz answers or copy course materials.

## Courses

| # | Course | Status | Notes |
|---|---|---|---|
| 1 | Foundations of Cybersecurity | ✅ Completed | [Go to notes](#course-1-foundations-of-cybersecurity) |
| 2 | Play It Safe: Manage Security Risks | ✅ Completed | [Go to notes](#course-2-play-it-safe-manage-security-risks) |
| 3 | Connect and Protect: Networks and Network Security | 🔄 In progress | [Go to notes](#course-3-connect-and-protect-networks-and-network-security) |
| 4 | Tools of the Trade: Linux and SQL | 📅 Planned | [Go to notes](#course-4-tools-of-the-trade-linux-and-sql) |
| 5 | Assets, Threats, and Vulnerabilities | 📅 Planned | [Go to notes](#course-5-assets-threats-and-vulnerabilities) |
| 6 | Sound the Alarm: Detection and Response | 📅 Planned | [Go to notes](#course-6-sound-the-alarm-detection-and-response) |
| 7 | Automate Cybersecurity Tasks with Python | 📅 Planned | [Go to notes](#course-7-automate-cybersecurity-tasks-with-python) |
| 8 | Put It to Work: Prepare for Cybersecurity Jobs | 📅 Planned | [Go to notes](#course-8-put-it-to-work-prepare-for-cybersecurity-jobs) |
| 9 | Accelerate Your Job Search with AI | 📅 Planned | [Go to notes](#course-9-accelerate-your-job-search-with-ai) |

## Overall summary

The certificate has nine courses. So far (courses 1 and 2) I learned how security professionals think. Course 1 introduced what we protect (assets, data, people), what threatens it (attackers, social engineering, malware) and the basic goals of security: confidentiality, integrity and availability. Course 2 moved from "what can go wrong" to "how organizations manage it": identifying risks, using frameworks such as NIST, controlling access, auditing, monitoring with SIEM tools and responding with playbooks.

*This summary will be updated as I finish more courses.*

**My reflection:** [2-3 sentences: what surprised you, what was most useful]

---

## Course 1: Foundations of Cybersecurity

**Status:** ✅ Completed

### Big picture
Security is about protecting networks, devices, people and data from unauthorized access and misuse. Everything starts with understanding **assets** (what has value), **threats** (what could harm them) and who the **threat actors** are (hackers, hacktivists, insiders).

### The CIA triad
| Principle | In my words |
|---|---|
| Confidentiality | Only the right people can see the data |
| Integrity | The data is correct and has not been tampered with |
| Availability | Authorized people can reach the data when they need it |

### Common attacks and tactics
| Attack | In my words |
|---|---|
| Phishing | Tricking people by message or email into giving data or running malware |
| Spear phishing | Phishing aimed at a specific person or group, pretending to be someone they trust |
| Business email compromise | Impersonating a known sender to get money |
| Vishing | The same trick over phone or voice calls |
| Social media phishing | Collecting details about a target online before attacking |
| Watering hole | Compromising a website that a target group often visits |
| USB baiting | Leaving an infected USB drive for someone to plug in |
| Physical social engineering | Pretending to be an employee or vendor to enter a building |
| Supply-chain attack | Attacking a weak point in the software or hardware that organizations rely on |
| Password and cryptographic attacks | Trying to break into accounts or weaken secure communication |
| Adversarial AI | Using or manipulating AI to make attacks more efficient |

The common thread is **social engineering**: attacks often exploit human mistakes rather than technical flaws.

### Data and privacy
- **PII**: information that can identify a person. **SPII** is the more sensitive kind and needs stricter handling.
- **PHI**: health-related information about a person. In the US, HIPAA is the law that protects it.
- **Privacy protection** means keeping personal information from being misused.

### Frameworks, controls and ethics
- **Security frameworks** give organizations a structure for planning how to reduce risk; **NIST CSF** is a voluntary example.
- **Security controls** are the specific safeguards that reduce a risk.
- **Security governance** and **security ethics** guide how decisions are made, including acting responsibly with sensitive data.
- **OWASP** is a non-profit that works on improving software security.

### Tools and skills introduced
- **SIEM** collects and analyzes logs to watch for suspicious activity. **IDS** alerts on possible intrusions. A **packet sniffer** captures and analyzes network traffic.
- **Logs** record what happens in a system.
- Skills mentioned: Linux, SQL and programming basics, plus transferable skills from other areas of life.
- **Order of volatility**: when collecting digital evidence, the most fragile data should be preserved first.

### What I learned
[Write 4-5 sentences in your own words.]

### What was difficult or interesting
[Your reflection]

### How I can use this in real life
[Example: spotting phishing messages, protecting my family's accounts]

---

## Course 2: Play It Safe: Manage Security Risks

**Status:** ✅ Completed

### Big picture
Risk management means finding what could go wrong, deciding how serious it is and reducing the damage.
- **Threat**: anything that could harm an asset
- **Vulnerability**: a weakness a threat can use
- **Risk**: the chance that an asset's confidentiality, integrity or availability is harmed
- **Risk mitigation**: having procedures ready to reduce the impact quickly

Threats can be **internal** (employees, vendors, partners) or **external** (outsiders). **Attack vectors** are the paths attackers use. **Ransomware** is one example: attackers lock data and demand payment.

### NIST Cybersecurity Framework: five functions
1. **Identify**: understand the risks to people, assets and data
2. **Protect**: put policies, training and tools in place
3. **Detect**: find possible incidents quickly through monitoring
4. **Respond**: contain and analyze incidents and improve afterwards
5. **Recover**: return systems to normal operation

### NIST Risk Management Framework: seven steps
Prepare → Categorize → Select → Implement → Assess → Authorize → Monitor

In short: get ready before a breach happens, sort systems by risk, choose and apply controls, check that the controls work, take responsibility for the remaining risk and keep watching. NIST also publishes **SP 800-53**, a detailed set of security controls used by U.S. federal systems.

### Access and data protection
- **Authentication** proves who you are; **authorization** decides what you may access.
- **Biometrics** use physical traits (like fingerprints) for authentication.
- **Encryption** turns readable data into an encoded form so only the right people can read it.

### Audits, posture and responsibility
- A **security audit** reviews controls, policies and procedures against a set of expectations.
- **Security posture** is how well an organization can defend its critical assets and adapt to change.
- **Business continuity** means staying productive through plans for disasters and recovery.
- **Shared responsibility**: everyone in an organization helps reduce risk.

### Monitoring and response tools
- **SIEM** tools
