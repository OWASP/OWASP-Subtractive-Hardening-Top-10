# OWASP CI/CD Pipeline Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** CI/CD Pipelines & Software Delivery Infrastructure  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP CI/CD Pipeline Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing software supply-chain risk through the elimination of attacker-accessible execution, trust, credential, and workflow manipulation paths.

Unlike traditional CI/CD security programs that focus primarily on vulnerability scanning, monitoring, policy enforcement, or pipeline observability, Subtractive Hardening prioritizes removal of architectural conditions that allow source-code compromise, pipeline manipulation, credential theft, unauthorized deployments, and supply-chain attacks to compose into business impact.

Rather than relying on reactive threat detection, audit review, or manual investigation, the objective is to physically remove executable attack paths from the software delivery graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Repositories, Runners, Workflows, Secrets, Artifacts, Dependencies, Branches, Approvals, Deployment Targets
E = Execution, Trust, Credential, Trigger, Merge, Dependency, Artifact, or Deployment Relationships
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

The objective of this standard is not to make attacks easier to detect.

The objective is to make attacks impossible by removing the pathways that enable them.

---

# Boundary Scope Note

This standard focuses exclusively on attack paths that exist within CI/CD systems and software delivery workflows.

The following attack surfaces are intentionally out of scope and are addressed by separate standards:

- Developer workstation compromise
- Endpoint exploitation
- Operating system compromise
- Cloud host compromise
- Network-layer compromise

Those attack paths should be addressed through:

- Endpoint Subtractive Hardening
- Host Hardening Standards
- AWS/Azure/GCP Subtractive Hardening Standards
- Network Subtractive Hardening

This standard focuses only on residual CI/CD logical attack paths.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The CI/CD Pipeline Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within software delivery environments.

Together they establish a repeatable security engineering cycle:

1. Identify attack paths.
2. Measure attack-path exposure.
3. Eliminate attack paths where possible.
4. Constrain residual attack paths where necessary.
5. Measure resulting reduction.
6. Continuously improve architectural resilience.

---

# The Subtractive Hierarchy of Efficacy

All recommendations within this standard follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 – Architectural Deletion

Remove the attack path completely.

Examples:

- Credential removal
- Trust relationship removal
- Execution pathway removal
- Deployment pathway removal
- Unsigned artifact pathway removal

## Tier 2 – Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Branch protections
- Required approvals
- Private dependency mirrors
- Job-scoped permissions
- Authenticated trigger paths
- Artifact signing requirements

## Tier 3 – Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- CI/CD audit logs
- Secret scanning alerts
- Pipeline anomaly detection
- SIEM correlation
- Repository activity monitoring

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever an attack path can be eliminated, elimination is preferred.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate software supply-chain attack paths.
- Reduce credential theft opportunities.
- Reduce pipeline privilege escalation opportunities.
- Reduce trust-boundary abuse.
- Reduce malicious code execution opportunities.
- Reduce unauthorized deployment opportunities.
- Reduce attack-path composability.
- Improve measurable Path Erasure Rate (PER).

Recommendations are not ranked based on:

- CVSS scores
- Vulnerability prevalence
- Compliance requirements
- Detection coverage
- Vendor capability claims

The primary selection criterion is architectural attack-path reduction.

---

# OWASP CI/CD Pipeline Subtractive Hardening Top 10

| ID | Title |
|------|------|
| C01 | Secrets Persistence Elimination |
| C02 | Runner Privilege Reduction |
| C03 | Dependency Chain Isolation |
| C04 | Pipeline Definition Integrity |
| C05 | Build Logic Injection Elimination |
| C06 | Trigger Path Authentication |
| C07 | Pull Request Context Isolation |
| C08 | Single-Actor Deployment Path Removal |
| C09 | Third-Party Integration Trust Reduction |
| C10 | Artifact Provenance Enforcement |

---

# C01: Secrets Persistence Elimination

## Description

Persistent secrets stored within repositories, variables, configuration files, or build systems create reusable attack paths.

## Strategic Objective

Eliminate long-lived credentials from software delivery systems.

## Attack Path Removed

```text
Repository / Pipeline
          ↓
Static Credential
          ↓
Infrastructure Access
```

## Architectural Deletion Goal

Remove persistent credential material from CI/CD environments. Erasure Criteria (P_{erased} = 1): Static secrets are removed from repository/runner storage; authentication occurs strictly via ephemeral OIDC tokens. (If static keys remain active in parallel, P_{erased} = 0.)

## Implementation Examples

- Use OIDC federation.
- Use ephemeral cloud credentials.
- Eliminate static access keys.
- Eliminate long-lived service credentials.
- Remove hardcoded secrets from repositories.
- Prefer secretless authentication architectures.

---

# C02: Runner Privilege Reduction

## Description

CI/CD runners frequently possess excessive privileges that allow pipeline compromise to become infrastructure compromise.

## Strategic Objective

Eliminate persistent administrative authority from build execution environments.

## Attack Path Removed

```text
Build Step
     ↓
Overprivileged Runner
     ↓
Cloud Control Plane
```

## Architectural Deletion Goal

Remove unnecessary runner privileges, cross-environment permissions, network reachability, and persistent trust relationships between execution contexts.

## Implementation Examples

- Use single-purpose runners.
- Use job-scoped permissions.
- Prefer ephemeral runners.
- Enforce least-privilege IAM roles.
- Remove root Docker socket access.
- Prevent persistent administrative privileges across jobs.
- Eliminate shared mutable caches between trust boundaries.
- Scope caches per branch, workflow, or commit.
- Restrict runner network access to required services only.
- Eliminate unrestricted east-west connectivity from runners.
---

# C03: Dependency Chain Isolation

## Description

External package repositories create trust paths capable of introducing malicious code into builds.

## Strategic Objective

Eliminate arbitrary dependency resolution.

## Attack Path Removed

```text
Build
  ↓
Untrusted Repository
  ↓
Malicious Package
```

## Architectural Deletion Goal

Remove direct internet dependency retrieval during builds. Erasure Criteria (P_erased = 1): Build runners are incapable of directly resolving dependencies from public repositories. All dependency retrieval occurs through organization-controlled, immutable, verified package sources.

## Implementation Examples

- Use immutable dependency mirrors.
- Use private package registries.
- Pin dependencies.
- Require hash-locked manifests.
- Eliminate arbitrary package downloads.
- Prevent runtime dependency resolution from untrusted sources.

---

# C04: Pipeline Definition Integrity

## Description

Pipeline definitions frequently control cloud credentials, build processes, deployment logic, and artifact production.

## Strategic Objective

Prevent unauthorized modification of pipeline execution logic.

## Attack Path Removed

```text
Code Change
     ↓
Pipeline Definition
     ↓
Build Control
```

## Architectural Deletion Goal

Remove repository-only control of deployment workflows.

## Implementation Examples

- Protect workflow definitions.
- Require secondary approvals for workflow changes.
- Use immutable deployment policies.
- Restrict pipeline modification rights.
- Use out-of-band authorization models.
- Prevent untrusted code from modifying execution definitions.

---

# C05: Build Logic Injection Elimination

## Description

Untrusted inputs frequently enable command injection within build environments.

## Strategic Objective

Eliminate dynamic command construction.

## Attack Path Removed

```text
User Input
      ↓
Script Execution
      ↓
Build Compromise
```

## Architectural Deletion Goal

Remove command injection opportunities from build logic.

## Implementation Examples

- Use parameterized build actions.
- Use immutable inputs.
- Use typed workflow variables.
- Eliminate dynamic shell execution.
- Restrict custom actions.
- Avoid command construction from untrusted commit messages, branch names, pull request titles, or issue text.

---

# C06: Trigger Path Authentication

## Description

Webhook and API-triggered workflows often expose unauthenticated execution paths.

## Strategic Objective

Eliminate unauthorized pipeline triggers.

## Attack Path Removed

```text
Attacker
      ↓
Pipeline Trigger
      ↓
Workflow Execution
```

## Architectural Deletion Goal

Remove unauthenticated trigger surfaces.

## Implementation Examples

- Require HMAC verification.
- Require mutual TLS where feasible.
- Use private trigger endpoints.
- Use IP allowlists.
- Require authenticated trigger workflows.
- Remove unauthenticated webhook receivers.

---

# C07: Pull Request Context Isolation

## Description

External pull requests frequently create trust-boundary violations between untrusted code and privileged repository or deployment contexts.

## Strategic Objective

Sever trust relationships between untrusted code and sensitive build contexts.

## Attack Path Removed

```text
Forked PR
      ↓
Repository Secrets
      ↓
Infrastructure Access
```

## Architectural Deletion Goal

Prevent untrusted contributors from accessing privileged execution contexts.

## Implementation Examples

- Isolate repository secrets from forked pull requests.
- Restrict token issuance in untrusted contexts.
- Use separate execution contexts.
- Use fork-safe workflows.
- Segregate untrusted contributors.
- Prevent privileged workflow execution from untrusted code paths.

---

# C08: Single-Actor Deployment Path Removal

## Description

Single-user deployment authority creates direct compromise pathways from one account, token, or approval action into production deployment.

## Strategic Objective

Remove single-person deployment capability.

## Attack Path Removed

```text
Single User
      ↓
Merge
      ↓
Production Deployment
```

## Architectural Deletion Goal

Eliminate single-actor deployment paths.

## Implementation Examples

- Require two-person approval.
- Enforce branch protections.
- Require mandatory automated validation.
- Enforce merge controls.
- Enforce change-control gates.
- Prevent direct-to-main pushes.

---

# C09: Third-Party Integration Trust Reduction

## Description

Marketplace actions, pipeline plugins, CI/CD extensions, and third-party SaaS integrations frequently introduce external trust paths into repositories and build environments.

## Strategic Objective

Eliminate unnecessary third-party execution authority.

## Attack Path Removed

```text
Third-Party Action
        ↓
Build Environment
        ↓
Repository Access
```

## Architectural Deletion Goal

Reduce trust exposure created by externally maintained integrations.

## Implementation Examples

- Pin actions to commit SHAs.
- Use allowlisted actions only.
- Prefer repository-controlled actions.
- Restrict marketplace extensions.
- Govern third-party integrations.
- Remove auto-updating or unverified integration paths.

---

# C10: Artifact Provenance Enforcement

## Description

Unsigned artifacts create execution paths with uncertain origin and integrity.

## Strategic Objective

Prevent deployment of artifacts without cryptographic provenance.

## Attack Path Removed

```text
Unknown Artifact
        ↓
Deployment
        ↓
Production Execution
```

## Architectural Deletion Goal

Erase deployment paths for artifacts lacking verified provenance.

## Implementation Examples

- Use Sigstore.
- Use Cosign.
- Sign container images.
- Sign software artifacts.
- Require supply-chain attestations.
- Block deployment of unsigned artifacts.
- Require provenance validation prior to deployment.

---

# Verification & PER Measurement

## Step 1 – Establish Baseline

Identify all eligible attack paths.

```text
P_eligible(t0)
```

## Step 2 – Implement Controls

Apply C01 through C10.

## Step 3 – Validate Erasure

Identify attack paths rendered non-traversable.

```text
P_erased(t1)
```

## Step 4 – Calculate PER

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Success Criteria

The objective is not improved visibility.

The objective is measurable reduction in reachable attack-path availability.

---

# Strategic Objective: Non-Conductive Software Delivery

The goal of these subtractions is to establish deterministic boundaries within software delivery systems.

By collapsing attack paths, the CI/CD environment becomes architecturally non-conductive.

In this model:

```text
Vulnerability = Spark
Supply-Chain Trust Path = Oxygen
Pipeline Architecture = Conductivity
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

*OWASP CI/CD Pipeline Subtractive Hardening Top 10 v1.0*
