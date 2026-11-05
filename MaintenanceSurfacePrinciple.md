# OWASP Subtractive Security Maintenance Surface Principle

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Governance Area:** Foundational Theory, Minimum Functional State & Engineering Sustainability  
**Alignment:** Subtractive Behavioral Baseline & Path Discovery Standard, Hierarchy of Efficacy, Attack Path Failure Mode Theory, Attacker Optionality Principle, PER-1.0  
**License:** Apache License 2.0

# Executive Summary

The OWASP Subtractive Security Maintenance Surface Principle establishes that technical capability imposes recurring cost even when that capability is not currently exploitable, reachable, or actively used.

Modern vulnerability management evaluates whether a defect is exploitable and prioritizes remediation using reachability, threat intelligence, severity, and consequence. These methods help determine what defenders should address first. They do not answer a more fundamental architectural question:

> Why does the component, dependency, identity, configuration, privilege, protocol, service, or path still exist?

Every retained technical state can create recurring obligations to inventory, assess, patch, test, validate, monitor, document, support, audit, investigate, or eventually migrate. Components that provide little or no legitimate business value can therefore impose continuing engineering and security cost even when immediate exploitability is low.

Subtractive Security refers to this retained obligation as **Maintenance Surface**.

The objective is not minimum technology for its own sake. The objective is **Minimum Functional State** - the smallest defensible set of capabilities and paths required to satisfy legitimate business and operational requirements.

```text
Unnecessary State
-> Unnecessary Maintenance Obligation
-> Recurring Engineering and Security Cost

Deletion
-> Removes Current State
-> Eliminates Future Obligations Uniquely Attributable to That State
```

A vulnerability can be patched while leaving Maintenance Surface unchanged. A risk can be deprioritized while leaving Maintenance Surface unchanged. Deletion changes the architecture and the future obligation set.

# Core Proposition

> Security architectures SHOULD minimize technical states, components, dependencies, configurations, identities, privileges, interfaces, relationships, and paths that impose recurring maintenance or governance obligations beyond those required to satisfy Minimum Functional State.

A component does not need to be exploitable to impose security cost. Continued existence alone can create recurring obligations.

# Definition

## Maintenance Surface

**Maintenance Surface** is the total set of technical states, components, dependencies, configurations, identities, privileges, interfaces, and relationships whose continued existence requires an organization to expend resources to understand, inventory, secure, patch, test, validate, monitor, support, govern, audit, or eventually retire them.

Maintenance Surface may include:

- operating-system and container packages,
- application dependencies, libraries, frameworks, runtimes, and SDKs,
- APIs, services, daemons, and protocols,
- firewall, routing, egress, and trust relationships,
- identities, service accounts, privileges, and role assignments,
- cloud resources and permissions,
- CI/CD components and infrastructure-as-code modules,
- custom integrations and administrative tools,
- configuration and platform variants,
- legacy platforms and data stores,
- security exceptions and compensating-control records,
- and other retained technical states requiring continuing organizational attention.

# Attack Surface and Maintenance Surface

Attack Surface and Maintenance Surface describe different properties of the same environment.

## Attack Surface

Attack Surface describes the states, interfaces, capabilities, and transitions through which an adversary can establish or expand unauthorized capability.

> What can the attacker use?

## Maintenance Surface

Maintenance Surface describes retained technical states whose continued existence creates recurring defender obligations.

> What must the defender continue carrying because this exists?

```text
Attack Surface      = Adversary-Centric Exposure
Maintenance Surface = Defender-Centric Obligation
```

The surfaces overlap but are not identical. A component may impose high maintenance burden while presenting little immediate attacker utility. A small, exposed component may have low maintenance burden but high attacker utility.

# The Maintenance Liability Principle

> Every retained technical capability creates potential future obligations unless those obligations are eliminated by deletion of the state that creates them.

The acquisition cost of a component does not represent its total lifecycle cost. A dependency added at negligible monetary cost can create future obligations such as:

```text
Inventory
+ Vulnerability Assessment
+ Patch Evaluation
+ Regression Testing
+ Compatibility Analysis
+ SBOM Maintenance
+ License Review
+ Configuration Management
+ Detection Engineering
+ Audit Evidence
+ Exception Management
+ Incident Investigation
+ Upgrade or Migration
+ Eventual Removal
```

Not every component incurs every cost during every period. The exact future cost is not deterministic. The structural observation is simpler:

> A state that no longer exists cannot generate future maintenance work uniquely attributable to that state.

# Unfunded Technical Liability

Technical decisions frequently create future obligations without explicitly funding or accounting for those obligations at introduction.

```text
Add Dependency X Today
-> No Material Acquisition Cost
-> Dependency Persists
-> Future Vulnerabilities
-> Future Compatibility Work
-> Future Testing
-> Future Audit Scope
-> Future Incident Questions
-> Future Retirement Work
```

Subtractive Security treats unnecessary retained capability as an **unfunded technical liability** when the organization continues carrying those obligations without corresponding business value.

# Maintenance Surface and Minimum Functional State

The Subtractive Behavioral Baseline & Path Discovery Standard defines Minimum Functional State as the target of behavioral discovery. The objective is to identify the minimum set of paths and capabilities required for legitimate business operation.

Every unnecessary state above Minimum Functional State can create:

- additional attack surface,
- additional attacker optionality,
- additional defender assumption burden,
- additional maintenance surface,
- additional audit and governance burden,
- additional cognitive complexity.

```text
Observed State
-> Determine Legitimate Requirement
-> Define Minimum Functional State
-> Delete Unnecessary State
-> Constrain Required State
-> Maintain and Monitor Residual State
```

# Relationship to the Subtractive Behavioral Baseline & Path Discovery Standard

Maintenance reduction MUST be evidence-based. Organizations SHOULD NOT delete components solely because current telemetry shows no recent use without considering:

- seasonal operations,
- emergency workflows,
- disaster recovery and business continuity,
- infrequent administrative requirements,
- regulatory retention,
- batch processes,
- dependency relationships,
- latent service requirements,
- known logging or visibility limitations.

Behavioral discovery establishes defensible evidence about what the environment actually requires.

> You cannot subtract what you do not understand.

Observation is a means to an architectural decision, not an objective in itself.

# Relationship to Attack Path Failure Mode Theory

Attack Path Failure Mode Theory establishes that local defects become systemic failures through traversable paths. Maintenance Surface addresses a complementary concern: retained state can impose maintenance liability even when it does not currently participate in a traversable attack path.

```text
Unused Library
+ No Reachable Execution Path
= Low Immediate Attack Utility
```

The library may still generate:

```text
CVE Triage
+ Patch Evaluation
+ Regression Testing
+ Exception Documentation
+ Future CVE Triage
```

If unnecessary, deletion eliminates both its potential contribution to future attack paths and its recurring maintenance obligations.

```text
Path Erasure Reduces Adversary Capability
State Erasure Reduces Defender Obligation
```

Often the same subtractive change accomplishes both.

# Relationship to the Attacker Optionality Principle

The Attacker Optionality Principle seeks to minimize the number and diversity of viable transitions available to an adversary. Maintenance Surface examines the same retained states from the defender's perspective.

Unnecessary components can simultaneously provide additional attacker options, vulnerability opportunities, configuration states, dependencies, patch requirements, compatibility relationships, and governance obligations.

```text
Attacker Optionality Down
+
Maintenance Surface Down
```

The architectural objective is not merely fewer alerts. It is fewer unnecessary things capable of producing alerts or attacker options in the future.

## Graph Effect of State Pruning

Let the attack-path graph be:

```text
G = (V,E)
```

For an unnecessary node `v in V`, architectural deletion produces a new graph:

```text
V' = V - {v}
E' = E - {(u,v), (v,w)} for all incident executable edges
G' = (V',E') = G - v
```

Let:

```text
P_v = {p in P : v is part of p}
```

Then:

```text
G' = G - v
=> traversable paths through v in G' = empty set
=> P_v is erased from the resulting path set
```

This provides a direct relationship between defender-side Maintenance Surface and attacker-side graph structure:

```text
Maintenance State Removed
-> Node and Incident Edges Pruned from G
-> Dependent Paths Erased
-> Attacker Optionality Reduced
```

Not every Maintenance Surface reduction necessarily changes attacker optionality. Consolidating benign build processes may reduce defender burden without changing adversary reachability. Where a deleted state participates in traversable paths, Maintenance Surface reduction becomes a physical mechanism for reducing path density and attacker choice.

# Relationship to the Assumption Burden Principle

Maintenance Surface increases Assumption Burden by increasing the number of components and relationships that must remain correctly configured, patched, compatible, observable, and supported.

Each retained technical state may add assumptions such as:

```text
Component Remains Supported
-> Dependency Remains Compatible
-> Configuration Remains Correct
-> Patch Is Available
-> Patch Does Not Break Functionality
-> Telemetry Remains Accurate
-> Inventory Remains Current
-> Exception Remains Valid
```

## Maintenance Assumptions and Tail Risk

Let each retained component introduce one or more operational assumptions `A_i`, each with probability `P_i` of remaining valid over a defined operating interval. Under the simplifying assumption that all required assumptions are independent, chain reliability is:

```text
R_chain = product(P_i), for i = 1..n
```

and chain failure probability is:

```text
P_chain_failure = 1 - R_chain
```

This is a reliability abstraction, not a calibrated cyber-loss model. Real assumptions may be correlated, conditional, time-varying, or dormant until architecture or reachability changes.

The structural implication remains important: every unnecessary retained component keeps additional non-zero maintenance assumptions alive. Over extended time horizons, upstream supply-chain changes, newly discovered vulnerabilities, configuration drift, support expiration, identity changes, or reachability changes can convert previously low-consequence assumptions into contributors to high-consequence attack paths.

Maintenance Surface contributes to tail risk not because every retained component is presently exploitable, but because retained state preserves future opportunities for maintenance failure and path composition. Deletion removes the state and the assumptions uniquely attributable to maintaining it.

```text
More Retained State
-> More Maintenance Dependencies
-> More Continuing Assumptions
-> More Opportunities for Future Composition

Less Retained State
-> Fewer Maintenance Dependencies
-> Lower Continuing Assumption Burden
-> Fewer Opportunities for Future Composition
```

# Relationship to Fat-Tailed Cyber Risk

Many individual defects or control failures produce little material consequence. Occasionally, defects, privileges, trust relationships, reachability, maintenance failures, and adversary actions compose into outcomes whose impact is radically disproportionate to any individual condition.

```text
Dormant Dependency
-> New Upstream Vulnerability
-> Changed Reachability
-> Missed Detection
-> Credential
-> Privilege
-> Critical System
-> Impaired Recovery
-> Ransomware
```

Maintenance Surface preserves the states and assumptions that can participate in future compositions. Subtractive Security does not attempt to estimate precisely which retained state will become consequential. It reduces the number of unnecessary states capable of participating in the tail event.

# Relationship to the Hierarchy of Efficacy

The Hierarchy of Efficacy establishes:

```text
Architectural Deletion
-> Architectural Constraint
-> Monitoring & Detection
```

## Level 1 - Architectural Deletion

Deletion eliminates retained state and future maintenance obligations uniquely attributable to it.

Examples:

- remove an unused package,
- remove an obsolete runtime,
- delete a dormant service account,
- retire a legacy protocol,
- remove a redundant base-image variant,
- decommission an unnecessary service.

```text
Current Liability -> Removed
Future State-Specific Maintenance -> Removed
```

## Level 2 - Architectural Constraint

Constraint preserves necessary state while reducing its usable scope.

Examples include reducing permissions, restricting egress, standardizing runtimes, constraining service-account access, pinning supported dependencies, and reducing API reachability.

```text
Required Capability -> Preserved
Maintenance Complexity -> Reduced or Bounded
```

## Level 3 - Monitoring & Detection

Monitoring observes retained technical state through vulnerability scanning, EDR, SIEM, configuration monitoring, dependency monitoring, or continuous control validation.

```text
State -> Remains
Maintenance Obligation -> Remains
Potential Problem -> More Observable
```

> Delete unnecessary obligations first. Constrain necessary obligations second. Monitor the residual state that must remain.

# The Exception Expiry Trap

Security exceptions are frequently treated as low-cost administrative resolutions for vulnerabilities or configurations that cannot currently be remediated, are assessed as unreachable, or are covered by compensating controls.

An exception is not free.

> An active security exception is a maintenance debt instrument.

While the underlying state remains, the exception may require recurring:

- ownership validation,
- risk reassessment,
- compensating-control validation,
- expiration review,
- reapproval or rejustification,
- evidence retention,
- audit defense,
- ticket and GRC workflow maintenance.

```text
Unnecessary State Retained
-> Exception Created
-> Exception Expires
-> Reassessment
-> Rejustification
-> Reapproval
-> Exception Retained
-> Cycle Repeats
```

If the underlying state is legitimately required, recurring governance work may be justified. If unnecessary, repeated renewal converts a removable technical condition into permanent administrative labor.

```text
Unnecessary State Deleted
-> Underlying Exception Condition Removed
-> Exception Closed
-> Future State-Specific Rejustification Eliminated
```

Where safe and functionally valid, deletion retires both the technical exposure and its associated exception ledger. GRC and audit functions therefore have a direct interest in Maintenance Surface reduction, not merely in documenting residual risk.

# Vulnerability Prioritization Is Not Liability Elimination

Risk-based vulnerability prioritization is necessary when remediation demand exceeds engineering capacity. Exploitability analysis, reachability analysis, threat intelligence, EPSS, VEX, CVSS, asset criticality, and compensating-control analysis can improve decisions about which vulnerability should be addressed first.

> Prioritization determines which liability deserves attention first. It does not necessarily remove the liability-producing state.

```text
Critical CVE
-> Function Not Reachable
-> Immediate Exploitability Low
-> Deprioritize or Accept
```

This can be the correct immediate risk decision. But if the package is unnecessary, the stronger architectural question is:

```text
Why Retain the Package?
```

Deletion can remove the current vulnerability, future vulnerabilities unique to the package, future triage, patch evaluation, regression testing, exception management, and potential future attack-path contribution.

Prioritization optimizes the queue. Subtraction reduces the queue's future source population.

# Example: The Harmless Vulnerability

A software composition analysis tool identifies a critical vulnerability in a deeply nested utility included in a production container image. Engineering analysis establishes that the vulnerable function is not reachable.

Determining this may still require:

1. Security to analyze the finding and call path.
2. Engineering to determine why the dependency exists.
3. DevOps to validate runtime packaging and dependency relationships.
4. GRC to document the disposition or exception.
5. Future scanners to reassess the package when new vulnerabilities are published.

If the utility has no legitimate runtime purpose, declaring the CVE unreachable solves only today's vulnerability decision.

```text
Unreachable CVE + Retained Package
-> Current Risk Disposition Complete
-> Maintenance Liability Persists

Package Deleted
-> Current CVE Removed
-> Package-Specific Future CVEs Removed
-> Package-Specific Triage Removed
-> Package-Specific Patch Burden Removed
-> Package-Specific Exception Ledger Removed
```

The security, engineering, and governance benefits arise from the same architectural subtraction.

# The Maintenance Surface Matrix

| Attack Surface | Maintenance Surface | Interpretation |
|---|---|---|
| High | High | Necessary capability requiring strong discipline, or an urgent subtraction candidate if unnecessary |
| High | Low | Minimal but exposed capability; reduce reachability and instrument the residual |
| Low | Low | Preferred state for minimal, well-contained required functionality or deleted unnecessary capability |
| Low | High | Maintenance-heavy state with little immediate attacker utility; strong simplification candidate |

The low-attack/high-maintenance quadrant is susceptible to neglect because immediate security risk appears low while recurring engineering and governance cost remains high.

# Platform Standardization as Maintenance Surface Reduction

Local freedom can produce global maintenance complexity through bespoke container images, multiple runtime versions, duplicative libraries, ungoverned package selection, unique CI/CD patterns, one-off architectures, and inconsistent configuration models.

At enterprise scale, variation multiplies patch combinations, regression permutations, compatibility questions, exceptions, audit evidence, detection logic, and support paths.

```text
12 Bespoke Runtime Images
-> 12 Patch, Test, and Support Variants

2 Centrally Maintained Minimal Images
-> 2 Supported Variants
```

The exact engineering savings depend on the environment. The reduction in maintained variants is directly observable.

# Maintenance Surface and Container Hardening

General-purpose base images often include tools and packages unrelated to application function. Candidate reductions may include package managers, compilers, shells, debugging utilities, language tooling, OS packages, network utilities, unused libraries, excessive Linux capabilities, and writable filesystem locations.

Removal SHOULD be validated against Minimum Functional State.

```text
Minimal Image
-> Fewer Packages to Inventory
-> Fewer Packages to Patch
-> Fewer CVEs to Triage
-> Fewer Runtime Capabilities
-> Fewer Potential Attack Transitions
-> Smaller Regression Scope
```

The purpose is not minimalism as aesthetics. It is to retain only the runtime capability the application legitimately requires.

# Maintenance Surface Metrics

No single metric is sufficient across all technology domains. Organizations MAY use:

## Component Count

```text
Total Maintained Components
```

## Unused Component Ratio

```text
UCR = Unnecessary or Unused Components / Observed Components
```

The denominator and observation period MUST be defined.

## Maintenance Surface Reduction Rate

```text
MSRR = Maintenance Elements Removed / Eligible Maintenance Elements
```

Eligibility MUST be based on evidence that an element is unnecessary or can be consolidated without violating Minimum Functional State.

## Class 0 Remediation Rate

```text
C0RR = Vulnerabilities or Issue Classes Resolved Through Deletion
       / Remediated Vulnerabilities or Issue Classes
```

The counting unit MUST be defined.

## Exception Retirement Rate

```text
ERR = Exceptions Permanently Closed Through State Elimination
      / Exceptions Eligible for Structural Retirement
```

## Platform Convergence

```text
Paved-Road Adoption = Workloads on Supported Standard Platforms
                      / Eligible Workloads
```

# Measurement Caveats

Maintenance Surface metrics MUST NOT reward deletion that breaks legitimate functionality. Metrics SHOULD account for business criticality, emergency use, seasonal behavior, recovery requirements, legal retention, shared dependencies, incomplete telemetry, and unsupported discovery windows.

Raw component count is not itself a risk metric. Maintenance Surface measurement identifies obligations and trends. It does not imply that all components carry equal cost or risk.

# Engineering Requirements

Organizations implementing this principle SHOULD:

1. Inventory maintained technical states within scope.
2. Establish behavioral and functional baselines before deletion.
3. Define Minimum Functional State.
4. Identify states with no demonstrated legitimate requirement.
5. Evaluate attack contribution, maintenance obligation, continuing assumptions, and exception burden.
6. Prefer deletion when unnecessary state can be safely removed.
7. Prefer consolidation and constraint when function must remain.
8. Standardize platform layers where doing so reduces unnecessary variation.
9. Use monitoring and vulnerability prioritization for residual states.
10. Measure maintenance-state reduction and exception retirement.
11. Recalculate attack-path reachability after deleting graph-participating states.
12. Validate that subtraction did not violate functional, recovery, safety, or compliance requirements.
13. Reassess need as business requirements and technology change.

# Validation Questions

Teams SHOULD ask:

- Why does this component exist?
- What legitimate function requires it?
- What evidence demonstrates that requirement?
- What recurring work exists because it remains?
- Which assumptions must remain valid while it exists?
- What vulnerability, testing, compatibility, exception, and audit obligations does it create?
- What attacker capability or optionality does it add?
- Which paths traverse this state?
- What paths disappear if it is deleted?
- Could its function be provided by an already-supported platform component?
- Can it be eliminated?
- If not, can its scope be constrained?
- If retained, is it included in required maintenance and monitoring?
- What future work and governance debt disappear if it is deleted today?

# Strategic Interpretation

A portion of vulnerability-management demand is generated by architectural state that the organization has chosen, intentionally or unintentionally, to retain. The long-term capacity problem cannot always be solved by processing findings faster.

```text
Reactive Model:
More Findings
-> More Triage
-> More Prioritization
-> More Patching
-> More Exceptions

Subtractive Model:
Discover Requirement
-> Delete Unnecessary State
-> Consolidate Required State
-> Retire Associated Exceptions
-> Reduce Future Finding Sources
-> Apply Triage and Patching to Residual State
```

The objective is not to out-patch vulnerability generation. It is to reduce unnecessary vulnerability-generating and maintenance-generating state.

# Relationship to Engineering Capacity

Reducing unnecessary Maintenance Surface can return capacity consumed by repetitive vulnerability triage, low-value patching, dependency conflicts, compatibility testing, bespoke platform support, exception management, configuration drift, audit evidence, and operational troubleshooting.

Recovered capacity SHOULD be measured empirically rather than assumed. Useful measures include:

```text
Engineering Hours Avoided
Patch and Test Cycles Avoided
Exceptions Retired
Runtime Variants Retired
Issue Classes Eliminated
Recurring Findings Eliminated
```

# Relationship to Security Outcomes

Today's low-risk retained component can become tomorrow's attack-path edge when new vulnerabilities are discovered, reachability changes, permissions drift, identities are compromised, compensating controls fail, or formerly safe protocols become obsolete.

```text
Minimum Functional State
-> Lower Maintenance Surface
-> Fewer Continuing Assumptions
-> Lower Attack Surface
-> Lower Attacker Optionality
-> Fewer Eligible Failure Paths
-> Lower Opportunity for Tail-Risk Composition
```

# Statement of Intent

The Maintenance Surface Principle establishes defender carrying cost as an explicit security-engineering concern within OWASP Subtractive Security.

The existence of a technical component should not be justified merely because its current vulnerability is unreachable, compensating controls exist, or immediate exploitation probability is low.

> Does this state provide sufficient legitimate value to justify its continuing security, engineering, operational, governance, and assumption burden?

If not, deletion SHOULD be preferred where technically and operationally safe.

# Summary Principle

```text
Attack Surface measures opportunity presented to the attacker.
Maintenance Surface measures obligation retained by the defender.
Assumption Burden measures what must continue going right.
Attacker Optionality measures useful choices available to the adversary.
Minimum Functional State defines what the business actually needs.
Deletion eliminates unnecessary attacker capability and defender obligation.
Constraint bounds what must remain.
Monitoring and prioritization manage the residual.
```

> The strongest vulnerability-management improvement may not be finding a faster way to patch a component. It may be proving that the component does not need to exist.
