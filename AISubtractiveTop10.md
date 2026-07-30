# OWASP AI Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Artificial Intelligence, LLMs, Agents, RAG, and Model Infrastructure  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP AI Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing AI security risk through the elimination of attacker-accessible model, training-data, retrieval, tool-use, memory, identity, egress, and autonomous-action paths.

Unlike traditional AI security guidance that focuses primarily on prompt filtering, model monitoring, output review, runtime detection, or policy enforcement, Subtractive Hardening prioritizes the removal of architectural conditions that allow prompt injection, data poisoning, model compromise, excessive agency, unauthorized retrieval, and tool abuse to compose into business impact.

Rather than relying on reactive detection, output inspection, or continuous triage, the objective is to physically remove traversable edges from the AI system graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Models, Prompts, Tools, Agents, Memories, Vector Stores, Datasets, Tokens, APIs, Artifacts, Users
E = Retrieval, Tool-Use, Training, Fine-Tuning, Memory, Identity, Execution, Egress, or Delegation Relationships
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

The objective of this standard is not to make AI attacks easier to detect.

The objective is to make AI-enabled compromise, unauthorized action, data exposure, model manipulation, and resource amplification materially more difficult by removing the pathways that enable them.

---

# Residual AI Risk Scope Statement

The OWASP AI Subtractive Hardening Top 10 is intended to address residual AI-specific attack paths after foundational attack-path reduction controls have already been implemented within the supporting infrastructure.

This standard assumes prior implementation of applicable subtractive hardening standards for:

- Operating systems
- Cloud platforms
- Network infrastructure
- Identity and access management
- CI/CD pipelines
- Container and host environments
- SaaS and collaboration platforms

As a result, attack paths such as host compromise, container escape, excessive cloud permissions, software supply-chain compromise, traditional credential theft, unrestricted network reachability, and endpoint exploitation are considered out of scope except where AI systems introduce unique variations not adequately mitigated by those standards.

This standard focuses on residual AI-specific risks including:

- Training-data poisoning
- Fine-tuning corpus compromise
- Model artifact compromise
- Unsafe model loading
- Agentic authority abuse
- Persistent memory contamination
- Retrieval-augmented generation (RAG) reachability
- Model-driven exfiltration
- Autonomous execution chains
- Resource amplification and denial-of-wallet paths

The AI standard is therefore intended to be compounded with, not substituted for, the supporting platform standards.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The AI Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within AI systems by identifying residual AI-specific paths whose elimination reduces attacker optionality.

Together they establish a repeatable security engineering cycle:

1. Identify AI-specific attack paths.
2. Measure AI attack-path exposure.
3. Eliminate AI attack paths where possible.
4. Constrain residual AI attack paths where necessary.
5. Measure resulting reduction.
6. Continuously improve architectural resilience.

---

# The Subtractive Hierarchy of Efficacy

All recommendations within this standard follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 - Architectural Deletion

Remove the attack path completely.

Examples:

- Dataset ingestion path removal
- Unsafe model loading removal
- Tool-use path removal
- Persistent memory path removal
- Arbitrary egress path removal
- Autonomous recursion path removal

## Tier 2 - Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Signed ML-BOM requirements
- Tool permission boundaries
- Session-scoped memory
- Pre-retrieval authorization
- Human-in-the-loop circuit breakers
- Token, rate, duration, and compute caps

## Tier 3 - Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- Prompt and response logging
- Model behavior monitoring
- RAG retrieval audit logging
- Tool invocation logging
- Cost anomaly detection
- Abuse investigation workflows

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever an attack path can be eliminated, elimination is preferred.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate AI-specific attack-path edges.
- Reduce model poisoning opportunities.
- Reduce training-data poisoning opportunities.
- Reduce unauthorized retrieval opportunities.
- Reduce tool-use privilege escalation opportunities.
- Reduce identity and token abuse opportunities.
- Reduce autonomous action and recursive execution pathways.
- Reduce exfiltration and resource amplification pathways.
- Reduce attack-path composability.
- Improve measurable Path Erasure Rate (PER).

Recommendations are not ranked based on:

- CVSS scores
- Vulnerability prevalence
- Compliance requirements
- Detection coverage
- Vendor capability claims
- Model popularity

The primary selection criterion is architectural attack-path reduction.

---

# OWASP AI Subtractive Hardening Top 10

| ID | Title |
|------|------|
| A01 | Training Data & Fine-Tuning Pipeline Erasure |
| A02 | Model Artifact Integrity |
| A03 | AI Supply Chain & Plugin Minimization |
| A04 | Tool Authority & Privilege Reduction |
| A05 | Agent Memory & State Isolation |
| A06 | Identity & Token Isolation |
| A07 | RAG Reachability Reduction |
| A08 | Egress Determinism & Exfiltration Path Erasure |
| A09 | Agency & Autonomous Loop Constraint Enforcement |
| A10 | Consumption & Resource Boundary Erasure |

---

# A01: Training Data & Fine-Tuning Pipeline Erasure

## Description

Training and fine-tuning pipelines can introduce poisoned data, backdoors, corrupted labels, malicious examples, or unverified corpuses into model behavior.

## Strategic Objective

Eliminate unverified data-ingestion paths into model training and fine-tuning workflows.

## Attack Path Removed

```text
Unverified Data Source
          ↓
Training / Fine-Tuning Pipeline
          ↓
Model Behavior
```

## Architectural Deletion Goal

Remove unverified external dataset ingestion and non-attested training sources from model development pipelines.

## Implementation Examples

- Require signed Machine Learning Bills of Materials (ML-BOMs).
- Require cryptographically verified training datasets.
- Remove direct web-scraping paths for active model retraining.
- Restrict fine-tuning to approved, attested corpuses.
- Remove ingestion paths from unauthenticated or untrusted data sources.
- Maintain dataset provenance before model training or fine-tuning occurs.

---

# A02: Model Artifact Integrity

## Description

Untrusted model artifacts, unsafe serialization formats, tampered checkpoints, and unverified weights can introduce malicious behavior or code execution at model load time.

## Strategic Objective

Prevent execution or deployment of untrusted model artifacts.

## Attack Path Removed

```text
Untrusted Model Artifact
          ↓
Model Loading Runtime
          ↓
Code Execution / Model Compromise
```

## Architectural Deletion Goal

Erase execution pathways associated with untrusted model artifacts.

## Implementation Examples

- Eliminate unsafe deserialization formats where feasible.
- Prefer static, tensor-only model formats such as safetensors.
- Require cryptographically attested model provenance.
- Block execution of unsigned or unverified model artifacts.
- Restrict model execution environments to approved artifact sources.
- Remove unnecessary network egress from model-serving infrastructure.

---

# A03: AI Supply Chain & Plugin Minimization

## Description

Third-party libraries, model hubs, external connectors, plugins, and Model Context Protocol (MCP) servers can introduce external trust paths into AI runtimes.

## Strategic Objective

Reduce supply-chain and plugin-based execution authority.

## Attack Path Removed

```text
Third-Party Plugin / Dependency
             ↓
AI Runtime
             ↓
Tool or Data Access
```

## Architectural Deletion Goal

Remove unnecessary AI runtime dependencies, plugins, dynamic connectors, and external tool registrations.

## Implementation Examples

- Prune unused third-party dependencies.
- Remove unused API wrappers and connectors.
- Eliminate dynamic plugin registration.
- Require static tool declarations.
- Pin dependencies and plugins cryptographically.
- Restrict MCP servers and equivalent tool brokers to approved, verified endpoints.

---

# A04: Tool Authority & Privilege Reduction

## Description

AI agents can become dangerous when exposed tools possess excessive authority, write access, deletion capability, administrative permissions, or broad data-plane access.

## Strategic Objective

Reduce tool authority available to AI systems.

## Attack Path Removed

```text
Prompt Injection
       ↓
Overprivileged Tool
       ↓
Destructive or Unauthorized Action
```

## Architectural Deletion Goal

Remove high-impact permissions from tools exposed to AI models and agents.

## Implementation Examples

- Strip write permissions from LLM-exposed tools where feasible.
- Strip delete permissions from LLM-exposed tools where feasible.
- Remove administrative permissions from AI tool contexts.
- Replace direct database access with scoped API proxies.
- Prefer read-only tool bindings for retrieval and analysis tasks.
- Eliminate ambient administrative tokens in tool invocation layers.

---

# A05: Agent Memory & State Isolation

## Description

Persistent agent memory, vector-store memory, and reusable agentic state can allow prompt injection, context poisoning, or sensitive content to traverse between users, tenants, or sessions.

## Strategic Objective

Eliminate cross-session and cross-tenant memory traversal.

## Attack Path Removed

```text
User / Session A
        ↓
Persistent Agent Memory
        ↓
User / Session B
```

## Architectural Deletion Goal

Remove unnecessary persistent state relationships between unrelated users, sessions, tenants, or tasks.

## Implementation Examples

- Use ephemeral, single-session memory boundaries.
- Remove shared persistent memory where unnecessary.
- Segment vector memory by user, tenant, or task.
- Prevent memory reuse across unrelated sessions.
- Eliminate cross-tenant vector-store traversal paths.
- Require explicit approval for durable memory retention.

---

# A06: Identity & Token Isolation

## Description

AI workflows can inherit ambient host credentials, broad cloud tokens, service account privileges, or invoking-user entitlements that enable unauthorized pass-through execution.

## Strategic Objective

Eliminate broad or long-lived identity paths available to AI systems.

## Attack Path Removed

```text
AI Workflow
     ↓
Inherited Token / Ambient Credential
     ↓
Privileged System Access
```

## Architectural Deletion Goal

Remove long-lived or high-privilege tokens from AI workflows and tool execution layers.

## Implementation Examples

- Remove static tokens assigned to AI workflows.
- Remove broad service accounts from AI execution contexts.
- Use short-lived, transaction-scoped tokens.
- Constrain identity to the required micro-action.
- Prevent pass-through use of full invoking-user entitlements.
- Remove ambient host or cloud credentials from AI runtimes.

---

# A07: RAG Reachability Reduction

## Description

Retrieval-Augmented Generation (RAG) systems can expose unauthorized documents, prompt content, sensitive records, or indirect injection payloads if retrieval is not constrained before semantic search occurs.

## Strategic Objective

Eliminate unauthorized retrieval paths within RAG systems.

## Attack Path Removed

```text
User Query
     ↓
Unrestricted Vector Search
     ↓
Unauthorized Document Retrieval
```

## Architectural Deletion Goal

Remove unrestricted document reachability within RAG indices.

## Implementation Examples

- Enforce pre-retrieval access control filtering.
- Apply row-level or document-level authorization before vector search.
- Segment vector indices by tenant, user, or data domain.
- Remove cross-tenant embedding paths.
- Prevent post-retrieval filtering from serving as the primary access control.
- Restrict retrieval to documents the requester is authorized to access.

---

# A08: Egress Determinism & Exfiltration Path Erasure

## Description

AI runtimes can be induced to exfiltrate data through external web calls, markdown rendering, remote image loads, browsing tools, connector abuse, or unauthorized outbound sockets.

## Strategic Objective

Eliminate arbitrary outbound communication from AI execution nodes.

## Attack Path Removed

```text
AI Runtime
    ↓
Arbitrary Outbound Connection
    ↓
External Destination
```

## Architectural Deletion Goal

Remove raw egress pathways from AI runtimes and model-driven execution contexts.

## Implementation Examples

- Block arbitrary outbound network connections.
- Force strict destination allowlisting.
- Route AI runtime egress through approved proxies.
- Disable untrusted remote rendering triggers.
- Sanitize model outputs that can create dynamic URL fetches.
- Remove unauthorized web scraping capabilities from AI execution nodes.

---

# A09: Agency & Autonomous Loop Constraint Enforcement

## Description

Autonomous agents can create recursive execution chains, spawn sub-agents, iterate indefinitely, or initiate high-impact actions without appropriate architectural circuit breakers.

## Strategic Objective

Eliminate unconstrained autonomous execution paths.

## Attack Path Removed

```text
Prompt / Goal
      ↓
Autonomous Agent Loop
      ↓
Unbounded Tool or Action Chain
```

## Architectural Deletion Goal

Remove paths for recursive, unconstrained, or high-impact autonomous execution.

## Implementation Examples

- Enforce deterministic loop caps.
- Eliminate dynamic sub-agent creation APIs where unnecessary.
- Require human-in-the-loop approval for critical actions.
- Place immutable circuit breakers on irreversible operational sinks.
- Restrict agent access to high-impact tools.
- Prevent autonomous escalation from analysis to execution without explicit authorization.

---

# A10: Consumption & Resource Boundary Erasure

## Description

AI systems can be abused for denial of wallet, context-window flooding, recursive model-to-model amplification, compute exhaustion, memory exhaustion, or tool-loop cost expansion.

## Strategic Objective

Eliminate unbounded compute, context, memory, and API consumption paths.

## Attack Path Removed

```text
Prompt / Agent Loop
          ↓
Unbounded Resource Consumption
          ↓
Cost or Availability Impact
```

## Architectural Deletion Goal

Remove unlimited resource traversal paths from AI systems.

## Implementation Examples

- Hard-code token ingestion limits at the API gateway or proxy layer.
- Enforce execution duration caps.
- Enforce API rate limits.
- Enforce memory allocation limits.
- Enforce model invocation quotas.
- Prevent recursive model-to-model cost amplification.
- Apply limits independently of model reasoning.

---

# Verification & PER Measurement

## Step 1 - Establish Baseline

Identify all eligible residual AI attack paths after applicable platform standards are applied.

```text
P_eligible(t0)
```

## Step 2 - Implement Controls

Apply A01 through A10.

## Step 3 - Validate Erasure

Identify AI attack paths rendered non-traversable.

```text
P_erased(t1)
```

## Step 4 - Calculate PER

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Success Criteria

The objective is not improved visibility.

The objective is measurable reduction in reachable AI-specific attack-path availability.

---

# Strategic Objective: Non-Conductive AI Systems

The goal of these subtractions is to establish deterministic boundaries within AI systems.

By collapsing residual AI-specific attack paths, the AI environment becomes architecturally non-conductive.

In this model:

```text
Prompt / Poisoned Input = Spark
Tool, Retrieval, Memory, or Training Path = Oxygen
AI Architecture = Conductivity
```

Remove the path, and the spark goes nowhere.

---

# Guiding Principle

Attackers can only traverse paths that exist.

The objective of Subtractive Hardening is to systematically eliminate or constrain those paths until adversary activity can no longer compose into material business impact.

**Security effectiveness is maximized when attack paths are removed, not merely observed.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Evidence-Based Security ([Evidence-Based Security Article](https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and))
- The Law of Subtractive Risk ([The Law of Subtractive Risk](https://subtractivesecurity.substack.com/p/the-law-of-subtractive-risk-moving))
- The Science of Silence

---

*OWASP AI Subtractive Hardening Top 10 v1.0*
