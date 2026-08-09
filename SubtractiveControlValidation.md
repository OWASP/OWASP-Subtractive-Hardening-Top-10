# OWASP Subtractive Security Control Validation Standard

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Governance Area:** Security Control Validation & Evidence-Based Security  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Subtractive Security Control Validation Standard provides deterministic governance guidance for validating whether security controls actually reduce attacker capability, eliminate attack paths, constrain residual paths, or merely generate evidence after an attack path remains traversable.

Unlike traditional control assurance programs that focus primarily on control existence, policy compliance, tool deployment, dashboard coverage, or audit attestation, this standard requires security controls to be evaluated through falsifiable, evidence-based testing.

A control is not considered effective merely because it exists.

A control is effective when testing demonstrates that an attacker action is no longer possible, materially constrained, or reliably detected within the declared scope.

The purpose of this standard is to replace assumption-based security with validated security outcomes.

The central question is:

> **Does it work?**

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

```text
PER = P_erased / P_eligible
```

Where:

```text
P_eligible = Eligible attack paths identified within scope
P_erased   = Attack paths rendered non-traversable through architectural deletion
```

Control validation determines whether a claimed security improvement actually changes attack-path availability.

A control may contribute to PER only when validation demonstrates that a path has been structurally erased or rendered non-traversable within the declared scope.

Controls that merely generate alerts, logs, dashboards, or investigative evidence do not increase `P_erased` unless they are paired with architectural deletion or constraint that prevents path traversal.

Control validation therefore establishes the evidentiary bridge between:

```text
Control Implemented
        ↓
Control Tested
        ↓
Attack Path Erased / Constrained / Detected / Failed
        ↓
PER Updated
```

This standard is designed to ensure that PER is supported by reproducible evidence rather than assumptions, vendor claims, or compliance artifacts alone.

---

# The Subtractive Hierarchy of Control Validation

All control validation should follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 - Architectural Deletion Validation

Validate that the attack path no longer exists or cannot be traversed.

Examples:

- A disabled protocol cannot be used.
- A removed service cannot be reached.
- A blocked child-process relationship cannot execute.
- A removed trust relationship cannot be assumed.
- A deleted credential cannot authenticate.
- A removed egress path cannot communicate externally.

## Tier 2 - Architectural Constraint Validation

Validate that a required path exists only within allowed boundaries.

Examples:

- Segmentation blocks unauthorized lateral movement.
- Permission boundaries prevent privilege expansion.
- Conditional access prevents unauthorized authentication contexts.
- Egress filtering permits only approved destinations.
- Application schemas reject unauthorized input structures.
- Object authorization prevents access outside the authorized scope.

## Tier 3 - Monitoring & Detection Validation

Validate that residual activity is reliably observed when deletion or constraint is not feasible.

Examples:

- Detection rules identify specific residual behaviors.
- Alerts fire under controlled test conditions.
- Logs contain required evidence.
- Response workflows receive actionable signals.
- Monitoring is tied to a defined residual attack path.

**Architectural Deletion > Architectural Constraint > Monitoring**

A monitoring control should not be treated as equivalent to a deletion control.

A detected attack path is still a traversable attack path.

---

# Purpose

This standard defines how security controls should be tested, validated, classified, repeated, and governed when the objective is measurable attack-path reduction.

The purpose is to:

- distinguish control existence from control efficacy,
- define falsifiable success criteria,
- require evidence for security claims,
- validate whether controls produce a null result,
- support PER measurement with reproducible proof,
- identify controls that fail under realistic test conditions,
- drive remediation through architectural deletion or constraint,
- and prevent security programs from relying on unfalsifiable assertions.

The goal is not to prove that a control exists.

The goal is to determine whether the control materially changes what an attacker can do.

---

# Guiding Principles

## Existence Is Not Efficacy

A deployed tool, written policy, completed audit, or enabled configuration does not prove that a control works.

## Security Claims Must Be Falsifiable

A security claim should be testable under defined conditions and capable of failing.

If a claim cannot fail, it cannot be validated.

## The Null Result Is Evidence

A successful architectural control produces a null result against the tested attack step.

Examples:

- zero execution,
- zero lateral movement,
- zero unauthorized authentication,
- zero unauthorized egress,
- zero unauthorized access,
- zero persistence,
- or zero state change.

## Alerts Are Diagnostic, Not Proof of Resilience

An alert proves that activity was observed.

It does not prove that the attack path was eliminated.

## Simulation Should Drive Architecture

Validated attack simulation should identify conductive paths and drive architectural remediation.

## Validation Must Repeat

Controls must be revalidated because environments change, drift occurs, exceptions accumulate, and previously erased paths may reappear.

---

# Scope

This standard applies to validation of controls across:

- endpoints,
- servers,
- identity systems,
- cloud platforms,
- SaaS platforms,
- networks,
- applications,
- datastores,
- CI/CD systems,
- AI systems,
- IoT systems,
- physical security systems,
- third-party integrations,
- and other domains governed by OWASP Subtractive Hardening standards.

This standard applies to validation activities including:

- breach and attack simulation,
- adversary emulation,
- red team testing,
- purple team testing,
- control testing,
- configuration validation,
- attack-path validation,
- exposure validation,
- tabletop-supported technical validation,
- and regression testing.

This standard does not require a specific commercial platform.

Validation may be performed through commercial tools, open-source tools, custom scripts, manual testing, configuration inspection, or controlled adversary emulation where appropriate.

---

# Validation Lifecycle

# VAL01: Attack Path Mapping

## Description

Control validation begins by identifying the attack path, attacker action, or adversary technique the control is expected to prevent, constrain, or detect.

## Strategic Objective

Ensure validation tests are mapped to real attacker capability rather than generic control presence.

## Required Inputs

- Attack path or capability being tested.
- Relevant asset, system, identity, or business function.
- Applicable attack stage.
- Expected control behavior.
- Expected success criteria.

## Attack Path Modeled

```text
Attacker Action
        ↓
Target Path
        ↓
Expected Control Boundary
        ↓
Outcome
```

## Implementation Examples

- Map browser child-process execution to endpoint execution controls.
- Map outbound command-and-control simulation to egress controls.
- Map credential relay attempts to authentication protocol controls.
- Map service-to-service abuse to authorization boundaries.
- Map RAG retrieval abuse to pre-retrieval access controls.

---

# VAL02: Falsifiable Control Hypothesis

## Description

Before testing, the control claim must be expressed as a falsifiable hypothesis.

## Strategic Objective

Prevent ambiguous or unfalsifiable security claims from being treated as evidence.

## Required Format

A validation hypothesis should state:

```text
If an adversary attempts [defined action]
against [defined target]
within [defined scope],
then [control] will produce [defined outcome].
```

## Examples

```text
If a browser attempts to launch PowerShell on a managed workstation,
then the process creation attempt will be blocked.
```

```text
If a workload attempts outbound communication to an unauthorized domain,
then the connection will fail before data leaves the environment.
```

```text
If a low-privilege identity attempts to retrieve an unauthorized object,
then access will be denied before application or datastore retrieval occurs.
```

---

# VAL03: Null-Result Success Criteria

## Description

Validation must define the expected null result before testing begins.

## Strategic Objective

Measure control efficacy by attacker outcome, not by tool activity.

## Null Result Examples

A null result may include:

- no process execution,
- no network connection,
- no unauthorized authentication,
- no unauthorized data retrieval,
- no lateral movement,
- no credential exposure,
- no persistence created,
- no command execution,
- no state change,
- no workflow transition,
- no external egress.

## Architectural Deletion Goal

A Tier 1 control is validated when the attack step cannot complete because the path is structurally absent or non-traversable.

---

# VAL04: Controlled Simulation or Emulation

## Description

Controls must be tested against the mapped attack path using controlled simulation, emulation, or equivalent validation.

## Strategic Objective

Validate controls under realistic, reproducible conditions.

## Acceptable Validation Methods

- Breach and attack simulation.
- Atomic adversary emulation.
- Red-team or purple-team execution.
- Controlled command simulation.
- Configuration-based validation.
- Network reachability testing.
- Identity access testing.
- Application authorization testing.
- Data-access path testing.
- Physical walkthrough or access-path validation where applicable.

## Safety Requirements

Validation must be performed within authorized scope and with appropriate change, safety, operational, legal, and business approvals.

---

# VAL05: Outcome Classification

## Description

Each validation test must classify the actual outcome according to what happened to the attack path.

## Strategic Objective

Separate path erasure, path constraint, detection, and failure.

## Outcome Classes

### Class A - Path Erased

The tested attack path cannot be traversed.

This outcome may contribute to `P_erased`.

### Class B - Path Constrained

The tested attack path exists but is materially limited in scope, reachability, privilege, egress, or impact.

This outcome reduces risk but does not necessarily count as full erasure.

### Class C - Path Detected

The tested attack path remains traversable, but monitoring observes the behavior.

This outcome provides visibility but does not erase the path.

### Class D - Control Failed

The tested attack path remains traversable and the control fails to prevent, constrain, or reliably detect the behavior.

This outcome requires remediation, exception handling, or risk acceptance.

---

# VAL06: Architectural Remediation Feedback Loop

## Description

Validation results must drive remediation decisions.

## Strategic Objective

Convert validation failures into architectural correction rather than recurring alert triage.

## Required Actions

When a validation produces Class C or Class D outcomes, the control owner should evaluate whether the path can be:

1. eliminated,
2. constrained,
3. monitored as residual risk,
4. documented as temporary security debt,
5. or accepted through formal risk governance.

## Implementation Examples

- Replace recurring alert tuning with path removal.
- Convert repeated detection events into engineering tickets.
- Move failed controls into vulnerability or exception governance.
- Update platform standards when repeated validation failures reveal common path families.

---

# VAL07: Regression and Drift Validation

## Description

Controls that previously validated successfully must be retested because environments change.

## Strategic Objective

Prevent erased paths from reappearing through drift, exceptions, new deployments, or architectural change.

## Required Triggers

Revalidation should occur after:

- major system changes,
- new integrations,
- cloud architecture changes,
- identity model changes,
- firewall or segmentation changes,
- application releases,
- vendor onboarding,
- exception approvals,
- control upgrades,
- incident response findings,
- or scheduled validation cycles.

---

# VAL08: Evidence Requirements

## Description

Validation evidence must be sufficient to support the control outcome classification.

## Strategic Objective

Ensure control validation is reproducible, reviewable, and auditable.

## Required Evidence

Validation evidence should include:

- test objective,
- mapped attack path,
- falsifiable hypothesis,
- tested scope,
- test method,
- expected result,
- actual result,
- outcome classification,
- supporting logs or screenshots where appropriate,
- date of validation,
- tester or validation owner,
- remediation actions if needed,
- and revalidation date or trigger.

---

# VAL09: Validation Metrics

## Description

Control validation programs should measure security efficacy rather than security activity.

## Strategic Objective

Track whether the environment is becoming less conductive to attack.

## Recommended Metrics

- number of controls validated,
- number of attack paths tested,
- number of paths erased,
- number of paths constrained,
- number of paths merely detected,
- number of failed controls,
- percentage of tests producing null results,
- recurring validation failures by attack-path family,
- validation-driven PER improvement,
- time since last validation of critical controls,
- number of reintroduced paths detected through regression testing,
- number of validation failures converted into architectural remediation.

## Metrics to Avoid as Primary Success Measures

- test volume alone,
- alert volume alone,
- dashboard coverage,
- tool deployment coverage,
- audit completion percentage,
- or number of reports produced.

---

# VAL10: Control Retirement and Simplification

## Description

Validation may show that some controls are ineffective, redundant, or no longer needed because the underlying path has been erased.

## Strategic Objective

Reduce operational complexity by retiring controls that no longer provide meaningful risk reduction.

## Retirement Criteria

A control may be considered for retirement when:

- the underlying path has been erased,
- the control repeatedly fails validation and a better architectural control exists,
- the control produces noise without reducing attacker capability,
- the control duplicates another stronger control,
- or the control increases operational burden without measurable security value.

## Architectural Goal

Reduce the security stack to validated controls that either erase paths, constrain paths, or provide necessary visibility into residual risk.

---

# Relationship to Other Governance Standards

## Relationship to Vulnerability Management

Validation determines whether remediation actually changed attacker capability.

A closed finding should be validated where feasible to confirm that the associated attack path has been eliminated or constrained.

## Relationship to Exception Management

Compensating controls supporting exceptions must be validated.

An exception should not be approved solely because a compensating control is asserted to exist.

## Relationship to Third-Party Risk Management

Vendor compensating controls, segmentation, identity restrictions, data-flow restrictions, and egress controls should be validated where feasible.

Vendor assurance artifacts do not replace validation of organization-controlled boundaries.

---

# Verification & PER Measurement

## Step 1 - Identify Attack Path

Identify the specific attacker action, path, and expected control boundary.

```text
P_test(t0)
```

## Step 2 - Define Falsifiable Hypothesis

Document the expected control outcome before testing.

## Step 3 - Execute Validation

Perform controlled simulation, emulation, configuration validation, or equivalent testing.

## Step 4 - Classify Outcome

Classify the outcome as:

- Path Erased,
- Path Constrained,
- Path Detected,
- or Control Failed.

## Step 5 - Update PER Where Applicable

If validation proves path erasure, update PER.

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Step 6 - Remediate and Retest

If validation fails or only detects the path, evaluate deletion or constraint and retest after remediation.

## Success Criteria

The objective is not improved confidence.

The objective is reproducible evidence that attacker capability has been eliminated, constrained, or accurately classified as residual monitored risk.

---

# Strategic Objective: Evidence-Based Security Validation

The goal of this standard is to ensure security programs are governed by validated outcomes rather than assumptions, vendor claims, or control existence.

In this model:

```text
Control Claim = Hypothesis
Attack Simulation = Test
Null Result = Evidence of Efficacy
Detection-Only Result = Residual Path
Control Failure = Remediation Trigger
Repeated Validation = Drift Control
```

A control that has not been tested should be treated as a hypothesis.

A control that fails testing should be treated as an engineering input.

A control that produces a null result against a defined attack path provides evidence of architectural efficacy.

---

# Statement of Intent

Security must become falsifiable.

A control is not effective because it is deployed.

A control is effective when evidence shows that attacker capability has been removed, constrained, or reliably classified as residual monitored risk.

Security programs should stop treating control existence as proof of protection and instead demand validated outcomes.

**The fundamental question is not whether the control exists. The fundamental question is whether it works.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Evidence-Based Security Framework
- The Science of Silence
- The Cyber Falsifiability Crisis and the Fundamental Question No One Asks: Does it Work?

---

*OWASP Subtractive Security Control Validation Standard v1.0*
