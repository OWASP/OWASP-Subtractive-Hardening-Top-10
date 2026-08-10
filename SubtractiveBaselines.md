# OWASP Subtractive Behavioral Baseline & Path Discovery Standard

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Governance Area:** Behavioral Baseline, Path Discovery & Minimum Functional State  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Subtractive Behavioral Baseline & Path Discovery Standard provides deterministic engineering guidance for discovering legitimate system behavior before attack-path subtraction occurs.

Unlike traditional behavioral analytics programs that focus primarily on anomaly detection, insider-threat monitoring, alerting, or user/entity behavior analytics, this standard uses local behavioral analytics as a prerequisite for architectural subtraction.

The objective is not merely to identify suspicious behavior.

The objective is to identify what the business actually needs to do, so unnecessary execution, communication, privilege, trust, identity, egress, and data paths can be safely eliminated or constrained.

Subtractive Security depends on a simple operational truth:

> **You cannot subtract what you do not understand.**

This standard defines how organizations should establish behavioral baselines, identify authorized paths, distinguish necessary from unnecessary functionality, and use observed local behavior to define Minimum Functional State before applying subtractive controls.

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

Behavioral baseline and path discovery improves PER by establishing a defensible understanding of which paths are:

- required for legitimate business operation,
- unused or unnecessary,
- overbroad relative to actual use,
- anomalous but explainable,
- unauthorized,
- or eligible for deletion or constraint.

Without behavioral discovery, organizations risk either:

- removing paths that are legitimately required, or
- preserving paths that exist only because no one has measured whether they are needed.

Behavioral discovery therefore supports the identification of `P_eligible` and helps determine which paths can safely contribute to `P_erased`.

---

# The Subtractive Hierarchy of Behavioral Discovery

Behavioral baseline and path discovery should support the Subtractive Security Hierarchy of Efficacy.

## Tier 1 - Architectural Deletion Discovery

Identify paths that are not used, not required, or not justified by business function.

Examples:

- unused outbound destinations,
- unused protocols,
- dormant service accounts,
- unused administrative tools,
- unused application routes,
- unused firewall paths,
- unused cloud permissions,
- unused CI/CD integrations.

## Tier 2 - Architectural Constraint Discovery

Identify paths that are required but overbroad.

Examples:

- services that require access to one destination but have internet-wide egress,
- identities that require read access but possess write access,
- applications that require one API but can reach many APIs,
- developers who require repository access but not production deployment access,
- workloads that require tenant-specific data but can query cross-tenant data.

## Tier 3 - Monitoring & Detection Discovery

Identify behavior that cannot yet be removed or constrained and therefore requires residual monitoring.

Examples:

- required administrative actions,
- required vendor access,
- required legacy protocol use,
- required emergency paths,
- required externally facing services.

**Discovery Enables Deletion. Discovery Enables Constraint. Discovery Defines Residual Monitoring.**

Behavioral analytics should not be used only to generate alerts.

Behavioral analytics should be used to define what should exist.

---

# Purpose

This standard defines how organizations should use local behavioral analytics and path discovery to support safe, evidence-based subtraction.

The purpose is to:

- identify what systems actually do,
- identify who performs which actions,
- identify where activity occurs,
- identify which paths are legitimately required,
- identify unused or unnecessary paths,
- distinguish authorized behavior from inherited exposure,
- define Minimum Functional State,
- support PER measurement,
- reduce operational risk during subtraction,
- and prevent security controls from being based on assumptions.

The goal is not to monitor everything forever.

The goal is to understand enough to remove what should not exist.

---

# Guiding Principles

## Know Thyself Before Subtracting

Organizations must understand their own legitimate behavior before safely removing behavior.

## Local Behavior Matters

Vendor defaults, generalized best practices, and industry baselines cannot fully determine what a specific environment legitimately requires.

## Observation Is a Means, Not the Objective

Behavioral analytics should produce architectural decisions, not merely more alerts.

## Minimum Functional State Is the Target

The purpose of discovery is to identify the minimum set of paths required for the business function to operate safely and predictably.

## Unused Capability Is Attack Surface

If a capability is not required for legitimate operation, it should be treated as a candidate for deletion or constraint.

## Authorized Behavior Must Be Explicit

A path should not remain open merely because it has not yet caused an incident.

## Baselines Must Be Revalidated

Business behavior changes over time, and previously valid paths may become unnecessary or overbroad.

---

# Scope

This standard applies to behavioral baseline and path discovery across:

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

This standard applies to discovery activities including:

- process behavior analysis,
- command-line behavior analysis,
- network flow analysis,
- egress usage analysis,
- identity and privilege usage analysis,
- service-account activity analysis,
- API usage analysis,
- application route usage analysis,
- datastore query and access analysis,
- CI/CD workflow usage analysis,
- cloud permission usage analysis,
- and vendor integration behavior review.

This standard does not require a specific tool or analytics platform.

Discovery may be performed through logging, flow records, EDR telemetry, cloud telemetry, identity logs, application logs, configuration analysis, endpoint analytics, manual review, controlled observation, or equivalent evidence sources.

---

# Discovery Lifecycle

# B01: Functional Unit Definition

## Description

Behavioral discovery begins by defining the functional unit under review.

A functional unit is a bounded system, workload, environment, application, user population, business process, or technology domain with predictable behaviors and a defined security contract.

## Strategic Objective

Ensure behavioral analysis is scoped to a meaningful operational boundary.

## Required Inputs

- Functional unit name.
- Business owner.
- Technical owner.
- Supported business process.
- Assets in scope.
- Users, identities, or workloads in scope.
- Expected data flows.
- Expected administrative paths.

## Example Functional Units

- workstation fleet,
- production web application,
- CI/CD runners,
- AWS account,
- Microsoft 365 tenant,
- application database,
- AI agent runtime,
- vendor integration,
- privileged administrative plane.

---

# B02: Legitimate Behavior Inventory

## Description

Organizations should inventory observed behavior within the functional unit before applying subtractive controls.

## Strategic Objective

Identify what is actually used, who uses it, where it is used, and when it is used.

## Behavior Categories

The inventory should capture relevant behavior such as:

- executed binaries,
- scripts and interpreters,
- child-process relationships,
- network destinations,
- inbound connections,
- outbound connections,
- service account usage,
- privileged commands,
- API calls,
- data access patterns,
- administrative actions,
- authentication paths,
- CI/CD workflow actions,
- application route usage,
- and datastore access patterns.

## Architectural Goal

Create an evidence-based picture of functional behavior before subtractive controls are applied.

---

# B03: Authorized Path Classification

## Description

Observed behavior must be classified according to whether it is authorized, necessary, overbroad, unexplained, or unnecessary.

## Strategic Objective

Separate required paths from inherited exposure.

## Classification Outcomes

### Required Path

The path is necessary for a documented business or technical function.

### Overbroad Path

The path is needed in some form but is broader than required.

### Unused Path

The path exists but has no observed legitimate use during the analysis period.

### Unexplained Path

The path is observed but lacks business justification.

### Unauthorized Path

The path conflicts with the expected security contract or business function.

## Architectural Goal

Convert behavioral observation into subtraction candidates.

---

# B04: Minimum Functional State Definition

## Description

Minimum Functional State is the smallest set of paths, privileges, services, identities, protocols, communications, and behaviors required for a functional unit to perform its legitimate business purpose.

## Strategic Objective

Define the target state for subtraction.

## Minimum Functional State Should Define

- required processes,
- required services,
- required protocols,
- required network destinations,
- required inbound paths,
- required outbound paths,
- required identities,
- required privileges,
- required data access,
- required administrative paths,
- required integrations,
- required runtime capabilities.

## Architectural Goal

Anything outside Minimum Functional State becomes a candidate for deletion, constraint, or residual monitoring.

---

# B05: Subtraction Candidate Identification

## Description

Discovery should produce a prioritized list of paths eligible for deletion or constraint.

## Strategic Objective

Translate behavioral analysis into actionable attack-path reduction.

## Candidate Types

Subtraction candidates may include:

- unused services,
- unused protocols,
- unused application routes,
- unused cloud permissions,
- unused service accounts,
- unused outbound destinations,
- unused administrative tools,
- unused scripting engines,
- unused vendor integrations,
- overbroad egress,
- overbroad role assignments,
- overbroad API scopes,
- overbroad datastore permissions,
- overbroad CI/CD runner permissions.

## Prioritization Criteria

Prioritize candidates that reduce:

- credential theft paths,
- execution paths,
- lateral movement paths,
- persistence paths,
- control-plane access paths,
- data exposure paths,
- egress paths,
- or business-impact paths.

---

# B06: Business Justification Review

## Description

Before deletion or constraint, candidate paths should be reviewed for legitimate business justification.

## Strategic Objective

Prevent accidental disruption while preserving subtractive intent.

## Review Questions

- What business process requires the path?
- Who uses the path?
- How often is the path used?
- What system depends on the path?
- What happens if the path is removed?
- Can the path be narrowed instead of preserved broadly?
- Can the dependency be redesigned?
- Is there a safer substitute?

## Architectural Goal

Confirm whether the path should be deleted, constrained, monitored, or temporarily excepted.

---

# B07: Pre-Subtraction Risk and Change Planning

## Description

Subtraction should be planned with awareness of operational risk, rollback needs, and validation requirements.

## Strategic Objective

Ensure subtraction improves security without avoidable operational disruption.

## Required Planning Elements

- change owner,
- affected functional unit,
- path to be removed or constrained,
- expected security improvement,
- expected operational impact,
- rollback or recovery plan where appropriate,
- validation plan,
- communication plan,
- and exception path if the control cannot be applied.

## Architectural Goal

Make subtraction controlled, intentional, and evidence-based.

---

# B08: Post-Subtraction Validation

## Description

After a path is removed or constrained, validation must confirm that the intended behavior was achieved.

## Strategic Objective

Ensure subtraction produced the expected null result or constraint.

## Validation Questions

- Is the path no longer traversable?
- Is legitimate business behavior still functional?
- Did unexpected dependencies fail?
- Did the control produce the expected null result?
- Did alert noise decrease?
- Did PER improve?
- Did any compensating exception become necessary?

## Architectural Goal

Confirm that behavioral discovery led to measurable attack-path reduction.

---

# B09: Drift and Recurrence Monitoring

## Description

Previously removed or constrained paths can reappear through configuration drift, new deployments, exceptions, vendor changes, or business process changes.

## Strategic Objective

Prevent the environment from returning to a more conductive state.

## Drift Indicators

- previously blocked destinations reappearing,
- dormant identities becoming active,
- old protocols returning,
- removed routes being redeployed,
- new broad permissions appearing,
- new unmanaged integrations,
- new application behavior outside baseline,
- recurring exceptions for the same path family.

## Architectural Goal

Use behavioral monitoring to prevent path reintroduction.

---

# B10: Continuous Baseline Refinement

## Description

Behavioral baselines must evolve as business processes, applications, systems, and threat models change.

## Strategic Objective

Keep Minimum Functional State aligned to the current business reality.

## Refinement Triggers

Rebaseline when:

- major applications change,
- cloud architecture changes,
- identity architecture changes,
- network architecture changes,
- new vendors are integrated,
- AI agents or automation are introduced,
- CI/CD workflows change,
- incident response identifies unexpected paths,
- validation detects drift,
- or business processes materially change.

## Architectural Goal

Maintain an environment where legitimate behavior is understood and unnecessary paths are continuously identified for subtraction.

---

# Relationship to Other Governance Standards

## Relationship to Vulnerability Management

Behavioral discovery helps determine whether a finding has attack-path impact by revealing whether the affected path is actually reachable, used, unnecessary, or overbroad.

## Relationship to Exception Management

If a candidate path cannot be removed because of business need, the exception process governs the residual security debt.

## Relationship to Third-Party Risk Management

Vendor integrations should be assessed through observed access, data flows, authentication paths, and egress behavior.

## Relationship to Control Validation

Behavioral baselines define expected system behavior; validation confirms whether subtractive controls enforce that expected state.

---

# Verification & PER Measurement

## Step 1 - Define Functional Unit

Identify the system, workload, environment, or business process being analyzed.

```text
FU(t0)
```

## Step 2 - Observe Behavior

Collect evidence of legitimate behavior within the functional unit.

## Step 3 - Classify Paths

Classify paths as required, overbroad, unused, unexplained, or unauthorized.

## Step 4 - Define Minimum Functional State

Document the minimum required set of paths for legitimate operation.

## Step 5 - Identify Subtraction Candidates

Identify paths eligible for deletion or constraint.

## Step 6 - Apply Subtraction

Remove or constrain unnecessary paths.

## Step 7 - Validate Outcome

Confirm the path is erased or constrained and legitimate function remains intact.

```text
P_erased(t1)
```

## Step 8 - Update PER

Update PER based on paths erased or constrained through the discovery process.

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Success Criteria

The objective is not improved observability.

The objective is a defensible understanding of legitimate behavior that enables measurable attack-path reduction.

---

# Strategic Objective: Minimum Functional State

The goal of this standard is to guide organizations toward Minimum Functional State.

In this model:

```text
Observed Behavior = Evidence
Authorized Path = Required Function
Unused Path = Subtraction Candidate
Overbroad Path = Constraint Candidate
Minimum Functional State = Target Architecture
Path Discovery = PER Input
```

A system is not more secure because more behavior is monitored.

A system is more secure when unnecessary behavior no longer exists.

---

# Statement of Intent

Subtractive Security requires knowledge of the environment.

The purpose of behavioral baseline and path discovery is to ensure subtraction is precise, evidence-based, and operationally safe.

Behavioral analytics should not merely produce alerts.

Behavioral analytics should reveal what the business actually needs so everything else can be removed, constrained, or governed as residual risk.

**You cannot subtract what you do not understand.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Know Thyself: An Analytics-Based Approach to Combating Living off the Land Attacks ([Healthcare IT News Article](https://www.healthcareitnews.com/blog/know-thyself-analytics-based-approach-combating-living-land-attacks))
- Evidence-Based Security Framework
- The Science of Silence
- The Cyber Falsifiability Crisis and the Fundamental Question No One Asks: Does it Work?

---

*OWASP Subtractive Behavioral Baseline & Path Discovery Standard v1.0*
