# OWASP Subtractive Security Hierarchy of Efficacy & Assumption Burden Principle

**Document Version:** 1.0
**Project:** OWASP Subtractive Hardening Top 10
**Governance Area:** Foundational Theory & Security Engineering
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)
**License:** Apache License 2.0

---

# Executive Summary

The Hierarchy of Efficacy defines the reliability order of defensive controls based on the number of assumptions required for successful operation.

The hierarchy is derived from a broader engineering principle:

> The reliability of a defensive control is inversely proportional to the number of operational assumptions required for the control to succeed.

This principle is formally defined as the Assumption Burden Principle.

Unlike many cybersecurity frameworks that categorize controls based upon tool type, vendor category, compliance mapping, or visibility generated, the Hierarchy of Efficacy ranks controls according to deterministic engineering reliability.

Every mature engineering discipline follows a similar hierarchy:

1. Eliminate the failure mode.
2. Constrain the remaining failure modes.
3. Monitor what cannot be eliminated or constrained.

Cybersecurity frequently inverts this order by prioritizing observation before structural risk reduction.

The purpose of this document is to establish a consistent engineering basis for prioritization across PER, Vulnerability Management, Validation, Collective Path Reduction, Behavioral Baseline Discovery, Platform Standards, and all Subtractive Security implementations.

---

# Relationship to PER-1.0

PER measures attack-path reduction.

```text
PER = P_erased / P_eligible
```

The Hierarchy of Efficacy explains why path erasure contributes more structural risk reduction than path observation.

Architectural deletion directly increases:

```text
P_erased
```

Constraint reduces reachable attack space.

Monitoring primarily produces evidence about a path that remains available.

Therefore:

```text
Deletion > Constraint > Detection
```

is not a preference.

It is a consequence of differing reliability characteristics.

---

# The Assumption Burden Principle

## Definition

The Assumption Burden Principle states:

> A defensive control's functional reliability is inversely proportional to the number of assumptions required for that control to successfully prevent attacker progression.

As required assumptions increase:

```text
Reliability decreases.
```

As required assumptions decrease:

```text
Reliability increases.
```

## Engineering Interpretation

Every control relies upon assumptions.

Examples include:

- software operating correctly,
- policies remaining enforced,
- telemetry being collected,
- storage being available,
- detection rules firing,
- analysts responding,
- network communications succeeding,
- credentials remaining valid,
- integrations continuing to operate,
- automation functioning correctly.

Each additional dependency increases overall control fragility.

---

# Reliability Model

## Observational Controls

A typical detection pipeline may require:

```text
Sensor Functional
        ↓
Telemetry Collected
        ↓
Telemetry Ingested
        ↓
Rule Parses Correctly
        ↓
Detection Logic Fires
        ↓
Alert Generated
        ↓
Alert Delivered
        ↓
Analyst Reviews Alert
        ↓
Response Executed
        ↓
Containment Successful
```

Failure at any point may invalidate the prevention objective.

## Architectural Deletion

A deleted path requires:

```text
Path = ∅
```

No runtime decision exists.

No analyst intervention exists.

No detection dependency exists.

No response dependency exists.

The path simply does not exist.

---

# The Hierarchy of Efficacy

## Level 1 - Architectural Deletion

### Definition

Eliminate the attack path or hazard entirely.

### Objective

Remove attacker capability through structural modification of system geometry.

### Examples

- Remove unnecessary protocols.
- Remove local administrator privileges.
- Remove workstation-to-workstation communication.
- Remove unauthorized egress paths.
- Remove unused services.
- Remove trust relationships.
- Remove exposed administrative interfaces.
- Remove dormant credentials.

### Reliability Characteristics

```text
Lowest Assumption Burden
Highest Reliability
Highest Predictability
```

### Validation Question

```text
Can the attack path still be traversed?
```

Successful outcome:

```text
No.
```

---

## Level 2 - Architectural Constraint

### Definition

When deletion is not feasible, restrict operation to explicitly authorized boundaries.

### Objective

Reduce attacker capability while preserving required business functionality.

### Examples

- Microsegmentation.
- Application control.
- Egress filtering.
- Permission boundaries.
- Conditional access.
- API authorization boundaries.
- Data access restrictions.
- Object and field-level security.

### Reliability Characteristics

```text
Moderate Assumption Burden
High Reliability
Bounded Risk
```

### Validation Question

```text
Does the path operate only within approved boundaries?
```

Successful outcome:

```text
Yes.
```

---

## Level 3 - Monitoring & Detection

### Definition

Observe activity occurring on paths that remain available.

### Objective

Provide evidence regarding residual attack paths.

### Examples

- EDR.
- SIEM.
- IDS.
- UEBA.
- Log analytics.
- Threat hunting.
- Dashboarding.
- Alerting.

### Reliability Characteristics

```text
Highest Assumption Burden
Lowest Deterministic Reliability
Dependent Upon Human And Technical Workflows
```

### Validation Question

```text
Was activity observed?
```

Successful outcome:

```text
Maybe.
```

Observation does not prove path removal.

---

# The Great Cybersecurity Inversion

Traditional engineering follows:

```text
Identify Hazard
        ↓
Eliminate Hazard
        ↓
Constrain Hazard
        ↓
Monitor Residual Hazard
```

Cybersecurity frequently operates as:

```text
Identify Hazard
        ↓
Monitor Hazard
        ↓
Improve Monitoring
        ↓
Improve Dashboarding
        ↓
Improve Triage
```

This inversion creates excessive architectural conductivity, operational fatigue, and alert dependence.

---

# Relationship to Validation

Validation should follow the hierarchy.

### Architectural Deletion Validation

Ask:

```text
Can the attacker still perform the action?
```

### Constraint Validation

Ask:

```text
Can the attacker exceed approved boundaries?
```

### Monitoring Validation

Ask:

```text
Did observation occur?
```

The first two questions evaluate resilience.

The third evaluates visibility.

Visibility and resilience are not equivalent.

---

# Relationship to Vulnerability Management

The hierarchy directly informs prioritization.

Preferred remediation sequence:

```text
Delete Path
        ↓
Constrain Path
        ↓
Monitor Path
```

A lower-severity deletion opportunity may provide greater risk reduction than a higher-severity monitoring enhancement.

---

# Relationship to Collective Path Reduction

Collective Path Reduction prioritizes broadly deployable deletions and constraints.

The Hierarchy of Efficacy determines:

```text
Which category of action is strongest.
```

Collective Path Reduction determines:

```text
How broadly that action can be applied.
```

Together they drive engineering optimization.

---

# Relationship to Behavioral Baseline & Path Discovery

Behavioral discovery answers:

```text
What should exist?
```

The Hierarchy of Efficacy answers:

```text
Once identified,
what should be removed first?
```

You cannot subtract what you do not understand.

Once understood:

```text
Delete > Constrain > Monitor
```

---

# Engineering Interpretation

The objective of cybersecurity is not maximum visibility.

The objective is minimum attacker capability.

A deleted attack path requires fewer assumptions than a constrained attack path.

A constrained attack path requires fewer assumptions than a detected attack path.

Therefore:

```text
Deletion is inherently more reliable.
```

The hierarchy is not vendor-specific.

The hierarchy is not technology-specific.

The hierarchy emerges from reliability engineering itself.

---

# Statement of Intent

The Hierarchy of Efficacy establishes the foundational reliability model for Subtractive Security.

Security controls should be prioritized according to their ability to eliminate assumptions.

The fewer assumptions a control requires, the more reliable its outcome becomes.

Controls should therefore be pursued in the following order:

```text
Architectural Deletion
        ↓
Architectural Constraint
        ↓
Monitoring & Detection
```

Security maturity is not measured by how much activity is observed.

Security maturity is measured by how many attacker actions are no longer possible.

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Evidence-Based Security Framework([Evidence-Based Security Article](https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and))
- The Science of Silence
- The Cyber Falsifiability Crisis and the Fundamental Question No One Asks: Does it Work?([The Cyber Falsifiability Crisis](https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and))
