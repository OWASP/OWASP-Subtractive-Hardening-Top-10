# OWASP Linux Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Linux  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Linux Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing cyber risk through the elimination of attacker-accessible execution, trust, privilege escalation, credential exposure, and persistence paths within Linux environments.

Unlike traditional Linux hardening guidance that focuses primarily on vulnerability remediation, configuration management, monitoring, or compliance, Subtractive Hardening prioritizes the removal of architectural conditions that allow attackers to compose isolated weaknesses into meaningful system compromise.

Rather than relying on reactive detection, alert tuning, or operational monitoring, the objective is to physically remove executable edges from the Linux system graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Users, Processes, Services, Containers, Filesystems, Credentials
E = Trust, Execution, Authentication, Privilege, or Communication Relationships
```

Each recommendation within this standard is intentionally selected based on its ability to reduce adversary reachability and improve measurable attack-path reduction through the Path Erasure Rate (PER) Engineering Standard.

```text
PER = P_erased / P_eligible
```

Where:

```text
P_eligible = Eligible attack paths identified within scope
P_erased   = Attack paths rendered non-traversable through architectural deletion
```

The objective of this standard is not to make attacks easier to detect.

The objective is to make attacks impossible by removing the pathways that enable them.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The Linux Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within Linux infrastructure.

Together they establish a repeatable security engineering cycle:

1. Identify attack paths.
2. Measure attack-path exposure.
3. Eliminate attack paths where possible.
4. Constrain residual attack paths where necessary.
5. Measure resulting reduction.
6. Continuously improve architectural resilience.

---

# The Subtractive Hierarchy of Efficacy

All recommendations within this standard follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 – Architectural Deletion

Remove the attack path completely.

Examples:

- Remove unnecessary services
- Remove unnecessary trust relationships
- Remove unnecessary privileges
- Remove unnecessary kernel capabilities
- Remove unnecessary execution paths

## Tier 2 – Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Sudo restrictions
- Container isolation
- SSH restrictions
- Network segmentation
- Application allow-listing

## Tier 3 – Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- EDR
- SIEM
- Auditd
- Syslog monitoring
- Alerting

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever an attack path can be eliminated, elimination is preferred.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate executable attack-path edges.
- Reduce credential theft opportunities.
- Reduce privilege escalation opportunities.
- Reduce lateral movement pathways.
- Reduce persistence opportunities.
- Reduce attack-path composability.
- Improve measurable Path Erasure Rate (PER).

Recommendations are not ranked based on:

- CVSS scores
- Vulnerability prevalence
- Compliance requirements
- Detection coverage
- Vendor capability claims

The primary selection criterion is architectural impact through attack-path reduction.

---

# OWASP Linux Subtractive Hardening Top 10

| ID | Title |
|------|------|
| L01 | Inline Execution Path Elimination |
| L02 | Filesystem Execution Locality |
| L03 | Administrative Trust Path Reduction |
| L04 | Sudo Privilege Path Reduction |
| L05 | Service & Daemon Surface Reduction |
| L06 | Authentication Backdoor Elimination |
| L07 | Credential Material Protection |
| L08 | Container Escape Path Reduction |
| L09 | Kernel Extension & Capability Reduction |
| L10 | Egress Determinism |

---

# L01: Inline Execution Path Elimination

## Description

Linux attackers frequently leverage shell interpreters and runtime environments to execute untrusted content directly from network streams.

## Strategic Objective

Eliminate the ability to transform downloaded content directly into executable instructions.

## Attack Path Removed

```text
Network Content
       ↓
Interpreter
       ↓
Code Execution
```

## Architectural Deletion Goal

Remove inline execution pathways that permit remote content to execute without validation.

## Implementation Examples

- Eliminate curl | bash workflows.
- Eliminate wget | sh workflows.
- Remove direct execution of decoded payloads.
- Require validated deployment mechanisms.
- Prefer immutable provisioning.

---

# L02: Filesystem Execution Locality

## Description

World-writable and transient directories provide a common staging area for malicious code execution.

## Strategic Objective

Restrict execution to explicitly approved locations.

## Attack Path Removed

```text
User-Writable Directory
           ↓
Executable Content
           ↓
Execution
```

## Architectural Deletion Goal

Eliminate execution originating from untrusted filesystem locations.

## Implementation Examples

- noexec on temporary filesystems.
- Block execution from:
  - /tmp
  - /var/tmp
  - /dev/shm
- Restrict user-writable execution paths.
- Require approved execution locations.

---

# L03: Administrative Trust Path Reduction

## Description

Administrative trust relationships enable Linux lateral movement and credential propagation between systems.

## Strategic Objective

Reduce administrative trust between Linux systems.

## Attack Path Removed

```text
Compromised Host
         ↓
Administrative Trust
         ↓
Additional Hosts
```

## Architectural Deletion Goal

Eliminate unnecessary administrative trust relationships.

## Implementation Examples

- Reduce SSH trust relationships.
- Eliminate shared SSH keys.
- Restrict agent forwarding.
- Reduce automation trust where feasible.
- Segment administrative access.

---

# L04: Sudo Privilege Path Reduction

## Description

Overly broad sudo privileges provide a direct path to root-level compromise.

## Strategic Objective

Reduce privilege escalation opportunities.

## Attack Path Removed

```text
User
   ↓
Excessive sudo Rights
   ↓
Root
```

## Architectural Deletion Goal

Remove unnecessary sudo privilege pathways.

## Implementation Examples

- Restrict sudo delegation.
- Eliminate unnecessary ALL and NOPASSWD sudo entries.
- Reduce shell-capable sudo entries.
- Review privilege inheritance.
- Minimize root-equivalent access.

---

# L05: Service & Daemon Surface Reduction

## Description

Unnecessary services increase attack surface while providing little or no business value.

## Strategic Objective

Minimize exposed functionality.

## Attack Path Removed

```text
Unnecessary Service
         ↓
Vulnerability
         ↓
Compromise
```

## Architectural Deletion Goal

Reduce service-related attack surface.

## Implementation Examples

- Remove unused daemons.
- Eliminate legacy services.
- Remove unnecessary listeners.
- Remove obsolete software.
- Minimize installed packages.

---

# L06: Authentication Backdoor Elimination

## Description

Persistent authentication artifacts frequently provide durable attacker access.

## Strategic Objective

Prevent unauthorized persistence through identity modification.

## Attack Path Removed

```text
Authentication Store
          ↓
Unauthorized Credential
          ↓
Persistence
```

## Architectural Deletion Goal

Remove persistent authentication backdoors.

## Implementation Examples

- Restrict authorized_keys modifications.
- Eliminate unauthorized account creation.
- Review SSH trust paths.
- Minimize persistent credentials.

---

# L07: Credential Material Protection

## Description

Credential stores and memory structures provide opportunities for credential theft.

## Strategic Objective

Protect authentication material from disclosure.

## Attack Path Removed

```text
Credential Store
        ↓
Credential Theft
        ↓
Privilege Escalation
```

## Architectural Deletion Goal

Reduce credential extraction opportunities.

## Implementation Examples

- Restrict access to /etc/shadow.
- Protect in-memory credentials.
- Reduce credential duplication.
- Isolate secrets.

---

# L08: Container Escape Path Reduction

## Description

Containerized workloads often share trust and execution relationships with underlying hosts.

## Strategic Objective

Prevent transitions from container context to host context.

## Attack Path Removed

```text
Container
      ↓
Escape
      ↓
Host
```

## Architectural Deletion Goal

Remove host escape pathways.

## Implementation Examples

- Minimize privileges.
- Eliminate privileged containers.
- Restrict namespace abuse.
- Harden container boundaries.

---

# L09: Kernel Extension & Capability Reduction

## Description

Kernel modules, eBPF programs, and excessive Linux capabilities provide high-impact privilege escalation pathways.

## Strategic Objective

Reduce kernel-level attack paths.

## Attack Path Removed

```text
Attacker
     ↓
Kernel Extension
     ↓
Kernel Privilege
```

## Architectural Deletion Goal

Remove unnecessary kernel modules, eBPF programs, loadable extensions, and excessive Linux capabilities that provide high-impact privilege escalation pathways.

## Implementation Examples

- Remove unused kernel modules.
- Restrict eBPF.
- Remove unnecessary capabilities.
- Minimize kernel attack surface.

---

# L10: Egress Determinism

## Description

Unrestricted outbound communications provide command-and-control and data exfiltration pathways.

## Strategic Objective

Eliminate arbitrary outbound connectivity.

## Attack Path Removed

```text
Host
   ↓
Internet
   ↓
Command & Control
```

## Architectural Deletion Goal

Restrict egress to approved destinations.

## Implementation Examples

- Explicit allowlists.
- Authenticated proxies.
- DNS governance.
- Egress filtering.

---

# Verification & PER Measurement

## Step 1 – Establish Baseline

Identify all eligible attack paths.

```math
|P_{eligible}(t_0)|
```

## Step 2 – Implement Controls

Apply S01 through S10.

## Step 3 – Validate Erasure

Identify attack paths rendered non-traversable.

```math
|P_{erased}(t_1)|
```

## Step 4 – Calculate PER

```math
PER(t_1)=\frac{|P_{erased}(t_1)|}{|P_{eligible}(t_1)|}
```

## Success Criteria

The objective is not improved visibility.

The objective is measurable reduction in reachable attack-path availability.

---

# Strategic Objective: Non-Conductivity

The goal of these subtractions is to establish deterministic boundaries within the enterprise.

By collapsing attack paths, the environment becomes architecturally non-conductive.

In this model:

- Vulnerabilities are sparks.
- Architecture determines whether those sparks become breaches.
- Attack paths provide the oxygen.

Remove the path, and the spark goes nowhere.

---

# Guiding Principle

Attackers can only traverse paths that exist.

The objective of Subtractive Hardening is to systematically eliminate or constrain those paths until adversary activity can no longer compose into material business impact.

**Security effectiveness is maximized when attack paths are removed, not merely observed.**

---

# References

- OWASP Subtractive Hardening Top 10 Project (https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main)
- Path Erasure Rate (PER-1.0) Engineering Standard (https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md)
- Evidence-Based Security (https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and)
- The Law of Subtractive Risk (https://subtractivesecurity.substack.com/p/the-law-of-subtractive-risk-moving)
- The Science of Silence

---

*OWASP Linux Subtractive Hardening Top 10 v1.0*
