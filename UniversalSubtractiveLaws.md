# OWASP Universal Subtractive Security Laws Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Universal / Platform-Agnostic Security Architecture  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Universal Subtractive Security Laws Top 10 defines a platform-agnostic architectural model for reducing cyber risk through the elimination of attacker-accessible execution, trust, reachability, credential, privilege, control-plane, and data-flow paths.

Unlike traditional security frameworks that focus primarily on vulnerabilities, signatures, alerts, tooling, or compliance control inventories, Subtractive Security prioritizes the removal of architectural conditions that allow local weaknesses to compose into credential theft, privilege escalation, lateral movement, persistence, exfiltration, operational disruption, or material business impact.

This universal standard is not tied to a single platform, technology stack, operating system, cloud provider, identity system, network architecture, SaaS tenant, or embedded-device environment. Instead, it defines recurring attack-path reduction laws that apply across abstraction layers.

Rather than relying on reactive detection, alert tuning, or continuous monitoring as the primary security mechanism, the objective is to physically remove conductive edges from the system graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Assets, Identities, Processes, Services, Devices, Workloads, Networks, Applications, Data Stores
E = Execution, Trust, Reachability, Authentication, Authorization, Privilege, Control, or Data-Flow Relationships
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

# Relationship to Platform-Specific Subtractive Hardening Standards

This universal standard defines platform-agnostic subtractive security laws that can be instantiated within specific technology environments.

Platform-specific standards such as Windows, Linux, macOS, Active Directory, AWS, Microsoft 365, Network, IoT, Kubernetes, CI/CD, Azure, GCP, and AI infrastructure should be understood as implementation guides for these universal laws.

The platform-specific details differ because each environment exposes different implementations of execution, trust, privilege, reachability, credential, control-plane, and data-flow paths.

The underlying architectural laws remain consistent.

Examples:

- Adjacent reachability may appear as workstation-to-workstation SMB on Windows, SSH trust on Linux, inter-VLAN routing in networks, or peer-device discovery in IoT.
- Static credentials may appear as local administrator passwords, IAM access keys, OAuth refresh tokens, default IoT passwords, or embedded API secrets.
- Control-plane exposure may appear as router management interfaces, cloud administrative APIs, SaaS admin roles, device web consoles, or Kubernetes API servers.
- Egress paths may appear as endpoint internet access, DNS tunneling, mail forwarding, cloud NAT, vendor telemetry relays, or arbitrary socket creation.

This standard provides the law-level abstraction. Platform standards provide implementation-level guidance.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The Universal Subtractive Security Laws Top 10 provides platform-agnostic engineering guidance for identifying the classes of attack paths whose removal most consistently reduces attacker optionality across system graphs.

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
- Credential removal
- Protocol removal
- Reachability removal
- Service removal
- Privilege removal
- Execution pathway removal

## Tier 2 – Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Segmentation
- Conditional access
- Permission boundaries
- Authenticated mediation
- Allowlisting
- Platform integrity enforcement
- JIT or least-privilege access

## Tier 3 – Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- EDR
- SIEM
- IDS/IPS
- Audit logging
- Behavioral detection
- Alerting

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever an attack path can be eliminated, elimination is preferred. If elimination is not feasible, the path should be constrained. Monitoring is reserved for residual paths that cannot be removed or sufficiently constrained.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their recurring presence across multiple platform-specific standards and their ability to:

- Eliminate executable attack-path edges.
- Reduce unnecessary reachability.
- Reduce credential theft opportunities.
- Reduce privilege escalation opportunities.
- Reduce lateral movement pathways.
- Reduce transitive trust and delegation pathways.
- Reduce exfiltration and command-and-control pathways.
- Reduce attack-path composability.
- Improve measurable Path Erasure Rate (PER).

Recommendations are not ranked based on:

- CVSS scores
- Vulnerability prevalence
- Compliance requirements
- Detection coverage
- Vendor capability claims
- Platform popularity

The primary selection criterion is architectural impact through attack-path reduction.

---

# OWASP Universal Subtractive Security Laws Top 10

| ID | Title |
|------|------|
| U01 | Adjacent Reachability & Lateral Conductive Edge Erasure |
| U02 | Static & Persistent Credential Elimination |
| U03 | Cleartext & Unauthenticated Control Plane Extinction |
| U04 | Unconstrained Egress & Exfiltration Path Erasure |
| U05 | Management & Diagnostic Interface Surface Reduction |
| U06 | Cross-Domain & Heterogeneous Trust Severing |
| U07 | Execution Scope & Privilege Surface Pruning |
| U08 | Implicit Trust & Transitive Delegation Elimination |
| U09 | Integrity & Boot-Chain Verification Enforcement |
| U10 | Dynamic Protocol & Automatic Discovery Surface Deletion |

---

# U01: Adjacent Reachability & Lateral Conductive Edge Erasure

## Description

Default peer-to-peer communication, broadcast domains, same-subnet reachability, cross-workload access, and unmediated adjacency create conductive paths that allow compromise to propagate across systems.

## Strategic Objective

Eliminate unnecessary adjacent reachability and lateral movement paths.

## Attack Path Removed

```text
Compromised Node
        ↓
Adjacent Reachability
        ↓
Additional Node
```

## Architectural Deletion Goal

Remove unnecessary peer-to-peer, broadcast, workload-to-workload, and lateral communication pathways.

## Implementation Examples

- Remove default peer-to-peer communication paths.
- Eliminate unnecessary host-to-host reachability.
- Collapse unnecessary broadcast domains.
- Restrict cross-workload movement.
- Remove lateral administrative transit paths.
- Enforce explicit communication boundaries.

---

# U02: Static & Persistent Credential Elimination

## Description

Long-lived credentials, hardcoded secrets, default passwords, persistent service tokens, static API keys, and reusable shared secrets create durable attack paths that survive compromise, replay, and theft.

## Strategic Objective

Eliminate static and persistent authentication material wherever possible.

## Attack Path Removed

```text
Attacker
      ↓
Static / Persistent Credential
      ↓
System Access
```

## Architectural Deletion Goal

Remove reusable credentials that provide durable, transferable, or replayable access.

## Implementation Examples

- Remove hardcoded secrets.
- Eliminate default passwords.
- Remove long-lived API keys.
- Replace static service tokens with short-lived credentials.
- Remove unused credential material.
- Prefer hardware-backed or ephemeral authentication where feasible.

---

# U03: Cleartext & Unauthenticated Control Plane Extinction

## Description

Cleartext listeners, unauthenticated APIs, legacy management protocols, weak RPC paths, and unauthenticated control-plane interfaces create direct paths to interception, replay, unauthorized control, and privilege escalation.

## Strategic Objective

Eliminate cleartext and unauthenticated control-plane access.

## Attack Path Removed

```text
Attacker
      ↓
Cleartext / Unauthenticated Control Path
      ↓
System Control
```

## Architectural Deletion Goal

Remove unauthenticated or weakly authenticated control-plane pathways.

## Implementation Examples

- Remove cleartext management protocols.
- Disable unauthenticated APIs.
- Remove legacy RPC paths.
- Require authenticated control-plane access.
- Remove weak administrative listeners.
- Replace unauthenticated protocols with verified, authenticated mechanisms.

---

# U04: Unconstrained Egress & Exfiltration Path Erasure

## Description

Implicit outbound routing, arbitrary DNS access, unrestricted socket creation, broad telemetry relays, and unconstrained internet egress allow compromised systems to establish command-and-control, exfiltrate data, or communicate with attacker-controlled infrastructure.

## Strategic Objective

Eliminate arbitrary outbound communication and exfiltration pathways.

## Attack Path Removed

```text
Compromised Asset
        ↓
Unconstrained Egress
        ↓
External Attacker-Controlled Destination
```

## Architectural Deletion Goal

Restrict outbound communication to deterministic, approved, and necessary destinations.

## Implementation Examples

- Remove implicit 0.0.0.0/0 outbound routing where feasible.
- Restrict arbitrary DNS and socket creation.
- Eliminate unauthorized telemetry relays.
- Enforce explicit egress allowlists.
- Route outbound traffic through controlled mediation points.
- Remove unnecessary external communication paths.

---

# U05: Management & Diagnostic Interface Surface Reduction

## Description

Administrative consoles, diagnostic endpoints, debug ports, maintenance interfaces, management APIs, and support backdoors provide direct pathways to system control.

## Strategic Objective

Reduce exposed management and diagnostic surfaces.

## Attack Path Removed

```text
Attacker
      ↓
Management / Diagnostic Interface
      ↓
Administrative Control
```

## Architectural Deletion Goal

Remove or isolate administrative, diagnostic, and maintenance interfaces from production attack paths.

## Implementation Examples

- Disable unnecessary administrative consoles.
- Remove exposed debug interfaces.
- Isolate maintenance endpoints.
- Restrict management APIs.
- Remove unused diagnostic services.
- Physically isolate management planes where feasible.

---

# U06: Cross-Domain & Heterogeneous Trust Severing

## Description

Direct trust relationships and unmediated routing between environments with different risk profiles allow compromise to propagate across architectural boundaries.

## Strategic Objective

Eliminate direct trust and routing paths between heterogeneous domains.

## Attack Path Removed

```text
Lower-Trust Domain
          ↓
Direct Trust / Routing Path
          ↓
Higher-Impact Domain
```

## Architectural Deletion Goal

Sever unmediated paths between environments with differing trust, sensitivity, ownership, or operational risk.

## Implementation Examples

- Remove direct IT-to-OT routing.
- Separate production and development trust boundaries.
- Restrict guest-to-corporate reachability.
- Remove unnecessary cloud-to-on-premises trust.
- Mediate cross-domain access through controlled gateways.
- Eliminate direct trust between incompatible risk zones.

---

# U07: Execution Scope & Privilege Surface Pruning

## Description

Unnecessary runtimes, interpreters, binaries, administrative rights, peripheral access, service roles, and execution pathways increase the number of ways attackers can convert access into control.

## Strategic Objective

Reduce the amount of executable and privileged functionality available to attackers.

## Attack Path Removed

```text
Compromised Context
          ↓
Unnecessary Execution / Privilege Surface
          ↓
Privilege Expansion or Code Execution
```

## Architectural Deletion Goal

Remove unnecessary software, execution scopes, administrative rights, peripheral privileges, and over-privileged service roles.

## Implementation Examples

- Remove unnecessary runtimes and interpreters.
- Remove unused binaries and services.
- Minimize administrative rights.
- Remove unnecessary peripheral access.
- Reduce over-privileged service accounts.
- Remove shell or scripting pathways where unnecessary.

---

# U08: Implicit Trust & Transitive Delegation Elimination

## Description

Automatic trust inheritance, wildcard permissions, broad delegation, unconstrained impersonation, and cross-tenant or cross-domain trust create hidden paths through which compromise can propagate beyond the initially affected system.

## Strategic Objective

Eliminate implicit or transitive trust pathways.

## Attack Path Removed

```text
Compromised Principal
          ↓
Implicit Trust / Delegation
          ↓
Additional Privilege or Data Access
```

## Architectural Deletion Goal

Remove trust relationships that allow privilege, identity, or access to propagate automatically.

## Implementation Examples

- Remove wildcard permissions.
- Remove unconstrained delegation.
- Remove broad service impersonation.
- Reduce cross-tenant trust.
- Remove automatic trust inheritance.
- Enforce explicit trust boundaries.

---

# U09: Integrity & Boot-Chain Verification Enforcement

## Description

Unsigned, unverified, or unauthenticated code, firmware, payloads, containers, images, packages, or updates create paths for attackers to introduce executable content below, within, or adjacent to trusted runtime environments.

## Strategic Objective

Eliminate execution of unverified or unauthenticated code and updates.

## Attack Path Removed

```text
Unverified Code / Update
          ↓
Trusted Execution Context
          ↓
Persistent or Privileged Compromise
```

## Architectural Deletion Goal

Prevent unverified execution at the firmware, boot-chain, operating-system, package, container, application, or update layer.

## Implementation Examples

- Enforce secure boot.
- Require signed firmware.
- Require signed packages or images.
- Remove unsigned update pathways.
- Enforce application or workload integrity.
- Remove unauthenticated code-loading paths.

---

# U10: Dynamic Protocol & Automatic Discovery Surface Deletion

## Description

Dynamic negotiation, automatic discovery, broadcast advertisement, convenience protocols, and unauthenticated peer discovery create unintended trust, topology exposure, lateral movement, and spoofing opportunities.

## Strategic Objective

Eliminate unnecessary dynamic discovery and auto-negotiation pathways.

## Attack Path Removed

```text
Asset
  ↓
Dynamic Discovery / Auto-Negotiation
  ↓
Unintended Trust or Reachability
```

## Architectural Deletion Goal

Remove dynamic, automatic, or unauthenticated discovery mechanisms that create unnecessary trust or reachability.

## Implementation Examples

- Disable unnecessary broadcast discovery.
- Disable auto-negotiation where unsafe.
- Remove unauthenticated peer advertisement.
- Remove convenience protocols where unnecessary.
- Reduce topology disclosure.
- Remove automatic trust establishment mechanisms.

---

# Verification & PER Measurement

## Step 1 – Establish Baseline

Identify all eligible attack paths within the declared scope.

```text
P_eligible(t0)
```

## Step 2 – Apply Universal Subtractive Laws

Apply U01 through U10 directly or through relevant platform-specific implementation standards.

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

# Stack Composition & Parallel Adoption

The Universal Subtractive Security Laws are intended to be composed with platform-specific standards.

Modern enterprise systems are composed of multiple interacting layers. A single business service may include endpoints, servers, cloud workloads, SaaS applications, identity systems, network paths, embedded devices, and third-party integrations.

Attack paths do not respect architectural boundaries.

A compromised endpoint may leverage identity paths. A compromised identity may leverage SaaS or cloud paths. A compromised workload may leverage network or egress paths. A compromised IoT device may leverage enterprise reachability paths.

For this reason, organizations should apply subtractive controls concurrently across all relevant layers.

Examples:

- Windows + Active Directory + Network
- Linux + AWS + Network
- Microsoft 365 + Identity + Endpoint
- IoT + Network + Vendor Trust
- CI/CD + Cloud + Identity

The objective is not to harden individual components in isolation.

The objective is to reduce total attack-path conductivity across the system as a whole.

---

# Defense in Depth Through Layered Path Erasure

Subtractive Security recognizes that all controls, including subtractive controls, may fail due to misconfiguration, implementation error, operational drift, software defects, incomplete deployment, or changing business requirements.

For this reason, organizations should seek to eliminate or constrain critical attack paths across multiple independent architectural layers.

This approach provides defense in depth through layered path erasure. If a control fails at one layer, independently implemented attack-path reductions at other layers continue to prevent adversary progression.

Traditional defense in depth often layers monitoring around a path that remains open.

Subtractive defense in depth independently removes or constrains the same path at multiple locations in the architecture.

The objective is not perfect controls.

The objective is resilient non-conductivity.

---

# Strategic Objective: Non-Conductivity

The goal of these subtractions is to establish deterministic boundaries across the enterprise system graph.

By collapsing attack paths, the environment becomes architecturally non-conductive.

In this model:

```text
Vulnerability = Spark
Attack Path = Oxygen
System Architecture = Conductivity
```

Remove the path, and the spark goes nowhere.

---

# Guiding Principle

Attackers can only traverse paths that exist.

The objective of Subtractive Security is to systematically eliminate or constrain those paths until adversary activity can no longer compose into material business impact.

**Security effectiveness is maximized when attack paths are removed, not merely observed.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Evidence-Based Security ([Evidence-Based Security Article](https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and))
- The Law of Subtractive Risk ([The Law of Subtractive Risk](https://subtractivesecurity.substack.com/p/the-law-of-subtractive-risk-moving))
- The Science of Silence

---

*OWASP Universal Subtractive Security Laws Top 10 v1.0*
