# OWASP Path Erasure Precedence Standard

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Specification Alignment:** PER-1.0 Path Erasure Rate Engineering Standard  
**License:** Apache License 2.0  

---

## Executive Summary

The OWASP Path Erasure Precedence Standard defines an engineering methodology for determining when and where security-relevant attack paths should be eliminated, constrained, or dynamically interrupted.

Traditional security architectures frequently leave unnecessary capabilities, trust relationships, privileges, services, dependencies, and communication paths intact, then compensate for their continued existence through monitoring, detection, or runtime response.

Subtractive Security establishes a different engineering priority:

> **An unnecessary adversary-capable state transition should be erased at the earliest feasible point in time and the lowest feasible architectural layer consistent with required system functionality.**

This is the **Path Erasure Precedence Principle**.

The standard distinguishes three temporal forms of path erasure:

1. Preventive Subtraction
2. Reactive Subtraction
3. Corrective Subtraction

It further establishes a preference for permanent structural erasure over dynamic constraint when equivalent required functionality can be maintained.

The objective is not to eliminate reactive security controls.

The objective is to reserve reactive controls for residual paths that cannot reasonably be eliminated or structurally constrained.

---

## 1. Purpose

The purpose of this standard is to establish repeatable criteria for:

- determining whether a security-relevant state transition is necessary;
- selecting the earliest feasible point at which an unnecessary transition can be erased;
- selecting the lowest feasible architectural layer at which erasure can occur;
- distinguishing permanent structural erasure from dynamic interruption;
- identifying the assumption burden associated with runtime enforcement;
- verifying that claimed path erasure has occurred; and
- moving security interventions from corrective and reactive mechanisms toward preventive structural outcomes.

This standard does not prohibit monitoring, detection, dynamic response, or autonomous enforcement.

It establishes the order in which architectural deletion, constraint, reactive intervention, corrective remediation, and monitoring should be considered.

---

## 2. Scope

This standard applies to security-relevant system elements and transitions, including:

- network reachability;
- identity and privilege relationships;
- credentials and tokens;
- trust relationships;
- process execution;
- software dependencies;
- services and protocols;
- administrative capabilities;
- interfaces and APIs;
- data access and transfer paths;
- workload communication;
- delegation relationships;
- external integrations;
- runtime capabilities; and
- other attacker-traversable state transitions.

The standard may be applied during:

- system design;
- threat modeling;
- architecture review;
- software development;
- build and deployment;
- infrastructure provisioning;
- security testing;
- control validation;
- vulnerability remediation;
- incident response;
- post-incident review; and
- continuous improvement.

---

## 3. System Model

A system MAY be represented as a directed graph:

\[
G = (V,E)
\]

Where:

- \(V\) represents system states, identities, workloads, services, resources, processes, interfaces, or other security-relevant entities.
- \(E\) represents executable transitions between those entities, including network reachability, privilege, trust, execution, dependency, communication, credential, or delegation relationships.

An attack path is a sequence of traversable edges:

\[
P = (e_1, e_2, \ldots, e_n)
\]

Path erasure occurs when one or more required executable transitions are removed such that the defined path is no longer traversable.

For a specified transition \(e_{ij}\), verified deletion of \(e_{ij}\) eliminates traversal through that transition within the defined system model.

This statement applies to the scoped transition or path. It does not imply that every possible attack path within the larger system has been eliminated.

---

## 4. Definitions

### 4.1 Attack Path

A sequence of executable state transitions that enables an adversary to move from an initial state to a defined security-relevant outcome.

### 4.2 Eligible Path

An identified attack path that is within the defined assessment scope and is technically or operationally eligible for deletion or constraint.

### 4.3 Path Erasure

The removal of one or more executable transitions required for traversal of a specified attack path.

### 4.4 Structural Erasure

The permanent removal of the capability, relationship, component, dependency, or architectural condition that makes a specified transition possible.

### 4.5 Architectural Constraint

A persistent boundary that prevents or limits traversal while some portion of the underlying capability remains present.

### 4.6 Dynamic Constraint

A control that conditionally prevents or interrupts a transition through active runtime observation, decision, authorization, or enforcement.

### 4.7 Preventive Subtraction

Path erasure completed before the specified transition becomes available for adversary traversal.

### 4.8 Reactive Subtraction

Path erasure or interruption performed during attempted or observed traversal.

### 4.9 Corrective Subtraction

Path erasure performed after successful traversal, compromise, persistence, exfiltration, or other security impact.

### 4.10 Required Functionality

Functionality that has a defined, current, authorized, and validated operational purpose.

Historical presence, administrative convenience, anticipated future use, or lack of ownership SHALL NOT by themselves establish that functionality is required.

### 4.11 Control Plane

The collection of systems, services, telemetry, communications, identities, credentials, decision logic, and enforcement mechanisms required to administer or dynamically control a security-relevant transition.

### 4.12 Assumption Burden

The set of conditions that must remain true for a security mechanism to produce and sustain its intended security outcome.

---

## 5. Path Erasure Precedence Principle

The fundamental principle of this standard is:

> **Subtraction SHOULD occur at the earliest point in time and lowest architectural layer at which required functionality permits it.**

Two dimensions govern path-erasure precedence:

1. **Temporal Precedence:** When can the path be removed?
2. **Architectural Precedence:** At what layer can the condition enabling the path be removed?

Security engineering SHOULD move path erasure earlier in time and deeper into the architecture whenever doing so preserves required system functionality.

Where multiple mechanisms preserve equivalent required functionality and produce equivalent attack-path reduction, the mechanism with the lowest continuing assumption burden SHOULD be preferred.

---

## 6. Temporal Classes of Path Erasure

### 6.1 Preventive Subtraction

**Temporal State:** Before adversary traversal is possible.

Preventive subtraction removes an unnecessary state transition before it becomes available for exploitation.

Examples include:

- removing unused services before deployment;
- removing unnecessary network routes;
- eliminating unused identities or privileges;
- removing compilers or interpreters from production workloads where they are not required;
- removing unnecessary outbound connectivity;
- eliminating obsolete trust relationships;
- removing unnecessary administrative interfaces; and
- omitting unnecessary software dependencies from production artifacts.

Preventive subtraction is preferred because successful defense does not depend upon detection of traversal, classification of adversary behavior, or successful intervention after execution begins.

Verified preventive structural erasure does not require a runtime control plane to continuously prevent traversal through the erased transition. The transition is absent by construction.

### 6.2 Reactive Subtraction

**Temporal State:** During attempted or observed traversal.

Reactive subtraction leaves an edge available during normal operation and attempts to remove, disable, or interrupt it when malicious activity is detected.

Examples include:

- terminating a malicious process;
- dynamically isolating an endpoint;
- revoking an active credential or token;
- terminating an active network connection;
- dynamically modifying a firewall rule; and
- disabling an account following detected misuse.

Reactive subtraction MAY be necessary when the underlying transition is required for legitimate operation and cannot reasonably be removed in advance.

#### Control-Plane Dependency and Assumption Burden

Reactive subtraction relies on an active runtime control plane, such as an identity broker, telemetry agent, orchestration API, policy engine, or other enforcement mechanism.

Its effectiveness therefore depends upon the continued availability, integrity, authorization, and timely operation of the systems required to:

1. observe the transition;
2. collect and transmit relevant telemetry;
3. determine that intervention is necessary;
4. authorize the intervention;
5. communicate the decision; and
6. execute the response before material impact occurs.

If the control plane, its telemetry, its communication paths, or its authorization credentials are compromised, unavailable, delayed, or degraded, reactive subtraction capabilities may themselves be degraded or blinded.

Under the **Assumption Burden Principle**, each dependency introduces an additional condition that must remain true for the security mechanism to succeed.

Reactive subtraction therefore carries a greater continuing assumption burden than verified preventive structural erasure.

Preventive structural erasure carries no equivalent ongoing control-plane dependency for the erased transition because the transition is absent by construction. No runtime system must continuously observe, classify, authorize, or interrupt traversal through an edge that does not exist.

Reactive subtraction SHOULD NOT substitute for preventive structural erasure when equivalent required functionality can be maintained without the underlying attack path.

### 6.3 Corrective Subtraction

**Temporal State:** After successful traversal or security impact.

Corrective subtraction removes a path after exploitation, compromise, persistence, exfiltration, or other security-relevant activity has already occurred.

Examples include:

- removing persistence discovered during incident response;
- revoking credentials following confirmed compromise;
- removing an exposed service following exploitation;
- eliminating an unnecessary trust relationship identified during post-incident review;
- rebuilding a compromised system without the exploited capability; and
- removing vulnerable functionality after exploitation demonstrates that it is not operationally necessary.

Corrective subtraction SHOULD generate an engineering review to determine whether the same path can subsequently be eliminated preventively.

Repeated corrective subtraction of the same class of path SHOULD trigger review of the architecture, deployment process, or operational requirement responsible for recreating the path.

---

## 7. Architectural Classes of Intervention

Path erasure SHOULD be evaluated according to the architectural layer at which the enabling condition exists.

Possible interventions include:

1. detecting use of the vulnerable behavior;
2. interrupting the vulnerable behavior;
3. constraining the capability enabling the behavior;
4. removing the capability enabling the behavior;
5. removing the component providing the capability;
6. removing the dependency requiring the component; or
7. removing the architectural relationship that created the dependency.

Where multiple approaches preserve equivalent required functionality, the approach that eliminates the enabling condition at the lowest feasible architectural layer SHOULD be preferred.

### Example: Unauthorized Shell Execution

Consider unauthorized shell execution within a production workload.

#### Monitoring

Detect and alert upon malicious shell execution.

#### Reactive Subtraction

Detect malicious shell execution and terminate the process.

#### Architectural Constraint

Prevent shell execution through an enforced execution policy.

#### Structural Erasure

Remove the shell from the production workload.

#### Deeper Structural Erasure

Remove the architectural dependency that caused a shell-capable component to exist.

The preferred intervention is the lowest feasible architectural layer that preserves required application functionality.

---

## 8. Normative Requirements

### PEPS-1: Necessity

Security-relevant state transitions that are not required for defined system functionality SHOULD be eliminated.

The continued existence of an unnecessary path SHOULD NOT be justified solely by:

- monitoring;
- logging;
- detection;
- alerting;
- response capability;
- historical presence;
- administrative convenience; or
- hypothetical future use.

System owners SHOULD document the required functionality supported by retained security-relevant transitions.

### PEPS-2: Temporal Precedence

Path erasure SHOULD occur at the earliest lifecycle stage at which required system functionality permits the transition to be removed.

Where the same unnecessary path can be eliminated before deployment or dynamically removed during attack, preventive elimination SHOULD be preferred.

### PEPS-3: Architectural Precedence

Path erasure SHOULD occur at the lowest architectural layer at which required functionality permits elimination.

Where practical, engineering teams SHOULD remove the condition that creates an unnecessary path rather than repeatedly controlling its downstream manifestations.

### PEPS-4: Structural Preference

Permanent structural erasure SHOULD be preferred to dynamic constraint when both approaches satisfy equivalent functional requirements.

Dynamic controls SHOULD primarily govern residual paths that cannot reasonably be eliminated.

The selection of a dynamic control SHOULD account for the additional assumption burden introduced by its required telemetry, decision, authorization, communication, and enforcement dependencies.

Where two mechanisms preserve equivalent required functionality and attack-path reduction, the mechanism with the lower continuing assumption burden SHOULD be preferred.

### PEPS-5: Reactive Subordination

Reactive subtraction SHOULD be applied to residual transitions that cannot reasonably be eliminated preventively or structurally constrained.

Reactive security SHALL NOT be considered equivalent to verified structural path erasure.

The use of reactive subtraction SHOULD identify:

- the transition being dynamically controlled;
- the reason the transition cannot be preventively erased;
- the runtime control plane responsible for intervention;
- the telemetry required to detect attempted traversal;
- the authority required to execute the response;
- the maximum acceptable intervention delay;
- the expected result of successful intervention; and
- the consequences of control-plane failure, degradation, compromise, or unavailability.

This documentation SHOULD make the reactive mechanism’s assumption burden explicit and testable.

### PEPS-6: Corrective Feedback

A path erased following successful exploitation, incident response, or post-event remediation SHOULD be evaluated for conversion into preventive structural erasure.

Repeated reactive or corrective deletion of the same class of path SHOULD trigger review of the architectural condition responsible for recreating the path.

### PEPS-7: Verification

Claims of structural path erasure SHOULD be validated by demonstrating that the specified transition is no longer traversable within the defined system model.

Evidence that a traversal attempt was:

- detected;
- alerted upon;
- logged;
- dynamically blocked; or
- terminated after initiation

SHALL NOT by itself constitute evidence that the underlying path has been structurally erased.

### PEPS-8: Scope Definition

Path-erasure claims SHOULD identify:

- the system boundary;
- the affected vertices or entities;
- the transition or path being evaluated;
- the initial state;
- the prohibited destination or outcome;
- the required functionality being preserved;
- the evidence used to validate non-traversability; and
- known out-of-scope paths or alternative transitions.

A scoped erasure claim SHALL NOT be represented as proof that the entire system is invulnerable or that all possible paths have been removed.

### PEPS-9: Regression Resistance

Verified path erasure SHOULD be protected against unintended reintroduction.

Where applicable, organizations SHOULD use architecture review, configuration validation, deployment controls, testing, or other appropriate mechanisms to verify that erased transitions have not been recreated.

Controls used to prevent regression SHALL NOT be treated as substitutes for the underlying structural erasure.

### PEPS-10: Residual Path Governance

Paths that cannot reasonably be erased SHOULD be:

- explicitly identified;
- justified by required functionality;
- reduced to the minimum necessary scope;
- constrained where feasible;
- assigned an accountable owner;
- tested against defined failure conditions; and
- periodically reevaluated for earlier or deeper subtraction.

---

## 9. Subtractive Order of Preference

Where required system functionality permits, the order of preference is:

1. **Preventive Structural Erasure**
2. **Preventive Architectural Constraint**
3. **Reactive Subtraction**
4. **Corrective Subtraction**
5. **Monitoring Without Path Reduction**

This ordering does not imply that lower-order mechanisms are unnecessary.

Lower-order mechanisms remain necessary for residual paths that cannot reasonably be eliminated at higher levels. The hierarchy establishes engineering precedence, not exclusivity.

The ordering also reflects increasing assumption burden.

Preventive structural erasure requires verification that the specified transition has been removed.

Reactive subtraction additionally requires successful:

- observation;
- telemetry;
- classification;
- communication;
- authorization;
- orchestration;
- enforcement; and
- intervention before material impact occurs.

Corrective subtraction further assumes that effective remediation remains possible after successful traversal or security impact.

Moving path erasure earlier in time and deeper into the architecture generally reduces the number of conditions that must remain true for the defense to succeed.

---

## 10. Decision Methodology

For each identified security-relevant transition, engineering teams SHOULD ask:

1. Is the transition required for defined system functionality?
2. What current and validated operational requirement does it satisfy?
3. If it is not required, can the transition be eliminated?
4. Can it be eliminated before deployment or exposure?
5. What architectural component creates the transition?
6. Can the enabling capability itself be removed?
7. Can the component providing that capability be removed?
8. Can the dependency requiring that component be removed?
9. Can the architectural relationship creating the dependency be removed?
10. If structural erasure is not feasible, can the transition be architecturally constrained?
11. If the transition must remain available, what reactive mechanism governs the residual risk?
12. What telemetry, identity, authorization, communication, orchestration, or enforcement dependencies must remain trustworthy and available for that mechanism to succeed?
13. What happens if any of those dependencies are delayed, degraded, compromised, or unavailable?
14. Can the same security outcome be achieved with fewer continuing assumptions?
15. If the path has previously been exploited, can corrective remediation be moved earlier in the lifecycle?
16. How will erasure be validated?
17. How will unintended path reintroduction be identified?

The analysis SHOULD prefer:

- the earliest feasible temporal intervention;
- the lowest feasible architectural intervention; and
- the mechanism with the lowest continuing assumption burden.

---

## 11. Implementation Examples

### 11.1 Network Egress

Consider a production workload that does not require direct Internet egress.

#### Monitoring

Monitor outbound connections and alert when suspicious destinations are observed.

The path remains traversable.

#### Reactive Subtraction

Detect suspicious outbound communication and terminate the connection or dynamically isolate the workload.

The path exists until intervention succeeds.

Successful defense depends upon observation, classification, communication, authorization, and timely enforcement.

#### Preventive Architectural Constraint

Restrict outbound connectivity to explicitly required destinations.

The reachable state space is reduced, but approved egress paths remain.

#### Preventive Structural Erasure

Remove direct Internet egress from the workload when no business requirement exists for it.

The unnecessary transition is no longer traversable.

Under Path Erasure Precedence, preventive structural erasure is preferred when required functionality permits it.

### 11.2 Production Execution Capability

Consider a production workload containing a compiler that is not required during runtime.

#### Monitoring

Monitor compiler invocation and alert upon suspicious use.

#### Reactive Subtraction

Detect unauthorized compiler execution and terminate the process.

#### Preventive Architectural Constraint

Apply an execution policy that prevents the compiler from running.

#### Preventive Structural Erasure

Remove the compiler and associated toolchain from the production artifact.

#### Deeper Structural Erasure

Modify the build and deployment architecture so that compilation occurs only within a dedicated build environment and compiler-bearing artifacts cannot enter production.

The deeper structural intervention removes both the immediate capability and the deployment relationship capable of recreating it.

### 11.3 Privileged Identity

Consider an identity with administrative privileges that are not continuously required.

#### Monitoring

Monitor use of the administrative privilege and alert upon anomalous activity.

#### Reactive Subtraction

Detect suspicious privilege use and revoke the active session or token.

#### Preventive Architectural Constraint

Restrict the privilege by scope, time, system, or approved workflow.

#### Preventive Structural Erasure

Remove the standing administrative assignment.

#### Deeper Structural Erasure

Redesign the operational workflow so that the underlying administrative capability is no longer required for the routine task.

The preferred intervention is the earliest and deepest form of subtraction compatible with the required operational outcome.

---

## 12. Verification Methodology

Verification SHOULD determine whether the targeted transition remains executable.

Verification activities MAY include:

- architecture inspection;
- configuration inspection;
- graph analysis;
- reachability testing;
- adversarial simulation;
- execution testing;
- privilege testing;
- dependency analysis;
- artifact inspection; and
- negative functional testing.

Verification SHOULD distinguish among the following outcomes.

### 12.1 Detection

The attempted transition was observed.

### 12.2 Reactive Prevention

The attempted transition began or was requested, and a runtime mechanism prevented or interrupted completion.

### 12.3 Architectural Constraint

A persistent boundary prevented the transition while the underlying capability remained present.

### 12.4 Structural Erasure

The capability or relationship required for the transition was absent.

Only the final category constitutes structural path erasure.

A valid verification record SHOULD contain:

- the path or transition tested;
- the defined system scope;
- the starting state;
- the intended destination or outcome;
- the required functionality preserved;
- the test or evidence used;
- the observed result;
- the classification of the result; and
- known remaining or alternative paths.

---

## 13. Relationship to Path Erasure Rate

The Path Erasure Rate provides a quantitative measure of structural attack-path reduction:

$PER = \frac{|P_{\text{erased}}|}{|P_{\text{eligible}}|}$

Where:

- (P_{\text{eligible}}\) represents eligible attack paths identified within scope.
- (P_{\text{erased}}\) represents the subset rendered non-traversable through structural deletion.

PEPS and PER address complementary engineering questions.

**PEPS asks:**

> Where and when should subtraction occur?

**PER asks:**

> How much eligible attack-path reduction was achieved?

PEPS provides placement precedence.

PER provides quantitative measurement.

Reactive interruption of an attack path SHALL NOT be classified as permanent path erasure unless the underlying transition has been structurally removed and verified as non-traversable within the defined scope.

---

## 14. Relationship to the Subtractive Hierarchy of Efficacy

The OWASP Subtractive Security model establishes the general hierarchy:

> **Architectural Deletion > Architectural Constraint > Monitoring**

Path Erasure Precedence extends that hierarchy by introducing temporal and architectural placement dimensions.

The resulting engineering principle is:

> **Delete what is unnecessary. Constrain what cannot be deleted. React to what cannot be predetermined. Monitor what necessarily remains.**

### 14.1 Assumption Burden Principle

Path Erasure Precedence is consistent with the **Assumption Burden Principle**:

> **The reliability of a security mechanism decreases as the number of conditions that must remain true for the mechanism to succeed increases.**

Moving a security intervention later in time generally introduces additional dependencies and conditions, including:

- successful telemetry collection;
- accurate event classification;
- timely communication;
- available decision infrastructure;
- uncompromised authorization credentials;
- functioning orchestration;
- available enforcement systems; and
- intervention before adversary traversal produces material impact.

Each dependency creates an additional failure mode and an additional condition that an adversary may attempt to degrade, evade, compromise, delay, or weaponize.

Verified structural erasure eliminates the need for continued enforcement of the erased transition.

The system does not need to detect, classify, or interrupt traversal through an edge that is no longer present.

Reactive mechanisms, including automated and autonomous response systems, therefore operate above a structurally minimized substrate rather than substitute for one.

---

## 15. Continuous Improvement

Path erasure SHOULD operate as an architectural ratchet.

Paths discovered through runtime detection, incident response, penetration testing, adversarial simulation, threat modeling, control validation, or operational experience SHOULD be evaluated for movement toward earlier and deeper forms of subtraction.

### Desired Temporal Progression

> **Corrective → Reactive → Preventive**

### Desired Architectural Progression

> **Detection → Constraint → Structural Erasure**

### Desired Assumption-Burden Progression

> **Many Continuing Dependencies → Fewer Continuing Dependencies → No Continuing Enforcement Dependency for the Erased Transition**

A mature subtractive architecture progressively reduces its dependence on successful runtime intervention by converting discovered attack paths into persistent architectural constraints or permanent path erasure.

A path that requires repeated detection, interruption, remediation, or exception handling SHOULD be treated as a candidate for architectural redesign.

---

## 16. Conformance

An implementation conforms to this standard when it:

1. defines the relevant system scope;
2. identifies eligible security-relevant paths or transitions;
3. evaluates whether those transitions are required;
4. applies temporal precedence;
5. applies architectural precedence;
6. documents the justification for retained paths;
7. identifies the assumption burden of dynamic controls;
8. distinguishes structural erasure from detection or reactive interruption;
9. validates claimed erasure through evidence of non-traversability;
10. governs residual paths that cannot be erased; and
11. reevaluates reactive and corrective interventions for migration toward preventive structural outcomes.

Conformance does not require elimination of every identified attack path.

Conformance requires that retained paths be subject to explicit necessity analysis, precedence analysis, constraint, ownership, and verification appropriate to their role and risk.

---

## 17. Core Principles

### Path Erasure Objective

> **The objective of security engineering is not merely to react faster to adversary traversal. It is to reduce the number of traversable paths for which reaction is necessary.**

### Path Erasure Precedence Principle

> **Subtraction should occur at the earliest point in time and lowest architectural layer at which required functionality permits it.**

### Assumption Burden Application

> **Where multiple mechanisms preserve equivalent required functionality, security engineering should prefer the mechanism that erases or constrains the path with the fewest conditions that must remain true for the security outcome to persist.**

### Architectural Ratchet

> **Paths discovered through corrective or reactive security should be evaluated for conversion into preventive structural erasure.**

---

## 18. Conclusion

Preventive, reactive, and corrective security mechanisms frequently perform variations of the same physical action: they remove, constrain, or interrupt a state transition.

Their security properties are not equivalent.

A path removed before exposure does not create the same race condition, control-plane dependency, or assumption burden as a path dynamically removed during adversary traversal.

A path dynamically removed during traversal does not provide the same protection as a path removed only after compromise.

Path Erasure Precedence therefore establishes a durable engineering order:

1. erase unnecessary paths before they become available;
2. erase them at the deepest feasible architectural layer;
3. constrain paths that cannot be erased;
4. apply reactive subtraction to irreducible runtime states;
5. use corrective subtraction to generate permanent architectural improvement; and
6. verify erasure by demonstrating non-traversability rather than detection alone.

> **The most reliable defensive transition is the one the system no longer permits.**
