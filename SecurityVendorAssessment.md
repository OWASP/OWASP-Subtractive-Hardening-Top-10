# OWASP Subtractive Vendor Assessment Scorecard

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Artifact Type:** Vendor Evaluation Worksheet  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Purpose

The OWASP Subtractive Vendor Assessment Scorecard provides a concise method for evaluating whether a security vendor, product, platform, or service contributes to measurable attack-path reduction.

This scorecard does not evaluate vendor market share, analyst rankings, feature breadth, sales maturity, compliance coverage, or brand reputation.

It evaluates one question:

> **Does this vendor help erase attack paths, or does it merely observe them?**

The scorecard is intended to support vendor evaluations, procurement reviews, proof-of-concept design, third-party risk assessments, product comparisons, and internal security architecture discussions.

---

# Core Principle

A vendor is subtractive when its product or service helps reduce the number of executable attack paths in the environment.

A vendor is not subtractive merely because it provides:

- visibility,
- alerts,
- dashboards,
- exposure scoring,
- path visualization,
- control recommendations,
- analyst workflow,
- or risk prioritization.

These capabilities may be valuable, but they operate primarily in the observational layer unless they result in structural edge removal, deterministic constraint, or validated prevention of attacker progression.

Consistent with PER-1.0:

```text
Discovery is not erasure.
Validation is not erasure.
Prioritization is not erasure.
Monitoring is not erasure.
Subtraction begins when the path ceases to exist.
```

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) measures the proportion of eligible attack paths that have been structurally erased.

```text
PER = P_erased / P_eligible
```

Where:

```text
P_eligible = Eligible attack paths identified within scope
P_erased   = Attack paths rendered non-traversable through architectural deletion
```

PER distinguishes between:

1. discovering attack paths,
2. validating attack paths,
3. prioritizing attack paths,
4. monitoring attack paths,
5. and structurally erasing attack paths.

A vendor may support PER measurement by helping discover, validate, or prioritize paths.

A vendor contributes directly to PER improvement only when its product or service helps remove or deterministically constrain executable edges in the system graph.

---

# PER Vendor Maturity Classification

Use the following maturity model to classify where the vendor primarily operates.

| Level | Classification | Description |
|------|----------------|-------------|
| PER-0 | Observational | Provides alerts, telemetry, dashboards, logs, findings, or visibility without path-level modeling. |
| PER-1 | Path-Aware | Models assets, exposures, relationships, or attack paths, but does not empirically validate traversal or erase paths. |
| PER-2 | Path-Validated | Validates reachability through BAS, CTEM, adversary emulation, red-team testing, or exposure validation, but does not erase paths by itself. |
| PER-3 | Path-Erasing | Directly removes, blocks, constrains, or strips executable attack-path edges. |
| PER-4 | Continuously Subtractive | Continuously identifies, erases, validates, tracks Delta PER, and prevents path reintroduction over time. |

A vendor can provide useful capabilities at any maturity level.

However, a vendor should not be described as subtractive unless it materially supports PER-3 or PER-4 outcomes.

---

# Scoring Instructions

Score each category from 0 to 2.

```text
0 = Does not support the capability
1 = Partially supports the capability
2 = Strongly supports the capability
```

Maximum score:

```text
20 points
```

---

# Scorecard

| ID | Category | Scoring Question | Score |
|------|----------|------------------|-------|
| S01 | Path Discovery | Can the solution identify relevant attack paths, capability edges, or TTP x Asset surfaces? | 0-2 |
| S02 | Path Validation | Can the solution empirically validate path reachability or attacker capability? | 0-2 |
| S03 | Direct Path Erasure | Can the solution directly increase `P_erased` or `S_erased`? | 0-2 |
| S04 | Architectural Persistence | Does the path remain non-traversable by default without analyst action or post-execution response? | 0-2 |
| S05 | Assumption Burden | How many operational assumptions are required for the control to succeed? | 0-2 |
| S06 | Delta PER Potential | Can the solution produce measurable positive Delta PER? | 0-2 |
| S07 | Attacker Optionality Reduction | Does the solution reduce attacker choices, or merely provide visibility into them? | 0-2 |
| S08 | Exception Debt Reduction | Can the solution reduce security exceptions, residual paths, or compensating control burden? | 0-2 |
| S09 | Path Reintroduction Resistance | Does the solution prevent erased or constrained paths from being reintroduced through drift? | 0-2 |
| S10 | Continuous Subtractiveness | Does the solution support ongoing path reduction, validation, and regression tracking? | 0-2 |

---

# Detailed Scoring Criteria

## S01: Path Discovery

**Question:** Can the solution identify relevant attack paths, capability edges, or TTP x Asset surfaces?

| Score | Criteria |
|------|----------|
| 0 | Identifies isolated events, findings, assets, or alerts without path context. |
| 1 | Identifies some relationships, exposures, or dependencies but does not create a usable path inventory. |
| 2 | Identifies attack paths, capability edges, graph relationships, or TTP x Asset surfaces within a declared scope. |

---

## S02: Path Validation

**Question:** Can the solution empirically validate path reachability or attacker capability?

| Score | Criteria |
|------|----------|
| 0 | Does not validate whether a path can be traversed. |
| 1 | Provides indirect evidence or simulation but limited validation of actual reachability. |
| 2 | Validates reachability through controlled testing, BAS, CTEM, adversary emulation, red-team testing, or equivalent methods. |

---

## S03: Direct Path Erasure

**Question:** Can the solution directly increase `P_erased` or `S_erased`?

| Score | Criteria |
|------|----------|
| 0 | Does not remove or block executable edges. |
| 1 | Constrains paths but does not fully erase them. |
| 2 | Removes or deterministically blocks execution, communication, identity, privilege, data, or control-plane edges. |

Examples of direct path erasure include:

- microsegmentation that removes traversal edges,
- application control that removes execution paths,
- identity trust removal,
- protocol removal,
- egress path removal,
- privilege path severing.

---

## S04: Architectural Persistence

**Question:** Does the path remain non-traversable by default without analyst action or post-execution response?

| Score | Criteria |
|------|----------|
| 0 | Effect depends on alert triage, analyst response, manual containment, or runtime decision-making. |
| 1 | Effect persists under normal conditions but can be routinely re-enabled or bypassed. |
| 2 | Effect is persistent by default and can only be changed through authorized configuration, deployment, exception, or architectural change. |

A vendor should not receive full credit if the control depends primarily on detection, alert review, or post-execution response.

---

## S05: Assumption Burden

**Question:** How many operational assumptions are required for the control to succeed?

| Score | Criteria |
|------|----------|
| 0 | Requires multiple fragile assumptions, including sensor function, alert generation, analyst response, and timely containment. |
| 1 | Relies primarily on automation, orchestration, or runtime decisioning. |
| 2 | Operates structurally or deterministically with minimal runtime assumptions. |

This category aligns to the Assumption Burden Principle:

> A defensive control's reliability is inversely proportional to the number of operational assumptions required for success.

---

## S06: Delta PER Potential

**Question:** Can the solution produce measurable positive Delta PER?

| Score | Criteria |
|------|----------|
| 0 | Does not provide measurable path erasure or constraint. |
| 1 | Indirectly supports PER improvement through discovery, validation, prioritization, or recommendations. |
| 2 | Directly supports measurable increases in `P_erased` or reductions in executable attack-path availability. |

---

## S07: Attacker Optionality Reduction

**Question:** Does the solution reduce attacker choices, or merely provide visibility into them?

| Score | Criteria |
|------|----------|
| 0 | Observes attacker options without reducing them. |
| 1 | Narrows attacker options through constraint or policy guidance. |
| 2 | Removes attacker options by eliminating capabilities, trust, reachability, or execution paths. |

---

## S08: Exception Debt Reduction

**Question:** Can the solution reduce security exceptions, residual paths, or compensating control burden?

| Score | Criteria |
|------|----------|
| 0 | Adds operational burden or creates additional exception requirements. |
| 1 | Helps manage or monitor exception debt but does not reduce it structurally. |
| 2 | Reduces the need for exceptions by eliminating or constraining residual attack paths. |

---

## S09: Path Reintroduction Resistance

**Question:** Does the solution prevent erased or constrained paths from being reintroduced through drift?

| Score | Criteria |
|------|----------|
| 0 | Does not detect or prevent reintroduction of paths. |
| 1 | Detects drift or path reintroduction after it occurs. |
| 2 | Prevents or automatically corrects path reintroduction through policy, architecture, or continuous enforcement. |

---

## S10: Continuous Subtractiveness

**Question:** Does the solution support ongoing path reduction, validation, and regression tracking?

| Score | Criteria |
|------|----------|
| 0 | Produces point-in-time findings or alerts. |
| 1 | Supports periodic review or remediation tracking. |
| 2 | Supports continuous path discovery, erasure, validation, Delta PER tracking, and regression prevention. |

---

# Score Interpretation

| Total Score | Classification | Meaning |
|------------|----------------|---------|
| 0-4 | Observational | Primarily provides visibility, alerts, reports, or dashboards. |
| 5-8 | Path-Aware | Helps identify paths or relationships but does not validate or erase them. |
| 9-12 | Path-Validated | Helps validate attack paths but does not directly remove them. |
| 13-16 | Subtractive | Helps remove or constrain executable paths. |
| 17-20 | Strongly Subtractive | Continuously supports path erasure, validation, persistence, and regression prevention. |

---

# Vendor Evaluation Summary Template

Use the following template during vendor evaluation.

```text
Vendor Name:
Product / Service:
Evaluation Date:
Evaluator:
Declared Scope:
Primary Use Case:

PER Maturity Classification:
Total Score:
Subtractive Classification:

Top Path Families Addressed:
- 
- 
- 

Does the vendor primarily:
[ ] Discover paths
[ ] Validate paths
[ ] Prioritize paths
[ ] Monitor paths
[ ] Constrain paths
[ ] Erase paths
[ ] Prevent path reintroduction

Evidence Reviewed:
- 
- 
- 

P_erased Contribution:

Delta PER Potential:

Exception Debt Impact:

Key Assumptions Required:

Residual Risks:

Recommendation:
[ ] Proceed
[ ] Proceed with constraint requirements
[ ] Proceed only with compensating controls
[ ] Defer
[ ] Reject
```

---

# Example Vendor Classification Patterns

The following examples are illustrative.

| Vendor Type | Typical Classification | Notes |
|------------|------------------------|-------|
| SIEM | Observational | Valuable for visibility, but generally does not erase paths by itself. |
| EDR Detection-Only | Observational / Path-Validated | May validate or observe behavior without eliminating path traversal. |
| BAS / Emulation | Path-Validated | Helps validate paths and define denominators, but does not erase paths by itself. |
| CTEM / Exposure Validation | Path-Validated | Useful for discovery and prioritization, but not subtractive unless paired with structural remediation. |
| Attack Path Management | Path-Aware / Path-Validated | Useful for graph construction and prioritization; not path erasure unless paired with enforcement. |
| Microsegmentation | Subtractive | Can remove network traversal edges when enforced. |
| Application Control | Subtractive / Strongly Subtractive | Can erase execution paths when fail-closed and persistent. |
| Identity Governance / Trust Reduction | Subtractive | Can erase privilege and identity trust paths when it removes standing access or trust chains. |
| Egress Filtering / Proxy Enforcement | Subtractive | Can erase arbitrary outbound communication paths when enforced deterministically. |

---

# Non-Subtractive Indicators

A vendor should not be considered subtractive if its primary value proposition is limited to:

- more alerts,
- more dashboards,
- more exposure scores,
- more executive reporting,
- more findings,
- more asset inventory,
- more attack graphs without enforcement,
- more prioritization without remediation,
- more detection without prevention,
- more analyst workflow,
- more compensating monitoring,
- or more risk acceptance documentation.

These may be useful inputs, but they do not constitute path erasure.

---

# Strong Subtractive Indicators

A vendor is more likely to be subtractive if it can demonstrate:

- deterministic edge removal,
- fail-closed enforcement,
- architectural persistence,
- reduced attacker optionality,
- reduced exception debt,
- reduced alert volume from erased paths,
- measurable Delta PER,
- prevented path reintroduction,
- validated null results,
- and continuous path reduction over time.

---

# Recommended Vendor Questions

Use these questions during vendor review or proof-of-concept evaluation.

1. What specific attack paths does the product erase?
2. What execution, communication, identity, privilege, data, or control-plane edges are removed?
3. What attack paths does the product only discover or visualize?
4. What attack paths does the product validate but not remove?
5. What control evidence proves the path is non-traversable?
6. Does the control fail closed?
7. Can the path be reintroduced by normal users, workloads, or attackers operating within the declared model?
8. Does the product reduce exception debt?
9. Does the product reduce or increase operational alert volume?
10. Can the product support Delta PER reporting?
11. Can the product distinguish discovery from erasure?
12. What assumptions must remain true for the product to succeed?
13. How does the product prevent drift or path reintroduction?
14. What access, credentials, integrations, or data paths does the vendor itself introduce?
15. How is vendor access removed during offboarding?

---

# Statement of Intent

The purpose of this scorecard is to prevent the conflation of visibility with security improvement.

A vendor is not subtractive because it sees more paths.

A vendor is subtractive when fewer paths remain executable after the solution is implemented.

Security buyers should therefore ask:

```text
What attacker capability disappears?
```

not merely:

```text
What new telemetry appears?
```

**A vendor is subtractive to the extent that it measurably reduces executable attacker pathways.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- OWASP Subtractive Third-Party Risk & Integration Governance Standard
- OWASP Subtractive Security Control Validation Standard
- OWASP Subtractive Security Hierarchy of Efficacy & Assumption Burden Principle

---

*OWASP Subtractive Vendor Assessment Scorecard v1.0*
