# OWASP Salesforce Subtractive Hardening Top 10

**Document Version:** 1.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Salesforce, Sales Cloud, Service Cloud, Experience Cloud, Apex, Flow, Connected Apps, External Client Apps, Named Credentials, External Credentials, and Salesforce Integrations  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Salesforce Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing Salesforce security risk through the elimination of attacker-accessible guest access, integration credential, system-mode execution, unauthenticated endpoint, mass export, callout, administrative tooling, cross-org trust, implicit sharing, extension, and discovery paths.

Unlike traditional Salesforce security guidance that focuses primarily on configuration checklists, health scores, access reviews, or compliance evidence, Subtractive Hardening prioritizes the removal of architectural conditions that allow Salesforce weaknesses to compose into unauthorized data access, mass extraction, privilege escalation, trusted connector abuse, external data flow, persistence, and material business impact.

Rather than relying primarily on monitoring, event review, or downstream investigation, the objective is to physically remove conductive edges from the Salesforce tenant graph.

System Graph:

```text
G = (V,E)
```

Where:

```text
V = Users, Guest Users, Experience Sites, Profiles, Permission Sets, Records, Objects, Fields, Apex Classes, Flows, Connected Apps, External Client Apps, OAuth Tokens, Named Credentials, External Credentials, Reports, APIs, Packages, Sandboxes, External Systems
E = Access, Sharing, Credential, API, Execution, Integration, Callout, Trust, Export, Metadata, Discovery, or Delegation Relationships
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

The objective of this standard is not to make Salesforce attacks easier to detect.

The objective is to make Salesforce compromise, unauthorized application execution, excessive data access, mass extraction, connector abuse, and cross-environment trust traversal materially more difficult by removing the pathways that enable them.

---

# Boundary Scope Note

This standard addresses residual Salesforce-specific attack paths within Salesforce tenants and Salesforce-integrated environments.

Operating system hardening, enterprise identity infrastructure, endpoint security, network segmentation, cloud platform security, application security, third-party risk management, and general SaaS governance are addressed by their respective Subtractive Hardening standards.

This document focuses on Salesforce-specific attack paths involving:

- Guest user and Experience Cloud reachability
- OAuth, connected app, external client app, Named Credential, External Credential, and integration credential exposure
- Apex, Flow, and system-mode execution boundaries
- Unauthenticated Apex REST, Aura, Lightning, and Visualforce entry points
- Bulk data extraction and mass record enumeration
- External callouts, Named Credentials, External Credentials, CORS, Trusted URLs, Remote Site Settings, and external data-flow paths
- Administrative setup, tooling, Developer Console, and debug surfaces
- Production, sandbox, and cross-org trust paths
- Role hierarchy, implicit sharing, manual sharing, and Apex managed sharing
- Dynamic SOQL/SOSL, unmanaged packages, external scripts, global classes, and metadata discovery

This standard is intended to be compounded with, not substituted for, Identity, SaaS, Application, Datastore, Third-Party Risk, and Behavioral Baseline standards where applicable.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The Salesforce Subtractive Hardening Top 10 provides practical engineering guidance for achieving measurable PER improvements within Salesforce environments by identifying Salesforce-specific paths whose elimination reduces attacker optionality.

Together they establish a repeatable security engineering cycle:

1. Identify Salesforce-specific attack paths.
2. Measure Salesforce attack-path exposure.
3. Eliminate Salesforce attack paths where possible.
4. Constrain residual Salesforce attack paths where necessary.
5. Measure resulting reduction.
6. Continuously improve tenant and integration resilience.

---

# The Subtractive Hierarchy of Efficacy

All recommendations within this standard follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 - Architectural Deletion

Remove the Salesforce attack path completely.

Examples:

- Remove guest record access.
- Remove unused connected apps and external client apps.
- Revoke stale OAuth tokens.
- Remove overprivileged permission assignments.
- Remove unauthenticated endpoints.
- Remove unused Apex, Flows, packages, and integrations.
- Remove broad export paths.
- Remove cross-org trust paths.
- Remove unused Remote Site Settings, Named Credentials, External Credentials, Trusted URLs, and CORS origins.

## Tier 2 - Architectural Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Scoped integration users.
- OAuth 2.0 Client Credentials Flow for approved server-to-server integrations.
- JWT Bearer Flow for approved enterprise integrations.
- Permission set groups.
- Explicit object and field-level security.
- Named Credentials and External Credentials with managed token exchange.
- Restricted callout allowlists.
- Connected app and external client app access policies.
- Report/export restrictions.
- Sandbox data masking.
- Predefined API scopes.

## Tier 3 - Monitoring & Detection

Monitoring is reserved for residual Salesforce attack paths that cannot be deleted or reasonably constrained.

Examples:

- Setup Audit Trail.
- Login History.
- Event Monitoring.
- API usage monitoring.
- Data export monitoring.
- Connected app monitoring.
- Debug log review.
- Package activity review.

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever a Salesforce attack path can be eliminated, elimination is preferred.

---

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate Salesforce-specific attack-path edges.
- Reduce unauthorized guest and external user reachability.
- Reduce OAuth, API token, external client app, connected app, and integration credential abuse.
- Reduce system-mode and elevated execution paths.
- Reduce unauthenticated remote procedure call paths.
- Reduce mass export and bulk enumeration paths.
- Reduce arbitrary callout and external data-flow paths.
- Reduce administrative and tooling surface exposure.
- Reduce cross-org and sandbox trust traversal.
- Reduce implicit sharing and transitive access paths.
- Reduce untrusted extension, dynamic execution, and metadata discovery paths.
- Improve measurable Path Erasure Rate (PER).

Recommendations are not ranked based on:

- Salesforce Health Check score alone
- Vendor marketing claims
- Compliance requirements
- Scanner output alone
- Visibility or alert coverage
- Administrative convenience

The primary selection criterion is architectural attack-path reduction.

---

# OWASP Salesforce Subtractive Hardening Top 10

| ID | Title |
|------|------|
| SF01 | Guest & Experience Cloud Record Reachability Erasure |
| SF02 | API Token, OAuth & Integration Credential Elimination |
| SF03 | System-Mode Execution & Privilege Boundary Enforcement |
| SF04 | Unauthenticated Endpoint & Remote Procedure Call Elimination |
| SF05 | Bulk Data Extraction & Mass Enumeration Path Reduction |
| SF06 | Unconstrained Callout & External Data-Flow Erasure |
| SF07 | Administrative Setup & Tooling Surface Reduction |
| SF08 | Cross-Org, Sandbox & External Trust Severing |
| SF09 | Implicit Sharing & Transitive Access Elimination |
| SF10 | Dynamic Execution, Untrusted Extension & API Discovery Reduction |

---

# SF01: Guest & Experience Cloud Record Reachability Erasure

## Description

Guest users, Experience Cloud users, community users, and external identities can create unintended paths from internet-facing Salesforce surfaces into internal CRM data when record access, sharing rules, object permissions, or external user models are overbroad.

## Strategic Objective

Eliminate unmediated record reachability from unauthenticated and external identities.

## Attack Path Removed

```text
Internet / External User
          ↓
Guest or Experience Cloud Access
          ↓
Internal Salesforce Records
```

## Architectural Deletion Goal

Remove unnecessary record, object, and field access from guest and external user contexts.

## Implementation Examples

- Enforce secure guest user configuration defaults.
- Remove guest user edit and delete paths where unnecessary.
- Remove guest ownership or implicit sharing relationships for sensitive records.
- Remove broad sharing rules that expose sensitive objects to external populations.
- Remove public Experience Cloud page access where authentication is required.
- Restrict external profile and permission set access to required objects and fields only.

---

# SF02: API Token, OAuth & Integration Credential Elimination

## Description

Salesforce integrations often rely on connected apps, external client apps, OAuth refresh tokens, API users, Named Credentials, External Credentials, static secrets, and long-lived integration credentials. These paths can persist after business need ends and may be abused through trusted connector compromise, source exposure, admin turnover, or stolen tokens.

## Strategic Objective

Eliminate durable and reusable Salesforce credential paths while constraining remaining machine-to-machine access to explicit OAuth trust relationships.

## Attack Path Removed

```text
Stolen Token / API Credential
          ↓
Connected App / External Client App / Integration User
          ↓
Salesforce Data / API Access
```

## Architectural Deletion Goal

Remove static, stale, overbroad, and persistent integration credential material.

## Architectural Constraint Goal

Constrain required integrations to modern, scoped, auditable OAuth flows and dedicated integration identities.

## Implementation Examples

- Revoke OAuth tokens for inactive integrations and former administrators.
- Remove unused connected apps and external client apps.
- Remove hard-coded API keys, passwords, private keys, and tokens from Apex, metadata, custom settings, custom metadata, logs, and source repositories.
- Eliminate legacy username/password integrations and static password/token authentication patterns.
- Prefer OAuth 2.0 Client Credentials Flow for approved server-to-server integrations using dedicated Salesforce Integration User licenses where appropriate.
- Prefer JWT Bearer Flow for approved enterprise integrations where appropriate.
- Use dedicated integration users with minimum access and distinct auditability.
- Use Named Credentials and External Credentials for authenticated callouts where appropriate.
- Scope API access to required objects, fields, records, and operations.
- Avoid admin accounts for integrations.
- Apply connected app or external client app access policies and permission-set based access controls.

---

# SF03: System-Mode Execution & Privilege Boundary Enforcement

## Description

Apex, Flow, automation, triggers, and elevated permission assignments can allow code or users to operate outside intended sharing, object, field, and business-rule boundaries. System-mode execution can convert limited user interaction into unauthorized access or modification when privilege boundaries are not explicit.

## Strategic Objective

Reduce implicit Salesforce privilege expansion through system-mode execution and excessive permissions.

## Attack Path Removed

```text
User / Input / Automation
          ↓
System-Mode Execution or Excessive Permission
          ↓
Unauthorized Data Access or Mutation
```

## Architectural Deletion Goal

Remove unnecessary system-level execution paths and overbroad permissions.

## Implementation Examples

- Replace unnecessary `without sharing` Apex with `with sharing` or `inherited sharing`.
- Enforce object and field-level security in Apex, Flow, and automation paths.
- Remove unused Apex classes, triggers, Flows, and automation.
- Remove `Modify All Data`, `View All Data`, `Manage Users`, and other broad permissions where unnecessary.
- Use Permission Set Groups to grant narrowly scoped capabilities.
- Separate administrative, integration, support, and standard user permission models.

---

# SF04: Unauthenticated Endpoint & Remote Procedure Call Elimination

## Description

Apex REST resources, Aura-enabled methods, Lightning controller methods, Visualforce pages, webhooks, and public site endpoints can expose remote procedure call paths into Salesforce logic and data. If authentication, authorization, sharing, object, and field controls are incomplete, these endpoints can become direct execution and data-access paths.

## Strategic Objective

Eliminate unauthenticated or under-authorized Salesforce remote execution paths.

## Attack Path Removed

```text
External Request
        ↓
Unauthenticated Apex / Aura / Visualforce Endpoint
        ↓
Salesforce Logic or Data Access
```

## Architectural Deletion Goal

Remove public or unauthenticated Salesforce endpoints that are not required for business operation.

## Implementation Examples

- Remove public Apex REST endpoints that lack explicit authentication and authorization.
- Remove sensitive Aura or Lightning methods from guest-accessible contexts.
- Remove unauthenticated Visualforce pages that expose business data or actions.
- Restrict webhook entry points to explicitly validated sources.
- Require object, field, sharing, and business-rule enforcement before data access.
- Remove legacy public site pages that are no longer required.

---

# SF05: Bulk Data Extraction & Mass Enumeration Path Reduction

## Description

Salesforce breaches often become material when an attacker can enumerate and export large volumes of records through reports, APIs, Data Loader, Bulk API, report exports, dashboards, or overly broad read access. Read access becomes business impact when mass extraction paths remain available.

## Strategic Objective

Reduce paths that enable large-scale Salesforce data extraction.

## Attack Path Removed

```text
Compromised User / Integration
             ↓
Bulk Export or Enumeration Path
             ↓
Mass Data Exposure
```

## Architectural Deletion Goal

Remove unnecessary mass export, bulk API, report export, and broad enumeration capabilities.

## Implementation Examples

- Remove unnecessary `Export Reports` permissions.
- Restrict Data Loader and Bulk API use to approved integration users.
- Remove `View All Data`, `View All`, `Read All`, and broad object read access where unnecessary.
- Restrict report folders containing sensitive data.
- Remove scheduled exports that are no longer required.
- Constrain integration-user access to required objects, fields, records, and actions.
- Constrain API access for integrations to required objects and fields only.
- Monitor residual bulk data access after deletion and constraint are applied.

---

# SF06: Unconstrained Callout & External Data-Flow Erasure

## Description

Salesforce can send data externally through Apex callouts, Flow actions, External Services, Named Credentials, External Credentials, Remote Site Settings, Trusted URLs, CORS, outbound messages, webhooks, and third-party integrations. Overbroad outbound paths can enable exfiltration, SSRF-style abuse, or unauthorized data transfer.

Modern Salesforce callout architecture should prefer explicit Named Credential and External Credential trust relationships over unmanaged or legacy destination patterns.

## Strategic Objective

Eliminate arbitrary Salesforce-originated external data flows and constrain required callouts to explicit, managed external trust relationships.

## Attack Path Removed

```text
Salesforce Logic / Automation
             ↓
Unrestricted External Callout
             ↓
External Destination
```

## Architectural Deletion Goal

Remove unused, legacy, wildcard, or overly broad external destination paths.

## Architectural Constraint Goal

Migrate required external data flows to explicit Named Credential and External Credential patterns using scoped authentication and managed token exchange where supported.

## Implementation Examples

- Remove unused Remote Site Settings.
- Remove wildcard or overly broad Remote Site Settings.
- Remove unused Named Credentials.
- Remove orphaned External Credentials.
- Remove unused Trusted URLs and CORS origins.
- Remove arbitrary or user-controlled external endpoints where feasible.
- Route required authenticated callouts through approved Named Credentials.
- Use External Credentials to define authentication protocol and principal relationships for required external systems.
- Use system-managed token exchange where supported by the selected authentication pattern.
- Validate dynamic endpoints against explicit allowlists.
- Remove arbitrary `HttpRequest.setEndpoint()` paths where feasible.
- Restrict outbound messages and webhooks to approved destinations.

---

# SF07: Administrative Setup & Tooling Surface Reduction

## Description

Salesforce administrative and developer capabilities such as Setup access, Tooling API, Developer Console, API Enabled, Author Apex, debug logs, and setup visibility can expose control-plane functionality to users or integrations that do not require it.

## Strategic Objective

Reduce Salesforce administrative and tooling access paths.

## Attack Path Removed

```text
Standard User / Integration
             ↓
Administrative or Tooling Capability
             ↓
Tenant Control Plane or Sensitive Metadata
```

## Architectural Deletion Goal

Remove administrative, developer, and diagnostic capabilities from identities that do not require them.

## Implementation Examples

- Remove `Modify All Data`, `Customize Application`, and `Author Apex` from non-administrative identities.
- Remove `View Setup and Configuration` where not required.
- Remove Developer Console access from standard users.
- Restrict Tooling API and Metadata API access to approved administrators and integrations.
- Disable unnecessary Debug Logs and TraceFlags.
- Limit debug log collection to defined troubleshooting windows.
- Prevent sensitive credential or PII leakage through diagnostic logs.

---

# SF08: Cross-Org, Sandbox & External Trust Severing

## Description

Salesforce production orgs, sandboxes, development environments, connected orgs, Salesforce Connect, external objects, and third-party SaaS integrations can create trust paths between environments with different assurance levels. Lower-trust environments can become stepping stones into production if data, credentials, sessions, integrations, or trust relationships persist across boundaries.

## Strategic Objective

Remove unnecessary trust paths between production, sandbox, external, and lower-trust Salesforce environments.

## Attack Path Removed

```text
Sandbox / External Org / Third-Party Integration
                 ↓
Cross-Org Trust or Shared Credential
                 ↓
Production Salesforce Access
```

## Architectural Deletion Goal

Sever unnecessary cross-org, cross-environment, and sandbox-to-production trust relationships.

## Implementation Examples

- Mask or purge production-sensitive data during sandbox refresh.
- Remove production API tokens and integration endpoints from sandbox environments.
- Remove unnecessary Salesforce-to-Salesforce connections.
- Remove unused Salesforce Connect, OData, or external object integrations.
- Revoke connected app sessions crossing sandbox and production boundaries.
- Separate production and non-production integration credentials.
- Prevent lower-environment compromise from traversing into production.

---

# SF09: Implicit Sharing & Transitive Access Elimination

## Description

Salesforce sharing models can create implicit or transitive access through role hierarchy, groups, teams, manual sharing, Apex managed sharing, object-level `View All` or `Modify All`, parent-child access, and broad sharing rules. Attackers can exploit inherited access even when direct access appears limited.

## Strategic Objective

Eliminate unintended transitive access paths across records, objects, users, roles, and groups.

## Attack Path Removed

```text
Identity A
    ↓
Implicit Sharing / Role / Group / Delegation
    ↓
Identity B Data or Record Scope
```

## Architectural Deletion Goal

Remove unnecessary implicit sharing, broad object permissions, and transitive delegation paths.

## Implementation Examples

- Disable `Grant Access Using Hierarchies` on custom objects where managerial inheritance is not required.
- Remove broad sharing rules that do not map to explicit business rules.
- Remove legacy manual sharing entries.
- Review and reduce Apex managed sharing logic.
- Remove `View All`, `Modify All`, `Read All`, and broad object permissions where unnecessary.
- Review public groups, queues, territories, and teams that create unintended access paths.
- Enforce explicit tenant, role, object, and ownership boundaries.

---

# SF10: Dynamic Execution, Untrusted Extension & API Discovery Reduction

## Description

Dynamic SOQL/SOSL, dynamic Apex patterns, unmanaged packages, unverified AppExchange applications, external JavaScript, broad metadata/API exposure, global class visibility, and excessive schema discovery can expand attacker capability after initial access. These paths enable discovery, flexible execution, injection, and untrusted code expansion inside the Salesforce tenant.

## Strategic Objective

Reduce attacker capability expansion through dynamic execution, untrusted extensions, and excessive discovery surfaces.

## Attack Path Removed

```text
Initial Access
      ↓
Dynamic Execution / Untrusted Extension / Metadata Discovery
      ↓
Expanded Capability or Data Access
```

## Architectural Deletion Goal

Remove unnecessary dynamic code, untrusted extension, external script, global visibility, and discovery paths.

## Implementation Examples

- Replace dynamic SOQL/SOSL string concatenation with binding and safe query construction.
- Use object and field access enforcement in custom code.
- Remove unused unmanaged packages and unused AppExchange packages.
- Prefer verified and reviewed packages where third-party packages are required.
- Remove external CDN scripts from Visualforce and Lightning components where feasible.
- Host approved dependencies as verified Static Resources.
- Remove unnecessary `global` visibility from Apex classes and components.
- Restrict API access through connected app policies, external client app policies, permission sets, and integration profiles.
- Reduce metadata and schema visibility for low-privileged users and integrations.

---

# Verification & PER Measurement

## Step 1 - Establish Baseline

Identify all eligible residual Salesforce attack paths within the declared tenant, Experience Cloud, integration, and environment scope.

```text
P_eligible(t0)
```

## Step 2 - Implement Controls

Apply SF01 through SF10.

## Step 3 - Validate Erasure

Identify Salesforce attack paths rendered non-traversable.

```text
P_erased(t1)
```

## Step 4 - Calculate PER

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Success Criteria

The objective is not improved visibility alone.

The objective is measurable reduction in reachable Salesforce attack-path availability.

---

# Strategic Objective: Non-Conductive Salesforce Tenants

The goal of these subtractions is to establish deterministic boundaries within Salesforce tenants and Salesforce-integrated environments.

By collapsing residual Salesforce-specific attack paths, the Salesforce environment becomes architecturally non-conductive.

In this model:

```text
Credential / Token / Guest Access / Misconfiguration = Spark
Sharing, API, Integration, Export, or Execution Path = Oxygen
Salesforce Tenant Architecture = Conductivity
```

Remove the path, and the spark goes nowhere.

---

# Guiding Principle

Attackers can only traverse paths that exist.

The objective of Subtractive Hardening is to systematically eliminate or constrain Salesforce paths until adversary activity can no longer compose into unauthorized data exposure, mass extraction, privilege escalation, tenant control-plane abuse, or material business impact.

**Security effectiveness is maximized when attack paths are removed, not merely observed.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Salesforce REST API OAuth and Connected Apps Documentation ([Salesforce Developers](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm))
- Salesforce Named Credentials and External Credentials Documentation ([Salesforce Help](https://help.salesforce.com/s/articleView?id=sf.nc_named_creds_and_ext_creds.htm&language=en_US&type=5))
- Salesforce Integration User OAuth Client Credentials Guidance ([Salesforce Developers Blog](https://developer.salesforce.com/blogs/2024/02/invoke-rest-apis-with-the-salesforce-integration-user-and-oauth-client-credentials))
- The Science of Silence

---

*OWASP Salesforce Subtractive Hardening Top 10 v1.0*
