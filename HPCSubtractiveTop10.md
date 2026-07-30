# OWASP HPC Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** High-Performance Computing (HPC), Scientific Computing, and Distributed Research Compute  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP HPC Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing security risk in high-performance computing environments through the elimination of attacker-accessible scheduler, fabric, shared-state, software supply-chain, storage, allocation, and co-tenancy paths.

Unlike traditional HPC security guidance that focuses primarily on account controls, SSH configuration, host hardening, monitoring, or generalized Linux protections, Subtractive Hardening prioritizes the removal of architectural conditions that allow scientific workloads, shared compute resources, high-speed interconnects, batch schedulers, and parallel filesystems to compose into privilege escalation, lateral movement, data compromise, resource abuse, and research integrity impact.

Rather than relying on reactive detection, log review, or continuous triage, the objective is to physically remove conductive edges from the HPC system graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Users, Jobs, Schedulers, Compute Nodes, Head Nodes, Fabrics, Queues, Containers, Modules, Filesystems, Datasets, Accelerators
E = Scheduling, Execution, Fabric, Storage, Trust, Allocation, State, Dependency, or Co-Tenancy Relationships
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

The objective of this standard is not to make HPC attacks easier to detect.

The objective is to make HPC compromise, research-data manipulation, cluster-wide execution abuse, unauthorized compute consumption, and cross-tenant workload impact materially more difficult by removing the pathways that enable them.

---

# Boundary Scope Note

This standard addresses residual attack paths unique to high-performance computing environments.

General Linux host hardening, SSH controls, endpoint security, cloud identity, CI/CD pipeline integrity, container host hardening, and network segmentation are addressed by their respective Subtractive Hardening standards.

This document focuses on HPC-specific attack paths involving:

- High-speed compute fabrics
- MPI and inter-process trust relationships
- Multi-tenant compute context isolation
- Batch schedulers and queue control planes
- Workflow state and scratch-path integrity
- Container and module runtime manipulation
- Resource allocation and compute-abuse paths
- Shared scientific software repositories
- Parallel filesystem isolation
- Accelerator and microarchitectural co-tenancy

This standard is intended to be compounded with, not substituted for, Linux, Network, Cloud, CI/CD, Identity, and AI Subtractive Hardening standards where applicable.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The HPC Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within scientific computing and high-performance compute environments by identifying residual HPC-specific paths whose elimination reduces attacker optionality.

Together they establish a repeatable security engineering cycle:

1. Identify HPC-specific attack paths.
2. Measure HPC attack-path exposure.
3. Eliminate HPC attack paths where possible.
4. Constrain residual HPC attack paths where necessary.
5. Measure resulting reduction.
6. Continuously improve architectural resilience.

---

# The Subtractive Hierarchy of Efficacy

All recommendations within this standard follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 - Architectural Deletion

Remove the attack path completely.

Examples:

- Cross-job fabric reachability removal
- Shared execution-state removal
- Scheduler privilege path removal
- Shared scratch execution path removal
- Global software write-path removal
- Default egress path removal

## Tier 2 - Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Per-job fabric partitioning
- Queue-level trust boundaries
- Ephemeral scratch allocation
- Signed scientific software promotion paths
- Dedicated high-assurance partitions
- Accelerator and node co-tenancy controls

## Tier 3 - Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- Scheduler audit logs
- Job anomaly detection
- File access auditing
- Fabric telemetry
- Resource consumption alerts
- Cluster SIEM correlation

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever an attack path can be eliminated, elimination is preferred.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate HPC-specific attack-path edges.
- Reduce scheduler abuse opportunities.
- Reduce cross-job and cross-tenant workload influence.
- Reduce shared scientific software poisoning opportunities.
- Reduce unauthorized fabric and storage traversal.
- Reduce resource allocation abuse.
- Reduce accelerator and hardware co-tenancy leakage.
- Reduce attack-path composability.
- Improve measurable Path Erasure Rate (PER).

Recommendations are not ranked based on:

- CVSS scores
- Vulnerability prevalence
- Compliance requirements
- Detection coverage
- Vendor capability claims
- Scheduler or cluster popularity

The primary selection criterion is architectural attack-path reduction.

---

# OWASP HPC Subtractive Hardening Top 10

| ID | Title |
|------|------|
| H01 | High-Speed Fabric & Inter-Process Trust Reduction |
| H02 | Multi-Tenant Compute Context Isolation |
| H03 | Scheduler Control Plane Privilege Reduction |
| H04 | Workflow State & Scratch Path Integrity |
| H05 | Container, Module & Runtime Environment Integrity |
| H06 | Resource Allocation & Queue Abuse Constraint |
| H07 | Shared Scientific Software Supply Chain Integrity |
| H08 | Fabric Egress Determinism |
| H09 | Parallel Filesystem & Shared Storage Isolation |
| H10 | Microarchitectural & Accelerator Co-Tenancy Erasure |

---

# H01: High-Speed Fabric & Inter-Process Trust Reduction

## Description

HPC workloads often rely on high-speed interconnects and inter-process communication paths that prioritize performance over authentication, encryption, and tenant isolation.

## Strategic Objective

Reduce unauthorized trust and reachability across compute fabrics and inter-process communication paths.

## Attack Path Removed

```text
Compromised Job / Node
          ↓
Shared Compute Fabric / Inter-Process Trust
          ↓
Additional Job / Node
```

## Architectural Deletion Goal

Remove unnecessary cross-job fabric reachability and inter-process trust relationships.

## Implementation Examples

- Enforce per-job or per-partition fabric isolation.
- Use dedicated fabric partitions where supported.
- Restrict cross-job inter-node communication.
- Disable insecure default transport paths where feasible.
- Prevent unrelated jobs from sharing unnecessary interconnect trust.
- Align scheduler allocations with fabric-level segmentation boundaries.

---

# H02: Multi-Tenant Compute Context Isolation

## Description

Co-resident workloads sharing physical compute nodes, cores, memory domains, NUMA regions, or thread contexts can create memory scraping, timing, race-condition, or cross-tenant state exposure paths.

## Strategic Objective

Eliminate unsafe compute co-tenancy for sensitive or high-assurance workloads.

## Attack Path Removed

```text
Job A
  ↓
Shared Compute Context
  ↓
Job B State / Memory / Execution Influence
```

## Architectural Deletion Goal

Remove unnecessary shared compute contexts between unrelated workloads.

## Implementation Examples

- Eliminate multi-tenant node sharing for high-assurance partitions.
- Use dedicated nodes for sensitive workloads.
- Enforce rigid core-pinning for allocated jobs.
- Enforce NUMA and cgroup isolation where feasible.
- Prevent unrelated users from sharing sensitive compute contexts.
- Separate high-trust and low-trust workloads into distinct execution partitions.

---

# H03: Scheduler Control Plane Privilege Reduction

## Description

HPC schedulers control execution across large numbers of compute nodes and often possess broad authority over job launch, resource allocation, prolog and epilog scripts, environment construction, and cluster-wide execution behavior.

## Strategic Objective

Reduce scheduler-mediated privilege escalation and unauthorized execution paths.

## Attack Path Removed

```text
User / Job Submission
          ↓
Scheduler Control Plane
          ↓
Cluster-Wide Execution or Privilege
```

## Architectural Deletion Goal

Remove unnecessary user influence over privileged scheduler execution paths.

## Implementation Examples

- Remove user ability to specify privileged prolog or epilog hooks.
- Strip root execution permissions from user-triggered batch hooks.
- Scope scheduler API tokens narrowly.
- Restrict job control parameters that influence privileged execution.
- Separate scheduler administration from ordinary job submission.
- Remove unauthenticated scheduler API paths.

---

# H04: Workflow State & Scratch Path Integrity

## Description

Scientific workflows frequently chain jobs based on intermediate files, exit codes, scratch outputs, generated scripts, or pipeline state. If intermediate state is mutable or executable across trust boundaries, attackers can manipulate subsequent workflow execution without altering the original source workflow.

## Strategic Objective

Prevent shared workflow state from becoming an execution authority.

## Attack Path Removed

```text
Intermediate Workflow State
             ↓
Subsequent Job Decision / Execution
             ↓
Altered Workflow Path
```

## Architectural Deletion Goal

Remove untrusted mutable scratch state as a control path for subsequent workflow execution.

## Implementation Examples

- Use per-job scratch directories.
- Purge scratch state automatically after job completion.
- Separate data outputs from executable workflow definitions.
- Use no-exec scratch mounts where operationally feasible.
- Require signed or hashed workflow handoff artifacts for sensitive pipelines.
- Prevent workflow routing decisions from being driven by untrusted mutable files.

---

# H05: Container, Module & Runtime Environment Integrity

## Description

HPC environments often rely on containers, runtime modules, user-selectable software stacks, and library path manipulation. User-writable module paths or untrusted images can alter the runtime environment for scientific jobs and create privilege or integrity failures.

## Strategic Objective

Eliminate untrusted runtime-environment manipulation paths.

## Attack Path Removed

```text
User-Controlled Runtime Path
             ↓
Job Execution Environment
             ↓
Privilege Escalation or Scientific Output Manipulation
```

## Architectural Deletion Goal

Remove unauthorized influence over container images, modules, and runtime library resolution.

## Implementation Examples

- Require signed container images for batch execution.
- Restrict user-writable module paths in trusted partitions.
- Lock approved module search paths.
- Restrict library override mechanisms where feasible.
- Strip unnecessary setuid paths from container runtimes.
- Prefer approved runtime images for regulated or high-assurance queues.

---

# H06: Resource Allocation & Queue Abuse Constraint

## Description

Schedulers grant access to large-scale compute capacity. Overbroad allocation policies, excessive runtime windows, bypassable queue limits, or persistent reservations can allow unauthorized compute consumption, crypto-mining, distributed cracking, or hidden background execution.

## Strategic Objective

Eliminate unbounded or unauthorized compute allocation paths.

## Attack Path Removed

```text
User / Job
     ↓
Overbroad Resource Allocation
     ↓
Unauthorized Compute Consumption
```

## Architectural Deletion Goal

Remove unbounded compute authority from queue and allocation systems.

## Implementation Examples

- Enforce hard limits on resource requests.
- Restrict maximum runtime windows.
- Revoke unused node allocations automatically.
- Use preemption policies for orphaned or abusive allocations.
- Restrict persistent reservations.
- Require approval for unusual high-scale allocations.

---

# H07: Shared Scientific Software Supply Chain Integrity

## Description

HPC clusters often rely on shared scientific software repositories and globally mounted application stacks. A poisoned library, compiler, module, or shared binary can affect many users and many jobs simultaneously.

## Strategic Objective

Prevent shared scientific software from becoming a cluster-wide compromise path.

## Attack Path Removed

```text
Poisoned Shared Software
          ↓
Global Software Mount
          ↓
Many Jobs / Many Users
```

## Architectural Deletion Goal

Remove unauthorized write paths into shared scientific software and library repositories.

## Implementation Examples

- Remove user write privileges from global application directories.
- Remove user write privileges from shared library directories.
- Require signed build pipelines for central cluster software.
- Maintain SBOMs for centrally deployed scientific software.
- Promote shared software through controlled release paths.
- Prevent untrusted upstream builds from being globally exposed without verification.

---

# H08: Fabric Egress Determinism

## Description

Compute nodes may lack ordinary internet access but still possess non-deterministic egress paths through head nodes, management networks, storage bridges, or high-speed fabrics. These paths can enable data exfiltration, command-and-control, or covert movement through infrastructure not designed for general egress control.

## Strategic Objective

Eliminate arbitrary egress from compute fabrics and cluster execution environments.

## Attack Path Removed

```text
Compute Node / Job
          ↓
Fabric / Head Node / Storage Bridge
          ↓
External or Sensitive Destination
```

## Architectural Deletion Goal

Restrict compute-node and fabric egress to deterministic, required paths only.

## Implementation Examples

- Remove default external routing from compute nodes.
- Restrict fabric interfaces to explicit inter-node communication.
- Block arbitrary outbound paths through head nodes.
- Restrict storage bridge traversal paths.
- Enforce explicit egress gateways for cluster workloads.
- Monitor residual fabric egress only after unnecessary paths are removed.

---

# H09: Parallel Filesystem & Shared Storage Isolation

## Description

Parallel filesystems and shared storage are optimized for throughput and collaboration, but over-permissive storage models can allow one user, job, or project to access, overwrite, influence, or poison another user's datasets, outputs, or binaries.

## Strategic Objective

Eliminate cross-job and cross-tenant storage traversal paths.

## Attack Path Removed

```text
Job A
  ↓
Shared Filesystem
  ↓
Job B Data / Output / Binary
```

## Architectural Deletion Goal

Remove unnecessary shared writable storage paths between unrelated jobs, users, projects, or tenants.

## Implementation Examples

- Use per-job ephemeral scratch allocations.
- Use project-scoped storage boundaries.
- Remove cross-tenant writable paths.
- Automatically purge or unmount job scratch after completion.
- Enforce strong POSIX permissions or ACLs where feasible.
- Promote outputs through immutable or controlled publication paths.

---

# H10: Microarchitectural & Accelerator Co-Tenancy Erasure

## Description

Massively parallel systems frequently share CPU caches, memory buses, PCIe lanes, RDMA-capable devices, GPUs, accelerators, or other hardware resources. Co-located workloads can create side-channel, residue, timing, or cross-context influence paths.

## Strategic Objective

Eliminate unsafe hardware and accelerator co-tenancy for sensitive workloads.

## Attack Path Removed

```text
Workload A
     ↓
Shared Microarchitectural / Accelerator Resource
     ↓
Workload B State or Signal
```

## Architectural Deletion Goal

Remove shared hardware execution paths for workloads requiring high assurance, confidentiality, or integrity.

## Implementation Examples

- Disable SMT or hyperthreading on multi-tenant sensitive partitions.
- Use dedicated nodes for sensitive workloads.
- Isolate GPU or accelerator contexts where supported.
- Prevent shared accelerator memory exposure.
- Restrict RDMA or PCIe adjacency for sensitive workloads.
- Use physical workload isolation when logical isolation is insufficient.

---

# Verification & PER Measurement

## Step 1 - Establish Baseline

Identify all eligible residual HPC attack paths after applicable platform standards are applied.

```text
P_eligible(t0)
```

## Step 2 - Implement Controls

Apply H01 through H10.

## Step 3 - Validate Erasure

Identify HPC attack paths rendered non-traversable.

```text
P_erased(t1)
```

## Step 4 - Calculate PER

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Success Criteria

The objective is not improved visibility.

The objective is measurable reduction in reachable HPC-specific attack-path availability.

---

# Strategic Objective: Non-Conductive Scientific Computing

The goal of these subtractions is to establish deterministic boundaries within high-performance computing and scientific computing environments.

By collapsing residual HPC-specific attack paths, the cluster environment becomes architecturally non-conductive.

In this model:

```text
Compromise / Poisoned Input = Spark
Scheduler, Fabric, Storage, or Runtime Path = Oxygen
HPC Architecture = Conductivity
```

Remove the path, and the spark goes nowhere.

---

# Guiding Principle

Attackers can only traverse paths that exist.

The objective of Subtractive Hardening is to systematically eliminate or constrain those paths until adversary activity can no longer compose into material business impact, research integrity compromise, unauthorized compute consumption, or operational disruption.

**Security effectiveness is maximized when attack paths are removed, not merely observed.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Evidence-Based Security ([Evidence-Based Security Article](https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and))
- The Law of Subtractive Risk ([The Law of Subtractive Risk](https://subtractivesecurity.substack.com/p/the-law-of-subtractive-risk-moving))
- The Science of Silence

---

*OWASP HPC Subtractive Hardening Top 10 v1.0*
