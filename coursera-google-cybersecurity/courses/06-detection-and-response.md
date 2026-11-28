# Course 6: Sound the Alarm: Detection and Response

[← Back to certificate overview](../README.md)

| | |
|---|---|
| **Status** | ✅ Completed |
| **Focus** | Detecting security incidents, investigating them and responding |
| **Modules** | 4: Introduction to detection and incident response · Network monitoring and analysis · Incident investigation and response · Network traffic and logs using IDS and SIEM tools |
| **Official page** | [Coursera](https://www.coursera.org/learn/detection-and-response) |

## Big picture
Prevention will not stop everything, so analysts also need to notice when something goes wrong and know what to do next. This course follows an incident from the first alert to the final report.

## Incidents and the response lifecycle
A **security incident** is an event that threatens the confidentiality, integrity or availability of an asset. The response follows a lifecycle, based on the NIST model:

1. **Preparation:** plans, tools and trained people before anything happens
2. **Detection and analysis:** notice the event and decide whether it is a real incident
3. **Containment, eradication and recovery:** stop the damage, remove the cause and restore normal work
4. **Post-incident activity:** review what happened and improve

Incident response is a team effort. A computer security incident response team (**CSIRT**) has defined roles, and **documentation** such as playbooks and clear records keeps everyone consistent.

## Network monitoring and analysis
A **packet sniffer** captures network traffic so it can be read and filtered. **Wireshark** has a graphical interface and **tcpdump** works in the command line. Analysts use filters to find the traffic that matters, for example by address or port, and then check it for signs of attacks.

## Investigating an incident
- **Artifacts** such as files, logs and hashes show what happened. Checking a **file hash** against a reputation service shows whether a file is known to be malicious.
- **Indicators of compromise (IoCs)** are signs that a system may be compromised, such as a strange IP address or file hash.
- Good **documentation** and evidence handling matter, because the record may be used later.
- Mapping the artifacts in order builds a **timeline** of the incident.

## IDS and SIEM
| Tool | What it does |
|---|---|
| Intrusion detection system (IDS) | Watches traffic or hosts and raises an alert when something matches a rule or signature |
| Network IDS (NIDS) | An IDS that watches network traffic |
| SIEM | Collects logs from many sources and lets an analyst search and correlate them. Examples: Splunk and Chronicle |

**Logs** record events in a system. An IDS **signature** describes what bad traffic looks like and usually has three parts: an action, a header (protocol, addresses and ports) and options that say what to match. Basic rules are readable once you know that structure. In a SIEM, an analyst writes queries to find the events linked to an alert.

## What I learned
I learned that detection is only useful if it leads to a clear next step. The lifecycle gave me a simple order to follow: prepare, detect, contain, then learn from it. I also learned how analysts work with packets, hashes, logs and SIEM queries to confirm whether an alert is real, and why careful documentation is part of the job and not an extra.
