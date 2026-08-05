# OWASP Data Center Physical Security Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Data Center, Telecommunications Room, and Computing-Facility Physical Security  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Data Center Physical Security Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing physical attack-path risk to information systems through the elimination of attacker-accessible movement, access, credential, equipment, console, media, utility, maintenance, and egress paths within computing facilities.

Unlike traditional physical security programs that focus primarily on cameras, alarms, guards, visitor logs, or after-the-fact investigation, Subtractive Hardening prioritizes the removal of architectural conditions that allow unauthorized physical access to compose into server compromise, data theft, console access, device tampering, media removal, service disruption, and business impact.

Rather than relying on reactive monitoring, video review, dispatch response, or manual guard intervention as the primary security mechanism, the objective is to physically remove conductive edges from the data center physical-access graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Entrances, Corridors, Doors, Gates, Vehicles, Loading Areas, Visitors, Badges, Racks, Cages, Consoles, Media, Equipment, Utility Systems, Maintenance Paths
E = Movement, Access, Credential, Trust, Service, Console, Equipment, Media, Utility, or Egress Relationships
```

Each recommendation within this standard is intentionally selected based on its ability to reduce adversary reachability and improve measurable attack-path reduction through the Path Erasure Rate (PER) Engineering Standard.

```text
PER = P_erased / P_eligible
```

Where:

```text
P_eligible = Eligible physical attack paths identified within scope
P_erased   = Physical attack paths rendered non-traversable through architectural deletion
```

The objective of this standard is not to make physical attacks easier to observe.

The objective is to make unauthorized physical traversal, equipment access, media removal, console compromise, and facility disruption materially more difficult by removing the pathways that enable them.

---

# Boundary Scope Note

This standard applies to physical security controls protecting information systems, including data centers, telecommunications rooms, network closets, server rooms, compute facilities, colocation cages, and associated facility infrastructure that supports enterprise computing environments.

The underlying architectural principles may also apply to broader physical-security domains such as campuses, offices, public spaces, transportation systems, and critical infrastructure sites. Those domains are outside the formal scope of this standard.

This document focuses on physical attack paths that directly affect information systems and computing facilities, including:

- Facility perimeter traversal
- Vehicle approach paths
- Public-to-restricted-space movement
- Badge and access credential paths
- Tailgating and piggybacking paths
- Rack, cage, console, and port access
- Removable media and equipment egress
- Vendor, visitor, and maintenance trust paths
- Utility and building systems paths supporting computing infrastructure
- Emergency, bypass, and override paths

This standard is intended to be compounded with, not substituted for, the supporting digital and infrastructure standards, including Network, Linux, Windows, Cloud, Identity, Datastore, Application, OT, and IoT Subtractive Hardening standards where applicable.

# Life Safety & Regulatory Priority Statement

All recommendations within this standard are subordinate to applicable life-safety, fire-safety, building-code, occupational-safety, accessibility, and regulatory requirements.

Physical attack-path elimination should only be performed where doing so does not impair emergency egress, emergency responder access, fire suppression operations, evacuation procedures, accessibility accommodations, or other legally required safety functions.

Where a physical attack path cannot be eliminated because of safety, legal, regulatory, or operational requirements, the Subtractive Hierarchy of Efficacy applies:

1. Eliminate the path where permissible.
2. Constrain the path where elimination is not permissible.
3. Monitor residual risk where neither elimination nor constraint is feasible.

Examples include:

- Fire exits that must remain operable.
- Emergency responder access requirements.
- Accessibility and ADA compliance obligations.
- Building-code-required ingress and egress paths.
- Emergency override mechanisms required by law.
- Utility and life-safety access required for facility operation.

This standard does not advocate security controls that increase risk to human life or violate applicable safety regulations.

---

## Shared Facility & Colocation Environments

In shared-tenancy environments such as colocation facilities, cloud-adjacent edge facilities, and managed computing environments, portions of the physical attack graph may be outside the tenant's administrative authority.

Where perimeter entrances, loading docks, utility systems, or facility-level paths cannot be modified by the tenant, the tenant should apply this standard to the subset of the graph under their operational control.

In these environments, controls such as:

- P04 Badge & Physical Credential Reduction
- P06 Rack, Cage, Console & Port Access Reduction
- P07 Media, Device & Equipment Egress Path Erasure
- P08 Vendor, Visitor & Maintenance Trust Reduction

often become the primary deterministic boundaries available for attack-path reduction.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The Data Center Physical Security Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within computing-facility physical security by identifying physical paths whose elimination reduces attacker optionality.

Together they establish a repeatable security engineering cycle:

1. Identify physical attack paths.
2. Measure physical attack-path exposure.
3. Eliminate physical attack paths where possible.
4. Constrain residual physical attack paths where necessary.
5. Measure resulting reduction.
6. Continuously improve architectural resilience.

---
### Physical Path Enumeration Considerations

Physical attack paths frequently exist as compositions of multiple individually legitimate paths.

Examples:

Lobby
 ↓
Elevator
 ↓
Sub-Floor
 ↓
Utility Corridor
 ↓
Server Room

or

Loading Dock
 ↓
Maintenance Corridor
 ↓
HVAC Access
 ↓
Restricted Area

PER measurements should account for composed traversal paths in addition to individual doors, gates, corridors, credentials, and access-control systems.

Failure to account for path composition may underestimate the true size of the physical attack graph.

---

# The Subtractive Hierarchy of Efficacy

All recommendations within this standard follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 - Architectural Deletion

Remove the physical attack path completely.

Examples:

- Entrance removal
- Vehicle path removal
- Corridor or routing removal
- Badge access removal
- Console path removal
- Media egress path removal
- Maintenance path removal

## Tier 2 - Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Mantraps
- Crash-rated barriers
- Restricted service corridors
- Access-controlled cages
- Single-person entry controls
- Escort-only maintenance paths
- Physical interlocks

## Tier 3 - Monitoring & Detection

Monitoring is reserved for residual physical attack paths that cannot be deleted or reasonably constrained.

Examples:

- Cameras
- Door alarms
- Guard response
- Access logs
- Intrusion detection
- Video analytics

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever a physical attack path can be eliminated, elimination is preferred.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate physical attack-path edges.
- Reduce unauthorized facility reachability.
- Reduce vehicle, pedestrian, and service-path traversal.
- Reduce badge and physical credential abuse.
- Reduce unauthorized rack, cage, console, and equipment access.
- Reduce removable media and equipment exfiltration opportunities.
- Reduce vendor, visitor, and maintenance trust paths.
- Reduce utility and facility-system compromise paths affecting information systems.
- Reduce attack-path composability.
- Improve measurable Path Erasure Rate (PER).

Recommendations are not ranked based on:

- Camera coverage
- Guard staffing levels
- Alarm volume
- Compliance requirements
- Vendor capability claims
- Physical security product availability

The primary selection criterion is architectural physical attack-path reduction.

---

# OWASP Data Center Physical Security Subtractive Hardening Top 10

| ID | Title |
|------|------|
| P01 | Facility Perimeter & Movement Path Erasure |
| P02 | Vehicle, Loading Dock & Service Approach Deletion |
| P03 | Public-to-Restricted Zone Transition Constraint |
| P04 | Badge, Key & Physical Credential Path Reduction |
| P05 | Tailgating & Piggybacking Path Constraint |
| P06 | Rack, Cage, Console & Port Access Reduction |
| P07 | Media, Device & Equipment Egress Path Erasure |
| P08 | Vendor, Visitor & Maintenance Trust Reduction |
| P09 | Utility, Building System & Physical Control Plane Isolation |
| P10 | Emergency, Bypass & Override Path Governance |

---

# P01: Facility Perimeter & Movement Path Erasure

## Description

Unnecessary entrances, corridors, side doors, internal passages, and facility movement paths increase the number of ways an unauthorized person can approach computing infrastructure.

## Strategic Objective

Eliminate unnecessary physical traversal paths into computing facilities.

## Attack Path Removed

```text
Unauthorized Person
          ↓
Unnecessary Entrance / Corridor
          ↓
Computing Facility
```

## Architectural Deletion Goal

Remove non-essential physical movement paths that connect public, semi-public, or low-trust areas to computing infrastructure.

## Implementation Examples

- Remove unnecessary exterior entrances.
- Dead-end or lock out unused internal corridors.
- Remove direct paths from public spaces to server rooms.
- Consolidate access through controlled entry points.
- Remove unused doors from facility access plans.
- Reconfigure layouts to reduce physical path density.

---

# P02: Vehicle, Loading Dock & Service Approach Deletion

## Description

Vehicle access paths, loading docks, service entrances, driveways, and delivery routes can create direct physical paths to sensitive infrastructure, power systems, cooling systems, or data center perimeters.

## Strategic Objective

Eliminate unnecessary vehicle and service approach paths.

## Attack Path Removed

```text
Vehicle / Delivery Path
          ↓
Service Approach
          ↓
Facility Perimeter / Critical Infrastructure
```

## Architectural Deletion Goal

Remove or physically block unnecessary vehicle approach paths to computing facilities and supporting infrastructure.

## Implementation Examples

- Remove unnecessary vehicle access lanes.
- Install permanent bollards where vehicle traversal is not required.
- Separate loading docks from data center perimeters.
- Restrict service roads to approved operational uses.
- Remove direct vehicle paths to critical utility areas.
- Design delivery routes that do not traverse sensitive computing zones.

---

# P03: Public-to-Restricted Zone Transition Constraint

## Description

Weak transitions between public, lobby, office, support, and restricted computing zones allow unauthorized movement toward sensitive infrastructure.

## Strategic Objective

Constrain transitions between lower-trust and higher-trust physical zones.

## Attack Path Removed

```text
Public / Low-Trust Area
          ↓
Uncontrolled Zone Transition
          ↓
Restricted Computing Area
```

## Architectural Constraint Goal

Prevent direct movement from public or low-trust zones into restricted computing areas without structurally enforced transition controls.

## Implementation Examples

- Use mantraps for data center entry.
- Use single-point-of-entry choke points.
- Separate public, office, support, and restricted computing zones.
- Use crash-rated turnstiles where appropriate.
- Require physical interlocks between trust zones.
- Remove direct lobby-to-data-center movement paths.

---

# P04: Badge, Key & Physical Credential Path Reduction

## Description

Badges, keys, access cards, PINs, temporary credentials, and shared physical credentials create durable paths into restricted areas when they are over-issued, stale, shared, or poorly scoped.

## Strategic Objective

Reduce unnecessary physical credential access paths.

## Attack Path Removed

```text
Person / Credential
        ↓
Overbroad Physical Access
        ↓
Restricted Computing Area
```

## Architectural Deletion Goal

Remove unnecessary physical access rights, shared credentials, and persistent access grants.

## Implementation Examples

- Remove dormant badge access.
- Remove stale key assignments.
- Eliminate shared physical credentials.
- Scope badge access by role and facility need.
- Time-bound temporary access.
- Remove access immediately when business need ends.

---

# P05: Tailgating & Piggybacking Path Constraint

## Description

Even when badge controls exist, unauthorized persons may traverse controlled doors by following authorized personnel through access points.

## Strategic Objective

Constrain physical entry so access cannot be transferred casually from one person to another.

## Attack Path Removed

```text
Authorized Entry
        ↓
Shared Door Opening
        ↓
Unauthorized Person Entry
```

## Architectural Constraint Goal

Remove or constrain shared-entry paths that allow unauthorized persons to enter restricted computing zones without individual authorization.

## Implementation Examples

- Use mantraps or interlocked doors.
- Use single-person entry controls where appropriate.
- Separate entry and exit lanes.
- Use anti-passback controls.
- Require individual authentication for each entrant.
- Design entry points to prevent group traversal on one credential event.

---

# P06: Rack, Cage, Console & Port Access Reduction

## Description

Physical access to racks, cages, KVMs, crash carts, serial consoles, patch panels, USB ports, and management ports can convert facility access into direct system control.

## Strategic Objective

Reduce physical paths from facility access to equipment control.

## Attack Path Removed

```text
Facility Access
      ↓
Rack / Console / Port Access
      ↓
System Control
```

## Architectural Deletion Goal

Remove unnecessary physical access to equipment, console interfaces, and management ports.

## Implementation Examples

- Lock racks and cages.
- Restrict crash cart access.
- Restrict KVM and console access.
- Block unused physical ports.
- Protect patch panels and management interfaces.
- Separate visitor-accessible areas from rack-level access.

---

# P07: Media, Device & Equipment Egress Path Erasure

## Description

Removable media, backup drives, laptops, storage devices, network equipment, servers, and other assets may leave controlled areas through insufficiently constrained physical egress paths.

## Strategic Objective

Eliminate unauthorized removal paths for data-bearing assets and computing equipment.

## Attack Path Removed

```text
Data-Bearing Asset
          ↓
Uncontrolled Physical Egress
          ↓
Data or Equipment Loss
```

## Architectural Deletion Goal

Remove uncontrolled physical paths for media, device, and equipment removal.

## Implementation Examples

- Restrict removable media movement.
- Require approved asset-removal paths.
- Physically secure backup media.
- Remove uncontrolled exits from equipment areas.
- Separate trash, recycling, and disposal flows from secure media handling.
- Use controlled chain-of-custody for equipment leaving secure areas.

### Tier 2 Constraint Example

Where media movement cannot be eliminated due to business continuity, disaster recovery, legal retention, or regulatory requirements, organizations should constrain movement through deterministic chain-of-custody controls.

Examples include:

- Dual-person authorization
- Dual-key retrieval systems
- Controlled media vaults
- Tamper-evident transport containers
- Immutable custody tracking
- Separation of storage and retrieval authority

---

# P08: Vendor, Visitor & Maintenance Trust Reduction

## Description

Vendors, visitors, contractors, facilities personnel, and maintenance teams may require limited physical access, but broad or persistent trust can create unnecessary paths into restricted computing areas.

## Strategic Objective

Reduce third-party and temporary physical trust paths.

## Attack Path Removed

```text
Visitor / Vendor / Maintenance Role
              ↓
Overbroad Facility Trust
              ↓
Restricted Computing Area
```

## Architectural Deletion Goal

Remove unnecessary vendor, visitor, and maintenance access paths into computing infrastructure.

## Implementation Examples

- Require escort-only access where appropriate.
- Time-bound vendor and visitor access.
- Remove persistent vendor access where not required.
- Scope maintenance access to specific rooms, racks, or systems.
- Separate facilities maintenance areas from computing equipment areas.
- Revoke temporary access immediately after work completion.

---

# P09: Utility, Building System & Physical Control Plane Isolation

## Description

Power, cooling, fire suppression, HVAC, building automation, UPS, generators, and environmental control systems support computing availability. Physical or logical access to these systems can create paths to disrupt computing operations.

## Strategic Objective

Reduce physical and operational paths from facility systems to computing impact.

## Attack Path Removed

```text
Building / Utility System Access
              ↓
Environmental or Power Control
              ↓
Computing Service Disruption
```

## Architectural Deletion Goal

Remove unnecessary access paths to facility control systems that can affect computing infrastructure.

## Implementation Examples

- Physically separate building control equipment from general access areas.
- Restrict access to UPS, generator, and power distribution controls.
- Restrict access to cooling and environmental control systems.
- Isolate building management control rooms.
- Remove unnecessary local override access.
- Separate facilities access from computing-equipment access.

---

# P10: Emergency, Bypass & Override Path Governance

## Description

Emergency exits, fire doors, crash bars, override keys, master keys, break-glass access, and maintenance bypasses are necessary for safety and operations but can create alternate physical access paths if not minimized and constrained.

## Strategic Objective

Constrain necessary emergency and bypass paths without allowing them to become routine traversal paths.

## Attack Path Removed

```text
Bypass / Override Mechanism
           ↓
Alternate Physical Access Path
           ↓
Restricted Computing Area
```

## Architectural Constraint Goal

Ensure emergency, safety, and maintenance bypass paths exist only where required and cannot be used as ordinary access paths.

## Implementation Examples

- Minimize emergency egress paths into sensitive areas while preserving life safety.
- Restrict master key access.
- Control break-glass mechanisms.
- Alarm emergency exits and bypass doors.
- Remove unused override paths.
- Review bypass routes as part of physical attack-path analysis.

---

# Verification & PER Measurement

## Step 1 - Establish Baseline

Identify all eligible physical attack paths within the declared computing-facility scope.

```text
P_eligible(t0)
```

## Step 2 - Implement Controls

Apply P01 through P10.

## Step 3 - Validate Erasure

Identify physical attack paths rendered non-traversable.

```text
P_erased(t1)
```

## Step 4 - Calculate PER

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Success Criteria

The objective is not improved visibility.

The objective is measurable reduction in reachable physical attack-path availability for information-system environments.

---

# Strategic Objective: Non-Conductive Physical Security

The goal of these subtractions is to establish deterministic physical boundaries around computing environments.

By collapsing physical attack paths, the computing facility becomes architecturally non-conductive.

In this model:

```text
Threat Actor / Physical Opportunity = Spark
Movement, Access, Credential, Equipment, or Egress Path = Oxygen
Facility Architecture = Conductivity
```

Remove the path, and the spark goes nowhere.

---

# Guiding Principle

Attackers can only traverse paths that exist.

The objective of Subtractive Hardening is to systematically eliminate or constrain those physical paths until unauthorized physical activity can no longer compose into system compromise, data exposure, equipment tampering, or material business impact.

**Security effectiveness is maximized when attack paths are removed, not merely observed.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Evidence-Based Security ([Evidence-Based Security Article](https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and))
- The Law of Subtractive Risk ([The Law of Subtractive Risk](https://subtractivesecurity.substack.com/p/the-law-of-subtractive-risk-moving))
- The Science of Silence

---

*OWASP Data Center Physical Security Subtractive Hardening Top 10 v1.0*
