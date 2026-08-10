# OWASP Collective Path Reduction & Security Herd Immunity Standard

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Governance Area:** Collective Path Reduction, Population-Scale Subtraction & Security Herd Immunity  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Collective Path Reduction & Security Herd Immunity Standard provides deterministic engineering guidance for prioritizing attack-path deletion and constraint opportunities that can be applied across a sufficiently large population of assets, identities, workloads, applications, or endpoints to materially reduce adversary optionality at scale.

Unlike traditional remediation models that prioritize isolated findings primarily by severity, asset criticality, or exploitability, Collective Path Reduction prioritizes changes that can remove or constrain commonly reused attacker paths across large portions of the environment.

The objective is not to make every asset perfect before value is realized.

The objective is to reduce the environmental availability of attacker paths sufficiently that adversary movement, execution, persistence, egress, or privilege escalation becomes unreliable, expensive, or impossible across the population.

This standard formalizes the security herd immunity concept: when a deletion or constraint can be applied broadly enough across a population, attackers lose dependable terrain even if some residual paths remain.

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

Collective Path Reduction improves PER by prioritizing remediation actions that erase or constrain the same path family across a large portion of the eligible population.

A broadly deployable subtraction may produce more meaningful risk reduction than a narrowly scoped fix with a higher vendor severity label.

For example:

```text
One control applied to 80% of endpoints
may erase more attack paths than
one severe finding remediated on one isolated system.
```

Collective Path Reduction therefore emphasizes:

- population coverage,
- attacker dependency on the path,
- uniformity of enforcement,
- residual attacker optionality,
- and measured PER improvement across the population.

---

# The Subtractive Hierarchy of Collective Path Reduction

All population-scale security decisions should follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 - Population-Scale Architectural Deletion

Remove a common attack path across a large portion of the environment.

Examples:

- Disable an unused protocol across the endpoint fleet.
- Remove a scripting host from all standard-user workstations.
- Block browser-to-shell child process execution across managed endpoints.
- Remove legacy authentication across identity populations.
- Remove broad egress paths across workloads.
- Remove default trust relationships across cloud accounts.

## Tier 2 - Population-Scale Architectural Constraint

Where deletion is not feasible, constrain a common path across a large portion of the environment.

Examples:

- Apply endpoint-to-endpoint segmentation broadly.
- Constrain administrative tools to management systems.
- Restrict egress to approved destinations across workloads.
- Apply permission boundaries across service identities.
- Enforce application schemas across API populations.
- Require scoped tokens across service-to-service communication.

## Tier 3 - Population-Scale Monitoring & Detection

Monitor residual paths that cannot be removed or constrained across enough of the population.

Examples:

- Detection for residual use of required administrative tools.
- Monitoring for legacy paths that remain under exception.
- Alerting on attempted traversal of constrained paths.
- Telemetry for path reintroduction or drift.

**Population-Scale Deletion > Population-Scale Constraint > Population-Scale Monitoring**

Whenever a common path can be removed from a large enough portion of the population, broad removal is preferred.

---

# Purpose

This standard defines how organizations should prioritize scalable deletion and constraint opportunities that produce disproportionate reductions in attacker optionality.

The purpose is to:

- identify attack paths shared across large asset populations,
- prioritize remediations with broad environmental reach,
- define minimum useful coverage thresholds,
- reduce attacker dependency on common techniques,
- improve PER through population-scale erasure,
- avoid over-prioritizing isolated findings with limited path impact,
- and guide engineering teams toward high-leverage security changes.

The goal is not perfect coverage before action.

The goal is sufficient coverage to materially degrade the attacker's ability to rely on a path.

---

# Guiding Principles

## Attackers Prefer Reliable Terrain

Attackers favor paths that are consistently available across many systems, identities, workloads, and environments.

## Broad Path Removal Changes the Environment

A subtraction applied across a large population changes the attacker's operating conditions, not just an individual asset.

## Seventy Percent Is a Practical Decision Threshold

When a deletion or constraint can be applied to approximately 70% or more of the eligible population, it should generally be treated as strategically worthwhile, even if residual exceptions remain.

The 70% threshold is not a universal constant.

It is a practical engineering decision point indicating that a broadly used attack path can be made unreliable across the environment.

## Partial Coverage Can Still Be High Value

A control does not need 100% coverage to materially reduce attacker optionality.

A path that works on nearly every asset is more valuable to an attacker than a path that works inconsistently.

## Residual Paths Require Governance

Assets or identities that cannot receive the population-scale deletion or constraint should be governed through exception management, compensating controls, and targeted monitoring.

## Coverage Must Be Validated

Declared coverage is not sufficient.

Organizations must validate that the deletion or constraint is actually enforced across the intended population.

---

# Scope

This standard applies to population-scale attack-path reduction across:

- endpoint fleets,
- server fleets,
- identity populations,
- cloud accounts,
- workloads,
- applications,
- APIs,
- datastores,
- CI/CD systems,
- AI runtimes,
- IoT device populations,
- network segments,
- vendor integrations,
- and other environments governed by OWASP Subtractive Hardening standards.

This standard applies to common path families including:

- execution paths,
- credential paths,
- lateral movement paths,
- egress paths,
- identity trust paths,
- privilege escalation paths,
- service-to-service paths,
- application route paths,
- data access paths,
- persistence paths,
- and recovery-denial paths.

---

# Collective Path Reduction Lifecycle

# C01: Population Definition

## Description

Collective path reduction begins by defining the population to which the deletion or constraint could apply.

## Strategic Objective

Ensure coverage is measured against the correct eligible population.

## Required Inputs

- Population name.
- Population type.
- Total eligible assets, identities, workloads, or systems.
- Business owner or functional unit owner.
- Systems excluded from scope.
- Rationale for exclusions.

## Example Populations

- managed workstation fleet,
- Linux server fleet,
- cloud workloads,
- service identities,
- CI/CD runners,
- SaaS users,
- application routes,
- vendor accounts,
- AI agents,
- database service accounts.

---

# C02: Common Path Family Identification

## Description

Organizations should identify path families that exist across the population and are commonly useful to attackers.

## Strategic Objective

Prioritize paths whose broad removal meaningfully changes attacker optionality.

## Examples of Common Path Families

- browser-to-shell execution,
- workstation-to-workstation administrative access,
- unrestricted outbound egress,
- shared local administrator credentials,
- legacy authentication,
- excessive cloud role assumption,
- broad service-account permissions,
- unused scripting engines,
- public administrative interfaces,
- unmanaged API tokens.

## Architectural Goal

Identify path families that are both broadly available and operationally unnecessary or overbroad.

---

# C03: Attacker Dependency Assessment

## Description

Not all common paths are equally valuable to attackers.

A population-scale subtraction is most valuable when the path is frequently used during realistic attack chains.

## Strategic Objective

Prioritize common paths that enable meaningful attacker progression.

## Dependency Factors

Assess whether the path supports:

- initial execution,
- credential theft,
- lateral movement,
- privilege escalation,
- persistence,
- command and control,
- exfiltration,
- control-plane access,
- or recovery denial.

## Architectural Goal

Prioritize paths that adversaries depend on, not merely paths that are visible or easy to count.

---

# C04: Coverage Feasibility Assessment

## Description

Organizations should assess whether the deletion or constraint can be applied broadly enough to materially degrade attacker reliability.

## Strategic Objective

Determine whether the change can reach a population-scale threshold.

## Coverage Bands

### High Coverage

```text
>= 70% of eligible population
```

Generally strategic and worth prioritizing.

### Moderate Coverage

```text
40% - 69% of eligible population
```

Potentially valuable, especially if the path has high attacker dependency or affects high-value systems.

### Low Coverage

```text
< 40% of eligible population
```

May still be useful, but should usually be evaluated against more scalable alternatives.

## Architectural Goal

Prioritize changes that create broad environmental friction.

---

# C05: Uniformity and Drift Risk Assessment

## Description

A population-scale control is strongest when it can be applied consistently and kept consistent over time.

## Strategic Objective

Avoid controls that appear broad but degrade through exceptions, drift, or inconsistent enforcement.

## Assessment Questions

- Can the control be applied uniformly?
- Can exceptions be tracked?
- Can enforcement be centrally validated?
- Can drift be detected?
- Can new assets inherit the control automatically?
- Can coverage be measured continuously?

## Architectural Goal

Ensure collective path reduction remains durable over time.

---

# C06: Residual Population Governance

## Description

Population-scale deletion or constraint may leave residual systems where the path remains.

## Strategic Objective

Ensure residual paths do not silently preserve attacker terrain.

## Required Treatment

Residual systems should be governed through:

- documented exceptions,
- compensating controls,
- segmentation,
- restricted egress,
- privilege reduction,
- targeted monitoring,
- remediation plans,
- and expiration dates.

## Architectural Goal

Prevent residual exceptions from becoming the attacker's preferred path.

---

# C07: Collective PER Impact Estimation

## Description

Before implementation, organizations should estimate the expected PER improvement from population-scale deletion or constraint.

## Strategic Objective

Compare candidate actions by expected attack-path reduction rather than severity labels alone.

## Estimation Factors

- number of eligible assets,
- expected coverage percentage,
- number of attack stages affected,
- attacker dependency on the path,
- number of alternative paths remaining,
- blast-radius reduction,
- and expected reduction in alert noise.

## Example

```text
Path: Browser-to-shell execution
Eligible population: 5,000 workstations
Expected coverage: 4,300 workstations
Coverage: 86%
Expected outcome: path becomes unreliable across the workstation population
```

## Architectural Goal

Prioritize high-leverage changes that collapse common paths across large populations.

---

# C08: Population-Scale Implementation

## Description

Population-scale controls should be implemented through repeatable, centrally managed mechanisms where possible.

## Strategic Objective

Ensure broad path reduction can be applied safely and consistently.

## Implementation Examples

- policy-based endpoint control,
- infrastructure-as-code,
- identity governance policies,
- cloud organization policies,
- configuration management,
- network segmentation templates,
- CI/CD policy enforcement,
- application gateway policies,
- API gateway schemas,
- centralized egress controls.

## Architectural Goal

Make broad subtraction repeatable rather than manually applied.

---

# C09: Validation of Coverage and Null Result

## Description

Organizations must validate both coverage and efficacy.

## Strategic Objective

Confirm that the path is actually erased or constrained across the intended population.

## Validation Requirements

Validate:

- population coverage,
- enforcement status,
- attack-step failure,
- residual exceptions,
- legitimate business function,
- drift controls,
- and PER impact.

## Success Criteria

A successful population-scale deletion or constraint should show:

- high coverage,
- tested null result where deletion applies,
- constrained residual behavior where deletion does not apply,
- no unacceptable business disruption,
- and measurable improvement in PER or attacker optionality.

---

# C10: Continuous Collective Immunity Maintenance

## Description

Population-scale path reduction must be maintained as environments change.

## Strategic Objective

Prevent new systems, identities, workloads, or applications from reintroducing broadly removed paths.

## Maintenance Requirements

Organizations should track:

- coverage percentage over time,
- new assets missing the control,
- exceptions by population,
- drift events,
- reintroduced path families,
- recurring failures,
- validation results,
- and residual population risk.

## Architectural Goal

Maintain environmental non-conductivity as the population evolves.

---

# Relationship to Other Governance Standards

## Relationship to Behavioral Baseline & Path Discovery

Behavioral discovery identifies which paths are used, unused, overbroad, or unnecessary across populations.

Collective Path Reduction prioritizes broadly applicable subtraction opportunities discovered through that process.

## Relationship to Vulnerability Management

Vulnerability management prioritizes findings by attacker capability removed.

Collective Path Reduction adds population coverage as an optimization factor.

A broadly applicable Medium-severity finding may outrank a narrowly scoped Critical finding when the broader change erases more attacker optionality.

## Relationship to Exception Management

Residual systems that cannot receive the collective deletion or constraint must be governed as exceptions or temporary security debt.

## Relationship to Control Validation

Collective controls must be validated for both coverage and efficacy.

A declared 80% rollout does not prove path erasure unless the control produces the expected null result across the covered population.

## Relationship to PER

Population-scale deletion increases PER by erasing many instances of a common path family across the eligible population.

---

# Verification & PER Measurement

## Step 1 - Define Population

Identify the eligible population.

```text
N_eligible
```

## Step 2 - Identify Common Path

Identify the path family targeted for deletion or constraint.

```text
P_common
```

## Step 3 - Estimate Coverage

Estimate expected coverage.

```text
Coverage = N_covered / N_eligible
```

## Step 4 - Apply Deletion or Constraint

Implement the population-scale control.

## Step 5 - Validate Coverage

Confirm which members of the population actually received the control.

```text
N_validated
```

## Step 6 - Validate Efficacy

Test whether the attack step fails or is constrained where the control applies.

## Step 7 - Govern Residual Population

Document exceptions, compensating controls, and remediation plans for uncovered systems.

## Step 8 - Update PER

Update PER based on paths erased across the population.

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Success Criteria

The objective is not universal perfection.

The objective is sufficient population-scale path reduction to materially reduce attacker reliability, reachability, and optionality.

---

# Strategic Objective: Security Herd Immunity

The goal of this standard is to make common attacker paths unreliable at environmental scale.

In this model:

```text
Eligible Population = Systems where the path could exist
Covered Population = Systems where the path is deleted or constrained
Residual Population = Systems where the path remains
Coverage Threshold = Decision point for strategic value
Collective Immunity = Population-scale reduction in attacker optionality
```

A path does not need to be removed everywhere to become strategically less useful.

When a path is removed or constrained across a sufficient portion of the environment, attackers lose confidence that the path will work reliably.

That loss of reliability changes the attack economics.

---

# Statement of Intent

Subtractive Security is most powerful when common attack paths are removed at scale.

A single deletion on one asset may be useful.

The same deletion across a fleet can change the architecture.

The purpose of Collective Path Reduction is to prioritize actions that make entire classes of attacker behavior unreliable across the environment.

**When a deletion or constraint can be applied to approximately 70% or more of an eligible population, it should generally be treated as strategically worthwhile because it reduces attacker optionality at environmental scale.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Evidence-Based Security Framework
- The Science of Silence
- The Cyber Falsifiability Crisis and the Fundamental Question No One Asks: Does it Work?

---

*OWASP Collective Path Reduction & Security Herd Immunity Standard v1.0*
