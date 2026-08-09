# OWASP Subtractive Third-Party Risk & Integration Governance Standard

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Governance Area:** Third-Party Risk Management & Integration Governance  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

---

# Executive Summary

The OWASP Subtractive Third-Party Risk & Integration Governance Standard provides deterministic governance guidance for managing third-party relationships according to the attack paths they introduce, rather than relying solely on questionnaire completion, vendor attestations, audit reports, or inherited trust.

Third-party vendors, service providers, partners, and integrations can create pathways for unauthorized access, data exposure, operational disruption, credential abuse, lateral movement, exfiltration, and business impact.

Vendor security controls do not replace the organization's responsibility to restrict access, control data exposure, and enforce secure integration design.

The objective of this standard is to ensure that third-party relationships are governed according to:

- the attack paths they introduce,
- the data they can access,
- the systems they can reach,
- the identities or credentials they depend on,
- the integrations they require,
- the egress or data-flow paths they enable,
- and the compensating controls required where vendor capability is insufficient.

The purpose of third-party governance is not to collect security questionnaires indefinitely.

The purpose is to eliminate, constrain, validate, monitor, and retire vendor-introduced attack paths.

---

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

```text
PER = P_erased / P_eligible
```

Where:

```text
P_eligible = Eligible attack paths identified within scope
P_erased   = Attack paths rendered non-traversable through architectural deletion
```

Third-party relationships introduce eligible attack paths through access, data exchange, identity federation, API integrations, SaaS connectivity, network tunnels, service accounts, managed services, support access, and operational dependencies.

A third-party integration improves PER when it eliminates or constrains paths that would otherwise allow unauthorized access, data exposure, privilege escalation, lateral movement, persistence, exfiltration, or operational disruption.

Third-party risk management should therefore identify:

- vendor-introduced access paths,
- vendor-introduced data paths,
- vendor-introduced identity paths,
- vendor-introduced network paths,
- vendor-introduced API and integration paths,
- vendor-introduced egress paths,
- vendor-introduced operational dependency paths,
- and vendor-introduced fourth-party or subprocessor paths.

A vendor relationship does not become low risk because a questionnaire was completed.

A vendor relationship becomes lower risk when unnecessary paths are removed, required paths are constrained, compensating controls are validated, and residual risk is explicitly accepted where unavoidable.

---

# The Subtractive Hierarchy of Third-Party Risk Governance

All third-party risk decisions should follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 - Architectural Deletion

Remove the vendor-introduced path completely.

Examples:

- Avoid direct vendor network connectivity.
- Remove unnecessary data-sharing paths.
- Remove unused vendor accounts.
- Remove persistent vendor credentials.
- Remove unnecessary identity federation.
- Remove unused API integrations.
- Remove vendor access when the business relationship ends.

## Tier 2 - Architectural Constraint

Where deletion is not feasible, constrain the vendor-introduced path.

Examples:

- Brokered or segmented access.
- Least-privilege service accounts.
- Dedicated vendor access zones.
- Controlled outbound-only integration models.
- Dataset minimization.
- Field-level masking or tokenization.
- Strong authentication and conditional access.
- Strict API scopes and rate limits.

## Tier 3 - Monitoring & Detection

Monitoring is reserved for residual vendor paths that cannot be deleted or reasonably constrained.

Examples:

- Vendor activity logging.
- Anomalous behavior alerting.
- Vendor access monitoring.
- Data transfer monitoring.
- API usage monitoring.
- Incident notification workflows.

**Architectural Deletion > Architectural Constraint > Monitoring**

Whenever a vendor-introduced attack path can be eliminated, elimination is preferred.

---

# Purpose

This standard defines how third-party vendors, service providers, partners, and integrations should be classified, assessed, governed, constrained, monitored, reassessed, and offboarded when the objective is structural attack-path reduction.

The purpose is to:

- classify third-party risk based on data sensitivity, access scope, and integration risk,
- assess vendor security posture using evidence rather than assertion alone,
- enforce secure integration design,
- minimize vendor-introduced attack paths,
- apply compensating controls where vendor capabilities are insufficient,
- govern risk acceptance and reassessment,
- and ensure vendor offboarding removes all access and data paths.

---

# Guiding Principles

## Vendors Introduce Paths

Third-party risk is created when a vendor can access systems, process data, exchange credentials, integrate with workflows, or influence operations.

## Vendor Assurance Is Not Path Removal

SOC 2 reports, questionnaires, attestations, and contractual commitments are useful evidence, but they do not by themselves remove attack paths.

## Integration Design Matters

The safest vendor relationship is one that exposes only the minimum data, access, connectivity, and authority required for the business function.

## Evidence Is Required

Vendor claims should be supported by evidence appropriate to the level of risk.

## Compensation Is Mandatory Where Vendor Controls Are Insufficient

Where a vendor cannot meet required controls, the organization must eliminate, constrain, or compensate for the residual path before accepting risk.

## Offboarding Is Path Erasure

Vendor termination must remove identity, API, network, data, and operational paths introduced by the vendor relationship.

---

# Scope

This standard applies to third-party vendors, partners, suppliers, service providers, subprocessors, contractors, managed service providers, SaaS providers, integration providers, and other external parties that:

- access organizational systems,
- process organizational data,
- store organizational data,
- transmit organizational data,
- integrate with internal or cloud-based environments,
- provide managed services,
- provide operational support,
- or influence business-critical workflows.

This standard applies to:

- SaaS integrations,
- API integrations,
- identity federation,
- privileged vendor access,
- automated data exchange,
- outsourced business processes,
- managed infrastructure services,
- network connectivity,
- private links,
- VPNs,
- support portals,
- and third-party tools used to support organizational operations.

---

# Third-Party Risk Classification

Vendors must be classified based on data sensitivity, access scope, and integration risk.

# T01: Low-Risk Third Parties

## Description

Low-risk vendors do not introduce meaningful access, data, integration, authentication, or persistent dependency paths into the organization.

## Classification Criteria

A vendor may be classified as Low Risk when all of the following are true:

- No access to internal systems.
- No access to confidential, regulated, or sensitive data.
- No persistent integration or authentication dependency.
- No automated data exchange.
- No privileged access.
- No network connectivity.

## Assessment Requirements

Low-risk vendors require:

- business owner attestation,
- confirmation that no sensitive data is exposed,
- confirmation that no system access exists,
- and security approval.

---

# T02: Medium-Risk Third Parties

## Description

Medium-risk vendors introduce limited or controlled access paths but do not possess direct infrastructure access, privileged access, or broad data access.

## Classification Criteria

A vendor may be classified as Medium Risk when one or more of the following are true:

- Access to non-sensitive or limited internal data.
- Interaction occurs only through controlled interfaces such as APIs or portals.
- Limited SaaS integration.
- Limited business process dependency.
- No direct infrastructure or network-level access.

## Assessment Requirements

Medium-risk vendors require a targeted security assessment focused on:

- data handling practices,
- authentication and access controls,
- relevant control evidence,
- integration design,
- data-flow review,
- and access-scope verification.

---

# T03: High-Risk Third Parties

## Description

High-risk vendors introduce sensitive data paths, persistent integrations, privileged access, identity trust, automated data exchange, network connectivity, or business-critical operational dependencies.

## Classification Criteria

A vendor should be classified as High Risk when any of the following are true:

- Access to sensitive, regulated, or business-critical data.
- Direct or persistent integration with internal systems.
- Identity federation.
- Privileged access.
- Automated data exchange.
- Network connectivity such as VPN, private link, or equivalent access.
- Managed service access.
- Administrative access to organizational systems.
- Material operational dependency.

## Assessment Requirements

High-risk vendors require a comprehensive assessment including:

- detailed security questionnaire,
- independent audit reports such as SOC 2 Type II or equivalent where available,
- architecture and data-flow review,
- disclosure of critical subprocessors,
- review of subprocessor governance controls,
- validation of identity and access controls,
- validation of data protection mechanisms,
- validation of logging and incident response capabilities,
- and contractual support for validation, including right-to-audit clauses where appropriate.

Security reserves the right to request additional validation, request supporting evidence, or require remediation prior to approval.

---

# Integration Security Requirements

All third-party integrations must be designed to minimize attack surface and prevent abuse, regardless of vendor risk classification.

At minimum, integrations must:

- enforce least-privilege access,
- deny access by default,
- explicitly grant only access required for defined business functions,
- restrict data access to explicitly required datasets,
- prevent unrestricted data egress,
- avoid persistent or unnecessary connectivity,
- use identity-bound and auditable authentication mechanisms,
- document data sources, destinations, and permitted transfer paths,
- and define ownership for the integration.

Where possible, organizations should:

- avoid direct network connectivity,
- use brokered or segmented access models,
- prefer outbound-only controlled integrations,
- ensure all access is logged and attributable,
- and remove integrations when business need ends.

---

# Compensating Controls Requirement

Where a vendor does not meet required security standards, compensating controls must be implemented to reduce risk to an acceptable level.

## When Compensating Controls Are Required

Compensating controls are mandatory when:

- a vendor lacks required security capabilities,
- identified risks cannot be remediated by the vendor in a timely manner,
- residual risk exceeds acceptable thresholds,
- vendor access cannot be eliminated,
- vendor data exposure cannot be eliminated,
- or integration paths cannot be removed without disrupting required business services.

## Acceptable Compensating Controls

Compensating controls must be:

- technical where feasible,
- procedural only where technical controls are unavailable,
- directly mapped to the identified risk,
- verifiable,
- enforceable,
- tested for effectiveness,
- and revalidated during reassessment cycles.

## Access & Identity Controls

Examples include:

- restrict vendor access to dedicated service accounts,
- enforce strong authentication,
- enforce conditional access,
- eliminate shared credentials,
- eliminate persistent credentials,
- use scoped API tokens,
- and require identity-bound authentication.

## Network & Connectivity Controls

Examples include:

- segmentation of vendor access zones,
- prohibition of inbound connections from vendor environments,
- controlled outbound-only access,
- strict egress filtering,
- private access mediation,
- and removal of unnecessary network tunnels.

## Data Protection Controls

Examples include:

- tokenization,
- masking of sensitive data,
- limiting data exposure to minimum required fields,
- restricting bulk extraction,
- preventing unrestricted exports,
- and separating production data from non-production vendor workflows.

## Monitoring & Detection Controls

Examples include:

- enhanced logging of vendor activity,
- alerting on anomalous vendor behavior,
- independent monitoring of vendor access patterns,
- alerting on bulk data movement,
- and incident notification paths.

Monitoring should not be used as a substitute for deletion or constraint where deletion or constraint is feasible.

---

# Order of Preference for Third-Party Risk Treatment

Third-party risk must be addressed using the following order of preference:

1. Eliminate the risk by avoiding or redesigning the integration.
2. Reduce exposure by limiting access, data, authority, connectivity, or persistence.
3. Apply compensating controls.
4. Accept residual risk as a last resort.

Risk acceptance must never be used to replace feasible deletion, constraint, or compensating control implementation.

---

# Control Validation Requirements

Controls must be validated through evidence, not assertion alone.

Validation should demonstrate that the control prevents or materially limits the identified risk scenario.

Examples include:

- unauthorized access attempt blocked,
- bulk data extraction prevented,
- vendor account restricted to approved datasets,
- network path blocked,
- API scope enforced,
- egress limited to approved destinations,
- identity federation restricted,
- or vendor access revoked successfully.

Compensating controls must be revalidated during reassessment cycles.

---

# Risk Acceptance

If residual risk remains after applying deletion, constraint, and compensating controls, formal risk acceptance is required.

Risk acceptance must include:

- description of the residual risk,
- attack-path impact,
- business impact analysis,
- compensating controls in place,
- residual exposure statement,
- business owner approval,
- security leadership approval,
- defined expiration date,
- and reassessment criteria.

Risk acceptance must be time-bound and should not exceed one year without formal reassessment.

---

# Reassessment and Continuous Oversight

Third-party vendors must be reassessed based on risk classification and material changes.

Medium-risk and high-risk vendors should be reassessed at least annually.

Reassessment is also required upon:

- contract renewal,
- material changes in integration or access,
- changes in data types processed,
- movement from public to sensitive or regulated data,
- architectural changes such as SaaS to on-premises or VPN-enabled access,
- vendor ownership changes,
- new subprocessors,
- security incident involving the vendor,
- or expanded scope of service.

Security may require ad hoc reassessment at any time.

Security may suspend or restrict vendor access pending investigation where a vendor is suspected or confirmed to be involved in a security incident.

---

# Vendor Termination and Offboarding

Vendor offboarding is path erasure.

When a vendor relationship ends, all vendor-introduced access, identity, data, network, API, and operational paths must be removed.

Termination and offboarding must include:

- return of organizational data where applicable,
- certified destruction of organizational data retained by the vendor where applicable,
- revocation of identity federation,
- revocation of API keys,
- revocation of service accounts,
- revocation of vendor portal access,
- revocation of network tunnels,
- removal of private links or equivalent connectivity,
- termination of automated data exchange,
- verification that access has been removed,
- and retention of vendor activity logs according to organizational logging standards.

Identity federation, API keys, and network tunnels should be revoked within the required organizational offboarding timeline and verified through documented evidence.

---

# Roles and Responsibilities

## Business Owner

The Business Owner:

- initiates vendor assessment,
- identifies business need,
- confirms required scope of vendor access,
- participates in risk acceptance decisions,
- and ensures continued business justification for the vendor relationship.

## Security Team

The Security Team:

- conducts or reviews assessments,
- defines required controls,
- validates compensating controls,
- reviews vendor-introduced attack paths,
- approves or rejects vendor risk,
- and may suspend access where risk exceeds acceptable thresholds.

## Legal / Compliance

Legal and Compliance:

- ensure contractual protections,
- support regulatory alignment,
- review data protection requirements,
- support audit and evidence rights,
- and ensure termination and data-return clauses are included where appropriate.

## Vendor Owner / Functional Unit Owner

The Vendor Owner or Functional Unit Owner:

- owns technical integration details,
- documents data flows,
- identifies required access paths,
- ensures approved architecture is followed,
- and coordinates remediation or offboarding.

---

# Third-Party Risk Metrics

Third-party governance should track metrics that reflect path reduction rather than questionnaire completion alone.

Recommended metrics include:

- number of active high-risk vendors,
- number of vendors with direct network connectivity,
- number of vendors with privileged access,
- number of vendors with identity federation,
- number of vendors with persistent API keys,
- number of vendors with sensitive data access,
- number of vendors with unmanaged subprocessors,
- number of vendor paths eliminated,
- number of vendor paths constrained,
- number of integrations converted to brokered or outbound-only models,
- number of vendor access paths revoked during offboarding,
- number of exceptions tied to third-party relationships,
- number of overdue reassessments,
- and number of vendor relationships retired through path elimination.

---

# Verification & PER Measurement

## Step 1 - Establish Vendor Path Context

Identify vendor-introduced paths.

Examples:

- access paths,
- data paths,
- identity paths,
- network paths,
- API paths,
- egress paths,
- and operational dependency paths.

```text
P_vendor(t0)
```

## Step 2 - Classify Vendor Risk

Classify vendor risk based on data sensitivity, access scope, and integration risk.

## Step 3 - Apply Deletion Where Feasible

Remove unnecessary vendor paths.

Examples:

- remove unused accounts,
- remove unnecessary data sharing,
- remove unnecessary network connectivity,
- remove unnecessary federation,
- remove unused API integrations,
- and avoid direct access where brokered access is sufficient.

## Step 4 - Apply Constraint Where Deletion Is Not Feasible

Constrain required paths through least privilege, segmentation, scoped access, egress filtering, brokered access, and data minimization.

## Step 5 - Validate Controls

Confirm that controls prevent or materially limit the identified vendor risk scenario.

## Step 6 - Measure Path Reduction

Update PER based on vendor-introduced paths erased or constrained.

```text
PER(t1) = P_erased(t1) / P_eligible(t1)
```

## Success Criteria

The objective is not completed questionnaires.

The objective is measurable reduction in vendor-introduced attack paths.

---

# Strategic Objective: Third-Party Path Reduction

The goal of this standard is to ensure third-party relationships do not introduce unnecessary attack paths into the organization.

In this model:

```text
Vendor Relationship = Potential Path Source
Integration Design = Path Shape
Data Scope = Exposure Boundary
Compensating Control = Conductivity Reduction
Offboarding = Path Erasure
```

A third-party relationship is secure when the vendor can access only what is required, only through controlled paths, only for the required purpose, and only for as long as the business need exists.

---

# Statement of Intent

Third-party risk management should not become a paperwork exercise.

Vendor attestations, questionnaires, and audit reports are useful, but they do not replace architectural control over vendor-introduced paths.

The purpose of third-party governance is to eliminate unnecessary vendor paths, constrain required paths, validate controls, and retire vendor access when business need ends.

**A vendor path that cannot be removed must be constrained, monitored, time-bounded, and periodically revalidated.**

---

# References

- OWASP Subtractive Hardening Top 10 Project ([OWASP Project Repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main))
- Path Erasure Rate (PER-1.0) Engineering Standard ([PER-1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md))
- Evidence-Based Security ([Evidence-Based Security Article](https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and))
- The Law of Subtractive Risk ([The Law of Subtractive Risk](https://subtractivesecurity.substack.com/p/the-law-of-subtractive-risk-moving))
- The Science of Silence

---

*OWASP Subtractive Third-Party Risk & Integration Governance Standard v1.0*
