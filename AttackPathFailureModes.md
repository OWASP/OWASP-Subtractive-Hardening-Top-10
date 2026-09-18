# OWASP Attack Path Failure Mode Theory

**Document Version:** 1.0.0
**Project:** OWASP Subtractive Hardening Top 10
**Governance Area:** Foundational Theory & Security Engineering
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)
**License:** Apache License 2.0

---

# Executive Summary

This specification establishes attack paths as cybersecurity's fundamental failure mode.

Traditional cybersecurity frequently treats vulnerabilities, misconfigurations, phishing events, exposed services, or individual compromises as primary causes of security failure.

A vulnerability, credential, misconfiguration, insider action, or phishing event is a local condition.

A breach occurs only when a traversable path exists that allows that local condition to propagate into an unauthorized state transition that violates a system security invariant.

Under this model:

```text
Defect != Failure Mode
Path = Failure Mode
```

The attack path acts as the conductive mechanism that converts localized compromise into material business impact.

---

# Core Proposition

> Every breach can be explained without reference to a specific vulnerability, but no breach can be explained without reference to a path.

---

# Formal Definition

## Cybersecurity Failure Mode

A cybersecurity failure mode is defined as:

> A traversable execution path capable of converting a local defect, credential, trust relationship, misconfiguration, or authorized capability into an unauthorized state transition that violates a system security invariant.

Examples of violated invariants include:

- Confidentiality
- Integrity
- Availability
- Authorization Boundaries
- Trust Boundaries
- Safety Constraints
- Business Logic Constraints

---

# Distinguishing Defects from Failure Modes

## Defects

Examples:

- Vulnerabilities
- Misconfigurations
- Weak credentials
- User mistakes
- Phishing clicks
- Excessive permissions

These are local conditions.

## Failure Modes

Examples:

- Lateral movement routes
- Trust relationships
- Network adjacency
- Privilege inheritance chains
- Administrative execution paths
- Token propagation paths
- Data access paths
- Control-plane reachability

These mechanisms transform local compromise into enterprise impact.

---

# The Ingress and Egress Invariants

## Ingress Invariant

A defect without ingress cannot be exploited.

```text
Critical Remote Code Execution
        +
No Reachable Ingress
        =
No Exploitation
```

A vulnerability cannot self-actuate.

A path into the vulnerable component must exist.

## Egress Invariant

A defect without egress cannot compose into systemic loss.

```text
Remote Code Execution
         +
No Child Processes
         +
No Credentials
         +
No Network Egress
         =
Local Containment
```

A local state transition is not equivalent to enterprise failure.

The system must provide a conductive path to broader impact.

## Transitive Reachability Principle

For purposes of this specification, executable edges are not limited to electronic communications paths.

Edges may include:

```text
E_net   = network connectivity and routing
E_proc  = execution capability
E_cred  = credential propagation
E_perm  = authorization relationships
E_trust = federated and transitive trust relationships
E_phys  = physical transport mechanisms
E_human = human-mediated state transitions
```

Air-gap bypasses, removable media transfer, courier transport, printed material movement, and human-assisted transfer mechanisms remain executable edges within the graph model.

An air gap bridged by removable media is not a pathless breach.

The removable media simply acts as:

```text
E_phys
```

within the attack path.

---

# Necessary Condition Principle

A vulnerability is neither necessary nor sufficient for enterprise compromise.

Examples:

```text
Valid Accounts
No CVE
Compromise Occurs
```

and:

```text
Critical CVE
No Traversable Path
Compromise Fails
```

Therefore:

```text
Vulnerability != Necessary
Attack Path = Necessary
```

Attack paths are the invariant common to every successful breach.

---

# Distributed State Machines

Computer systems are distributed deterministic state machines.

Every boundary asserts a hypothesis.

```text
H:
No Valid State Transition Exists
Between State A and State B
```

When an attacker moves from State A to State B, the hypothesis is falsified.

An attack is therefore an empirical falsification event against an assumed security boundary.

---

# MITRE ATT&CK as Evidence

ATT&CK is structured as a state-transition system:

```text
Initial Access
 -> Execution
 -> Persistence
 -> Privilege Escalation
 -> Lateral Movement
 -> Impact
```

The framework predominantly catalogs conductive paths and capabilities rather than software defects.

---

# Graph Theory Foundation

Enterprise environments can be modeled as:

```text
G = (V,E)
```

Where:

```text
E_net   = network reachability and routing
E_proc  = execution primitives and process spawning
E_cred  = credential storage and token reuse
E_perm  = authorization policies and access control lists
E_trust = federated, ambient, delegated, inherited, and transitive trust relationships
E_phys  = physical transfer mechanisms
E_human = human-mediated state transitions
```

Attack paths are ordered walks through the graph.

---

# The Empty Path Principle

Let:

```text
S = adversary ingress states
T = target assets
```

If:

```text
P(S -> T) = empty set
```

then systemic compromise cannot occur.

---
# Path Reduction and Cut Sets

Security improvement is achieved by removing execution edges that prevent unauthorized state transitions from composing into material impact.

Formally:

```text
P(S -> T) = ∅

where:
S = adversary ingress states

T = impact-producing target states
---

# Relationship to PER

PER measures how many eligible attack paths have been erased.

Let:

```text
P_prior = reachable paths before architectural change
P_post  = reachable paths after architectural change
```

Conceptually:

```text
Path Reduction Ratio = 1 - (|P_post| / |P_prior|)
```

PER operationalizes this principle through formal measurement of eligible path erasure:

```text
PER = P_erased / P_eligible
```

This document explains why attack paths are the unit being measured.

---

# Relationship to Vulnerability Management

```text
Defect
   +
Path
   =
Potential Impact
```

Vulnerabilities are potential inputs.

Paths are the failure mode.

---

# Relationship to the Hierarchy of Efficacy

The Hierarchy of Efficacy establishes:

```text
Delete > Constrain > Monitor
```

Attack Path Failure Mode Theory establishes what should be deleted:

```text
Executable attack paths.
```

---

# Engineering Implications

If attack paths are the failure mode, security programs should prioritize:

- Path discovery
- Path validation
- Path reduction
- Path erasure
- Path regression prevention

The primary question becomes:

```text
What attacker capability disappears
when this control is implemented?
```

---

# Statement of Intent

A breach occurs not because a defect exists.

A breach occurs because a traversable path exists that allows the defect to compose into an unauthorized state transition that violates a system security invariant.

Security therefore improves when attack paths are removed.

---

# Summary Principle

```text
Vulnerabilities are potential inputs.
Controls are mechanisms.
Paths are the failure mode.
Path erasure is the engineering outcome.
PER is the measurement standard.
```

Subtractive Security begins where observational security ends:

```text
When the path no longer exists.

```
# References

- Path Erasure Rate (PER-1.0) Engineering Specification
- OWASP Subtractive Security Hierarchy of Efficacy & Assumption Burden Principle
- OWASP Subtractive Security Control Validation Standard
- Evidence-Based Security
- The Science of Silence
- MITRE ATT&CK Framework
- IEC 60812 Failure Modes and Effects Analysis (FMEA)

---

*OWASP Attack Path Failure Mode Theory v1.0*
