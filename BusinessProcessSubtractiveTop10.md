# OWASP Fraud & Insider Risk Subtractive Hardening Top 10

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Platform:** Business Processes, Financial Workflows, Fraud Prevention, and Insider Risk  
**Specification Alignment:** OWASP Universal Subtractive Security Laws v1.0 and PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

# Executive Summary

The OWASP Fraud & Insider Risk Subtractive Hardening Top 10 provides deterministic engineering guidance for reducing fraud and insider risk through the elimination of attacker-accessible authority, trust, approval, payment, data-access, delegation, and business-process paths.

Unlike traditional fraud and insider-risk programs that focus primarily on awareness training, behavioral monitoring, anomaly detection, case management, transaction review, or post-event investigation, Subtractive Hardening prioritizes removal of the organizational and procedural conditions that allow external influence, compromised identities, malicious insiders, collusion, or routine human error to compose into material financial, operational, regulatory, data, or reputational impact.

Rather than relying on reactive detection, employee vigilance, or manual intervention as the primary control mechanism, the objective is to physically remove or deterministically constrain conductive edges from the business-process graph.

System Graph:

```
G = (V,E)
```

Where:

```
V = Employees, Contractors, Executives, Vendors, Customers, Approvers,
    Business Processes, Financial Systems, HR Systems, Procurement Systems,
    Data Stores, Accounts, Transactions, Records, and External Destinations

E = Trust, Authority, Approval, Delegation, Authentication, Authorization,
    Access, Modification, Payment, Data-Flow, Communication, or Control Relationships
```

Each recommendation within this standard is intentionally selected based on its ability to reduce adversary and insider reachability and improve measurable attack-path reduction through the Path Erasure Rate (PER) Engineering Standard.

```
PER = P_erased / P_eligible
```

Where:

```
P_eligible = Eligible fraud, insider-abuse, and business-process attack paths identified within scope
P_erased   = Paths rendered non-traversable through architectural or procedural deletion
```

The objective of this standard is not to make fraud or insider abuse easier to detect.

The objective is to make material abuse impossible or non-composable by removing the authority and process pathways that enable it.

# Boundary Scope Note

This standard focuses on adversarial and unauthorized paths within business processes, financial workflows, organizational authority structures, sensitive-data workflows, and insider-access models.

The following technical attack surfaces are addressed by parallel platform standards:

- Endpoint exploitation
- Operating-system compromise
- Network-layer compromise
- Cloud control-plane compromise
- Microsoft 365 compromise
- Application and API exploitation
- Datastore compromise
- CI/CD and software supply-chain compromise
- Identity-platform compromise

Technical compromise may initiate or accelerate fraud and insider-risk paths, but this standard focuses on the residual business-process pathways through which influence or access becomes material impact.

# Relationship to the Universal Subtractive Security Laws

This standard instantiates the OWASP Universal Subtractive Security Laws within fraud, insider-risk, financial, HR, procurement, customer-service, and other business-process contexts.

The underlying laws remain consistent:

- Adjacent reachability appears as unnecessary access from one business function, role, or actor to another stage of a sensitive process.
- Static credentials appear as permanent approval rights, standing payment authority, reusable delegated access, or persistent access to sensitive records.
- Unauthenticated control planes appear as email-only instructions, unverified callbacks, informal chat approvals, or identity assertions that can directly change authoritative records.
- Unconstrained egress appears as arbitrary payment destinations, unrestricted data export, unsupervised refunds, or uncontrolled disclosure channels.
- Management interfaces appear as vendor-master administration, payroll administration, treasury consoles, HR-system administration, and privileged case-management functions.
- Cross-domain trust appears as external communications or lower-trust functions directly influencing higher-impact financial, HR, legal, or operational processes.
- Privilege surface appears as excessive approval limits, incompatible duties, standing override authority, bulk export rights, or unrestricted record-modification capability.
- Transitive delegation appears as inherited approval, executive impersonation, proxy authority, emergency overrides, or broad delegated decision rights.
- Integrity verification appears as validation of payees, instructions, supporting documents, transaction data, authoritative records, and change provenance.
- Automatic discovery and trust appear as auto-populated recipients, inherited vendor details, automatic routing, workflow auto-approval, or unverified synchronization of authoritative data.

This standard provides business-process implementation guidance for those universal laws.

# Relationship to PER-1.0

The Path Erasure Rate (PER) provides a quantitative measure of structural attack-path reduction.

The Fraud & Insider Risk Subtractive Hardening Top 10 provides practical guidance for identifying and erasing paths through which external actors, compromised identities, insiders, or colluding parties can reach material business impact.

Together they establish a repeatable engineering cycle:

1. Identify fraud, insider-abuse, and business-process attack paths.
2. Measure process-path exposure.
3. Eliminate paths where possible.
4. Constrain residual paths where deletion is not feasible.
5. Validate that prohibited outcomes cannot be completed.
6. Measure the resulting path reduction.
7. Continuously improve business-process non-conductivity.

# The Subtractive Hierarchy of Efficacy

All recommendations within this standard follow the Subtractive Security Hierarchy of Efficacy.

## Tier 1 - Business-Process Path Deletion

Remove the fraud or insider-abuse path completely.

Examples:

- Remove single-person transaction authority.
- Remove the ability to create and approve the same vendor.
- Remove permanent payment-release authority.
- Remove email as an authoritative change channel.
- Remove unnecessary bulk data-export rights.
- Remove direct access from lower-trust roles to high-impact records.
- Remove dormant delegated authority.

## Tier 2 - Deterministic Process Constraint

Where deletion is not feasible, constrain the path.

Examples:

- Segregation of duties
- Dual or independent approval
- Transaction limits
- Destination allowlists
- Out-of-band verification
- Just-in-time authority
- Purpose-bound data access
- Immutable workflow gates
- Independent reconciliation
- Time-, value-, and scope-bound delegation

## Tier 3 - Monitoring & Detection

Monitoring is reserved for residual paths that cannot be deleted or reasonably constrained.

Examples:

- Transaction monitoring
- Behavioral analytics
- Insider-risk analytics
- Data-loss prevention alerts
- Fraud case management
- Exception reporting
- Audit logging
- Post-transaction review

**Business-Process Deletion > Deterministic Constraint > Monitoring**

Whenever a fraud or insider-risk path can be eliminated, elimination is preferred. If elimination is not feasible, the path should be constrained. Monitoring is reserved for residual paths that cannot be removed or sufficiently constrained.

# Selection Methodology

Entries included within this Top 10 were selected according to their ability to:

- Eliminate single-actor paths to material impact.
- Reduce unnecessary authority and process reachability.
- Reduce payment-diversion opportunities.
- Reduce vendor-master and payroll manipulation opportunities.
- Reduce insider data-access and extraction opportunities.
- Reduce implicit trust and delegated-authority paths.
- Reduce cross-function and cross-domain propagation.
- Reduce fraud-path composability.
- Reduce dependence on perfect human judgment.
- Improve measurable Path Erasure Rate (PER).

Recommendations are not ranked based on:

- Fraud-loss estimates alone
- Risk heat-map scores
- Training completion rates
- Alert volume
- Case volume
- Policy coverage
- Audit findings
- Vendor capability claims
- Control-count maturity

The primary selection criterion is architectural and procedural impact through adversarial path reduction.

# OWASP Fraud & Insider Risk Subtractive Hardening Top 10

| ID | Title | Primary Universal-Law Alignment |
| --- | --- | --- |
| F01 | Single-Actor Material Action Path Elimination | U01, U07 |
| F02 | External Instruction & Identity-Assertion Path Severing | U03, U06 |
| F03 | Vendor, Payee & Destination Change Path Erasure | U04, U05, U09 |
| F04 | Persistent Authority & Standing Delegation Elimination | U02, U08 |
| F05 | Cross-Function & Incompatible-Duty Path Severing | U06, U07 |
| F06 | Sensitive Data Access & Extraction Path Reduction | U04, U07 |
| F07 | Override, Emergency & Exception Path Constraint | U05, U08 |
| F08 | Authoritative Record & Transaction Integrity Enforcement | U09 |
| F09 | Automatic Trust, Routing & Workflow Propagation Deletion | U08, U10 |
| F10 | Insider Offboarding & Residual Authority Extinction | U02, U05, U08 |

# F01: Single-Actor Material Action Path Elimination

## Description

Any business process that allows one person, identity, or service to initiate, approve, and complete a material action creates a direct path from compromised or malicious context to impact.

This condition commonly appears in payment release, refunds, journal entries, payroll changes, vendor creation, customer credits, purchasing, data export, account recovery, entitlement changes, and destructive administrative actions.

## Strategic Objective

Eliminate single-actor pathways to material financial, operational, data, or regulatory impact.

## Attack Path Removed

```
Single Actor / Compromised Identity
                ↓
     Unilateral Material Authority
                ↓
        Irreversible Business Impact
```

## Architectural Deletion Goal

Remove the ability of one principal to complete every required state transition from request initiation to material impact.

A claimed multi-person control must be implemented through independently attributable principals and independently enforced authorization decisions. Shared mailboxes, shared accounts, shared credentials, generic service accounts, common workflow identities, or any other principal accessible by multiple actors do not establish independent approval. They collapse the apparent multi-principal design back into a single traversable principal path.

## Collusion Threshold Model

Separation of duties does not eliminate every possible collusive path. It deterministically raises the minimum number of independent principals required to complete the prohibited outcome.

Let:

```
k = Minimum number of independent principals required to complete the material action
n = Total number of eligible principals within the declared approval population
```

Tier 1 deletion under F01 eliminates all single-principal paths where `k = 1` and establishes a deterministic lower bound of `k >= 2` within the declared scope. This does not claim that collusion is impossible. It proves that a lone compromised, coerced, mistaken, or malicious principal cannot independently reach impact and forces an adversary to recruit or compromise additional independent principals.

The declared assessment scope must state the collusion threshold being tested. If the control objective is resistance to two-person collusion, the architecture must enforce `k >= 3`, and the corresponding test must attempt the action using two independent principals.

Independence requires distinct, attributable identities and separately enforced decisions. Two people using the same mailbox, account, credential, service identity, browser session, API token, approval queue, or unattended automation do not satisfy `k = 2`. Shared principals collapse `k >= 2` back to `k = 1`.

## Implementation Examples

- Separate transaction initiation from approval and release.
- Prevent the same person from creating and approving a vendor.
- Require independent approval for refunds above defined limits.
- Require two-person control for payroll creation and activation.
- Prevent one administrator from both granting and using high-impact authority.
- Separate data-export request, authorization, and execution.
- Remove direct user capability to bypass mandatory workflow gates.

## Erasure Criteria

For the single-principal path class, `P_erased = 1` when no single independent principal can complete the scoped material action through normal, delegated, emergency, administrative, API, batch, service-account, shared-mailbox, or alternate workflow paths, and the enforced collusion threshold is `k >= 2`.

If any single-actor bypass remains available, or if multiple nominal approvers act through a shared principal that one actor can control, `P_erased = 0` for that path.

A higher-order collusion path is counted separately. A control that eliminates all `k = 1` paths may receive erasure credit for that defined path class without claiming elimination of `k >= 2` collusion paths. The PER denominator and validation record must identify the threshold and path class being measured.

# F02: External Instruction & Identity-Assertion Path Severing

## Description

Business email compromise, vendor impersonation, executive impersonation, social engineering, and account-recovery fraud rely on external or weakly authenticated communications being accepted as authoritative instructions.

Email addresses, caller ID, display names, signatures, chat accounts, known facts, and apparent urgency are identity assertions, not deterministic proof of authority.

## Strategic Objective

Sever direct paths from unverified communications to sensitive business actions.

## Attack Path Removed

```
External or Compromised Communication
                  ↓
         Unverified Identity Claim
                  ↓
          Sensitive Business Action
```

## Architectural Deletion Goal

Remove communication channels such as email, text, voice, or chat as sufficient standalone authorization for high-impact changes or transactions.

## Implementation Examples

- Prohibit payment release based solely on email instructions.
- Require independent verification through an approved channel.
- Use pre-established contacts rather than contact details supplied in the request.
- Prevent executive urgency from overriding mandatory approval controls.
- Require authenticated workflow initiation for sensitive requests.
- Remove help-desk account-recovery paths based solely on biographical knowledge.
- Require verified requests for payroll, benefits, bank-account, and direct-deposit changes.

## Erasure Criteria

`P_erased = 1` when an unverified communication cannot directly produce a material change, even if the message is convincing, originates from a compromised account, or impersonates an authorized person.

# F03: Vendor, Payee & Destination Change Path Erasure

## Description

Fraud frequently succeeds by changing authoritative destination data before a legitimate transaction executes. Common targets include vendor banking details, settlement accounts, payroll destinations, refund destinations, mailing addresses, payment tokens, and customer payout instructions.

## Strategic Objective

Eliminate direct and unverified paths from a change request to an approved payment or data destination.

## Attack Path Removed

```
Fraudulent Change Request
            ↓
Authoritative Destination Modification
            ↓
Legitimate Process Sends Value to Attacker
```

## Architectural Deletion Goal

Ensure destination changes cannot be requested, approved, and activated through a single channel, actor, or unchecked workflow.

## Implementation Examples

- Separate vendor creation from banking-detail modification.
- Require independent verification for payee or bank-account changes.
- Use known contact records rather than request-supplied contact information.
- Delay activation of high-risk destination changes where operationally feasible.
- Require independent approval before the first payment to a changed destination.
- Restrict destination changes to designated roles and controlled workflows.
- Limit payments to approved destinations where business processes permit.
- Notify independent stakeholders of material destination changes.

## Erasure Criteria

`P_erased = 1` when possession of one communication channel, one employee identity, or one application session cannot both change a destination and cause value to be sent to it.

# F04: Persistent Authority & Standing Delegation Elimination

## Description

Permanent approval rights, standing transaction authority, persistent proxy access, broad delegated authority, and reusable emergency privileges create durable paths that survive role changes, compromise, absence, and organizational drift.

In business processes, standing authority functions as a persistent credential.

## Strategic Objective

Eliminate persistent high-impact authority and unconstrained delegation wherever feasible.

## Attack Path Removed

```
Compromised or Malicious Principal
               ↓
      Persistent Standing Authority
               ↓
       Repeated or Delayed Impact
```

## Architectural Deletion Goal

Replace permanent and broadly reusable authority with time-bound, purpose-bound, value-bound, and transaction-bound authorization.

Authority must remain bound to independently attributable human or workload principals. Shared mailboxes, shared administrative accounts, common credentials, generic service accounts, and unattended workflow identities must not be used to simulate independent delegation or approval. When multiple actors can exercise the same principal, the authorization graph contains one reusable authority edge, not multiple independent decision points.

## Implementation Examples

- Use just-in-time approval or payment-release authority.
- Expire delegated authority automatically.
- Limit delegation by amount, process, legal entity, destination, and duration.
- Remove dormant approvers and unused proxy relationships.
- Prevent sub-delegation unless explicitly authorized.
- Eliminate shared mailboxes, shared accounts, shared credentials, and generic service identities as approval principals.
- Bind automation to a narrowly scoped workload identity that cannot independently originate and approve the same material action.
- Require reauthorization following role or organizational changes.
- Remove standing emergency privileges after the approved event.

## Erasure Criteria

`P_erased = 1` when the scoped authority cannot be reused outside its approved purpose, value, time, and process boundaries and cannot be exercised through a shared principal that collapses independent authorization into `k = 1`.

If a shared mailbox, shared account, common credential, service account, unattended automation, or equivalent principal can originate, approve, release, or bypass the scoped action without an independent authorization decision, `P_erased = 0` for that path.

# F05: Cross-Function & Incompatible-Duty Path Severing

## Description

Fraud and insider abuse become composable when one principal or colluding group can cross business-function boundaries that should remain independent. Examples include procurement-to-payment, HR-to-payroll, sales-to-refund, development-to-production, case creation-to-case closure, and access request-to-access approval.

## Strategic Objective

Sever authority paths between incompatible functions and prevent one compromised context from controlling an end-to-end process.

## Attack Path Removed

```
Lower-Control or Initiating Function
                 ↓
      Cross-Function Authority Path
                 ↓
      High-Impact Execution Function
```

## Architectural Deletion Goal

Separate initiation, authorization, execution, custody, and reconciliation where their combination would create a material abuse path.

## Implementation Examples

- Separate procurement, vendor administration, invoice approval, and payment release.
- Separate HR employee creation from payroll activation.
- Separate sales concessions from refund execution.
- Separate privileged-access request from approval and provisioning.
- Separate transaction execution from reconciliation.
- Prevent system administrators from approving their own access.
- Require independent review of transactions involving related parties or conflicts of interest.

## Erasure Criteria

`P_erased = 1` when compromise or misuse of one function cannot independently traverse into the incompatible execution or reconciliation function.

# F06: Sensitive Data Access & Extraction Path Reduction

## Description

Insider data theft, privacy abuse, customer-data misuse, trade-secret theft, and extortion require paths from an authorized or compromised context to sensitive information and then to a removable, exportable, transferable, or externally usable form.

## Strategic Objective

Reduce unnecessary access, aggregation, export, and transfer pathways for sensitive information.

## Attack Path Removed

```
Employee / Contractor / Compromised Identity
                     ↓
          Excessive Sensitive Data Access
                     ↓
          Collection, Export, or Disclosure
```

## Architectural Deletion Goal

Remove access to data outside legitimate purpose and remove unnecessary paths for bulk collection, export, forwarding, printing, copying, synchronization, or external transfer.

## Implementation Examples

- Restrict access by role, purpose, dataset, field, customer, case, and duration.
- Remove bulk export where it is not required.
- Separate search access from export capability.
- Prevent arbitrary external forwarding or sharing.
- Limit local download and removable-media paths where feasible.
- Use purpose-bound or case-bound access.
- Remove access promptly when work assignments end.
- Minimize replicated datasets and secondary copies.

## Erasure Criteria

`P_erased = 1` when the scoped principal cannot access or extract the protected dataset beyond the minimum approved business purpose through any available interface or alternate process.

# F07: Override, Emergency & Exception Path Constraint

## Description

Override, emergency, break-glass, manual adjustment, exception, and expedited-processing mechanisms frequently bypass the controls applied to normal workflows. These paths become preferred attack routes when they are broad, persistent, weakly approved, or poorly bounded.

## Strategic Objective

Eliminate unnecessary override paths and tightly constrain residual emergency or exceptional authority.

## Attack Path Removed

```
Actor
  ↓
Override / Emergency / Exception Mechanism
  ↓
Bypass of Normal Control Boundary
  ↓
Material Action
```

## Architectural Deletion Goal

Remove permanent or discretionary bypass mechanisms and ensure necessary exceptions cannot silently recreate the prohibited path.

## Implementation Examples

- Remove unused override features.
- Require explicit time-bound activation of emergency authority.
- Prevent self-approval of overrides.
- Scope overrides to a defined transaction, case, system, amount, and duration.
- Require independent post-use validation without treating review as a substitute for constraint.
- Automatically revoke emergency privileges.
- Prevent local administrators from disabling mandatory workflow controls.
- Track exceptions as temporary path debt with a defined elimination date.

## Erasure Criteria

`P_erased = 1` when no standing or self-authorized bypass can recreate the prohibited business-process path.

# F08: Authoritative Record & Transaction Integrity Enforcement

## Description

Fraud and insider abuse often depend on altering records, supporting documents, transaction fields, evidence, logs, reconciliation data, or approval context while preserving the appearance of a legitimate workflow.

## Strategic Objective

Eliminate unverified or unattributable modification paths into authoritative business records and transactions.

## Attack Path Removed

```
Unverified or Unauthorized Change
                ↓
      Authoritative Business Record
                ↓
     Trusted Decision or Transaction
```

## Architectural Deletion Goal

Prevent authoritative processes from consuming unverified, unauthenticated, or insufficiently attributable changes.

## Implementation Examples

- Require authenticated and attributable record changes.
- Preserve immutable approval and change provenance.
- Prevent approvers from modifying material fields after approval begins.
- Invalidate prior approvals when material transaction fields change.
- Require independent source validation for critical supporting documents.
- Restrict deletion or alteration of reconciliation and audit records.
- Protect transaction templates and payment files from unauthorized modification.
- Verify integrity at the point of execution, not only at creation.

## Erasure Criteria

`P_erased = 1` when an unverified or unauthorized modification cannot enter or remain within the authoritative record used to drive the scoped action.

# F09: Automatic Trust, Routing & Workflow Propagation Deletion

## Description

Automatic routing, inherited trust, auto-approval, default recipients, convenience workflows, synchronized master data, and rules based on weak signals can propagate a fraudulent or malicious input through a business process without independent challenge.

## Strategic Objective

Eliminate automatic trust establishment and unintended propagation within sensitive workflows.

## Attack Path Removed

```
Untrusted or Manipulated Input
             ↓
Automatic Trust / Routing / Inheritance
             ↓
Sensitive Workflow or Additional Authority
```

## Architectural Deletion Goal

Remove automation that converts unverified input into authority, routing, payment, access, or sensitive-data exposure.

## Implementation Examples

- Disable auto-approval for material transactions.
- Prevent automatic trust based solely on sender, title, department, or prior communication.
- Remove auto-populated payment destinations from unverified sources.
- Require validation before synchronized master-data changes become authoritative.
- Limit workflow rules that redirect approvals or notifications.
- Remove automatic delegation based only on absence or hierarchy.
- Prevent unreviewed rules from suppressing independent approvers.
- Reduce topology disclosure that helps insiders identify high-value processes or approvers.

## Erasure Criteria

`P_erased = 1` when unverified input cannot automatically acquire trust, propagate authority, redirect a process, or reach a material action.

# F10: Insider Offboarding & Residual Authority Extinction

## Description

Departed employees, transferred personnel, contractors, vendors, temporary workers, and role-changed users may retain access, delegated authority, shared knowledge, payment capability, data access, approval rights, physical access, recovery channels, or informal influence after the legitimate need ends.

## Strategic Objective

Eliminate residual authority, access, trust, and process reachability when employment, assignment, contract, or business need ends or materially changes.

## Attack Path Removed

```
Former or Role-Changed Principal
              ↓
Residual Access / Authority / Trust
              ↓
Delayed Insider Abuse or Unauthorized Action
```

## Architectural Deletion Goal

Remove all technical, procedural, physical, and organizational paths associated with ended or changed authority.

## Implementation Examples

- Revoke system, application, financial, physical, and remote access.
- Remove payment, refund, payroll, vendor, procurement, and approval rights.
- Remove proxy, delegation, shared-mailbox, and workflow assignments.
- Rotate shared secrets and remove shared knowledge paths where feasible.
- Transfer ownership of records, queues, contracts, cases, and approvals.
- Remove external forwarding, personal synchronization, and recovery destinations.
- Terminate vendor and contractor trust paths at the end of need.
- Validate revocation across alternate interfaces and emergency processes.

## Erasure Criteria

`P_erased = 1` when the former or role-changed principal cannot access, approve, modify, influence, recover, or execute the scoped business process through any residual path.

# Example Attack-Path Mappings

## Business Email Compromise and Payment Diversion

```
External Actor
      ↓
Compromised or Impersonated Communication
      ↓
Employee Trust
      ↓
Vendor / Payee Destination Change
      ↓
Payment Approval
      ↓
Funds Transfer
```

Primary subtractive interventions:

- **F02:** Email or voice cannot serve as sufficient authorization.
- **F03:** Destination changes require independent verified workflow.
- **F01:** One person cannot change and release payment.
- **F05:** Vendor administration and treasury execution remain separate.
- **F08:** Material field changes invalidate existing approvals.

## Ghost Employee and Payroll Fraud

```
Insider
   ↓
Employee Record Creation
   ↓
Payroll Activation
   ↓
Bank Destination Assignment
   ↓
Recurring Payment
```

Primary subtractive interventions:

- **F01:** One principal cannot create, activate, and pay an employee.
- **F05:** HR record creation and payroll activation are separated.
- **F03:** Payment destinations require independent verification.
- **F08:** Payroll master-data changes retain verified provenance.
- **F09:** New records do not automatically become payable.

## Malicious Insider Data Theft

```
Authorized Insider
       ↓
Broad Sensitive Data Access
       ↓
Bulk Collection or Export
       ↓
External Transfer
```

Primary subtractive interventions:

- **F06:** Access, aggregation, export, and transfer paths are reduced.
- **F04:** Standing bulk-export authority is eliminated.
- **F05:** Access and export approval are separated.
- **F10:** Access is extinguished when role or employment ends.

## Refund or Credit Abuse

```
Employee / Compromised Account
              ↓
Customer or Transaction Selection
              ↓
Refund / Credit Creation
              ↓
Destination Selection
              ↓
Funds Release
```

Primary subtractive interventions:

- **F01:** One principal cannot create and release a material refund.
- **F03:** Refund destinations cannot be arbitrarily changed.
- **F04:** High-value refund authority is temporary and bounded.
- **F08:** Transaction and approval integrity are preserved.

## Procurement and Kickback Fraud

```
Insider / Colluding Vendor
          ↓
Vendor Creation or Selection
          ↓
Purchase Approval
          ↓
Receipt Confirmation
          ↓
Invoice Approval
          ↓
Payment Release
```

Primary subtractive interventions:

- **F01:** No single principal controls the end-to-end path.
- **F05:** Procurement, receipt, invoice approval, and payment are separated.
- **F03:** Vendor and destination changes are independently verified.
- **F08:** Supporting records and approvals retain integrity.
- **F09:** Vendor status does not automatically propagate trust.

# Verification & PER Measurement

## Step 1 - Declare Scope

Define the business process, material impact, system boundaries, actors, decision rights, authoritative records, and transaction stages included in measurement.

Examples:

- Vendor onboarding and payment
- Wire transfer
- Customer refund
- Payroll onboarding
- Direct-deposit modification
- Procurement and invoice payment
- Privileged access approval
- Sensitive-data export
- Employee offboarding

## Step 2 - Establish the Baseline

Identify all eligible paths from an external actor, insider, compromised identity, error, or colluding group to material business impact.

```
P_eligible(t0)
```

Eligible paths should include:

- Normal workflows
- Administrative interfaces
- Alternate channels
- Batch processes
- APIs and integrations
- Delegated authority
- Emergency and override paths
- Shared accounts or roles
- Manual workarounds
- After-hours processes
- Temporary and contractor access

## Step 3 - Apply F01 Through F10

Apply business-process deletion and deterministic constraints to erase or sever eligible paths.

## Step 4 - Validate Erasure

Attempt the prohibited outcome under realistic assumptions, including compromised identities, malicious insiders, convincing external instructions, collusion within declared scope, alternate channels, and known exception paths.

```
P_erased(t1)
```

Validation should determine whether the prohibited action can still be completed, not merely whether a control is documented, assigned, enabled, or monitored.

## Step 5 - Calculate PER

```
PER(t1) = P_erased(t1) / P_eligible(t0)
```

For ongoing measurement, organizations should preserve the original baseline or explicitly declare changes in scope so path reduction is not overstated by removing paths from the denominator without remediation.

## Success Criteria

The objective is not improved visibility, higher training completion, increased alert volume, or a larger fraud-control inventory.

The objective is measurable reduction in the availability of paths capable of composing into material business impact.

# Falsification Tests

Each claimed path erasure should be expressed as a binary proposition capable of being disproven.

Examples:

- A single finance user cannot create a vendor, modify banking details, and release payment.
- An email request alone cannot change a payment destination.
- A former employee cannot approve, modify, export, or recover access to the scoped process.
- A payroll administrator cannot independently create and activate a payable employee.
- A customer-service identity cannot redirect a refund to an unrelated destination.
- An approver cannot preserve approval after a material transaction field changes.
- A delegated approver cannot act outside the approved amount, process, or time window.
- A user with search access cannot perform bulk export unless the export path is separately authorized.

If the prohibited outcome succeeds, the control claim is falsified and the path remains eligible for remediation.

# Defense in Depth Through Layered Business-Process Path Erasure

Subtractive Security recognizes that all controls may fail due to misconfiguration, collusion, process drift, emergency workarounds, application defects, incomplete deployment, role changes, or changing business requirements.

Organizations should therefore eliminate or constrain critical business-process paths across multiple independent layers.

Example for payment diversion:

1. Email cannot authorize a destination change.
2. Destination changes require verified out-of-band confirmation.
3. Vendor administration is separate from payment release.
4. Material changes invalidate prior approval.
5. First payment to a changed destination requires independent approval.
6. Payment release is limited by value, role, and approved destination.

Traditional defense in depth may layer awareness, alerts, reviews, and investigations around a path that remains open.

Subtractive defense in depth independently removes or constrains the same path at multiple transitions.

The objective is not perfect controls.

The objective is resilient business-process non-conductivity.

# Stack Composition & Parallel Adoption

Business-process attack paths do not respect organizational or technology boundaries.

A BEC path may traverse Microsoft 365, identity, finance, vendor management, payment systems, and bank interfaces. An insider-data path may traverse HR, identity, SaaS, endpoints, datastores, collaboration platforms, and external storage. A procurement-fraud path may traverse vendor onboarding, contracts, purchasing, receiving, invoicing, and treasury.

Organizations should apply this standard concurrently with relevant platform standards.

Examples:

- Fraud & Insider Risk + Microsoft 365 + Identity
- Fraud & Insider Risk + Datastore + Endpoint
- Fraud & Insider Risk + SaaS + Network
- Fraud & Insider Risk + Third-Party Risk + Application
- Fraud & Insider Risk + Physical Security + Offboarding
- Fraud & Insider Risk + AI Agents + Business Workflow

The objective is not to secure each component in isolation.

The objective is to reduce total adversarial conductivity across the complete sociotechnical system.

# Strategic Objective: Business-Process Non-Conductivity

The goal of these subtractions is to establish deterministic boundaries across organizational workflows.

By collapsing authority, trust, approval, payment, data-access, delegation, and override paths, the business process becomes non-conductive to fraud and insider abuse.

In this model:

```
Fraudulent Intent or Insider Motive = Spark
Authority or Business-Process Path  = Oxygen
Organizational Process Architecture = Conductivity
```

Remove the path, and the spark goes nowhere.

# Guiding Principle

Fraudsters, insiders, compromised identities, and colluding actors can only traverse paths that exist.

The objective of Fraud & Insider Risk Subtractive Hardening is to systematically eliminate or constrain those paths until adversarial influence, insider access, or routine human error can no longer compose into material financial, operational, regulatory, data, or reputational impact.

**Fraud and insider-risk controls are most effective when paths to impact are removed, not merely observed.**

# References

- [OWASP Subtractive Hardening Top 10 Project](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/tree/main)
- [OWASP Universal Subtractive Security Laws Top 10](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10/blob/main/UniversalSubtractiveLaws.md)
- [Path Erasure Rate (PER-1.0) Engineering Standard](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md)
- [Evidence-Based Security](https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and)
- [The Law of Subtractive Risk](https://subtractivesecurity.substack.com/p/the-law-of-subtractive-risk-moving)
- The Science of Silence

_OWASP Fraud & Insider Risk Subtractive Hardening Top 10 v1.0_
