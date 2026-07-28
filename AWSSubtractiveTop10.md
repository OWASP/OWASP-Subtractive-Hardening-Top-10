# OWASP AWS Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Amazon Web Services (AWS)  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP AWS Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing cloud attack surface through the elimination of attacker-accessible attack paths.

Unlike traditional cloud security frameworks that emphasize visibility, compliance, and monitoring, Subtractive Hardening prioritizes the removal of architectural conditions that allow cloud compromise, privilege escalation, cross-account movement, persistence, and data exposure.

Rather than focusing on reactive detection, the goal is to alter the topology of the cloud attack graph by removing executable edges.

System Graph:

```text
G = (V, E)

Where:
V = Cloud Resources
E = Reachability, Trust, or Execution Relationships
```

Each recommendation is selected based on its ability to reduce adversary reachability and improve measurable attack-path reduction through the Path Erasure Rate (PER) Engineering Standard.

Path Erasure Rate:

```text
PER = P_erased / P_eligible
```

Where:

```text
P_eligible = Eligible attack paths identified within scope
P_erased   = Attack paths rendered non-traversable through architectural deletion
```

The objective is not to better observe attacks.

The objective is to make attacks impossible by removing the pathways that enable them.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The AWS Subtractive Hardening Top 10 provides practical cloud engineering guidance for achieving measurable PER improvements.

Together they establish a repeatable security engineering cycle:

1. Identify attack paths
2. Measure attack-path exposure
3. Eliminate attack paths where possible
4. Constrain residual attack paths where necessary
5. Measure resulting reduction
6. Continuously improve cloud architecture

---

# The Subtractive Hierarchy of Efficacy

All recommendations within this standard follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 – Architectural Deletion

Remove the attack path completely.

Examples:

- Remove trust relationships
- Remove public exposure
- Remove standing credentials
- Remove unnecessary network connectivity
- Remove unnecessary cloud services

## Tier 2 – Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- SCPs
- Permission boundaries
- Security groups
- Private endpoints
- Conditional access controls

## Tier 3 – Monitoring & Detection

Monitoring is reserved for attack paths that cannot be removed or constrained.

Examples:

- GuardDuty
- Security Hub
- CloudTrail
- SIEM integrations
- EDR

```text
Architectural Deletion
        >
Architectural Constraint
        >
Monitoring
```

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate executable attack-path edges
- Reduce credential theft opportunities
- Reduce privilege escalation opportunities
- Reduce lateral movement pathways
- Reduce persistence opportunities
- Improve measurable Path Erasure Rate (PER)

Recommendations are not ranked based on:

- Compliance requirements
- Alert volume
- Vulnerability counts
- Service popularity
- Detection effectiveness

The primary selection criterion is attack-path reduction.

---

# OWASP AWS Subtractive Hardening Top 10

| ID | Title |
|------|------|
| S01 | Metadata Credential Path Erasure |
| S02 | Wildcard Trust Elimination |
| S03 | Public Control Plane Removal |
| S04 | Default VPC Decommissioning |
| S05 | Cross-Account Trust Reduction |
| S06 | Egress Determinism |
| S07 | Identity Lifecycle Erasure |
| S08 | Public Data Plane Elimination |
| S09 | Regional Surface Reduction |
| S10 | Cloud Network Segmentation |

---

# S01: Metadata Credential Path Erasure

## Description

Instance Metadata Service Version 1 (IMDSv1) enables credential theft through SSRF and related attack chains.

## Strategic Objective

Eliminate direct metadata credential extraction paths.

## Attack Path Removed

```text
SSRF
   ↓
IMDSv1
   ↓
IAM Credentials
```

## Architectural Deletion Goal

Eliminate IMDSv1 and unnecessary metadata access.

## Implementation Examples

- Require IMDSv2.
- Enforce HttpTokens=required.
- Remove metadata access where operationally unnecessary.
- Enforce through SCPs.

---

# S02: Wildcard Trust Elimination

## Description

Wildcard principals and unrestricted resource policies create unauthorized trust relationships.

## Strategic Objective

Eliminate implicit trust.

## Attack Path Removed

```text
Principal *
      ↓
Resource Access
      ↓
Cross-Tenant Exposure
```

## Implementation Examples

- Remove Principal:"*"
- Remove Action:"*"
- Enforce aws:PrincipalOrgID
- Require explicit ARN scoping

---

# S03: Public Control Plane Removal

## Description

Public administrative interfaces create direct attack paths from the Internet.

## Strategic Objective

Remove Internet reachability.

## Attack Path Removed

```text
Internet
      ↓
Administrative Endpoint
      ↓
Control Plane Access
```

## Implementation Examples

- Disable public EKS endpoints.
- Eliminate public management interfaces.
- Use PrivateLink.
- Use Transit Gateway-based administration.

---

# S04: Default VPC Decommissioning

## Description

Default VPCs and default security groups provide unnecessary reachability.

## Strategic Objective

Remove inherited trust relationships.

## Attack Path Removed

```text
Default VPC
      ↓
Default Trust
      ↓
Lateral Movement
```

## Implementation Examples

- Remove default VPCs.
- Remove permissive default security groups.
- Deploy deny-by-default templates.

---

# S05: Cross-Account Trust Reduction

## Description

Broad AssumeRole trust relationships enable cloud lateral movement.

## Strategic Objective

Reduce cross-account mobility.

## Attack Path Removed

```text
Compromised Account
          ↓
AssumeRole
          ↓
Production Account
```

## Implementation Examples

- Restrict AssumeRole.
- Require ExternalId.
- Restrict trust by PrincipalArn.
- Reduce account-to-account trust.

---

# S06: Egress Determinism

## Description

Unrestricted outbound communications provide attacker command-and-control channels.

## Strategic Objective

Remove arbitrary egress.

## Attack Path Removed

```text
Compromised Workload
           ↓
Internet
           ↓
Command & Control
```

## Implementation Examples

- DNS firewalls.
- Egress proxies.
- VPC endpoints.
- Explicit outbound allow lists.

---

# S07: Identity Lifecycle Erasure

## Description

Dormant users, stale keys, and unused roles create long-lived attacker persistence opportunities.

## Strategic Objective

Remove unused identities.

## Attack Path Removed

```text
Unused Identity
        ↓
Credential Compromise
        ↓
Persistence
```

## Implementation Examples

- Remove unused IAM users.
- Remove inactive access keys.
- Remove dormant roles.
- Prohibit root access keys.

---

# S08: Public Data Plane Elimination

## Description

Internet-accessible storage and data services create direct exposure paths.

## Strategic Objective

Remove public data access.

## Attack Path Removed

```text
Internet
     ↓
S3 / Database
     ↓
Data Exposure
```

## Implementation Examples

- Global S3 Block Public Access.
- Deny PubliclyAccessible databases.
- Private-only storage architectures.

---

# S09: Regional Surface Reduction

## Description

Unused AWS regions increase attack surface and persistence opportunities.

## Strategic Objective

Remove unnecessary cloud geography.

## Attack Path Removed

```text
Compromised Account
          ↓
Unused Region
          ↓
Hidden Persistence
```

## Implementation Examples

- Restrict approved regions.
- SCP deny outside authorized regions.
- Restrict unnecessary services.

---

# S10: Cloud Network Segmentation

## Description

Flat VPC topology enables unrestricted cloud lateral movement.

## Strategic Objective

Reduce network reachability.

## Attack Path Removed

```text
Compromised VPC
         ↓
Flat Routing
         ↓
Additional VPCs
```

## Implementation Examples

- Remove unnecessary peering.
- Restrict Transit Gateway routes.
- Implement route segmentation.
- Limit east-west trust boundaries.

---

# Verification & PER Measurement

## Step 1 – Establish Baseline

```text
P_eligible(t0)
```

Identify all eligible cloud attack paths.

## Step 2 – Implement Controls

Apply S01 through S10.

## Step 3 – Validate Erasure

```text
P_erased(t1)
```

Identify paths rendered structurally non-traversable.

## Step 4 – Calculate PER

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Success Criteria

The objective is not increased monitoring visibility.

The objective is measurable reduction in cloud attack-path availability.

---

# Strategic Objective: Non-Conductivity

The goal of these subtractions is to establish deterministic trust boundaries within cloud environments.

By collapsing attack paths, AWS environments become architecturally non-conductive.

In this model:

```text
Vulnerability = Spark
Attack Path   = Oxygen
Architecture  = Conductivity
```

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

*OWASP AWS Subtractive Hardening Top 10 v1.0*
