# OWASP Active Directory Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Microsoft Active Directory  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Active Directory Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing identity-based cyber risk through the elimination of attack paths capable of enabling domain compromise.

Unlike traditional Active Directory hardening frameworks that focus primarily on auditing, monitoring, or compliance validation, Subtractive Hardening prioritizes the removal of architectural conditions that allow attackers to traverse from low privilege contexts to domain dominance.

Rather than relying on reactive detection, the objective is to physically remove exploitable trust, authentication, credential, and permission relationships from the Active Directory attack graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Identities, Systems, Directory Objects, Services
E = Authentication, Trust, Permission, or Reachability Relationships
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

The objective is to make domain compromise impossible by removing the pathways that enable it.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The Active Directory Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within enterprise identity environments.

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

- Authentication protocol removal
- Trust relationship removal
- Permission removal
- Service removal
- Replication path removal

## Tier 2 – Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Administrative tiering
- Segmentation
- Conditional access
- Authentication assurance
- Access restrictions

## Tier 3 – Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- Defender for Identity
- SIEM
- Event Logging
- EDR
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
- Reduce domain dominance pathways.
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

# OWASP Active Directory Subtractive Hardening Top 10

| ID | Title |
|------|------|
| AD01 | Legacy Authentication Extinction |
| AD02 | Kerberos Service Trust Reduction |
| AD03 | Directory Credential Exposure Elimination |
| AD04 | Authentication Relay Erasure |
| AD05 | Privileged Identity Mobility Restriction |
| AD06 | Directory Replication Path Elimination |
| AD07 | Certificate Trust Path Reduction |
| AD08 | Domain Controller Surface Area Pruning |
| AD09 | Directory Network Segmentation |
| AD10 | AD Data Exposure Reduction |

---

# AD01: Legacy Authentication Extinction

## Description

Legacy authentication protocols enable downgrade attacks, password cracking, relay opportunities, and credential abuse.

## Strategic Objective

Eliminate obsolete authentication mechanisms.

## Attack Path Removed

```text
Attacker
      ↓
DES / NTLMv1 / Legacy NTLM
      ↓
Credential Abuse
      ↓
Privilege Escalation
```

## Architectural Deletion Goal

Remove legacy authentication pathways from the identity plane.

## Implementation Examples

- Disable DES encryption support.
- Disable NTLMv1.
- Restrict NTLM usage.
- Prefer Kerberos wherever possible.
- Remove LM hash support.

---

# AD02: Kerberos Service Trust Reduction

## Description

Service Principal Names (SPNs) create opportunities for Kerberoasting and offline credential recovery.

## Strategic Objective

Reduce Kerberos-based credential extraction paths.

## Attack Path Removed

```text
Authenticated User
         ↓
SPN
         ↓
Service Ticket
         ↓
Offline Cracking
```

## Architectural Deletion Goal

Reduce unnecessary service trust relationships.

## Implementation Examples

- Remove stale SPNs.
- Eliminate unnecessary service accounts.
- Deploy gMSAs.
- Require long randomized service credentials.
- Review delegated service privileges.

---

# AD03: Directory Credential Exposure Elimination

## Description

Unprotected directory communications expose authentication material and directory operations to interception or abuse.

## Strategic Objective

Eliminate credential exposure during directory operations.

## Attack Path Removed

```text
Client
   ↓
LDAP
   ↓
Credential Disclosure
```

## Architectural Deletion Goal

Remove cleartext or weak directory communication pathways.

## Implementation Examples

- Require LDAPS.
- Require channel binding.
- Disable simple binds.
- Enforce secure LDAP communications.

---

# AD04: Authentication Relay Erasure

## Description

Unsigned authentication mechanisms enable relay attacks capable of providing unauthorized access.

## Strategic Objective

Remove relay opportunities.

## Attack Path Removed

```text
Attacker
      ↓
Unsigned Authentication
      ↓
Relay
      ↓
Privilege
```

## Architectural Deletion Goal

Eliminate replayable and relayable authentication paths.

## Implementation Examples

- Enable LDAP signing.
- Enable SMB signing.
- Enable Extended Protection for Authentication (EPA).
- Reduce NTLM dependencies.

---

# AD05: Privileged Identity Mobility Restriction

## Description

Many domain compromises occur when privileged identities traverse lower-trust systems and environments.

## Strategic Objective

Reduce privileged identity movement and credential exposure.

## Attack Path Removed

```text
Compromised User
          ↓
Privileged Credential Exposure
          ↓
Administrative Access
```

## Architectural Constraint Goal

Prevent privileged account mobility across trust zones.

## Implementation Examples

- Separate user and administrative accounts.
- Implement administrative tiering.
- Deploy Privileged Access Workstations (PAWs).
- Implement LAPS.
- Restrict administrative logon locations.

---

# AD06: Directory Replication Path Elimination

## Description

Replication permissions enable DCSync and DCShadow attacks capable of creating complete domain compromise.

## Strategic Objective

Remove unnecessary replication rights.

## Attack Path Removed

```text
Compromised Account
          ↓
Replication Rights
          ↓
DCSync
          ↓
KRBTGT Access
```

## Architectural Deletion Goal

Remove unauthorized replication capability.

## Implementation Examples

- Audit replication permissions.
- Remove unnecessary Replicating Directory Changes rights.
- Reduce synchronization accounts.
- Eliminate unauthorized replication principals.
- Restrict DCShadow opportunities.

---

# AD07: Certificate Trust Path Reduction

## Description

Misconfigured Active Directory Certificate Services (ADCS) creates direct pathways to domain privilege escalation.

## Strategic Objective

Reduce certificate abuse pathways.

## Attack Path Removed

```text
Authenticated User
          ↓
Certificate Enrollment
          ↓
Certificate Impersonation
          ↓
Privilege Escalation
```

## Architectural Deletion Goal

Remove dangerous certificate trust relationships.

## Implementation Examples

- Eliminate ADCS escalation (ESC1-16) attack paths (https://docs.specterops.io/ghostpack-docs/Certify.wik-mdx/4-escalation-techniques).
- Remove vulnerable certificate templates.
- Restrict enrollment permissions.
- Restrict Enrollment Agent rights.
- Reduce certificate issuance attack surface.

---

# AD08: Domain Controller Surface Area Pruning

## Description

Unnecessary services increase the attack surface of domain controllers.

## Strategic Objective

Reduce domain controller attack surface.

## Attack Path Removed

```text
Unnecessary Service
          ↓
Vulnerability
          ↓
Domain Compromise
```

## Architectural Deletion Goal

Eliminate unnecessary functionality.

## Implementation Examples

- Disable Print Spooler.
- Remove unnecessary software.
- Remove unnecessary agents.
- Remove unnecessary roles.
- Minimize domain controller functionality.

---

# AD09: Directory Network Segmentation

## Description

Unrestricted network reachability to domain controllers increases attacker optionality.

## Strategic Objective

Reduce domain controller accessibility.

## Attack Path Removed

```text
Compromised Endpoint
           ↓
Domain Controller
           ↓
Credential Theft
```

## Architectural Deletion Goal

Reduce unnecessary directory reachability.

## Implementation Examples

- Segment management networks.
- Restrict domain controller access.
- Limit administrative protocol exposure.
- Restrict east-west movement pathways.

---

# AD10: AD Data Exposure Reduction

## Description

Improper SYSVOL and NETLOGON permissions frequently expose credentials, scripts, and privileged configuration artifacts.

## Strategic Objective

Reduce identity intelligence gathering opportunities.

## Attack Path Removed

```text
User
   ↓
SYSVOL / NETLOGON
   ↓
Credential Discovery
   ↓
Privilege Escalation
```

## Architectural Deletion Goal

Remove unnecessary exposure of directory-resident data.

## Implementation Examples

- Audit SYSVOL permissions.
- Audit NETLOGON permissions.
- Remove credential artifacts.
- Remove legacy scripts containing secrets.
- Restrict unnecessary access.

---

# Verification & PER Measurement

## Step 1 – Establish Baseline

Identify all eligible attack paths.

```text
P_eligible(t0)
```

## Step 2 – Implement Controls

Apply AD01 through AD10.

## Step 3 – Validate Erasure

Identify attack paths rendered non-traversable.

```text
P_erased(t1)
```

## Step 4 – Calculate PER

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Success Criteria

The objective is not improved visibility.

The objective is measurable reduction in reachable attack-path availability.

---

# Strategic Objective: Non-Conductivity

The goal of these subtractions is to establish deterministic trust boundaries within Active Directory.

By collapsing attack paths, the identity environment becomes architecturally non-conductive.

In this model:

```text
Credential = Fuel
Trust Path = Oxygen
Identity Architecture = Conductivity
```

Remove the path, and compromise propagation becomes increasingly difficult.

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

*OWASP Active Directory Subtractive Hardening Top 10 v1.0*
