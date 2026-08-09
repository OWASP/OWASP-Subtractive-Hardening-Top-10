# OWASP Subtractive Exception & Security Debt Management Standard

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Governance Area:** Exception Management & Security Debt  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Subtractive Exception & Security Debt Management Standard provides deterministic governance guidance for managing deviations from security controls, architectural invariants, and subtractive hardening requirements.

Unlike traditional exception processes that document deviations indefinitely, this standard treats exceptions as **temporary security debt** that must be actively reduced, constrained, and eliminated through architectural correction.

An exception does not grant permission to remain insecure.

An exception represents a documented, time-bounded condition where an attack path remains present because immediate architectural deletion is not currently feasible.

The objective of this standard is to ensure that exceptions:

- identify the attack paths they preserve,
- include meaningful compensating controls,
- reduce attacker optionality while remediation proceeds,
- expire automatically,
- drive architectural correction,
- and prevent temporary deviations from becoming permanent security debt.

The purpose of exception governance is not to normalize residual risk.

The purpose is to expose, constrain, measure, and retire residual risk until the underlying attack path is erased.

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

An approved exception does **not** automatically count as path erasure.

Where an attack path remains traversable, the path remains part of `P_eligible` unless compensating controls render the path non-traversable or materially constrained within the declared scope.

Exception handling must follow the Subtractive Hierarchy of Efficacy:

1. Eliminate the dependency and erase the path.
2. Constrain the path where deletion is not currently feasible.
3. Monitor residual risk only after deletion and constraint have been evaluated.

Exceptions should therefore be treated as temporary observations of incomplete path erasure, not as substitutes for architectural correction.

---

# The Subtractive Hierarchy of Exception Governance

All exceptions must be managed according to the Subtractive Security Hierarchy of Efficacy.

## Tier 1 - Architectural Deletion

The preferred outcome is to eliminate the condition requiring the exception.

Examples:

- Remove the legacy dependency.
- Remove the exposed service.
- Remove the trust relationship.
- Remove the excessive permission.
- Remove the unsupported protocol.
- Remove the business process dependency that requires the deviation.

## Tier 2 - Architectural Constraint

Where deletion is not currently feasible, the remaining path must be constrained.

Examples:

- Network segmentation.
- Reduced privileges.
- Restricted egress.
- Conditional access.
- Bounded execution context.
- Additional validation or approval gates.
- High-confidence controls that materially reduce exploitability or blast radius.

## Tier 3 - Monitoring & Detection

Monitoring is reserved for residual risk that cannot be deleted or reasonably constrained.

Examples:

- Targeted logging.
- SIEM alerts.
- Compensating detection rules.
- Exception-specific alert correlation.
- Boundary-violation alerting.

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever the exception-causing path can be eliminated, elimination is preferred.

---

# Purpose

This standard defines how security exceptions are requested, evaluated, approved, reviewed, renewed, escalated, and retired in a way that reduces risk over time rather than documenting insecurity indefinitely.

The objective of the exception process is not to allow permanent deviation.

The objective is to:

- temporarily manage unavoidable constraints,
- require meaningful compensating controls,
- drive architectural correction,
- prevent recurrence of known attack paths,
- preserve the integrity of the security architecture,
- and continuously reduce security debt.

---

# Guiding Principles

## Exceptions Are Signals, Not Solutions

Every exception indicates that a control, dependency, or architectural invariant cannot currently be enforced.

## Risk Must Be Reduced, Not Deferred

An exception is only acceptable if it reduces risk relative to doing nothing while permanent remediation is pursued.

## Compensation Is Mandatory

No exception may be approved without explicit compensating controls that materially limit attacker capability, blast radius, exploitability, or path conductivity.

## All Exceptions Are Temporary

Exceptions must have a defined expiration date and require active re-decision to continue.

## Architecture Must Evolve

Every exception must include a remediation plan describing how the exception will be eliminated.

## Recurrence Is Failure

Repeated exceptions for the same condition indicate a governance or architectural failure and require escalation.

---

# Scope

This standard applies to exception requests involving:

- security controls,
- subtractive hardening standards,
- architectural invariants,
- platform security baselines,
- identity controls,
- endpoint controls,
- cloud controls,
- CI/CD controls,
- application controls,
- datastore controls,
- network controls,
- AI controls,
- physical security controls,
- and other controls governed by the OWASP Subtractive Hardening Top 10 project.

This standard applies to:

- production environments,
- non-production environments,
- employees,
- contractors,
- applications,
- infrastructure,
- cloud services,
- SaaS services,
- and third-party integrations where organizational security requirements apply.

---

# Definitions

## Security Exception

A formally approved, time-bounded deviation from an established security control, architecture requirement, or subtractive hardening invariant.

## Compensating Control

A technical or architectural control that demonstrably reduces risk introduced by an exception.

Examples include segmentation, reduced privileges, additional enforcement, restricted egress, bounded execution contexts, or high-confidence detection for residual boundary violations.

## Security Debt

Residual security risk temporarily accepted with the explicit intention of elimination through architectural change.

## Functional Unit

A bounded system or environment with predictable behaviors and a defined security contract.

Examples include endpoints, identity platforms, CI/CD systems, cloud accounts, applications, datastores, or administrative planes.

## Risk Debt Register

A governed inventory of approved exceptions, their attack-path impact, compensating controls, residual risk, owners, expiration dates, renewal history, and remediation status.

---

# Roles and Responsibilities

## Requestor

The Requestor:

- initiates the exception request,
- provides business justification,
- identifies operational constraints,
- and supplies required supporting information.

## Functional Unit Owner (FUO)

The Functional Unit Owner:

- describes the technical impact,
- identifies the relevant attack path,
- proposes compensating controls,
- and defines the architectural remediation plan.

## Business Risk Owner (BRO)

The Business Risk Owner:

- accepts residual business risk,
- approves the business justification,
- confirms the operational need,
- and owns the business tradeoff created by the exception.

## Security Governance Owner (SGO)

The Security Governance Owner:

- ensures policy adherence,
- confirms required information is complete,
- validates that compensating controls are defined,
- tracks the exception lifecycle,
- monitors recurrence,
- and escalates governance failures.

---

# Exception Classes

Exceptions should be categorized consistently to support governance and trend analysis.

## Class 1 - Temporary Implementation Delay

The control is approved and feasible, but implementation is not yet complete.

## Class 2 - Compensated Business Dependency

The path is currently required for business operation, but compensating controls reduce attacker optionality while remediation proceeds.

## Class 3 - Legacy Architectural Constraint

The path exists because of a legacy system, vendor dependency, technical limitation, or business process that requires architectural remediation.

## Class 4 - Non-Compensable Exception

No meaningful compensating control exists.

Class 4 exceptions should not be approved except through explicit executive risk acceptance and emergency governance.

---

# Exception Request Requirements

All exception requests must include the following sections.

Requests missing any required section must be rejected.

## 1. Description of Deviation

The request must describe:

- what control, invariant, or standard requirement cannot be enforced,
- what is being allowed that would otherwise be prohibited,
- and which system, application, business process, or functional unit is affected.

## 2. Attack Path Impact

The request must explicitly identify the attack-path impact of the deviation.

The request must answer:

- which attacker capability is enabled or made easier,
- which attack stage is affected,
- and which path remains traversable because of the exception.

Relevant attack stages may include:

- identity compromise,
- execution,
- privilege escalation,
- lateral movement,
- persistence,
- egress,
- exfiltration,
- impact,
- or recovery denial.

## 3. Business Justification

The request must explain why enforcement is infeasible at this time.

Acceptable justifications may include:

- technical dependency,
- legal or regulatory obligation,
- business continuity requirement,
- vendor constraint,
- migration timeline,
- or documented operational necessity.

The following are not sufficient justifications by themselves:

- convenience,
- legacy,
- user preference,
- cost avoidance without risk analysis,
- or "we have always done it this way."

## 4. Mandatory Compensating Controls

The request must identify explicit controls that reduce risk while the exception exists.

Examples include:

- reduced privileges,
- reduced scope,
- segmentation or isolation,
- restricted egress,
- bounded execution context,
- additional validation,
- additional approval gates,
- high-confidence detection for boundary violations.

If no meaningful compensating control can be identified, the exception must not be approved except through explicit executive risk acceptance.

## 5. Residual Risk Statement

The request must describe:

- what risk remains,
- what attacker action is still possible,
- what attacker action is no longer possible because of compensating controls,
- and what business impact remains plausible.

## 6. Architectural Remediation Plan

The request must define how the exception will be eliminated.

The plan must describe:

- what dependency will be removed,
- what architecture must change,
- what control will become enforceable afterward,
- who owns remediation,
- and what evidence will demonstrate completion.

## 7. Time Bound

All exceptions must include:

- start date,
- mandatory expiration date,
- review frequency,
- and renewal conditions.

No exception may be approved with an expiration of "until further notice."

---

# Approval Criteria

An exception may only be approved if all of the following are true:

- The deviation is clearly described.
- The attack-path impact is explicitly identified.
- The business justification is documented.
- Compensating controls materially reduce exploitability, blast radius, or attacker optionality.
- Residual risk is documented.
- A remediation plan exists.
- A business risk owner accepts residual risk.
- The exception is time-bounded.

An exception must not be approved if:

- it does not reduce risk relative to doing nothing,
- it merely documents exposure,
- it replaces engineering work with paperwork,
- it creates permanent operational debt,
- or it lacks meaningful compensating controls.

---

# Exception Duration and Renewal

All exceptions expire automatically.

Renewal requires a new decision, not a passive extension.

Renewal requests must include evidence showing:

- compensating controls remain effective,
- remediation has progressed,
- the original dependency still exists,
- risk has not increased,
- and no new lower-risk alternative is available.

Repeated renewals without architectural change must be escalated as a governance failure.

---

# Risk Debt Register

All approved exceptions must be recorded in the Risk Debt Register.

The register should include:

- exception identifier,
- affected system or functional unit,
- exception class,
- related Subtractive Hardening standard,
- attack-path family,
- compensating controls,
- residual risk statement,
- business risk owner,
- functional unit owner,
- security governance owner,
- start date,
- expiration date,
- renewal history,
- remediation plan,
- remediation status,
- and final retirement evidence.

---

# Exception Metrics

Security governance should track exception trends to identify architectural debt and recurring path families.

Recommended metrics include:

- total active exceptions,
- active exceptions by attack-path family,
- active exceptions by Subtractive Hardening standard,
- active exceptions by functional unit,
- exceptions by class,
- average exception age,
- exceptions approaching expiration,
- repeated renewals,
- exceptions without measurable compensating controls,
- exceptions blocking PER improvement,
- exceptions retired through architectural deletion,
- and repeat exceptions by root cause.

Exception trends should inform architectural prioritization.

---

# Relationship to Alerts and Incidents

Alerts linked to an active exception must be explicitly flagged.

Alerts caused by unresolved exceptions do not count as acceptable noise.

Repeated alerts related to an exception require reassessment of compensating controls.

Exception-related alert recurrence may trigger:

- early review,
- additional constraints,
- forced remediation,
- revocation of the exception,
- or escalation to executive leadership.

---

# Monitoring and Review

Exceptions nearing expiration should be reviewed before expiration.

Where practical, exceptions nearing expiration should be reviewed at least weekly during the final review period.

Exception trends should be reviewed regularly by security governance.

Reviews should evaluate:

- whether compensating controls remain effective,
- whether the attack path remains present,
- whether remediation has progressed,
- whether the exception has recurred,
- and whether architectural correction should be prioritized.

---

# Policy Enforcement

Failure to comply with this standard may result in:

- exception denial,
- forced control enforcement,
- additional compensating control requirements,
- accelerated remediation timelines,
- escalation to executive leadership,
- or removal of affected functionality until compliance is achieved.

---

# Verification & PER Measurement

## Step 1 - Establish Baseline

Identify the attack path preserved by the exception.

```text
P_exception(t0)
```

## Step 2 - Apply Compensating Controls

Apply required architectural constraints while remediation proceeds.

## Step 3 - Validate Constraint

Determine whether compensating controls materially reduce attacker optionality, blast radius, exploitability, or path conductivity.

## Step 4 - Retire the Exception

Complete the architectural remediation plan and remove the dependency that required the exception.

## Step 5 - Validate Erasure

Confirm the previously excepted path is no longer traversable.

```text
P_erased(t1)
```

## Success Criteria

The objective is not indefinite documentation of risk.

The objective is measurable reduction and eventual erasure of the attack path that required the exception.

---

# Strategic Objective: Temporary Security Debt Reduction

The goal of this standard is to prevent exceptions from becoming permanent security debt.

In this model:

```text
Exception = Temporary Security Debt
Compensating Control = Conductivity Reduction
Remediation Plan = Path Erasure Roadmap
Expiration Date = Forced Re-Decision
```

An exception exists to protect the organization while insecurity is being removed.

It must not normalize the insecurity itself.

---

# Statement of Intent

Exceptions exist to protect the organization while removing insecurity, not to normalize it.

This standard ensures that deviation is temporary, risk is visible, compensating controls are mandatory, and architecture continuously improves.

**Security exceptions should reduce risk over time, not preserve it indefinitely.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Evidence-Based Security ([Evidence-Based Security Article](https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and))
- The Law of Subtractive Risk ([The Law of Subtractive Risk](https://subtractivesecurity.substack.com/p/the-law-of-subtractive-risk-moving))
- Subtractive Exception Handling ([Subtractive Exception Handling](https://subtractivesecurity.com/wp-content/uploads/2026/04/exceptionhandling.pdf))
- The Science of Silence

---

*OWASP Subtractive Exception & Security Debt Management Standard v1.0*
