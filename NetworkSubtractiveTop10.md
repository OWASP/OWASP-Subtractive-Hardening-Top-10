# OWASP Network Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Network Infrastructure  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Network Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing cyber risk through the elimination of attacker-accessible reachability, routing, broadcast, management, control-plane, and exfiltration paths within enterprise network environments.

Unlike traditional network security guidance that focuses primarily on monitoring, intrusion detection, alerting, or perimeter inspection, Subtractive Hardening prioritizes the removal of architectural conditions that allow attackers to compose isolated compromise into lateral movement, control-plane access, data exfiltration, and material business impact.

Rather than relying on reactive detection, alert tuning, or continuous triage, the objective is to physically remove conductive edges from the enterprise network graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Hosts, Subnets, VLANs, Routers, Switches, Firewalls, Wireless Networks, OT/IoT Segments
E = Reachability, Routing, Broadcast, Management, Trust, or Data-Flow Relationships
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

The Network Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within enterprise network environments.

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

- Broadcast-domain removal
- Routing path removal
- Management-interface removal
- Legacy protocol removal
- Physical or wireless access path removal

## Tier 2 – Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Segmentation
- Private VLANs
- Out-of-band management
- Deterministic DNS routing
- Access-control boundaries

## Tier 3 – Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- IDS/IPS
- NetFlow
- SIEM
- Packet capture
- Alerting

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever an attack path can be eliminated, elimination is preferred.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate network attack-path edges.
- Reduce lateral movement opportunities.
- Reduce control-plane compromise opportunities.
- Reduce credential interception opportunities.
- Reduce exfiltration pathways.
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

# OWASP Network Subtractive Hardening Top 10

| ID | Title |
|------|------|
| N01 | Broadcast Domain & Layer 2 Path Erasure |
| N02 | Inter-VLAN & Peer-to-Peer Non-Conductivity |
| N03 | Control Plane & Management Interface Erasure |
| N04 | Unauthenticated Protocol Deletion |
| N05 | Implicit Egress Path Erasure |
| N06 | OT / IT / IoT Convergence Edge Severing |
| N07 | Management Trust Path Reduction |
| N08 | Dynamic Protocol & Discovery Surface Erasure |
| N09 | DNS & Exfiltration Path Determinism |
| N10 | Physical & Wireless Edge Deletion |

---

# N01: Broadcast Domain & Layer 2 Path Erasure

## Description

Flat broadcast domains and uncontrolled Layer 2 adjacency create opportunities for local credential interception, spoofing, denial-of-service, and lateral movement.

## Strategic Objective

Eliminate unnecessary Layer 2 attack paths.

## Attack Path Removed

```text
Host A
  ↓
Broadcast Domain / Layer 2 Adjacency
  ↓
Host B
```

## Architectural Deletion Goal

Sever unnecessary same-segment trust and broadcast-based attack paths.

## Implementation Examples

- Use Private VLANs (PVLANs).
- Enforce port isolation.
- Enable DHCP snooping.
- Reduce ARP spoofing exposure.
- Collapse unnecessary broadcast-domain adjacency.
- Remove LLMNR and NBT-NS exposure where supported by endpoint and network controls.

---

# N02: Inter-VLAN & Peer-to-Peer Non-Conductivity

## Description

Arbitrary east-west communication between subnets or peers creates the primary network graph used for lateral movement.

## Strategic Objective

Remove unnecessary lateral reachability.

## Attack Path Removed

```text
Compromised Host
        ↓
Inter-VLAN / Peer Reachability
        ↓
Additional Hosts
```

## Architectural Deletion Goal

Eliminate arbitrary peer-to-peer and inter-subnet movement paths.

## Implementation Examples

- Block arbitrary inter-VLAN flows.
- Restrict same-VLAN host-to-host communication.
- Enforce explicit segmentation boundaries.
- Permit only required application flows.
- Remove default east-west reachability.

---

# N03: Control Plane & Management Interface Erasure

## Description

In-band management interfaces expose switches, routers, firewalls, and other infrastructure systems to compromise from production networks.

## Strategic Objective

Remove production-network reachability to network control planes.

## Attack Path Removed

```text
Compromised Host
        ↓
Management Interface
        ↓
Network Infrastructure Control
```

## Architectural Deletion Goal

Eliminate in-band management paths wherever possible.

## Implementation Examples

- Restrict management to out-of-band networks.
- Remove management interfaces from production VLANs.
- Limit administrative reachability to approved jump networks.
- Isolate switch and router control planes.
- Remove unnecessary management exposure.

---

# N04: Unauthenticated Protocol Deletion

## Description

Cleartext and unauthenticated management protocols expose network devices to credential theft, replay, and unauthorized control.

## Strategic Objective

Eliminate legacy and unauthenticated network infrastructure protocols.

## Attack Path Removed

```text
Attacker
      ↓
Unauthenticated Protocol
      ↓
Infrastructure Access
```

## Architectural Deletion Goal

Remove unauthenticated or weakly authenticated management and routing paths.

## Implementation Examples

- Disable SNMP v1/v2c.
- Disable Telnet.
- Disable HTTP management.
- Require authenticated routing adjacencies.
- Remove unauthenticated OSPF or BGP peerings.
- Prefer secure management protocols.

---

# N05: Implicit Egress Path Erasure

## Description

Default outbound routing permits compromised systems to reach arbitrary external destinations.

## Strategic Objective

Eliminate unconstrained outbound network paths.

## Attack Path Removed

```text
Compromised Host
        ↓
0.0.0.0/0 Route
        ↓
Internet
```

## Architectural Deletion Goal

Remove implicit default egress from datacenter, branch, and enclave boundaries.

## Implementation Examples

- Remove unconstrained 0.0.0.0/0 paths where feasible.
- Use explicit outbound allowlists.
- Route outbound traffic through controlled egress points.
- Restrict branch and datacenter egress.
- Enforce deterministic outbound routing.

---

# N06: OT / IT / IoT Convergence Edge Severing

## Description

Direct routed paths between enterprise IT, guest networks, IoT devices, and OT or ICS segments create high-impact compromise propagation paths.

## Strategic Objective

Remove direct convergence edges between dissimilar trust zones.

## Attack Path Removed

```text
Enterprise IT
       ↓
Direct Routing
       ↓
OT / IoT / ICS Segment
```

## Architectural Deletion Goal

Sever unnecessary routed paths between enterprise, guest, IoT, and operational technology environments.

## Implementation Examples

- Remove direct IT-to-OT routing.
- Isolate IoT networks.
- Isolate guest networks.
- Restrict ICS and OT adjacency.
- Enforce controlled mediation points where connectivity is required.

---

# N07: Management Trust Path Reduction

## Description

Administrative trust relationships and weak management-plane configurations create paths to infrastructure control.

## Strategic Objective

Reduce management-plane trust exposure.

## Attack Path Removed

```text
Administrator / Automation
          ↓
Management Trust
          ↓
Network Infrastructure Control
```

## Architectural Deletion Goal

Remove unnecessary management trust pathways and weak administrative access mechanisms.

## Implementation Examples

- Prune legacy SSH ciphers and MACs.
- Disable password authentication where feasible.
- Remove agent forwarding.
- Remove X11 forwarding.
- Restrict management access to approved identities and systems.
- Reduce automation trust where feasible.

---

# N08: Dynamic Protocol & Discovery Surface Erasure

## Description

Dynamic discovery and convenience protocols can expose topology, create unintended trust relationships, or enable unauthorized network changes.

## Strategic Objective

Remove unnecessary discovery and dynamic negotiation pathways.

## Attack Path Removed

```text
Host / Network Device
           ↓
Discovery Protocol
           ↓
Topology or Trust Exposure
```

## Architectural Deletion Goal

Eliminate unnecessary dynamic discovery, negotiation, and convenience protocols.

## Implementation Examples

- Disable CDP where unnecessary.
- Disable LLDP where unnecessary.
- Disable mDNS where unnecessary.
- Disable UPnP.
- Disable Dynamic Trunking Protocol (DTP).
- Disable Proxy ARP where unnecessary.

---

# N09: DNS & Exfiltration Path Determinism

## Description

Unrestricted DNS permits command-and-control, tunneling, and data exfiltration through arbitrary resolvers.

## Strategic Objective

Eliminate arbitrary DNS paths.

## Attack Path Removed

```text
Compromised Host
        ↓
Untrusted DNS Resolver
        ↓
Command & Control / Exfiltration
```

## Architectural Deletion Goal

Constrain DNS to deterministic, approved resolution paths.

## Implementation Examples

- Block arbitrary outbound UDP/53.
- Block arbitrary outbound TCP/53.
- Force DNS through approved resolvers.
- Monitor and constrain DNS tunneling paths.
- Enforce deterministic internal-to-external resolution paths.

---

# N10: Physical & Wireless Edge Deletion

## Description

Unused switch ports, unauthenticated wireless paths, native VLAN exposure, and auto-trunking create unnecessary physical and wireless ingress paths.

## Strategic Objective

Remove unused physical and wireless network edges.

## Attack Path Removed

```text
Unauthorized Device
          ↓
Physical / Wireless Edge
          ↓
Enterprise Network
```

## Architectural Deletion Goal

Eliminate unnecessary physical and wireless ingress paths.

## Implementation Examples

- Disable unused switch ports.
- Remove native VLAN exposure.
- Disable auto-trunking.
- Restrict unauthenticated physical access.
- Restrict unauthenticated wireless access.
- Remove unnecessary wireless sharing paths.

---

# Verification & PER Measurement

## Step 1 – Establish Baseline

Identify all eligible attack paths.

```text
P_eligible(t0)
```

## Step 2 – Implement Controls

Apply N01 through N10.

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

The goal of these subtractions is to establish deterministic boundaries within the enterprise network.

By collapsing attack paths, the network becomes architecturally non-conductive.

In this model:

```text
Compromise = Spark
Reachability = Oxygen
Network Architecture = Conductivity
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

*OWASP Network Subtractive Hardening Top 10 v1.0*
