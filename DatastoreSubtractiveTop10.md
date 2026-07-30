# OWASP Datastore Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Persistent Datastores, Databases, and Managed Data Engines  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Datastore Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing cyber risk through the elimination of attacker-accessible execution, trust, credential, replication, egress, backup, metadata, and cross-tenant data paths within persistent datastore environments.

Unlike traditional database security guidance that focuses primarily on vulnerability remediation, query monitoring, audit logging, encryption settings, or compliance control inventories, Subtractive Hardening prioritizes the removal of architectural conditions that allow datastore compromise, data-plane manipulation, privilege escalation, trust chaining, unauthorized export, and business-impacting data exposure to compose across systems.

Rather than relying on reactive detection, alert tuning, or continuous query review, the objective is to physically remove conductive edges from the datastore system graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Databases, Tables, Collections, Schemas, Indexes, Users, Roles, Service Accounts, Backups, Replicas, Connectors, Queries, Applications, Data Stores
E = Query, Execution, Trust, Credential, Replication, Federation, Export, Backup, Metadata, Egress, or Data-Access Relationships
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

The objective is to make datastore compromise, unauthorized data access, destructive modification, privilege escalation, and exfiltration materially more difficult by removing the pathways that enable them.

---

# Boundary Scope Note

This standard applies to persistent datastores across multiple database architectures, including relational databases, document databases, key-value stores, columnar databases, graph databases, time-series databases, search indexes, data warehouses, vector databases, and managed database services.

While execution mechanics vary across datastore types, the subtractive objectives remain consistent: eliminate unnecessary execution, trust, credential, egress, replication, administrative, backup, export, discovery, and cross-tenant data paths across the datastore boundary.

This standard focuses on residual database and datastore attack paths not fully addressed by operating system, cloud, network, identity, CI/CD, application-layer, or AI standards.

Examples include:

- Database-to-host execution paths
- Cross-database trust relationships
- Overprivileged service identities
- Tenant, schema, collection, index, and data-boundary traversal
- Dynamic query and datastore API execution paths
- Replication, synchronization, and federation trust paths
- Shared data-plane write authority
- Database-originated egress and external connector paths
- Backup, snapshot, export, and dump reachability
- Metadata, schema, index, and discovery exposure

This standard is intended to be compounded with, not substituted for, Linux, Windows, Network, Cloud, Identity, CI/CD, Application Security, and AI Subtractive Hardening standards where applicable.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The Datastore Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within data persistence environments by identifying residual datastore-specific paths whose elimination reduces attacker optionality.

Together they establish a repeatable security engineering cycle:

1. Identify datastore-specific attack paths.
2. Measure datastore attack-path exposure.
3. Eliminate datastore attack paths where possible.
4. Constrain residual datastore attack paths where necessary.
5. Measure resulting reduction.
6. Continuously improve architectural resilience.

---

# The Subtractive Hierarchy of Efficacy

All recommendations within this standard follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 - Architectural Deletion

Remove the attack path completely.

Examples:

- Database-to-host execution removal
- Trust relationship removal
- Service identity privilege removal
- Cross-tenant access path removal
- Replication path removal
- Export path removal
- Metadata discovery path removal

## Tier 2 - Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Row-level or document-level access control
- Per-tenant datastore segmentation
- Read-only service identities
- Scoped replication channels
- Approved export paths
- Immutable backup access boundaries
- Query and API parameterization

## Tier 3 - Monitoring & Detection

Monitoring is reserved for residual attack paths that cannot be deleted or reasonably constrained.

Examples:

- Database audit logs
- Query anomaly detection
- Data access monitoring
- Backup access monitoring
- SIEM correlation
- Privileged database activity review

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever an attack path can be eliminated, elimination is preferred.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate datastore-specific attack-path edges.
- Reduce database-to-host execution opportunities.
- Reduce credential and service identity abuse opportunities.
- Reduce cross-tenant and cross-schema traversal.
- Reduce dynamic query and API execution risk.
- Reduce replication, sync, and federation trust paths.
- Reduce unauthorized export, backup, and snapshot exposure.
- Reduce datastore egress and external connector abuse.
- Reduce data-plane manipulation and shared write authority.
- Improve measurable Path Erasure Rate (PER).

Recommendations are not ranked based on:

- CVSS scores
- Vulnerability prevalence
- Compliance requirements
- Detection coverage
- Vendor capability claims
- Database engine popularity

The primary selection criterion is architectural attack-path reduction.

---

# OWASP Datastore Subtractive Hardening Top 10

| ID | Title |
|------|------|
| D01 | Database-to-Host Execution Path Elimination |
| D02 | Datastore Trust Relationship Reduction |
| D03 | Service Identity & Privilege Reduction |
| D04 | Tenant, Schema & Data Boundary Isolation |
| D05 | Dynamic Query & API Execution Reduction |
| D06 | Replication, Sync & Federation Trust Reduction |
| D07 | Shared Data-Plane Write Authority Reduction |
| D08 | Datastore Egress Determinism |
| D09 | Backup, Snapshot & Export Reachability Reduction |
| D10 | Metadata, Schema & Discovery Surface Reduction |

---

# D01: Database-to-Host Execution Path Elimination

## Description

Some datastore engines expose mechanisms that allow database logic, stored procedures, external runtimes, plug-ins, scripting engines, extensions, or administrative utilities to invoke operating-system-level execution or external code paths.

## Strategic Objective

Eliminate database-originated host execution paths.

## Attack Path Removed

```text
Database Principal
        ↓
Database Execution Feature
        ↓
Host / Runtime Execution
```

## Architectural Deletion Goal

Remove unnecessary datastore-to-host execution pathways.

## Implementation Examples

- Disable database shell invocation features where unnecessary.
- Remove external language runtimes where unnecessary.
- Disable unsafe stored procedure execution paths.
- Remove unnecessary database extensions capable of host interaction.
- Restrict user-defined functions that invoke external code.
- Prevent datastore engines from launching arbitrary host processes.

---

# D02: Datastore Trust Relationship Reduction

## Description

Linked servers, foreign data wrappers, federated queries, cross-instance trust, cross-cluster access, and managed datastore integrations can create transitive paths across data environments.

## Strategic Objective

Reduce unnecessary datastore-to-datastore trust relationships.

## Attack Path Removed

```text
Datastore A
     ↓
Trust / Federation Relationship
     ↓
Datastore B
```

## Architectural Deletion Goal

Remove unnecessary trust, federation, and linked access paths between datastores.

## Implementation Examples

- Remove unused linked servers.
- Remove unnecessary foreign data wrappers.
- Restrict federated query paths.
- Reduce cross-instance trust relationships.
- Remove broad cross-cluster datastore access.
- Mediate necessary cross-datastore access through scoped service interfaces.

---

# D03: Service Identity & Privilege Reduction

## Description

Database service accounts, application users, managed identities, service principals, and replication identities often possess excessive privileges that allow datastore compromise to become infrastructure, application, or data-plane compromise.

## Strategic Objective

Reduce privilege assigned to datastore identities and service accounts.

## Attack Path Removed

```text
Compromised Datastore Identity
             ↓
Overprivileged Service Account
             ↓
Infrastructure / Data Control
```

## Architectural Deletion Goal

Remove unnecessary privilege from datastore service identities, application accounts, and administrative roles.

## Implementation Examples

- Remove unused administrative roles.
- Separate read, write, migration, replication, and administration identities.
- Use least-privilege application accounts.
- Remove infrastructure privileges from database service identities.
- Avoid shared database service accounts.
- Use short-lived or scoped credentials where feasible.

---

# D04: Tenant, Schema & Data Boundary Isolation

## Description

Shared databases, schemas, collections, indexes, and partitions can create cross-tenant or cross-domain traversal paths when access controls, query filters, or data boundaries are incomplete.

## Strategic Objective

Eliminate unauthorized traversal between tenants, schemas, collections, indexes, partitions, or data domains.

## Attack Path Removed

```text
Tenant / Domain A
          ↓
Shared Datastore Context
          ↓
Tenant / Domain B Data
```

## Architectural Deletion Goal

Remove unnecessary shared data contexts between unrelated tenants, users, projects, or data domains.

## Implementation Examples

- Use tenant-isolated schemas, collections, tables, indexes, or databases where appropriate.
- Enforce row-level, document-level, or partition-level access control.
- Remove cross-tenant query paths.
- Prevent shared indexes from bypassing authorization boundaries.
- Separate production, development, analytics, and test data domains.
- Avoid relying solely on application-side filters for tenant isolation.

---

# D05: Dynamic Query & API Execution Reduction

## Description

Dynamic SQL, unsafe query construction, string-concatenated datastore APIs, unvalidated filters, scriptable aggregations, and dynamic map-reduce style operations can allow attacker-controlled input to influence datastore execution.

## Strategic Objective

Eliminate unnecessary dynamic datastore execution paths.

## Attack Path Removed

```text
Untrusted Input
        ↓
Dynamic Query / Data API Execution
        ↓
Unauthorized Data Access or Modification
```

## Architectural Deletion Goal

Remove unnecessary dynamic query execution and unsafe data API construction.

## Implementation Examples

- Eliminate string-concatenated query construction.
- Require parameterized queries or typed query builders.
- Restrict dynamic administrative statements.
- Disable unnecessary scriptable query features.
- Restrict user-controlled aggregation or map-reduce execution where feasible.
- Prefer fixed, scoped data-access APIs over arbitrary query surfaces.

---

# D06: Replication, Sync & Federation Trust Reduction

## Description

Replication channels, synchronization jobs, change-data-capture streams, data warehouse ingestion paths, search indexing pipelines, and federation links can propagate compromise, corruption, or unauthorized data movement across environments.

## Strategic Objective

Reduce unnecessary datastore replication and synchronization trust paths.

## Attack Path Removed

```text
Source Datastore
        ↓
Replication / Sync / Federation Channel
        ↓
Destination Datastore
```

## Architectural Deletion Goal

Remove unnecessary replication, synchronization, federation, and change-propagation paths.

## Implementation Examples

- Remove unused replication channels.
- Scope replication identities to required datasets only.
- Separate production replication from analytics ingestion.
- Restrict change-data-capture streams.
- Constrain search indexing and warehouse ingestion paths.
- Prevent broad bidirectional synchronization unless required.

---

# D07: Shared Data-Plane Write Authority Reduction

## Description

Broad write authority over shared tables, collections, catalogs, indexes, queues, or data domains can allow one compromised principal to corrupt records, poison downstream analytics, alter business logic inputs, or impact many applications simultaneously.

## Strategic Objective

Reduce broad shared write authority within datastore environments.

## Attack Path Removed

```text
Compromised Principal
          ↓
Shared Data-Plane Write Authority
          ↓
Many Applications / Many Users
```

## Architectural Deletion Goal

Remove unnecessary broad write paths into shared or high-impact data planes.

## Implementation Examples

- Separate write roles by application or data domain.
- Remove global write permissions.
- Restrict bulk update and bulk delete authority.
- Require controlled promotion paths for shared reference data.
- Isolate operational, analytics, and reference-data write channels.
- Prefer append-only or immutable logs where appropriate.

---

# D08: Datastore Egress Determinism

## Description

Datastores may initiate outbound communication through external procedures, database mail, HTTP extensions, foreign connectors, event integrations, notification channels, or managed service integrations.

## Strategic Objective

Eliminate arbitrary outbound communication from datastore engines and managed datastore services.

## Attack Path Removed

```text
Datastore Engine
        ↓
Outbound Connector / External Procedure
        ↓
External Destination
```

## Architectural Deletion Goal

Restrict datastore-originated egress to deterministic, approved, and necessary destinations.

## Implementation Examples

- Disable database mail where unnecessary.
- Remove unused external procedures or connectors.
- Restrict HTTP or network-capable extensions.
- Enforce allowlisted outbound endpoints.
- Block arbitrary external data connectors.
- Route required datastore egress through approved mediation points.

---

# D09: Backup, Snapshot & Export Reachability Reduction

## Description

Backups, snapshots, dumps, exports, restores, and cloned environments often contain high-value data and may be less protected than the production datastore itself.

## Strategic Objective

Reduce uncontrolled access to backup, snapshot, dump, export, and clone paths.

## Attack Path Removed

```text
Principal / Process
          ↓
Backup / Snapshot / Export Path
          ↓
Sensitive Data Exposure
```

## Architectural Deletion Goal

Remove unnecessary reachability to datastore copies and export mechanisms.

## Implementation Examples

- Restrict backup access to dedicated recovery identities.
- Remove broad snapshot or dump permissions.
- Disable ad hoc exports where unnecessary.
- Separate production data from development clones.
- Encrypt and access-control backup repositories.
- Remove unnecessary restore paths into lower-trust environments.

---

# D10: Metadata, Schema & Discovery Surface Reduction

## Description

Schema metadata, system catalogs, index descriptions, table names, collection names, graph labels, query plans, and repository discovery features can reveal sensitive structure that enables targeted exploitation or privilege expansion.

## Strategic Objective

Reduce unnecessary datastore metadata and schema discovery exposure.

## Attack Path Removed

```text
Low-Privilege Principal
          ↓
Metadata / Schema Discovery
          ↓
Targeted Data or Privilege Abuse
```

## Architectural Deletion Goal

Remove unnecessary metadata visibility from principals that do not require it.

## Implementation Examples

- Restrict access to system catalogs where feasible.
- Restrict schema discovery for low-privilege users.
- Hide sensitive table, collection, index, or graph metadata where supported.
- Limit query-plan visibility where unnecessary.
- Remove broad information-schema access where feasible.
- Avoid exposing internal datastore structure through application errors or APIs.

---

# Verification & PER Measurement

## Step 1 - Establish Baseline

Identify all eligible residual datastore attack paths after applicable platform standards are applied.

```text
P_eligible(t0)
```

## Step 2 - Implement Controls

Apply D01 through D10.

## Step 3 - Validate Erasure

Identify datastore attack paths rendered non-traversable.

```text
P_erased(t1)
```

## Step 4 - Calculate PER

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Success Criteria

The objective is not improved visibility.

The objective is measurable reduction in reachable datastore-specific attack-path availability.

---

# Strategic Objective: Non-Conductive Datastores

The goal of these subtractions is to establish deterministic boundaries within persistent datastore environments.

By collapsing residual datastore-specific attack paths, the datastore environment becomes architecturally non-conductive.

In this model:

```text
Injection / Credential / Compromise = Spark
Execution, Trust, Egress, Backup, or Data Path = Oxygen
Datastore Architecture = Conductivity
```

Remove the path, and the spark goes nowhere.

---

# Guiding Principle

Attackers can only traverse paths that exist.

The objective of Subtractive Hardening is to systematically eliminate or constrain those paths until adversary activity can no longer compose into material business impact, unauthorized data exposure, data integrity compromise, privilege escalation, or operational disruption.

**Security effectiveness is maximized when attack paths are removed, not merely observed.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Evidence-Based Security ([Evidence-Based Security Article](https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and))
- The Law of Subtractive Risk ([The Law of Subtractive Risk](https://subtractivesecurity.substack.com/p/the-law-of-subtractive-risk-moving))
- The Science of Silence

---

*OWASP Datastore Subtractive Hardening Top 10 v1.0*
