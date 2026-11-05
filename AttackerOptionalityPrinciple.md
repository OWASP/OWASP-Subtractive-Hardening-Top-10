# OWASP Subtractive Security Attacker Optionality Principle

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Governance Area:** Foundational Theory & Security Engineering Specification  
**Alignment:** Attack Path Failure Mode Theory, Hierarchy of Efficacy & Assumption Burden Principle, PER-1.0  
**License:** Apache License 2.0

# Executive Summary

The Attacker Optionality Principle establishes that cybersecurity architectures should minimize the number and diversity of viable state transitions and traversable attack paths available to an adversary following compromise, particularly paths capable of reaching high-consequence target states.

Attackers do not require every attempted action to succeed. They require one sufficiently useful path to remain traversable. When one credential, protocol, host, privilege relationship, trust, dependency, or route fails, an attacker may search for another. Security architectures with many alternative transitions therefore provide attackers with optionality: multiple ways to compose local compromise into systemic impact.

This principle extends OWASP Subtractive Security Attack Path Failure Mode Theory. If attack paths are cybersecurity's fundamental failure mode, then architectures containing multiple independently traversable paths expose multiple alternative failure modes to an adversary.

The engineering objective is therefore not only to make individual paths harder to traverse. It is to reduce how many useful paths exist.

Under this model:

```text
More Viable Paths = More Attacker Optionality
Fewer Viable Paths = Less Attacker Optionality
No Viable Path = No Systemic Progression to the Target State
```

The principle is especially important under uncertainty and fat-tailed cyber risk. Novel capabilities, including zero-day exploits, cannot always be predicted or prevented. However, novel capabilities generally must compose with existing states and transitions to create material impact. Removing known downstream paths can therefore reduce the consequence of attack techniques that do not yet exist or cannot yet be detected.

# Core Proposition

> Security architectures SHOULD minimize the number and diversity of traversable attack paths available to an adversary, particularly paths capable of composing local compromise into violations of critical security invariants.

Reducing attacker optionality reduces the utility of both known and unknown attacker capabilities.

# Definition

## Attacker Optionality

Attacker Optionality is the number and diversity of viable state transitions and traversable attack paths available to an adversary from an attained state toward one or more consequential target states.

Let:

```text
G = (V,E)
S = adversary-attainable states
T = consequential target states
P(S -> T) = set of traversable attack paths from S to T
```

Attacker optionality increases as the number and diversity of usable paths in `P(S -> T)` increases.

Conceptually:

```text
Optionality proportional to |P(S -> T)| and path diversity
```

This relationship is intentionally conceptual rather than a calibrated probability model. Two environments with the same number of paths can differ materially if one contains greater privilege, reachability, independence, diversity, or consequence.

# Relationship to Attack Path Failure Mode Theory

OWASP Subtractive Security Attack Path Failure Mode Theory establishes:

```text
Defect != Failure Mode
Path = Failure Mode
```

A vulnerability, credential, misconfiguration, excessive permission, phishing event, insider action, or other local defect does not independently produce enterprise compromise. Systemic failure occurs when a traversable execution path allows the local condition to propagate into an unauthorized state transition that violates a security invariant.

The Attacker Optionality Principle extends this model:

```text
Attack Path Failure Mode Theory asks:
What can fail?

Answer:
The traversable path.

Attacker Optionality asks:
How many alternative traversable paths can the attacker choose among?
```

If paths are failure modes, multiple viable paths provide multiple opportunities for systemic failure.

# Optionality Corollary

If attack paths constitute cybersecurity failure modes, then an architecture containing multiple independently traversable paths between adversary-accessible states and consequential target states provides multiple alternative failure modes through which compromise can propagate.

Therefore:

> Reducing the number and diversity of traversable attack paths reduces attacker optionality even when the probability or identity of the initiating defect cannot be reliably estimated.

# Ingress, Egress, and Optionality

Attack Path Failure Mode Theory defines both ingress and egress requirements.

## Ingress

A defect without reachable ingress cannot be exploited.

```text
Critical Remote Code Execution + No Reachable Ingress = No Exploitation
```

## Egress

A compromised state without useful egress cannot readily compose into systemic loss.

```text
Remote Code Execution
+ No Useful Credentials
+ No Child-Process Path
+ No Administrative Reachability
+ No Useful Network Egress
= Local Containment
```

Attacker Optionality is therefore relevant both before and after initial compromise.

Subtractive Security can reduce:

- ingress paths that allow adversaries to reach exploitable states,
- egress paths that allow attained states to propagate,
- privilege transitions that increase authority,
- trust relationships that expand reachability,
- credential transitions that enable identity reuse,
- execution transitions that enable chaining,
- data paths that expose consequential assets,
- recovery paths whose compromise increases impact.

# Unknown Capability Corollary

> An unknown attacker capability does not imply a wholly unknown attack path.

Novel exploits, techniques, or mechanisms may create previously unknown transitions. However, material impact generally requires the resulting state to compose with other executable edges in the environment.

A zero-day may provide:

```text
? -> Code Execution
```

The attacker must still convert that state into something consequential:

```text
Code Execution
-> Credential Access
-> Privilege
-> Reachability
-> Lateral Movement
-> Critical System
-> Impact
```

Subtractive Security does not require defenders to predict the unknown edge. It seeks to erase or constrain the known edges with which the unknown capability would need to compose.

The defensive question becomes:

> If this unknown capability succeeds, where can it go next?

A resilient architecture increasingly answers:

> Not very far.

# Same Unknown Exploit, Different Optionality

Consider two environments exposed to the same previously unknown remote-code-execution vulnerability. In both environments the exploit succeeds.

## Environment A - High Attacker Optionality

The compromised endpoint contains reusable credentials. Those credentials authenticate elsewhere. Additional privilege is available. Remote administrative protocols provide reachability. Server relationships provide access to recovery infrastructure.

```text
Unknown Exploit
-> Execution
-> Credential
-> Privilege
-> Lateral Movement
-> Recovery Infrastructure
-> Ransomware
```

The environment may possess excellent EDR, SIEM, MFA, vulnerability management, SOC, and incident response capabilities. However, the architecture gives the adversary numerous transitions and alternative routes. Preventing catastrophic impact may depend upon multiple runtime controls and human processes functioning correctly and quickly enough.

## Environment B - Low Attacker Optionality

The same exploit succeeds, but:

- reusable administrative credentials are absent,
- local identities provide no useful privilege elsewhere,
- unnecessary remote administration protocols have been removed,
- management interfaces are unreachable from the compromised zone,
- stale privileged identities do not exist,
- service identities possess narrowly constrained permissions,
- unnecessary trust relationships have been removed,
- recovery infrastructure is unreachable through the compromised security context.

The resulting path is:

```text
Unknown Exploit
-> Execution
-> Constrained State
-> No Consequential Path
```

Both environments failed to predict and prevent the initial unknown exploit.

The difference is what the successful unknown capability was allowed to compose with afterward.

# Relationship to the Assumption Burden Principle

The Assumption Burden Principle states that a defensive control's functional reliability is inversely related to the number of assumptions required for the control to successfully prevent attacker progression.

A detection and response chain may require assumptions such as:

```text
Sensor Functional
-> Telemetry Collected
-> Telemetry Ingested
-> Detection Logic Fires
-> Alert Generated
-> Alert Delivered
-> Analyst Reviews Alert
-> Response Executed
-> Containment Successful
```

The Attacker Optionality Principle describes the complementary adversary-side problem.

```text
Assumption Burden:
How many things must continue going right for the defender?

Attacker Optionality:
How many useful alternatives can go right for the attacker?
```

A particularly fragile architecture combines:

```text
High Defender Assumption Burden
+
High Attacker Optionality
```

The attacker can search across alternative paths while the defender depends upon multiple technical and human assumptions remaining true.

# Reliability Model

For a simplified independent defensive chain with `n` required dependencies, each having failure probability `p`, the probability that at least one required dependency fails is:

```text
P(chain failure) = 1 - (1 - p)^n
```

For six independent dependencies with a 5 percent failure probability each:

```text
P(chain failure) = 1 - (0.95)^6
                 ~= 26.5 percent
```

This is an illustrative reliability model, not an empirical estimate of the failure probability of a particular security architecture. Real-world probabilities are rarely known with precision, dependencies may not be independent, and correlated technical, human, or adversarial failures may materially change the result.

The engineering conclusion is narrower and more durable:

> Individually reliable assumptions can compose into a substantially less reliable defensive system when successful defense requires all of them to remain true.

Attacker optionality increases the adversary's opportunity to locate paths where those assumptions fail or can be bypassed.

# Relationship to Fat-Tailed Cyber Risk

Cyber loss can exhibit fat-tailed characteristics. Many individual defects or control failures produce little or no material consequence. Occasionally, however, defects, privileges, trust relationships, reachability, control failures, and adversary actions compose into outcomes whose impact is radically disproportionate to the apparent importance of any individual condition.

For example:

```text
Vulnerability
-> Missed Detection
-> Credential
-> Privilege
-> Reachability
-> Critical System
-> Impaired Recovery
-> Ransomware
```

No individual transition necessarily guarantees catastrophic loss.

The composition does.

Attacker optionality matters in this environment because each additional viable transition or alternative path provides another opportunity for an adversary to discover a combination capable of reaching a high-consequence state.

The relationship can be expressed conceptually as:

```text
Local Defect or Novel Capability
-> Available Attack Paths
-> Attacker Path Selection
-> Defensive Assumptions Challenged
-> Consequential State Reached
-> Tail Loss
```

Subtractive Security does not attempt to predict precisely which rare combination will eventually occur. It reduces the number of combinations capable of producing consequential outcomes.

# Fat-Tail Resilience Principle

Within a fat-tailed risk environment, security architecture SHOULD prioritize controls that reduce the ability of small or uncertain initiating events to compose into catastrophic outcomes.

This means preferring changes that:

- reduce the number of viable attack paths,
- reduce path diversity,
- reduce privilege propagation,
- reduce trust propagation,
- reduce identity reuse,
- reduce lateral reachability,
- reduce dependency and execution chaining,
- isolate recovery systems,
- reduce the consequence reachable from any single compromised state.

The objective is not to estimate the tail with precision.

The objective is to reduce the architecture's ability to propagate a tail event into catastrophe.

# Relationship to the Hierarchy of Efficacy

The Hierarchy of Efficacy establishes:

```text
Architectural Deletion
-> Architectural Constraint
-> Monitoring & Detection
```

The Attacker Optionality Principle explains an additional reason for this ordering.

## Level 1 - Architectural Deletion

Deletion removes an attacker option entirely.

Examples:

- remove an unnecessary protocol,
- delete a dormant privileged identity,
- eliminate a trust relationship,
- remove workstation-to-workstation communication,
- remove exposed administrative interfaces,
- eliminate unnecessary network reachability.

Effect:

```text
Attacker Option -> Removed
```

## Level 2 - Architectural Constraint

Constraint preserves a required path while reducing its usable state space.

Examples:

- microsegmentation,
- permission boundaries,
- conditional access,
- egress filtering,
- application control,
- narrowly scoped service identities.

Effect:

```text
Attacker Option -> Bounded
```

## Level 3 - Monitoring & Detection

Monitoring observes a path that remains available.

Examples:

- EDR,
- SIEM,
- IDS,
- UEBA,
- threat hunting,
- alerting.

Effect:

```text
Attacker Option -> Still Exists, Attempted Use May Be Observed
```

Therefore:

> Delete options first. Constrain required options second. Monitor the residual options that must remain.

# Relationship to PER

Path Erasure Rate measures structural attack-path reduction:

```text
PER = P_erased / P_eligible
```

Where:

```text
P_eligible = eligible attack paths before the architectural change
P_erased   = eligible attack paths whose executable edges have been structurally removed
```

Attack Path Failure Mode Theory explains why attack paths are the unit being measured.

The Attacker Optionality Principle explains why reducing their number matters.

PER therefore provides a quantitative mechanism for demonstrating one dimension of reduced attacker optionality: path elimination.

Conceptually:

```text
Higher Path Erasure
-> Fewer Traversable Paths
-> Lower Attacker Optionality
-> Fewer Ways for Local Failure to Compose into Systemic Failure
```

PER does not by itself capture every dimension of optionality. Remaining path diversity, independence, privilege, consequence, and reachability may still matter. Optionality analysis should therefore consider both path count and path characteristics.

# Relationship to MITRE ATT&CK

MITRE ATT&CK demonstrates that adversary behavior can be described through recurring objectives and state transitions even when specific implementations change.

An attacker may use a new exploit, tool, obfuscation mechanism, or execution technique while still requiring recognizable transitions such as:

```text
Initial Access
-> Execution
-> Persistence
-> Privilege Escalation
-> Credential Access
-> Discovery
-> Lateral Movement
-> Collection
-> Exfiltration
-> Impact
```

The purpose of the Attacker Optionality Principle is not to assume that every future transition is already known.

It is to recognize that novel capabilities generally require sufficient remaining system conductivity to compose into consequential outcomes.

Reducing optionality limits that conductivity.

# Relationship to Security Measurement

Attacker optionality cannot be reduced intelligently without visibility into the environment.

Security programs should therefore seek to discover:

- identities and credentials,
- privilege relationships,
- network reachability,
- execution relationships,
- trust relationships,
- dependencies,
- administrative interfaces,
- data-access paths,
- control-plane paths,
- recovery-system paths,
- human-mediated and physical transitions where relevant.

Discovery may initially increase the number of observed weaknesses or attack paths.

This does not necessarily represent security regression.

```text
Unknown != Zero
```

Expanded measurement can convert previously unknown paths into known paths. Once understood, those paths can be deleted, constrained, or monitored according to the Hierarchy of Efficacy.

Therefore:

> You cannot subtract what you do not understand.

Security measurement should increase understanding sufficiently to enable structural reduction of attacker capability.

# Engineering Requirements

Organizations implementing this principle SHOULD:

1. Identify adversary-accessible starting states.
2. Identify consequential target states and protected security invariants.
3. Discover traversable paths between starting and target states.
4. Identify alternative paths and independent transition mechanisms.
5. Prioritize elimination of unnecessary paths and transitions.
6. Constrain paths that cannot be eliminated.
7. Apply monitoring and detection to residual required paths.
8. Reassess path reachability after architectural change.
9. Measure eligible path erasure using PER where applicable.
10. Test whether compromise of a local state can still propagate to consequential target states.
11. Repeat discovery as architecture, identities, software, trust, and adversary capabilities change.

# Validation Questions

The following questions SHOULD be used during architecture review and control validation:

- If initial compromise succeeds, what can the attacker do next?
- How many independent paths exist from the attained state to a consequential target?
- Which credentials can be reused?
- Which privileges can be inherited, delegated, or escalated?
- Which trust relationships expand reachability?
- Which protocols or services enable progression?
- Which paths exist solely because legacy or unnecessary functionality remains enabled?
- Which path edges can be deleted?
- Which remaining edges can be constrained?
- Which remaining required paths depend primarily on monitoring and response?
- What happens if detection fails completely at the attained state?
- Can recovery systems be reached from ordinary compromise states?
- Can a novel initial-access capability compose with known downstream paths into material impact?
- After remediation, which attacker capabilities no longer exist?

# Engineering Interpretation

The objective of cybersecurity is not to predict every exploit, tool, or adversary technique.

The objective is to prevent attainable adversary states from composing into unacceptable outcomes.

A mature security architecture therefore seeks simultaneously to:

```text
Reduce Defender Assumption Burden
Reduce Attacker Optionality
Reduce Consequential Reachability
```

These objectives reinforce each other.

Deletion removes paths and assumptions.

Constraint bounds the paths that must remain.

Monitoring observes residual paths that cannot be removed or sufficiently constrained.

The strongest defensive outcome is not a path that is reliably detected.

It is a path that no longer exists.

# Statement of Intent

The Attacker Optionality Principle establishes attacker choice as an explicit security-engineering concern within OWASP Subtractive Security.

If attack paths are the fundamental cybersecurity failure mode, security architecture should not provide adversaries with unnecessary alternative paths through which local compromise can become systemic failure.

Unknown capabilities will continue to emerge. Defensive controls will sometimes fail. Human decisions will sometimes be wrong. Technologies considered secure today will eventually become legacy technologies.

The appropriate response to this uncertainty is not to depend exclusively on increasingly accurate prediction and detection.

It is to reduce the number of useful states and transitions available when prediction and detection fail.

# Summary Principle

```text
Paths are the failure mode.
Assumptions create defender fragility.
Optionality creates attacker opportunity.
Fat-tailed consequences make their interaction dangerous.
Deletion removes attacker options.
Constraint bounds what must remain.
Monitoring addresses the residual.
PER measures path erasure.
```

> The goal is not to predict every future attacker capability. The goal is to give that capability fewer paths through which to produce consequential harm.

