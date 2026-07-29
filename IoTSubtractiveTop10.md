# OWASP IoT Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Internet of Things (IoT), Embedded Devices, and Connected Systems  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP IoT Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing cyber risk through the elimination of attacker-accessible reachability, credential, protocol, firmware, management, and device-trust paths within IoT, embedded, and connected-device environments.

Unlike traditional IoT security guidance that focuses primarily on vulnerability remediation, device monitoring, asset inventory, or compensating controls, Subtractive Hardening prioritizes the removal of architectural conditions that allow constrained or unmanaged devices to compose into enterprise compromise, lateral movement, persistence, operational disruption, or data exposure.

Rather than relying on reactive detection, alert tuning, or continuous triage, the objective is to physically remove conductive edges from the IoT device graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Devices, Sensors, Gateways, Controllers, Firmware, Services, Management Planes, Cloud Relays
E = Reachability, Trust, Authentication, Protocol, Firmware, Control, or Data-Flow Relationships
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

The IoT Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within IoT, embedded-device, and connected-system environments.

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

- Device reachability removal
- Default credential removal
- Cleartext protocol removal
- Vendor cloud relay removal
- Physical debug path removal

## Tier 2 – Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Network segmentation
- Allowlisted egress
- Firmware signing
- Secure boot enforcement
- Controlled management access

## Tier 3 – Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- Network detection
- Device telemetry
- SIEM
- IDS/IPS
- Alerting

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever an attack path can be eliminated, elimination is preferred.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate device attack-path edges.
- Reduce credential compromise opportunities.
- Reduce unauthorized device control pathways.
- Reduce lateral movement pathways.
- Reduce firmware and boot compromise opportunities.
- Reduce unmanaged device-to-enterprise composability.
- Improve measurable Path Erasure Rate (PER).

Recommendations are not ranked based on:

- CVSS scores
- Vulnerability prevalence
- Compliance requirements
- Detection coverage
- Vendor capability claims

The primary selection criterion is architectural impact through attack-path reduction.

---

# OWASP IoT Subtractive Hardening Top 10

| ID | Title |
|------|------|
| I01 | Device Reachability & Local Discovery Erasure |
| I02 | Default Credential & Static Authentication Elimination |
| I03 | Cleartext & Unauthenticated Protocol Extinction |
| I04 | Cloud & Vendor Control Plane Trust Reduction |
| I05 | Management Interface & Control Plane Reduction |
| I06 | IT / OT / Corporate Segment Isolation |
| I07 | Firmware Integrity & Boot Trust Enforcement |
| I08 | Egress Determinism & Local Socket Restriction |
| I09 | Service Surface & Daemon Pruning |
| I10 | Administrative & Peripheral Trust Reduction |

---

# I01: Device Reachability & Local Discovery Erasure

## Description

Unconstrained local device reachability and discovery protocols create unnecessary paths for device enumeration, peer-to-peer interaction, lateral movement, and unauthorized control.

## Strategic Objective

Eliminate unnecessary local discovery and device-to-device reachability.

## Attack Path Removed

```text
Compromised Device / Host
          ↓
Local Discovery / Peer Reachability
          ↓
Additional IoT Devices
```

## Architectural Deletion Goal

Remove unnecessary local discovery and peer-to-peer device communication pathways.

## Implementation Examples

- Disable UPnP where unnecessary.
- Disable mDNS / Bonjour where unnecessary.
- Restrict peer-to-peer IoT communication.
- Isolate device broadcast domains.
- Remove unnecessary local discovery paths.
- Restrict device-to-device reachability.

---

# I02: Default Credential & Static Authentication Elimination

## Description

Default credentials, hardcoded passwords, static API keys, factory fallback accounts, and shared secrets create direct pathways to device compromise.

## Strategic Objective

Eliminate static and reusable authentication paths.

## Attack Path Removed

```text
Attacker
      ↓
Default / Static Credential
      ↓
Device Access
```

## Architectural Deletion Goal

Remove default, shared, hardcoded, or static authentication mechanisms.

## Implementation Examples

- Remove factory default credentials.
- Disable fallback backdoor accounts.
- Remove static API keys.
- Enforce unique device credentials.
- Remove shared administrative passwords.
- Rotate or eliminate embedded secrets.

---

# I03: Cleartext & Unauthenticated Protocol Extinction

## Description

Cleartext and unauthenticated protocols expose IoT devices to interception, replay, credential theft, and unauthorized control.

## Strategic Objective

Eliminate insecure protocol paths.

## Attack Path Removed

```text
Attacker
      ↓
Cleartext / Unauthenticated Protocol
      ↓
Device Control
```

## Architectural Deletion Goal

Remove cleartext and unauthenticated communication protocols wherever possible.

## Implementation Examples

- Disable Telnet.
- Disable HTTP management where unnecessary.
- Remove unauthenticated MQTT.
- Require DTLS or equivalent protection for CoAP where feasible.
- Remove cleartext serial-over-IP bridges.
- Replace unauthenticated protocols with authenticated alternatives.

---

# I04: Cloud & Vendor Trust Constraint

## Description

Vendor cloud platforms, telemetry relays, SaaS management services, and third-party support ecosystems frequently create persistent trust relationships that extend beyond enterprise-controlled boundaries.

For many commercial IoT deployments—including medical devices, smart-building infrastructure, HVAC systems, industrial controllers, and logistics platforms—vendor cloud connectivity is often operationally required and cannot be fully eliminated without impacting functionality, supportability, or contractual obligations.

## Strategic Objective

Minimize and constrain external vendor and cloud control pathways while preserving required operational functionality.

## Attack Path Removed

```text
Vendor Cloud
       ↓
Unconstrained Device Trust
       ↓
Device Fleet
```

## Architectural Constraint Goal

Reduce external control-plane exposure through gateway isolation, deterministic routing, bounded trust relationships, and explicit vendor allowlisting.

## Implementation Examples

### Enterprise Deployment

- Route device communications through enterprise-controlled gateways.
- Restrict vendor communications to approved FQDNs and destinations.
- Remove unnecessary third-party relay services.
- Minimize device-to-cloud trust relationships.
- Aggregate telemetry through enterprise-managed collection points.
- Restrict device access to approved vendor control planes.

### Greenfield / OEM Development

- Remove unnecessary third-party cloud brokers.
- Route telemetry directly to enterprise-controlled cloud services.
- Use hardware-backed device authentication.
- Implement mutual TLS (mTLS).
- Reduce external trust dependencies during product design.

---

# I05: Management Interface & Debug Surface Reduction

## Description

Administrative interfaces, diagnostic services, exposed APIs, and hardware-debug capabilities provide direct pathways to device control.

While software management interfaces are commonly removable by enterprise operators, physical debugging interfaces such as UART, JTAG, and SWD are often determined during device manufacturing and may not be removable after deployment.

## Strategic Objective

Reduce exposure to administrative and diagnostic interfaces that enable direct device compromise.

## Attack Path Removed

```text
Attacker
      ↓
Management / Debug Interface
      ↓
Device Control
```

## Architectural Deletion Goal

Remove unnecessary software management interfaces and constrain physical debug pathways wherever deletion is not operationally feasible.

## Implementation Examples

### Enterprise Deployment

- Disable local web administration interfaces where unnecessary.
- Disable exposed administrative APIs.
- Restrict management interfaces to approved networks.
- Block management ports through ACLs and segmentation.
- Remove unnecessary maintenance services.
- Restrict administrative access to approved management systems.

### OEM / Device Manufacturer

- Disable UART interfaces during production.
- Disable JTAG interfaces during production.
- Burn hardware debug-disable eFuses.
- Remove manufacturing interfaces prior to shipment.
- Restrict board-level diagnostic functionality.
- Reduce physical attack surface during product design.

---

# I06: IT / OT / Corporate Segment Isolation

## Description

Direct routed pathways between IoT devices, enterprise IT networks, OT/ICS environments, guest networks, and core data stores create high-impact compromise propagation paths.

## Strategic Objective

Sever unnecessary routing between dissimilar trust zones.

## Attack Path Removed

```text
IoT Device Segment
        ↓
Direct Routing
        ↓
Enterprise / OT / Core Data Environment
```

## Architectural Deletion Goal

Eliminate unnecessary routed pathways between IoT, IT, OT, guest, and corporate environments.

## Implementation Examples

- Isolate IoT device subnets.
- Sever direct IoT-to-enterprise routing.
- Sever direct IoT-to-OT routing.
- Restrict IoT-to-datacenter paths.
- Enforce mediated access where connectivity is required.
- Segment guest, IoT, OT, and enterprise networks separately.

---

# I07: Firmware Integrity & Boot Trust Enforcement

## Description

Unsigned firmware, weak boot chains, and unverified update mechanisms allow attackers to persist below the operating system or application layer.

## Strategic Objective

Prevent unauthorized firmware and boot-chain modification.

## Attack Path Removed

```text
Unauthorized Firmware
          ↓
Device Boot Chain
          ↓
Persistent Device Compromise
```

## Architectural Deletion Goal

Remove unverified firmware execution and insecure update pathways.

## Implementation Examples

- Enforce hardware Secure Boot where supported.
- Block unsigned firmware updates.
- Remove unverified OTA update mechanisms.
- Require signed firmware packages.
- Restrict firmware rollback paths.
- Validate update integrity before installation.

---

# I08: Egress Determinism & Local Socket Restriction

## Description

Unrestricted outbound communication enables command-and-control, vendor relay abuse, data exfiltration, and unauthorized telemetry paths.

## Strategic Objective

Eliminate arbitrary outbound connectivity.

## Attack Path Removed

```text
IoT Device
     ↓
Arbitrary Outbound Connection
     ↓
Command & Control / Exfiltration
```

## Architectural Deletion Goal

Restrict IoT device egress to explicitly approved destinations and protocols.

## Implementation Examples

- Restrict outbound connectivity to allowlisted IPs and ports.
- Enforce DNS sinkholing where appropriate.
- Block arbitrary internet access.
- Restrict device-originated sockets.
- Enforce deterministic egress paths.
- Remove unnecessary outbound telemetry channels.

---

# I09: Service Surface & Daemon Pruning

## Description

Embedded services and diagnostic tools increase attack surface while often providing little operational value after deployment.

## Strategic Objective

Remove unnecessary embedded services and diagnostic capabilities.

## Attack Path Removed

```text
Unnecessary Service
          ↓
Vulnerability
          ↓
Device Compromise
```

## Architectural Deletion Goal

Reduce device attack surface through service and daemon removal.

## Implementation Examples

- Remove unused embedded Linux services.
- Disable SSH where unnecessary.
- Disable FTP where unnecessary.
- Remove mDNSResponder where unnecessary.
- Remove unused open sockets.
- Remove unnecessary diagnostic tools.
- Minimize installed service footprint.

---

# I10: Administrative & Peripheral Trust Reduction

## Description

Physical interfaces, peripheral attachment paths, local privilege escalation paths, and over-privileged service accounts can provide attackers with direct paths to device control.

## Strategic Objective

Reduce administrative and peripheral trust exposure.

## Attack Path Removed

```text
Physical / Local Access
          ↓
Peripheral or Administrative Trust
          ↓
Device Control
```

## Architectural Deletion Goal

Remove unnecessary administrative, service-account, and peripheral trust pathways.

## Implementation Examples

- Restrict USB execution paths.
- Restrict serial interface access.
- Remove unnecessary peripheral trust.
- Reduce over-privileged device service accounts.
- Remove local privilege escalation paths where feasible.
- Restrict physical maintenance interfaces.

---

# Verification & PER Measurement

## Step 1 – Establish Baseline

Identify all eligible attack paths.

```text
P_eligible(t0)
```

## Step 2 – Implement Controls

Apply I01 through I10.

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

The goal of these subtractions is to establish deterministic boundaries around IoT, embedded, and connected-device environments.

By collapsing attack paths, IoT environments become architecturally non-conductive.

In this model:

```text
Device Vulnerability = Spark
Reachability / Trust Path = Oxygen
Device Architecture = Conductivity
```

Remove the path, and the spark goes nowhere.

---

# Guiding Principle

Attackers can only traverse paths that exist.

The objective of Subtractive Hardening is to systematically eliminate or constrain those paths until adversary activity can no longer compose into material business impact.

**Security effectiveness is maximized when attack paths are removed, not merely observed.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Evidence-Based Security ([Evidence-Based Security Article](https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and))
- The Law of Subtractive Risk ([The Law of Subtractive Risk](https://subtractivesecurity.substack.com/p/the-law-of-subtractive-risk-moving))
- The Science of Silence

---

*OWASP IoT Subtractive Hardening Top 10 v1.0*
