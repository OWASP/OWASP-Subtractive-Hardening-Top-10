# OWASP Windows Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Microsoft Windows  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Windows Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing cyber risk through the elimination of attacker-accessible execution paths.

Unlike traditional hardening frameworks that focus primarily on vulnerabilities, signatures, alerts, or tooling, Subtractive Hardening prioritizes the removal of architectural conditions that allow vulnerabilities to compose into credential theft, privilege escalation, lateral movement, persistence, and business impact.

Rather than relying on reactive threat detection, alert tuning, or continuous triage, the objective is to physically remove executable edges from the Windows system graph:

```math
G = (V,E)
```

Each recommendation within this standard is intentionally selected based on its ability to reduce adversary reachability and improve measurable attack-path reduction through the Path Erasure Rate (PER) Engineering Standard.

```math
PER = \frac{|P_{erased}|}{|P_{eligible}|}
```

Where:

- \(P_eligible\) represents eligible attack paths identified within scope.
- \(P_erased\) represents attack paths rendered non-traversable through architectural deletion.

The objective of this standard is not to make attacks easier to detect.

The objective is to make attacks impossible by removing the pathways that enable them.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The Windows Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within Microsoft Windows environments.

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

- Protocol removal
- Feature removal
- Trust relationship removal
- Permission removal
- Execution pathway removal

## Tier 2 – Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Application control
- Segmentation
- Conditional access
- Just Enough Administration
- Constrained execution models

## Tier 3 – Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- EDR
- SIEM
- IDS/IPS
- Logging
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

# OWASP Windows Subtractive Hardening Top 10

| ID | Title |
|------|------|
| S01 | Process Tree Integrity |
| S02 | Protocol Extinction |
| S03 | Execution Locality |
| S04 | Lateral Path Erasure |
| S05 | Credential Guardrails |
| S06 | Scripting Host Lockdown |
| S07 | Surface Area Pruning |
| S08 | Identity Path Silencing |
| S09 | Shell Contextualization |
| S10 | Egress Determinism |

---

# S01: Process Tree Integrity

## Description

Browsers, email clients, PDF readers, and office productivity applications frequently serve as the initial execution platform for adversary activity.

## Strategic Objective

Prevent user-facing applications from launching command interpreters, scripting engines, and administrative tooling.

## Attack Path Removed

```text
Browser / Office
        ↓
cmd.exe / powershell.exe
        ↓
Post-Exploitation Execution
```

## Architectural Deletion Goal

Remove shell-spawning capability from user-facing applications.

## Implementation Examples

- Microsoft Defender ASR: Block Office child process creation.
- Restrict Office-to-PowerShell execution.
- Restrict browser-launched shells.
- Restrict Office-launched command interpreters.

---

# S02: Protocol Extinction

## Description

Legacy discovery and authentication protocols enable credential harvesting, spoofing, relay attacks, and downgrade opportunities.

## Strategic Objective

Eliminate obsolete trust mechanisms.

## Attack Path Removed

```text
Attacker
      ↓
NTLM / LLMNR / NetBIOS
      ↓
Credential Capture
```

## Architectural Deletion Goal

Remove legacy protocol dependencies wherever possible.

## Implementation Examples

- Disable LLMNR.
- Disable NetBIOS.
- Eliminate NTLM dependencies.
- Require SMB signing.
- Prefer Kerberos authentication.

---

# S03: Execution Locality

## Description

User-writable locations provide one of the most common malware execution surfaces within Windows environments.

## Strategic Objective

Prevent execution from locations controlled by standard users.

## Attack Path Removed

```text
User-Writable Directory
            ↓
Unauthorized Binary
            ↓
Execution
```

## Architectural Deletion Goal

Eliminate executable attack paths originating from user-controlled storage locations.

## Implementation Examples

- WDAC deployment.
- AppLocker enforcement.
- Block execution from:
  - %AppData%
  - %Temp%
  - Downloads
  - User profile directories

---

# S04: Lateral Path Erasure

## Description

Direct workstation-to-workstation administrative connectivity forms the primary movement graph used during ransomware propagation and Active Directory compromise.

## Strategic Objective

Remove peer administrative transit between endpoints.

## Attack Path Removed

```text
Workstation A
      ↓
RDP / SMB / WinRM
      ↓
Workstation B
```

## Architectural Deletion Goal

Eliminate endpoint-to-endpoint administrative pathways.

## Implementation Examples

- Block workstation SMB.
- Block workstation RDP.
- Block workstation WinRM.
- Permit administration only from approved management systems.

---

# S05: Credential Guardrails

## Description

Credential material stored in memory creates opportunities for direct credential theft and replay.

## Strategic Objective

Prevent attacker access to authentication secrets.

## Attack Path Removed

```text
Process
    ↓
Credential Material
    ↓
Credential Theft
```

## Architectural Deletion Goal

Isolate credential material from attacker-accessible memory spaces.

## Implementation Examples

- Credential Guard.
- RunAsPPL.
- Disable WDigest.
- LSASS protection.

---

# S06: Scripting Host Lockdown

## Description

Windows Script Host provides a native execution mechanism frequently abused during malware campaigns.

## Strategic Objective

Remove unnecessary script execution capability.

## Attack Path Removed

```text
User
   ↓
wscript.exe / cscript.exe
   ↓
Execution
```

## Architectural Deletion Goal

Eliminate unnecessary scripting hosts from standard-user execution paths.

## Implementation Examples

- Disable Windows Script Host.
- Restrict VBScript.
- Remove unnecessary legacy automation engines.

---

# S07: Surface Area Pruning

## Description

Unused operating system components increase attack surface while providing little or no operational value.

## Strategic Objective

Remove unnecessary operating system features.

## Attack Path Removed

```text
Legacy Component
       ↓
Vulnerability
       ↓
Compromise
```

## Architectural Deletion Goal

Reduce exploitable surface area through subsystem removal.

## Implementation Examples

- Remove SMBv1.
- Remove XPS services.
- Remove unnecessary fax services.
- Reduce printing services where operationally feasible.
- Review optional feature footprint.

---

# S08: Identity Path Silencing

## Description

Shared administrative identities enable credential chaining and rapid compromise propagation.

## Strategic Objective

Eliminate network-accessible local administrator pathways.

## Attack Path Removed

```text
Compromised Host
        ↓
Local Administrator
        ↓
Additional Systems
```

## Architectural Deletion Goal

Remove shared administrative credential pathways.

## Implementation Examples

- Windows LAPS.
- Unique local administrative credentials.
- Removal from network-accessible groups.
- Restrict local administrator use.

---

# S09: Shell Contextualization

## Description

PowerShell provides powerful administrative capability frequently abused during Living-Off-the-Land operations.

## Strategic Objective

Constrain shell functionality to legitimate administrative operations.

## Attack Path Removed

```text
PowerShell
      ↓
Arbitrary Post-Exploitation
      ↓
Persistence / Movement
```

## Architectural Constraint Goal

Reduce attacker utility while preserving legitimate administration.

## Implementation Examples

- Constrained Language Mode.
- Just Enough Administration (JEA).
- Script Block Logging.
- Restricted PowerShell endpoints.

---

# S10: Egress Determinism

## Description

Unrestricted outbound communications provide command-and-control and data exfiltration pathways.

## Strategic Objective

Eliminate arbitrary outbound connectivity.

## Attack Path Removed

```text
Endpoint
    ↓
Internet
    ↓
Command and Control
```

## Architectural Deletion Goal

Restrict egress communications to approved, authenticated pathways.

## Implementation Examples

- Authenticated proxy-only egress.
- Explicit outbound allowlists.
- DNS governance.
- Egress filtering controls.

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

*OWASP Windows Subtractive Hardening Top 10 v1.0*
