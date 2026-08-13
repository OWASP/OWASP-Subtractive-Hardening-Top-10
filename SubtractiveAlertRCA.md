# OWASP Subtractive Alert RCA & Architectural Change Governance Standard

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Governance Area:** Alert Root Cause Analysis, Architectural Change & Residual Path Governance  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Subtractive Alert RCA & Architectural Change Governance Standard provides deterministic engineering guidance for transforming security alerts into measurable architectural improvement.

Unlike traditional security operations models that treat alerts primarily as operational events requiring investigation and response, this standard treats alerts as evidence of residual attack-path conductivity within the environment.

The objective is not merely to determine whether an alert represents malicious activity.

The objective is to determine:

- why the path existed,
- whether the path should exist,
- whether the path can be deleted,
- whether the path can be constrained,
- whether the path represents security debt,
- and how the organization can reduce future attack-path availability through architectural improvement.

Subtractive Security assumes a simple principle:

**An alert is evidence that a path exists.**

The preferred remediation is not alert tuning.

The preferred remediation is architectural deletion or architectural constraint whenever feasible.

This standard establishes a repeatable process for converting alerts into attack-path reduction opportunities aligned with the Path Erasure Rate (PER) Engineering Standard.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) measures structural attack-path reduction.

```text
PER = P_erased / P_eligible
```

Where:

```text
P_eligible = Eligible attack paths identified within scope
P_erased   = Attack paths rendered non-traversable through
             architectural deletion
```

Alert-driven architectural RCA improves PER by identifying attack paths that:

- remain reachable,
- remain executable,
- remain overly permissive,
- remain unnecessarily broad,
- or have reappeared through drift, exceptions, or operational change.

Alerts therefore represent valuable evidence regarding:

```text
P_remaining
```

which may become future contributors to:

```text
P_erased
```

through appropriate architectural remediation.

The purpose of alert handling is not merely to classify events.

The purpose of alert handling is to continuously reduce attack-path availability.

---

# Guiding Principles

## Alerts Represent Residual Conductivity

An alert should be presumed to indicate a reachable attack path, behavioral condition, trust relationship, communication path, privilege, or execution capability until proven otherwise.

---

## Detection Is Not The End State

The preferred outcome of an alert investigation is not improved detection coverage.

The preferred outcome is the elimination or reduction of the conditions that allowed the alert to occur.

---

## Tuning Is A Last Resort

Detection tuning should occur only after evaluating whether the triggering condition can:

- be removed,
- be constrained,
- be redesigned,
- or be governed as residual risk.

---

## Architectural Deletion Is Preferred

Whenever a path can be safely removed, removal is preferred over monitoring.

---

## Architectural Constraint Is Preferred To Monitoring

Where deletion is not feasible, the path should be constrained before reliance is placed upon monitoring.

---

## Alerts Must Produce Engineering Decisions

Alerts should generate architectural decisions rather than merely operational workload.

---

## Every Path Requires Justification

A path should not remain available merely because it has historically existed.

Continued existence must be justified by current business need.

---

# Alert RCA Hierarchy of Efficacy

Alert investigations should follow the Subtractive Security Hierarchy.

## Tier 1 – Architectural Deletion Review

Determine whether the triggering path can be removed entirely.

Examples:

- unused administrative utility,
- unnecessary outbound communication,
- unnecessary process execution path,
- legacy protocol usage,
- unused trust relationship,
- dormant identity,
- unnecessary application capability.

---

## Tier 2 – Architectural Constraint Review

Determine whether the path can be preserved in a narrower form.

Examples:

- administrative workstation restrictions,
- conditional access,
- segmentation,
- role reductions,
- process allowlists,
- destination restrictions,
- application control,
- path-specific authorization.

---

## Tier 3 – Residual Monitoring

Monitoring should be used only for paths that cannot currently be deleted or constrained.

Examples:

- emergency administrative access,
- required vendor connectivity,
- required legacy systems,
- approved third-party integrations,
- required privileged activity.

---

**Alert Investigation Should Produce Architectural Outcomes.**

---

# Purpose

The purpose of this standard is to ensure alerts contribute directly to attack-path reduction.

The standard seeks to:

- identify residual attack paths,
- identify overbroad permissions,
- identify overbroad communications,
- identify inherited exposure,
- identify security drift,
- identify unnecessary capabilities,
- identify opportunities for subtraction,
- support PER improvement,
- reduce recurring alerts,
- improve architectural resilience.

---

# Scope

This standard applies to alerts generated from:

- EDR,
- SIEM,
- XDR,
- Network Security Monitoring,
- Cloud Security Monitoring,
- Identity Monitoring,
- SaaS Monitoring,
- Application Security Monitoring,
- Datastore Monitoring,
- CI/CD Monitoring,
- Physical Security Monitoring,
- AI Monitoring,
- Custom Security Analytics.

The standard applies regardless of whether an alert ultimately proves:

- malicious,
- benign,
- expected,
- unexplained,
- false positive,
- or business justified.

---

# Alert RCA Lifecycle

## A01: Alert Intake

### Description

The alert is recorded and associated with the functional unit affected.

### Strategic Objective

Establish context.

### Required Inputs

- alert source,
- timestamp,
- affected asset,
- affected identity,
- affected business process,
- triggering condition,
- associated functional unit.

---

## A02: Behavioral Classification

### Description

Classify the behavior that triggered the alert.

### Classification Categories

#### Required Behavior

Necessary for legitimate business function.

#### Overbroad Behavior

Legitimate behavior implemented with unnecessary scope.

#### Unused Behavior

Behavior not required by normal operations.

#### Unexplained Behavior

Behavior lacking identified business justification.

#### Unauthorized Behavior

Behavior inconsistent with expected security contracts.

### Architectural Goal

Convert alerts into path classifications.

---

## A03: Attack Path Reconstruction

### Description

Identify the path that allowed the alert condition to occur.

### Example Path Categories

- execution,
- discovery,
- credential access,
- privilege escalation,
- persistence,
- lateral movement,
- command and control,
- exfiltration,
- cloud control plane,
- identity plane,
- CI/CD workflow,
- SaaS integration.

### Architectural Goal

Identify the actual conductive path rather than focusing solely on the event.

---

## A04: Architectural Gap Analysis

### Description

Evaluate why the path remained available.

### Review Questions

- Why did this path exist?
- Was the path intentionally preserved?
- Was the path inherited?
- Was the path reintroduced?
- Was the path insufficiently constrained?
- Did a control fail?
- Was the behavior unknown?

### Architectural Goal

Identify the root structural cause.

---

## A05: Minimum Functional State Review

### Description

Determine whether the path belongs within Minimum Functional State.

### Review Questions

- Who requires this path?
- How often is it used?
- What business process depends upon it?
- Can the capability be removed?
- Can the capability be narrowed?
- Is there a safer alternative?

### Architectural Goal

Separate required functionality from inherited exposure.

---

## A06: Path Disposition

### Description

Determine the appropriate architectural outcome.

### Permitted Outcomes

#### Delete

Remove the path entirely.

#### Constrain

Preserve functionality while reducing scope.

#### Govern

Maintain under documented residual risk.

#### Correct Detection

Detection logic requires modification.

#### Remediate Drift

Restore previously intended state.

### Architectural Goal

Ensure every alert produces an engineering decision.

---

## A07: Architectural Change Governance

### Description

Approved subtraction candidates enter change management.

### Required Elements

- path description,
- security improvement objective,
- expected PER improvement,
- validation requirements,
- rollback procedures,
- business owner approval,
- technical owner approval.

### Architectural Goal

Translate alert analysis into measurable architectural improvement.

---

## A08: Post-Change Validation

### Description

Validate that the path has been removed or constrained.

### Validation Questions

- Is the path still traversable?
- Has legitimate operation been preserved?
- Did expected null results occur?
- Were unintended side effects observed?
- Has alert frequency decreased?

### Architectural Goal

Confirm the architectural objective was achieved.

---

## A09: Residual Risk Governance

### Description

Paths that cannot currently be removed must be governed.

### Required Controls

- documented justification,
- compensating controls,
- owner assignment,
- exception tracking,
- periodic review.

### Architectural Goal

Prevent unmanaged attack-path persistence.

---

## A10: PER Update & Continuous Improvement

### Description

Architectural changes should be reflected in PER measurement activities.

### Strategic Objective

Measure structural improvement.

### Architectural Goal

Use alert-driven improvement to continuously reduce attack-path availability.

---

# Metrics

Recommended metrics include:

- Alerts resulting in path deletion
- Alerts resulting in path constraint
- Alerts resulting in residual exception
- Alert recurrence rate
- Mean time to path remediation
- Alert reduction resulting from architectural changes
- PER improvement attributable to alert-driven initiatives

---

# Success Criteria

The objective is not faster alert closure.

The objective is measurable reduction in attack-path availability.

Success is demonstrated when:

- recurring alerts decrease,
- attack paths are removed,
- attack paths are constrained,
- security debt is documented,
- PER improves,
- architectural resilience increases.

---

# Strategic Objective: Architectural Learning

In the Subtractive Security model:

```text
Alert
    ↓
Path Discovery

Path Discovery
    ↓
Architectural Decision

Architectural Decision
    ↓
Path Deletion or Constraint

Path Deletion or Constraint
    ↓
Improved PER

Improved PER
    ↓
Reduced Attack-Path Conductivity
```

An alert is not the final product.

An alert is an architectural feedback signal.

---

# Statement of Intent

Alerts should be treated as evidence of residual attack-path conductivity until analysis demonstrates otherwise.

Every alert represents an opportunity to determine whether a path can be:

- deleted,
- constrained,
- governed,
- or redesigned.

The preferred outcome of alert handling is not improved observation.

The preferred outcome is a more resilient architecture.

**Security effectiveness is maximized when the conditions that generate alerts are removed, not merely monitored.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Know Thyself: An Analytics-Based Approach to Combating Living off the Land Attacks ([Healthcare IT News Article](https://www.healthcareitnews.com/blog/know-thyself-analytics-based-approach-combating-living-land-attacks))
- Evidence-Based Security Framework
- The Science of Silence
- The Cyber Falsifiability Crisis and the Fundamental Question No One Asks: Does it Work?

*OWASP Subtractive Alert RCA & Architectural Change Governance Standard v1.0*
