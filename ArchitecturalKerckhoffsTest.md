# OWASP Architectural Kerckhoffs Test Standard

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Governance Area:** Architecture Validation, Adversarial Disclosure & Evidence-Based Security  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

## Executive Summary

The OWASP Architectural Kerckhoffs Test Standard provides deterministic engineering guidance for evaluating whether an enterprise architecture depends upon secrecy, adversary confusion, incomplete reconnaissance, or hidden complexity for its security.

Kerckhoffs's Principle holds that a system should remain secure even when its design is known to the adversary. Claude Shannon later condensed the principle into the adversarial assumption **the enemy knows the system.**

Enterprise cybersecurity frequently claims to reject security through obscurity while continuing to depend upon hidden network routes, undocumented trust relationships, unindexed identities, obscure service dependencies, legacy protocols, administrative pathways, and architectural complexity. These hidden paths may slow human reconnaissance, but they remain traversable once discovered.

The Architectural Kerckhoffs Test evaluates a narrower and falsifiable claim:

> Does complete architectural knowledge materially increase adversary capability beyond the operational paths already required by the business?

An architecture passes the test when disclosure of its topology, identity relationships, service inventory, trust boundaries, configurations, and control model does not reveal material new opportunities for adversary progression because non-essential attack paths have already been erased and essential paths remain strictly constrained.

The objective is not to prove universal invulnerability. The objective is to determine whether resilience derives from structural properties or from the adversary's temporary ignorance.

## Core Proposition

Security should derive from system geometry, enforced constraints, and eliminated attack paths, not from the assumption that the adversary will fail to understand the environment.

Under this model:

```text
Architectural Secrecy != Architectural Security
Knowledge of a Path != Ability to Traverse the Path
Path Erasure = Disclosure Resilience
```

Knowledge of terrain is only useful if viable roads exist to traverse.

## Formal Definition

### Architectural Kerckhoffs Test

The Architectural Kerckhoffs Test is a controlled evaluation of whether full or near-full disclosure of an architecture materially increases an adversary's ability to reach unauthorized states, cross trust boundaries, expand privilege, move laterally, establish persistence, exfiltrate data, disrupt operations, or produce material business impact.

An architecture passes the test when disclosure of the declared architectural model does not materially increase attacker capability because:

- non-essential attack paths have been eliminated,
- required paths are constrained to explicit operational invariants,
- trust relationships are minimized and bounded,
- standing privilege and reusable credentials are reduced,
- control-plane access is isolated,
- execution and egress paths are deterministic,
- and residual paths are explicitly governed and monitored.

### Declared Disclosure Set

Let:

```text
D = the architectural information disclosed to the evaluator
```

The disclosure set may include:

- network topology,
- routing and segmentation models,
- identity and role relationships,
- privilege assignments,
- trust relationships,
- service and asset inventories,
- data flows,
- administrative pathways,
- cloud account and subscription structures,
- infrastructure-as-code definitions,
- container and orchestration manifests,
- application dependency graphs,
- CI/CD relationships,
- external integrations,
- security control locations,
- and documented exceptions.

### Capability Sets

Let:

```text
C_prior = attacker capabilities identified before architectural disclosure
C_post  = attacker capabilities identified after architectural disclosure
```

The Architectural Disclosure Delta is:

```text
ADD = C_post - C_prior
```

Where `ADD` represents material attacker capabilities, traversable paths, or unauthorized state transitions newly identified because of architectural disclosure.

A resilient architecture seeks:

```text
ADD -> empty set
```

The test does not require the adversary to learn nothing. It requires that additional knowledge produce little or no material increase in executable attacker capability.

## Distinguishing Vulnerabilities from Architectural Disclosure Risk

The Architectural Kerckhoffs Test does not assert that applications, operating systems, services, or devices contain no vulnerabilities.

A zero-day vulnerability is a local defect. Architectural disclosure risk exists when knowledge of the environment reveals conductive relationships that allow a local defect to compose into broader compromise.

```text
Local Defect
     +
Disclosed Non-Essential Path
     =
Expanded Attacker Capability
```

Examples include:

- a development system with unnecessary routes to a production datastore,
- a dormant role capable of assuming a privileged cross-account identity,
- a legacy peering relationship that bypasses intended segmentation,
- an administrative interface reachable from a user network,
- an unused dependency that preserves an unnecessary execution path,
- or a standing credential that converts local compromise into durable privilege.

These are architectural defects whose security depends partly upon remaining undiscovered.

## Relationship to Attack Path Failure Mode Theory

Attack Path Failure Mode Theory establishes that a local defect becomes material only when a traversable path allows it to compose into an unauthorized state transition.

The Architectural Kerckhoffs Test assumes the adversary knows the system graph:

```text
G = (V,E)
```

Where:

```text
V = Assets, Identities, Processes, Services, Workloads, Networks, Applications, and Data Stores
E = Execution, Trust, Reachability, Authentication, Authorization, Privilege, Control, Physical, Human, or Data-Flow Relationships
```

The test asks whether disclosure of `G` exposes executable edges whose protection depended upon the adversary not identifying them.

A disclosed edge is not itself a failure. A disclosed edge becomes material when it enables an unauthorized path from an adversary-accessible state to an impact-producing state.

## Relationship to PER-1.0

The Path Erasure Rate (PER) measures structural attack-path reduction:

```text
PER = P_erased / P_eligible
```

Where:

```text
P_eligible = identified non-essential attack paths within the declared scope
P_erased   = eligible attack paths rendered non-traversable
```

PER and the Architectural Kerckhoffs Test are complementary:

- PER measures how many identified non-essential paths have been erased.
- The Architectural Kerckhoffs Test evaluates whether disclosure reveals material residual paths or attacker capabilities that remained protected by obscurity.
- Control validation determines whether claimed path erasure or constraint is real.
- Regression testing determines whether erased paths have reappeared.

A high PER should reduce the Architectural Disclosure Delta, but the relationship must be tested rather than assumed.

## Relationship to the Hierarchy of Efficacy

The Architectural Kerckhoffs Test follows the Subtractive Security Hierarchy of Efficacy.

### Tier 1 - Architectural Deletion

Remove the path completely.

Examples:

- remove unnecessary routes,
- remove unused services,
- remove dormant identities,
- remove standing credentials,
- remove legacy protocols,
- remove unneeded dependencies,
- remove administrative exposure,
- and remove obsolete trust relationships.

A deleted path cannot become more traversable because the adversary learned about it.

### Tier 2 - Architectural Constraint

Where deletion is not feasible, constrain the required path to explicit operational invariants.

Examples:

- narrowly scoped segmentation,
- ephemeral privilege,
- hardware-bound authentication,
- permission boundaries,
- deterministic egress,
- authenticated mediation,
- workload identity,
- and explicit service-to-service authorization.

A constrained path may remain visible, but disclosure should not allow operation outside its approved boundary.

### Tier 3 - Monitoring & Detection

Monitor residual paths that cannot be deleted or sufficiently constrained.

Monitoring may reveal attempted traversal, but it does not make architectural disclosure benign. A detected path remains a path.

```text
Architectural Deletion > Architectural Constraint > Monitoring
```

## Purpose

This standard defines how organizations should design, execute, classify, and repeat tests of architectural disclosure resilience.

The purpose is to:

- identify dependencies on architectural secrecy,
- expose hidden non-essential attack paths,
- evaluate whether knowledge becomes capability,
- challenge architecture and control assumptions,
- convert disclosure findings into path deletion or constraint,
- support PER measurement with adversarial validation,
- reduce dependency on human reconnaissance friction,
- and establish evidence that architecture remains resilient under informed attack.

The goal is not to protect the map.

The goal is to make possession of the map operationally unimportant.

## Guiding Principles

### Assume the Adversary Knows the System

Testing should assume that the adversary possesses accurate and current architectural information within the declared scope.

### Understanding Must Not Equal Access

Architectural comprehension should not create authorization, reachability, privilege, execution, persistence, or impact capability.

### Security Claims Must Be Falsifiable

A claim that an architecture is disclosure-resilient must define the conditions under which that claim would fail.

### Disclosure Is an Input, Not a Breach Outcome

Possession of an architecture diagram, configuration model, or identity graph may improve adversary understanding. The test evaluates whether that understanding produces executable capability.

### Hidden Non-Essential Paths Are Defects

A path that serves no required business function but becomes valuable when discovered is architectural waste and attacker opportunity.

### Human Reconnaissance Friction Is Not a Durable Control

Complexity, poor documentation, naming ambiguity, fragmented ownership, and tribal knowledge may slow human analysis. They should not be treated as structural defenses.

### The Null Result Is the Desired Outcome

A successful test should show that disclosure produces no material new attacker capability, no unauthorized state transition, and no meaningful increase in adversary reachability.

### Validation Must Repeat

Architectures change. New integrations, exceptions, identities, services, dependencies, routes, and privileges can reintroduce disclosure-sensitive paths.

## Scope

This standard applies to architecture validation across:

- enterprise networks,
- endpoints and servers,
- identity systems,
- cloud platforms,
- SaaS platforms,
- applications and APIs,
- datastores,
- container and orchestration platforms,
- CI/CD systems,
- AI systems,
- IoT and operational technology,
- physical and human-mediated paths,
- third-party integrations,
- and hybrid environments.

The standard may be applied during:

- threat modeling,
- architecture review,
- design assurance,
- breach and attack simulation,
- adversary emulation,
- red-team and purple-team exercises,
- penetration testing,
- control validation,
- merger or integration review,
- major platform change,
- and periodic regression testing.

## Architectural Kerckhoffs Test Lifecycle

## AKT01: Declare the System Boundary

### Description

Define the architecture, business function, trust boundaries, and impact-producing target states included in the test.

### Strategic Objective

Prevent ambiguous conclusions by establishing what the test does and does not evaluate.

### Required Inputs

- system or business-service name,
- in-scope assets and identities,
- ingress states,
- high-impact target states,
- trust boundaries,
- operationally required paths,
- excluded systems,
- and rationale for exclusions.

## AKT02: Establish the Disclosure Set

### Description

Define the architectural information available to the evaluator.

### Strategic Objective

Model an adversary with comprehensive environmental understanding rather than relying upon reconnaissance difficulty.

### Required Inputs

- topology and data-flow diagrams,
- route and segmentation definitions,
- identity and privilege models,
- service inventories,
- trust relationships,
- configuration and policy definitions,
- infrastructure-as-code,
- application and dependency models,
- control locations,
- known exceptions,
- and relevant operational documentation.

### Completeness Principle

The test should disclose enough information to remove obscurity as a meaningful variable within the declared scope.

## AKT03: Establish the Prior Capability Baseline

### Description

Document attacker capabilities and known paths before the evaluator receives the disclosure set.

### Strategic Objective

Create a baseline against which the effect of architectural knowledge can be measured.

### Required Outputs

- known attacker ingress states,
- known reachable systems,
- known privilege paths,
- known lateral movement paths,
- known egress paths,
- known impact paths,
- and known constraints.

## AKT04: State the Falsifiable Hypothesis

### Description

Express the architectural security claim in a form capable of failure.

### Required Format

```text
If an adversary receives [declared disclosure set]
for [declared architecture and scope],
then the adversary will not gain [defined material capability]
beyond [declared operational paths and residual risk].
```

### Example

```text
If an adversary receives the complete network topology, identity-role graph,
and cloud routing model for the payment platform,
then no new path from a user-accessible workload to the payment datastore
will become traversable beyond the explicitly approved application flow.
```

## AKT05: Perform Disclosure-Assisted Path Analysis

### Description

Provide the disclosure set to an authorized evaluator and identify paths, capabilities, and unauthorized state transitions that become apparent because of architectural knowledge.

### Strategic Objective

Determine whether the architecture relies upon hidden complexity, undiscovered relationships, or attacker confusion.

### Analysis Questions

- What new assets become identifiable?
- What new routes become apparent?
- What new trust relationships become exploitable?
- What privilege chains become visible?
- What standing credentials or tokens become relevant?
- What control-plane paths become reachable?
- What execution or dependency paths become usable?
- What business-process transitions become abusable?
- What egress or exfiltration paths become available?
- What human-mediated edges remain necessary for progression?

## AKT06: Validate Material Paths

### Description

Validate identified post-disclosure paths through controlled simulation, configuration analysis, reachability testing, adversary emulation, or equivalent reproducible evidence.

### Strategic Objective

Distinguish theoretical graph relationships from executable attacker capability.

### Safety Requirement

Validation must occur only within authorized scope and under appropriate legal, operational, safety, change, and business approvals.

### Evidence Standard

A path should be treated as material when evidence demonstrates that it:

- is traversable,
- crosses an unauthorized boundary,
- expands reach, privilege, persistence, execution, egress, data access, or impact,
- and became identifiable or meaningfully easier to exploit through disclosure.

## AKT07: Calculate the Architectural Disclosure Delta

### Description

Compare attacker capability after disclosure to the prior baseline.

### Model

```text
ADD = C_post - C_prior
```

### Assessment Dimensions

The delta should be evaluated across:

- reachability,
- privilege,
- trust,
- execution,
- credential access,
- persistence,
- lateral movement,
- control-plane access,
- data access,
- egress,
- recovery denial,
- and material business impact.

### Interpretation

The number of disclosed components is not the primary measure. The primary measure is the amount of material attacker capability created or revealed by disclosure.

## AKT08: Classify the Outcome

### Class A - Disclosure Resilient

No material new attacker capability or unauthorized path is validated after disclosure.

The architecture passes within the declared scope.

### Class B - Disclosure Tolerant

Disclosure reveals additional information or limited paths, but existing constraints prevent material expansion of attacker capability or impact.

The architecture conditionally passes, with residual findings governed.

### Class C - Disclosure Sensitive

Disclosure reveals one or more material attack paths, privilege chains, trust relationships, or operational dependencies that increase attacker capability.

The architecture fails and requires remediation.

### Class D - Obscurity Dependent

Material security boundaries depend substantially upon architectural secrecy, attacker confusion, undocumented complexity, or delayed reconnaissance.

The architecture fails and requires prioritized architectural correction.

## AKT09: Apply Architectural Remediation

### Description

Convert disclosure-sensitive findings into structural changes.

### Required Treatment Order

1. Delete the non-essential path.
2. Constrain any path required by the business.
3. Monitor residual risk that cannot be deleted or constrained.
4. Document temporary exceptions and security debt.
5. Retest after remediation.

### Remediation Examples

- remove obsolete routes or peering,
- eliminate dormant roles and identities,
- remove standing privilege,
- delete unused dependencies,
- isolate control planes,
- remove legacy protocols,
- restrict service-to-service paths,
- replace ambient trust with explicit authorization,
- reduce data flows,
- and eliminate unnecessary administrative access.

## AKT10: Retest and Prevent Regression

### Description

Repeat the test after remediation and after material architectural change.

### Revalidation Triggers

- new integrations,
- acquisitions or environment consolidation,
- identity model changes,
- network or cloud topology changes,
- new administrative paths,
- infrastructure-as-code changes,
- container-platform changes,
- major application releases,
- exception approvals,
- control failure,
- incident findings,
- and scheduled validation cycles.

### Strategic Objective

Prevent previously erased paths from being reintroduced and prevent new dependencies on obscurity from accumulating.

## Evidence Requirements

Each test record should include:

- declared scope,
- disclosure set,
- prior capability baseline,
- falsifiable hypothesis,
- analysis method,
- identified pre-disclosure paths,
- identified post-disclosure paths,
- validation method,
- expected result,
- actual result,
- Architectural Disclosure Delta,
- outcome classification,
- supporting evidence,
- remediation actions,
- validation owner,
- test date,
- and revalidation trigger or date.

## Relationship to Adversarial AI

The Architectural Kerckhoffs Test is technology-independent. It does not require artificial intelligence for execution.

However, automated and AI-assisted analysis can reduce the time required to correlate inventories, configurations, identity relationships, routes, manifests, dependencies, and control definitions. As architectural comprehension becomes faster and less expensive, security models that depend upon delayed reconnaissance become less durable.

The test therefore assumes that architectural understanding may be rapid, comprehensive, and repeatable.

The relevant question is not whether the architecture can remain hidden.

The relevant question is whether full understanding materially changes what the adversary can do.

## Human-Edge Reduction

The test is also a mechanism for reducing reliance upon human intervention.

A disclosure-resilient architecture should not depend primarily upon:

- an attacker failing to discover a path,
- an analyst recognizing malicious traversal in time,
- an operator remembering undocumented dependencies,
- an architect holding correct but untested assumptions,
- or an incident responder interrupting progression before impact.

Architectural deletion removes both attacker paths and future human decision points.

```text
Path Deleted
     ↓
No Traversal
     ↓
No Detection Dependency
     ↓
No Human Response Dependency
```

The objective is not to remove humans from governance or engineering. The objective is to remove unnecessary reliance upon timely, flawless human intervention for controls that can be made structural.

## Metrics

Recommended measures include:

- Architectural Disclosure Delta by capability class,
- material post-disclosure paths validated,
- percentage of post-disclosure findings erased,
- percentage of post-disclosure findings constrained,
- percentage of findings remaining detection-dependent,
- validation-driven PER improvement,
- number of obscurity-dependent boundaries identified,
- number of human-mediated edges removed,
- number of paths reintroduced after prior erasure,
- and time since last test of critical architectures.

Metrics should be interpreted within a declared scope. They should not be used to claim universal security or compare dissimilar architectures without normalization and context.

## Success Criteria

The Architecture Kerckhoffs Test succeeds as an engineering process when it:

- gives a defined security claim an opportunity to fail,
- identifies whether architectural knowledge becomes attacker capability,
- validates material findings with reproducible evidence,
- drives deletion or constraint of discovered paths,
- updates PER where path erasure is demonstrated,
- and repeats sufficiently to detect drift and invalid assumptions.

The architecture passes when the declared disclosure set produces no material increase in attacker capability within the declared scope.

## Strategic Objective: Disclosure Resilience

The goal is an architecture whose defensive properties remain effective under complete understanding.

In this model:

```text
Architecture = System Geometry
Disclosure   = Adversary Knowledge
Attack Path  = Executable Opportunity
Constraint   = Bounded Required Function
Deletion     = Removed Opportunity
```

The architecture should not require the adversary to remain confused.

It should require the adversary to confront paths that do not exist and boundaries that remain enforced even when fully understood.

## Statement of Intent

The Architectural Kerckhoffs Test turns anti-obscurity from a slogan into a falsifiable engineering claim.

A secure architecture should not depend upon hidden complexity, undocumented topology, delayed reconnaissance, or an adversary's incomplete understanding.

Every organization makes mistakes and invalid assumptions. The purpose of the test is not to claim perfection. The purpose is to create a repeatable process through which incorrect architectural assumptions become visible before they produce material harm.

**The fundamental question is not whether the adversary knows the architecture. The fundamental question is whether that knowledge changes what the adversary can do.**

## References

- [OWASP Subtractive Hardening Top 10 Project](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main)
- [Path Erasure Rate (PER-1.0) Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md)
- [The Architectural Kerckhoffs Test](https://subtractivesecurity.substack.com/p/the-architectural-kerckhoffs-test)
- OWASP Attack Path Failure Mode Theory
- OWASP Subtractive Security Control Validation Standard
- OWASP Subtractive Security Hierarchy of Efficacy & Assumption Burden Principle
- OWASP Universal Subtractive Security Laws Top 10
- Auguste Kerckhoffs, *La Cryptographie Militaire* (1883)
- Claude Shannon, *Communication Theory of Secrecy Systems* (1949)
- The Science of Silence

_OWASP Architectural Kerckhoffs Test Standard v1.0_
