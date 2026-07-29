# OWASP macOS Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** macOS  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP macOS Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing cyber risk through the elimination of attacker-accessible execution, trust, credential, persistence, and data-access pathways within Apple environments.

Unlike traditional hardening frameworks that focus primarily on vulnerabilities, signatures, alerts, detection content, or vendor tooling, Subtractive Hardening prioritizes the removal of architectural conditions that allow vulnerabilities to compose into credential theft, privilege escalation, persistence, lateral movement, and business impact.

Rather than relying on reactive detection, alert tuning, or continuous triage, the objective is to physically remove executable edges from the macOS system graph:

```math
G = (V,E)
```

Each recommendation within this standard is intentionally selected based on its ability to reduce adversary reachability and improve measurable attack-path reduction through the Path Erasure Rate (PER) Engineering Standard.

```math
PER = \frac{|P_{erased}|}{|P_{eligible}|}
```

Where:

- \(P_{eligible}\) represents eligible attack paths identified within scope.
- \(P_{erased}\) represents attack paths rendered non-traversable through architectural deletion.

The objective of this standard is not to make attacks easier to detect.

The objective is to make attacks impossible by removing the pathways that enable them.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The macOS Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within Apple environments.

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

- Trust relationship removal
- Feature removal
- Permission removal
- Persistence path removal
- Execution pathway removal

## Tier 2 – Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Application control
- MDM controls
- Identity restrictions
- Entitlement controls
- Container boundaries

## Tier 3 – Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- EDR
- SIEM
- Unified Logging
- Telemetry
- Alerting

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever an attack path can be eliminated, elimination is preferred.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate executable attack-path edges.
- Reduce credential theft opportunities.
- Reduce privilege escalation opportunities.
- Reduce persistence opportunities.
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

# OWASP macOS Subtractive Hardening Top 10

| ID | Title |
|------|------|
| M01 | Process Tree & Interpreter Integrity |
| M02 | Execution Locality & Path Restrictions |
| M03 | Administrative & Identity Trust Reduction |
| M04 | Credential Material & Keychain Protection |
| M05 | Persistence Path Elimination |
| M06 | Platform Trust Enforcement |
| M07 | TCC, Entitlement & Container Boundary Erasure |
| M08 | Service & Feature Surface Reduction |
| M09 | Egress Determinism |
| M10 | Device Management & Enrollment Trust Reduction |

---

# M01: Process Tree & Interpreter Integrity

## Description

Browsers, email clients, collaboration platforms, and productivity applications frequently serve as the initial execution platform for adversary activity.

## Strategic Objective

Prevent user-facing applications from launching interpreters, automation engines, and shell environments.

## Attack Path Removed

```text
Safari / Mail / Teams
          ↓
osascript / zsh / bash
          ↓
Post-Exploitation Execution
```

## Architectural Deletion Goal

Remove interpreter spawning capability from user-facing applications.

## Implementation Examples

- Restrict Safari-to-shell execution.
- Restrict Mail-to-osascript execution.
- Restrict collaboration applications from spawning interpreters.
- Remove unnecessary automation pathways.
- Block browser-to-shell execution chains.

---

# M02: Execution Locality & Path Restrictions

## Description

User-writable locations provide one of the most common malware execution surfaces within macOS environments.

## Strategic Objective

Prevent execution from untrusted user-controlled storage locations.

## Attack Path Removed

```text
Downloads / Writable Path
            ↓
Unauthorized Binary
            ↓
Execution
```

## Architectural Deletion Goal

Eliminate executable attack paths originating from user-controlled locations.

## Implementation Examples

- Restrict execution from Downloads.
- Restrict execution from /tmp.
- Restrict execution from user Library directories.
- Enforce approved execution locations.
- Enforce notarization requirements.

---

# M03: Administrative & Identity Trust Reduction

## Description

Administrative trust relationships enable privilege escalation and compromise propagation across systems.

## Strategic Objective

Reduce unnecessary administrative trust relationships.

## Attack Path Removed

```text
Compromised Mac
         ↓
Administrative Trust
         ↓
Additional Systems
```

## Architectural Deletion Goal

Remove unnecessary administrative and identity trust pathways.

## Implementation Examples

- Reduce local administrator assignments.
- Reduce sudo access.
- Remove shared local credentials.
- Eliminate unnecessary SSH trust.
- Limit directory binding relationships.

---

# M04: Credential Material & Keychain Protection

## Description

Keychain data and credential stores provide opportunities for credential theft, token theft, and identity compromise.

## Strategic Objective

Prevent unauthorized access to authentication material.

## Attack Path Removed

```text
Process
    ↓
Keychain / Token Store
    ↓
Credential Theft
```

## Architectural Deletion Goal

Reduce credential extraction opportunities.

## Implementation Examples

- Restrict Keychain access.
- Reduce application secret exposure.
- Protect authentication tokens.
- Constrain security tool exports.
- Reduce credential duplication.

---

# M05: Persistence Path Elimination

## Description

Persistent execution paths allow attackers to survive reboots and maintain long-term control.

## Strategic Objective

Remove unauthorized persistence mechanisms.

## Attack Path Removed

```text
Execution
     ↓
LaunchAgent / Login Item
     ↓
Persistence
```

## Architectural Deletion Goal

Eliminate unauthorized persistence pathways.

## Implementation Examples

- Restrict LaunchAgents.
- Restrict LaunchDaemons.
- Review Login Items.
- Remove unauthorized startup entries.
- Eliminate unnecessary persistence mechanisms.

---

# M06: Platform Trust Enforcement

## Description

Platform trust controls prevent the execution of unverified software and unauthorized code.

## Strategic Objective

Enforce operating-system integrity mechanisms.

## Attack Path Removed

```text
Unsigned Software
        ↓
Integrity Bypass
        ↓
Execution
```

## Architectural Deletion Goal

Prevent bypass of platform trust mechanisms.

## Implementation Examples

- Enforce Gatekeeper.
- Enforce notarization.
- Protect quarantine attributes.
- Enforce System Integrity Protection.
- Restrict trust bypass mechanisms.

---

# M07: TCC, Entitlement & Container Boundary Erasure

## Description

Excessive permissions and container boundary violations provide access to sensitive user data and system functionality.

## Strategic Objective

Reduce unnecessary permission and entitlement exposure.

## Attack Path Removed

```text
Application
      ↓
Excessive Entitlement
      ↓
Protected Data
```

## Architectural Deletion Goal

Remove unnecessary TCC permissions, entitlements, and container escape opportunities.

## Implementation Examples

- Reduce Full Disk Access grants.
- Reduce Accessibility permissions.
- Remove unnecessary entitlements.
- Restrict app container access.
- Review TCC permissions.

---

# M08: Service & Feature Surface Reduction

## Description

Unused operating system features increase attack surface while providing little operational value.

## Strategic Objective

Remove unnecessary operating-system functionality.

## Attack Path Removed

```text
Unused Feature
      ↓
Vulnerability
      ↓
Compromise
```

## Architectural Deletion Goal

Reduce exploitable surface area through feature removal.

## Implementation Examples

- Disable unnecessary SSH access.
- Remove unused file-sharing services.
- Restrict AirDrop where unnecessary.
- Disable unused remote management services.
- Reduce unnecessary Bluetooth sharing services.

---

# M09: Egress Determinism

## Description

Unrestricted outbound communications provide command-and-control and data-exfiltration pathways.

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

Restrict outbound communications to approved destinations.

## Implementation Examples

- Application-specific network controls.
- Explicit outbound allowlists.
- DNS governance.
- Proxy-controlled egress.
- Network-zone enforcement.

---

# M10: Device Management & Enrollment Trust Reduction

## Description

Device management systems create powerful trust relationships that directly influence device security posture.

## Strategic Objective

Reduce unnecessary management-plane trust.

## Attack Path Removed

```text
Management Plane
        ↓
Device Trust
        ↓
Device Control
```

## Architectural Deletion Goal

Reduce unnecessary enrollment and management trust pathways.

## Implementation Examples

- Remove dormant MDM profiles.
- Restrict enrollment profiles.
- Reduce administrative agent privileges.
- Review vendor management tooling.
- Minimize management-plane attack surface.

---

# Verification & PER Measurement

## Step 1 – Establish Baseline

Identify all eligible attack paths.

```math
|P_{eligible}(t_0)|
```

## Step 2 – Implement Controls

Apply M01 through M10.

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

*OWASP macOS Subtractive Hardening Top 10 v1.0*
