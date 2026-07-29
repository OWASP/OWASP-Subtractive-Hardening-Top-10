# OWASP Microsoft 365 Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Microsoft 365  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Microsoft 365 Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing cyber risk through the elimination of attacker-accessible trust, authentication, collaboration, privilege, and data-exfiltration paths within Microsoft 365 environments.

Unlike traditional SaaS security frameworks that focus primarily on monitoring, configuration assessment, alerting, or compliance, Subtractive Hardening prioritizes the removal of architectural conditions that allow adversaries to leverage identity compromise, OAuth abuse, mailflow manipulation, privilege escalation, and external trust relationships.

Rather than relying on reactive detection, alert triage, or incident response, the objective is to physically remove exploitable trust relationships and traversal paths from the Microsoft 365 tenant graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Identities, Applications, Mailboxes, Sites, Teams, Guests, Roles

E = Authentication, Authorization, Sharing,
    Trust, Privilege, or Data Relationships
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

The objective is to make tenant compromise, persistence, and data exfiltration significantly more difficult by removing the pathways that enable them.

---

# Relationship to Other Subtractive Hardening Standards

This standard focuses on Microsoft 365 tenant, identity, mailflow, collaboration, sharing, application trust, and SaaS attack paths.

Office application execution paths—including ActiveX, OLE, DDE, Office child-process execution, macro execution, and related endpoint attack paths—are intentionally addressed within the OWASP Windows Subtractive Hardening Top 10 under **Process Tree Integrity** and related execution-path controls.

These standards are designed for parallel adoption and should be implemented together where applicable.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The Microsoft 365 Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within Microsoft 365 environments.

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
- Guest account removal
- Application permission removal

## Tier 2 – Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Conditional Access
- Just-In-Time administration
- Session controls
- Sharing restrictions
- Application consent governance

## Tier 3 – Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- Unified Audit Logging
- Microsoft Defender
- SIEM
- Alerting
- Investigation workflows

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever an attack path can be eliminated, elimination is preferred.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate trust-based attack paths.
- Reduce identity compromise opportunities.
- Reduce privilege escalation opportunities.
- Reduce cross-tenant movement pathways.
- Reduce data exfiltration opportunities.
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

# OWASP Microsoft 365 Subtractive Hardening Top 10

| ID | Title |
|------|------|
| O01 | Enterprise Application & OAuth Trust Reduction |
| O02 | Legacy Authentication Extinction |
| O03 | Administrative Privilege Path Reduction |
| O04 | External Trust Path Reduction |
| O05 | Mailflow Exfiltration Path Elimination |
| O06 | Hybrid Identity Trust Reduction |
| O07 | Authentication Assurance Path Reduction |
| O08 | SharePoint & OneDrive Exposure Reduction |
| O09 | Tenant Service Surface Reduction |
| O10 | Collaboration Path Reduction |

---

# O01: Enterprise Application & OAuth Trust Reduction

## Description

Third-party applications and OAuth consents frequently create persistent tenant access pathways that bypass traditional authentication controls.

## Strategic Objective

Reduce unnecessary application trust relationships.

## Attack Path Removed

```text
User
   ↓
OAuth Consent
   ↓
Application
   ↓
Tenant Data
```

## Architectural Deletion Goal

Remove unnecessary application permissions and OAuth trust relationships.

## Implementation Examples

- Remove dormant enterprise applications.
- Remove unneeded OAuth consents.
- Eliminate unnecessary offline access permissions.
- Remove abandoned app registrations.
- Minimize application permissions.

---

# O02: Legacy Authentication Extinction

## Description

Legacy authentication protocols provide a common entry point for password-spray, credential-stuffing, and replay attacks.

## Strategic Objective

Eliminate legacy authentication dependencies.

## Attack Path Removed

```text
Attacker
      ↓
Legacy Protocol
      ↓
Credential Attack
      ↓
Account Access
```

## Architectural Deletion Goal

Remove legacy authentication pathways from the tenant.

## Implementation Examples

- Disable Basic Authentication.
- Disable POP3 where unnecessary.
- Disable IMAP where unnecessary.
- Eliminate legacy Exchange protocols.
- Remove legacy authentication exceptions.

---

# O03: Administrative Privilege Path Reduction

## Description

Permanent administrative assignments provide direct pathways to tenant-wide compromise.

## Strategic Objective

Reduce long-lived privilege.

## Attack Path Removed

```text
Compromised Identity
          ↓
Permanent Admin Role
          ↓
Tenant Control
```

## Architectural Deletion Goal

Remove standing administrative privilege.

## Implementation Examples

- Implement Just-In-Time administration.
- Remove dormant administrative roles.
- Eliminate unnecessary Global Administrators.
- Review custom Entra roles.
- Reduce Global Reader assignments.

---

# O04: External Trust Path Reduction

## Description

Guest access and federation relationships create pathways for external trust propagation.

## Strategic Objective

Reduce unnecessary external trust.

## Attack Path Removed

```text
External Identity
         ↓
Trust Relationship
         ↓
Tenant Resources
```

## Architectural Deletion Goal

Remove unnecessary external trust relationships.

## Implementation Examples

- Remove dormant guest accounts.
- Reduce broad B2B trust configurations.
- Review cross-tenant access settings.
- Restrict external directory visibility.
- Minimize federation trust.

---

# O05: Mailflow Exfiltration Path Elimination

## Description

Forwarding rules and transport rules are frequently abused as persistent data-exfiltration mechanisms.

## Strategic Objective

Eliminate unauthorized mailflow pathways.

## Attack Path Removed

```text
Mailbox
    ↓
Forwarding Rule
    ↓
External Destination
```

## Architectural Deletion Goal

Remove unnecessary mailflow-based exfiltration paths.

## Implementation Examples

- Disable automatic external forwarding.
- Review transport rules.
- Remove unauthorized inbox rules.
- Restrict external routing exceptions.
- Minimize mailflow trust relationships.

---

# O06: Hybrid Identity Trust Reduction

## Description

Synchronization and federation relationships can enable compromise propagation between cloud and on-premises identity environments.

## Strategic Objective

Reduce hybrid trust exposure.

## Attack Path Removed

```text
Cloud Identity
       ↓
Hybrid Trust
       ↓
On-Prem Identity
```

## Architectural Deletion Goal

Reduce unnecessary hybrid identity pathways.

## Implementation Examples

- Minimize synchronization scope.
- Remove unused federation relationships.
- Review writeback capabilities.
- Restrict privileged hybrid accounts.
- Reduce hybrid attack surface.

---

# O07: Authentication Assurance Path Reduction

## Description

Weak authentication assurance allows compromised credentials to remain operational.

## Strategic Objective

Eliminate low-assurance authentication paths.

## Attack Path Removed

```text
Attacker
      ↓
Credential
      ↓
Weak Authentication
      ↓
Tenant Access
```

## Architectural Deletion Goal

Remove low-assurance authentication pathways.

## Implementation Examples

- Deploy phishing-resistant MFA.
- Eliminate SMS-based MFA where feasible.
- Disable unnecessary authentication flows.
- Restrict legacy MFA methods.
- Increase authentication assurance requirements.

---

# O08: SharePoint & OneDrive Exposure Reduction

## Description

Excessive sharing permissions and anonymous access links create unnecessary data-exposure pathways.

## Strategic Objective

Reduce unauthorized data-access pathways.

## Attack Path Removed

```text
Shared Content
       ↓
Excessive Sharing
       ↓
External Access
```

## Architectural Deletion Goal

Reduce unnecessary sharing and exposure paths.

## Implementation Examples

- Remove anonymous sharing links.
- Restrict external sharing.
- Review sharing permissions.
- Minimize public content exposure.
- Reduce oversharing.

---

# O09: Tenant Service Surface Reduction

## Description

Unnecessary tenant services increase attack surface and administrative complexity.

## Strategic Objective

Reduce unnecessary tenant functionality.

## Attack Path Removed

```text
Unused Service
        ↓
Misconfiguration
        ↓
Compromise
```

## Architectural Deletion Goal

Reduce tenant attack surface through service reduction.

## Implementation Examples

- Disable unused services.
- Eliminate unnecessary workloads.
- Review service enablement.
- Remove obsolete integrations.
- Minimize exposed functionality.

---

# O10: Collaboration Path Reduction

## Description

Collaboration platforms can create unintended trust and data-sharing pathways between users, guests, and organizations.

## Strategic Objective

Reduce unnecessary collaboration trust.

## Attack Path Removed

```text
User
   ↓
Collaboration Platform
   ↓
External Access
```

## Architectural Deletion Goal

Remove unnecessary collaboration pathways.

## Implementation Examples

- Restrict Teams federation.
- Minimize external collaboration.
- Reduce guest collaboration scope.
- Review shared channels.
- Limit unnecessary tenant-to-tenant collaboration.

---

# Verification & PER Measurement

## Step 1 – Establish Baseline

Identify all eligible attack paths.

```text
P_eligible(t0)
```

## Step 2 – Implement Controls

Apply O01 through O10.

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

The goal of these subtractions is to establish deterministic trust boundaries within Microsoft 365.

By collapsing attack paths, the tenant becomes architecturally non-conductive.

In this model:

```text
Credential = Fuel
Trust Relationship = Oxygen
Tenant Architecture = Conductivity
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

*OWASP Microsoft 365 Subtractive Hardening Top 10 v1.0*
