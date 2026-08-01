# OWASP Application Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Application Architecture, APIs, Services, and Runtime Delivery  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Application Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing application security risk through the elimination of attacker-accessible route, input, identity, service-trust, dynamic-execution, runtime, dependency, egress, parser, memory, object, function, and workflow paths.

Unlike traditional application security guidance that focuses primarily on vulnerability classes, testing techniques, scanner findings, secure coding checklists, or exploit taxonomies, Subtractive Hardening prioritizes the removal of architectural conditions that allow application-layer weaknesses to compose into unauthorized access, privilege escalation, business logic abuse, data exposure, remote code execution, lateral service movement, and material business impact.

Rather than relying on reactive detection, scanner output, manual review, or continuous triage, the objective is to physically remove conductive edges from the application system graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Routes, Verbs, Schemas, Tokens, Sessions, Services, APIs, Objects, Functions, Workflows, Dependencies, Parsers, Runtimes, Sockets
E = Reachability, Input, Identity, Session, Trust, Execution, Dependency, Egress, Parser, Memory, Object, Function, or Workflow Relationships
```

Each recommendation within this standard is intentionally selected based on its ability to reduce adversary reachability and improve measurable attack-path reduction through the Path Erasure Rate (PER) Engineering Standard.

```text
PER = P_erased / P_eligible
```

Where:

```text
P_eligible = Eligible attack paths identified within scope
P_erased   = Attack paths rendered non-traversable through architectural deletion
```

The objective of this standard is not to make application attacks easier to detect.

The objective is to make application compromise, unauthorized business action, data exposure, privilege escalation, and post-compromise expansion materially more difficult by removing the pathways that enable them.

---

# Boundary Scope Note

This standard addresses residual attack paths unique to application architectures.

Operating system hardening, cloud security, identity infrastructure, network segmentation, container host security, CI/CD security, AI security, datastore security, and endpoint controls are addressed by their respective Subtractive Hardening standards.

This document focuses on attack paths that persist after those standards have been applied and that arise from application-specific architecture, including:

- Route and endpoint reachability
- HTTP verb and API method exposure
- Application input shape and schema boundaries
- Application session and token lifecycle management
- Service-to-service trust relationships
- Dynamic execution and runtime interpretation paths
- Application runtime capabilities bundled with the workload
- Application dependency and dead-code execution paths
- Application-originated egress and socket authority
- Payload, parser, and memory boundaries
- Object, function, and workflow authorization paths
- Cross-service authority propagation

This standard is intended to be compounded with, not substituted for, the supporting platform standards.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The Application Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within applications, APIs, services, and application runtimes by identifying residual application-specific paths whose elimination reduces attacker optionality.

Together they establish a repeatable security engineering cycle:

1. Identify application-specific attack paths.
2. Measure application attack-path exposure.
3. Eliminate application attack paths where possible.
4. Constrain residual application attack paths where necessary.
5. Measure resulting reduction.
6. Continuously improve architectural resilience.

---

# The Subtractive Hierarchy of Efficacy

All recommendations within this standard follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 - Architectural Deletion

Remove the attack path completely.

Examples:

- Route removal
- Verb removal
- Token persistence removal
- Dynamic execution removal
- Runtime capability removal
- Dependency removal
- Egress path removal
- Unauthorized workflow path removal

## Tier 2 - Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Strict schema enforcement
- Method-level authorization
- Object-level authorization
- Service-to-service token scoping
- Runtime capability minimization
- Parser hardening
- Egress proxy allowlisting
- Workflow state constraints

## Tier 3 - Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- Application telemetry
- API gateway logs
- Runtime anomaly detection
- WAF alerts
- Security monitoring
- SIEM correlation

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever an attack path can be eliminated, elimination is preferred.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate application-specific attack-path edges.
- Reduce unnecessary route and verb reachability.
- Reduce loose input parser execution paths.
- Reduce credential, token, and session persistence paths.
- Reduce transitive service-to-service trust paths.
- Reduce dynamic execution and runtime interpretation paths.
- Reduce post-compromise runtime expansion capability.
- Reduce third-party dependency and dead-code execution paths.
- Reduce SSRF, exfiltration, and arbitrary egress paths.
- Reduce parser, payload, memory, object, function, and workflow abuse paths.
- Improve measurable Path Erasure Rate (PER).

Recommendations are not ranked based on:

- CVSS scores
- Vulnerability prevalence
- Compliance requirements
- Detection coverage
- Vendor capability claims
- Scanner finding counts
- Framework popularity

The primary selection criterion is architectural attack-path reduction.

---

# OWASP Application Subtractive Hardening Top 10

| ID | Title |
|------|------|
| APP01 | Unused Route & Verb Erasure |
| APP02 | Schema-Enforced Input Boundary Reduction |
| APP03 | Ambient Token & Persistent State Deletion |
| APP04 | Transitive Service Trust Graph Collapse |
| APP05 | Dynamic Execution Edge Pruning |
| APP06 | Application Runtime Capability Minimization |
| APP07 | Unused Dependency & Dead-Code Stripping |
| APP08 | Application Egress Determinism |
| APP09 | Payload, Parser & Memory Boundary Constraint |
| APP10 | Object, Function & Workflow Authority Reduction |

---

# APP01: Unused Route & Verb Erasure

## Description

Applications frequently expose unused routes, debug endpoints, administrative interfaces, legacy API versions, unmapped URI paths, and unnecessary HTTP methods that increase reachable application attack surface.

## Strategic Objective

Eliminate unnecessary application transit paths.

## Attack Path Removed

```text
Client
  ↓
Unused Route / Verb
  ↓
Application Logic
```

## Architectural Deletion Goal

Remove non-essential HTTP methods, API routes, legacy endpoints, debug paths, and shadow application entry points from the production routing graph.

## Implementation Examples

- Remove non-essential HTTP verbs at the gateway and application layer.
- Disable TRACE, TRACK, OPTIONS, PUT, PATCH, or other methods where unnecessary.
- Remove debug endpoints from production builds.
- Remove administrative routes from public runtime paths.
- Remove legacy API versions where no longer required.
- Drop unmapped or shadow URI paths at the application gateway.

---

# APP02: Schema-Enforced Input Boundary Reduction

## Description

Loose input structures, permissive payload parsers, unbounded request objects, and weakly typed API inputs create execution and parsing paths that attackers can manipulate before business logic executes.

## Strategic Objective

Eliminate loose input parser execution paths.

## Attack Path Removed

```text
Untrusted Request
         ↓
Loose Input Parser
         ↓
Application Logic
```

## Architectural Deletion Goal

Remove unvalidated, unmapped, or loosely typed input structures before they reach application execution paths.

## Implementation Examples

- Enforce strict JSON, gRPC, GraphQL, XML, or API schemas.
- Reject extra, unmapped, or unexpected fields.
- Use no-additional-properties validation where feasible.
- Validate payload shape at the application edge.
- Use immutable request contracts.
- Reject requests that do not match the declared contract.

---

# APP03: Ambient Token & Persistent State Deletion

## Description

Long-lived session cookies, static API keys, persistent service credentials, ambient application tokens, and reusable authorization state create durable paths for replay, credential theft, session abuse, and privilege propagation.

## Strategic Objective

Eliminate persistent application identity and session authority.

## Attack Path Removed

```text
Application / Session
          ↓
Persistent Token or Credential
          ↓
Privileged Access
```

## Architectural Deletion Goal

Remove long-lived credentials, ambient tokens, and persistent session authority from application memory and storage.

## Implementation Examples

- Replace static API tokens with short-lived credentials.
- Use audience-bound and sender-constrained tokens where feasible.
- Reduce session lifetime.
- Remove persistent database or service credentials from application memory.
- Use workload identity federation where feasible.
- Avoid ambient application authority that persists beyond the required transaction.

---

# APP04: Transitive Service Trust Graph Collapse

## Description

Microservices, internal APIs, and service-to-service calls often inherit broad authority across multiple services. If Service A can call Service B, and Service B can call Service C with elevated authority, compromise may propagate through transitive trust.

## Strategic Objective

Eliminate implicit service-to-service trust propagation.

## Attack Path Removed

```text
Service A
   ↓
Service B
   ↓
Service C
```

## Architectural Deletion Goal

Remove transitive API trust and prevent one service from automatically inheriting authority across downstream services.

## Implementation Examples

- Enforce granular service-to-service authorization.
- Scope tokens to specific methods and resources.
- Use mTLS where applicable.
- Prevent broad service account reuse.
- Prevent Service A from inheriting Service B's authority to call Service C.
- Remove unnecessary internal API reachability between services.

---

# APP05: Dynamic Execution Edge Pruning

## Description

Applications may expose dynamic execution primitives such as unsafe deserialization, reflection, runtime code evaluation, dynamic class loading, template execution, command invocation, or script interpretation.

## Strategic Objective

Eliminate arbitrary dynamic instruction execution paths.

## Attack Path Removed

```text
Untrusted Input
        ↓
Dynamic Execution Primitive
        ↓
Code Execution
```

## Architectural Deletion Goal

Remove unnecessary dynamic code evaluation, unsafe reflection, deserialization, and command execution paths from application logic.

## Implementation Examples

- Disable dynamic code evaluation where unnecessary.
- Remove unsafe deserialization paths.
- Restrict dynamic class loading.
- Remove unnecessary reflection-based invocation.
- Remove Runtime.exec or equivalent system command invocation where unnecessary.
- Enforce language or build settings that remove unsafe execution primitives where feasible.

---

# APP06: Application Runtime Capability Minimization

## Description

Applications increasingly ship as self-contained runtime units. Even when the underlying host is hardened, application packages may include shells, package managers, interpreters, compilers, debug tools, writable filesystems, or system utilities that expand post-compromise capability.

## Strategic Objective

Reduce application-bundled runtime capability that the workload does not require.

## Attack Path Removed

```text
Application Compromise
           ↓
Excess Runtime Capability
           ↓
Post-Exploitation Expansion
```

## Architectural Deletion Goal

Remove runtime capabilities not required for application function.

## Implementation Examples

- Use distroless or minimal runtime images where feasible.
- Remove shell binaries from application runtimes where unnecessary.
- Remove package managers from production runtimes.
- Remove compilers and build tools from production runtimes.
- Remove curl, wget, and similar network utilities where unnecessary.
- Enforce read-only root filesystems where feasible.
- Remove writable binary or plugin paths from production workloads.

---

# APP07: Unused Dependency & Dead-Code Stripping

## Description

Applications frequently include unused transitive dependencies, dormant code paths, unreachable modules, and packages that are never required by the production workload but remain available for exploitation.

## Strategic Objective

Eliminate uncalled third-party and internal code execution paths.

## Attack Path Removed

```text
Application
     ↓
Unused Dependency / Dead Code
     ↓
Exploit Surface
```

## Architectural Deletion Goal

Remove unused dependencies, unreachable code, and unnecessary transitive packages from the production application build.

## Implementation Examples

- Perform automated dependency pruning.
- Use tree-shaking where applicable.
- Eliminate dead code before compilation or packaging.
- Remove unused transitive dependencies.
- Produce minimal production dependency sets.
- Treat SBOM findings as inputs to removal, not merely inventory.

---

# APP08: Application Egress Determinism

## Description

Applications often possess ambient outbound socket authority. This enables server-side request forgery, metadata service access, lateral API calls, arbitrary web callbacks, and data exfiltration.

## Strategic Objective

Eliminate arbitrary outbound application network paths.

## Attack Path Removed

```text
Application Runtime
          ↓
Arbitrary Outbound Socket
          ↓
Internal or External Destination
```

## Architectural Deletion Goal

Restrict application-originated outbound communication to approved, deterministic destinations.

## Implementation Examples

- Enforce default-deny outbound network policy.
- Route necessary outbound API calls through an egress proxy.
- Use domain-pinned allowlists for required external services.
- Block access to metadata services unless explicitly required.
- Remove arbitrary socket creation paths where feasible.
- Restrict application communication to declared dependencies.

---

# APP09: Payload, Parser & Memory Boundary Constraint

## Description

Applications may expose unsafe parsing, memory corruption, injection, interpreter, or boundary-crossing paths through malformed payloads, unsafe serialization, query construction, command construction, file parsing, or memory-unsafe runtimes.

## Strategic Objective

Constrain payload, parser, and memory boundaries before attacker input can influence unsafe execution.

## Attack Path Removed

```text
Untrusted Payload
        ↓
Parser / Query / Memory Boundary
        ↓
Memory Manipulation or Code Injection
```

## Architectural Constraint Goal

Remove or constrain unsafe parser, payload, query, command, and memory manipulation paths.

## Implementation Examples

- Use memory-safe languages where feasible.
- Compile memory-unsafe code with strong boundary protections.
- Enforce parameterized query construction.
- Prohibit inline string concatenation for SQL, NoSQL, LDAP, OS commands, and similar interpreter boundaries.
- Restrict unsafe file parsers and deserializers.
- Enforce strict payload size, type, and structure constraints.

---

# APP10: Object, Function & Workflow Authority Reduction

## Description

Applications expose business objects, functions, and workflow transitions through routes, APIs, GraphQL resolvers, service methods, and UI-driven actions. If authorization is enforced inconsistently, attackers can traverse object, function, or workflow paths that should not be reachable from their identity context.

## Strategic Objective

Eliminate unauthorized object access, function invocation, and business workflow transition paths.

## Attack Path Removed

```text
User / Token
      ↓
Object / Function / Workflow Action
      ↓
Unauthorized Business Impact
```

## Architectural Deletion Goal

Remove application paths where identity, role, tenant, object ownership, or workflow state does not explicitly authorize the requested action.

## Implementation Examples

- Enforce object-level authorization before data access.
- Enforce function-level authorization before method execution.
- Remove direct object reference paths that bypass ownership checks.
- Restrict workflow transitions to valid state changes.
- Prevent users from invoking administrative or privileged functions through hidden routes.
- Enforce tenant, role, and ownership boundaries at the application service layer.

---

# Verification & PER Measurement

## Step 1 - Establish Baseline

Identify all eligible residual application attack paths after applicable platform standards are applied.

```text
P_eligible(t0)
```

## Step 2 - Implement Controls

Apply APP01 through APP10.

## Step 3 - Validate Erasure

Identify application attack paths rendered non-traversable.

```text
P_erased(t1)
```

## Step 4 - Calculate PER

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Success Criteria

The objective is not improved visibility.

The objective is measurable reduction in reachable application-specific attack-path availability.

---

# Strategic Objective: Non-Conductive Applications

The goal of these subtractions is to establish deterministic boundaries within application architectures.

By collapsing residual application-specific attack paths, the application environment becomes architecturally non-conductive.

In this model:

```text
Input / Credential / Compromise = Spark
Route, Token, Trust, Runtime, Egress, or Workflow Path = Oxygen
Application Architecture = Conductivity
```

Remove the path, and the spark goes nowhere.

---

# Guiding Principle

Attackers can only traverse paths that exist.

The objective of Subtractive Hardening is to systematically eliminate or constrain those paths until adversary activity can no longer compose into unauthorized business action, data exposure, privilege escalation, remote execution, or material business impact.

**Security effectiveness is maximized when attack paths are removed, not merely observed.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Evidence-Based Security ([Evidence-Based Security Article](https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and))
- The Law of Subtractive Risk ([The Law of Subtractive Risk](https://subtractivesecurity.substack.com/p/the-law-of-subtractive-risk-moving))
- The Science of Silence

---

*OWASP Application Subtractive Hardening Top 10 v1.0*
