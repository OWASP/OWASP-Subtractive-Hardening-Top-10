# OWASP Subtractive Threat Modeling Standard

**Document Version:** 1.0.0  
**Project:** OWASP Subtractive Hardening Top 10  
**Governance Area:** Threat Modeling and Attack Path Prevention  
**Specification Alignment:** PER-1.0 (Path Erasure Rate Engineering Standard)  
**License:** Apache License 2.0

## Executive Summary

Traditional threat modeling focuses on identifying threats and implementing controls to reduce risk.

The OWASP Subtractive Threat Modeling Standard shifts the primary objective from threat mitigation to attack-path prevention and attack-path elimination.

Rather than asking:

> What controls should be implemented?

Subtractive Threat Modeling asks:

> What attack paths can be prevented?

and

> What attack paths can be eliminated?

The preferred outcome is not additional controls. The preferred outcome is architectural simplification that prevents attack paths from existing.

This standard integrates Attack Path Analysis, Abuse Case Analysis, Path Prevention, and Path Erasure into a unified methodology for designing systems with fewer opportunities for compromise.

---

# Core Principles

## Principle 1: Attack Paths Matter More Than Individual Vulnerabilities

Attackers do not compromise organizations by exploiting isolated vulnerabilities. Attackers achieve objectives by traversing attack paths.

A vulnerability with no path to a high-value objective may represent less risk than multiple low-severity weaknesses connected through a viable attack chain.

Threat modeling should prioritize understanding:

- Trust relationships
- Connectivity
- Permissions
- Privilege boundaries
- Data access paths
- Attack path density

rather than assessing weaknesses in isolation.

---

## Principle 2: Prevention Is Preferred Over Mitigation

The preferred order of operations is:

1. Prevent the path.
2. Erase the path.
3. Constrain the path.
4. Detect path traversal.
5. Respond to compromise.

Security controls should not be used as substitutes for architectural simplification.

---

## Principle 3: Every Design Decision Creates or Removes Paths

Every feature, integration, permission, trust relationship, credential, and network connection alters the attack graph.

Threat modeling should evaluate:

- Paths introduced
- Paths prevented
- Paths removed
- Net attack-path change

Security architecture should be evaluated based on its effect on attack-path availability.

---

## Principle 4: Attack Paths Are Design Artifacts

Attack paths are not solely the result of vulnerabilities.

Attack paths emerge from architectural decisions, trust relationships, permissions, connectivity, and assumptions.

Threat modeling should therefore evaluate systems even in the absence of known vulnerabilities.

A secure design should seek to minimize the number and quality of attack paths available to an adversary.

---

# Objectives

The objectives of Subtractive Threat Modeling are to:

- Identify attack paths.
- Identify abuse paths.
- Prevent attack-path introduction.
- Eliminate existing attack paths.
- Reduce attack-path density.
- Reduce attack-path availability.
- Reduce attacker optionality.
- Produce systems with lower residual attack surface.

Success is measured by reduction in attack-path availability rather than the quantity of documented threats.

---

# Threat Modeling Workflow

## Step 1: Define Scope

Document:

- Components
- Systems
- Data stores
- Integrations
- Trust assumptions
- Dependencies
- Out-of-scope items

The goal is to clearly establish what will be modeled and what assumptions are accepted.

---

## Step 2: Build the System Model

Document:

- Users
- Services
- APIs
- Databases
- Queues
- Background jobs
- Administrative interfaces
- Vendors
- Third-party services
- AI systems

Document all:

- Data flows
- Credential flows
- Trust relationships
- Administrative relationships

Threat modeling without an accurate system model is incomplete.

---

## Step 3: Identify Trust Boundaries

Trust boundaries should be explicitly documented.

Examples include:

- Internet to application
- User to administrator
- Vendor to organization
- Application to database
- Production to non-production
- Human to AI system

Trust boundaries frequently create attack paths and should receive special scrutiny.

---

## Step 4: Perform Attack Path Analysis

Attack Path Analysis evaluates attacker movement following compromise.

For each component ask:

### Compromise Analysis

If this component is compromised:

- What data becomes accessible?
- What credentials become available?
- What systems become reachable?
- What trust boundaries can be crossed?
- What privileges can be obtained?

### Movement Analysis

Can an attacker:

- Move laterally?
- Escalate privileges?
- Reach sensitive data?
- Reach administrative systems?
- Pivot through third parties?
- Expand influence beyond the original compromise?

Document every credible attack path.

---

# Attack Path Register

Every identified attack path should be documented.

### Example 1

```text
Internet
→ Web Application
→ Service Account
→ Database
→ PHI Exposure
```

### Example 2

```text
Vendor Integration
→ API Credential
→ Internal Application
→ Administrative Function
```

### Example 3

```text
Compromised User
→ Excessive Permissions
→ Sensitive Records
→ Mass Data Export
```

Document:

- Initial compromise point
- Intermediate pivots
- Trust boundaries crossed
- Final objective

---

# Step 5: Path Prevention Analysis

Path Prevention Analysis evaluates proposed designs before implementation. Path Prevention Analysis should be performed before implementation and revisited whenever a design materially changes.

For each feature ask:

> What attack paths would be created if this design is implemented?

Examples:

| Proposed Design | Potential Attack Path |
|----------------|----------------------|
| Public API | Internet → API → Internal Services |
| Third-Party Integration | Vendor → Internal Systems |
| Local Account Store | Credential Theft → Application Access |
| Shared Service Account | Credential Exposure → Privilege Escalation |
| Administrative Interface | User Compromise → Administrative Access |

All newly introduced attack paths should be documented.

---

# Step 6: Path Prevention Opportunities

Before discussing controls, ask:

> Can this attack path be prevented from existing?

Examples:

| Original Design | Prevention Approach |
|---------------|---------------------|
| Local authentication | Federated identity |
| Shared credentials | Unique identities |
| Public service exposure | Private connectivity |
| Standing privilege | Just-in-time access |
| Direct database access | Service isolation |
| Broad vendor access | Segmented integration |

The preferred outcome is that the attack path is never created.

Path Prevention should always be evaluated before discussing mitigation controls.

---

# Step 7: Abuse Case Analysis

Attackers are not the only threat actors.

Authorized users can intentionally misuse systems, workflows, permissions, and business processes.

Questions include:

- How could a user misuse this capability?
- Can business logic be exploited?
- Can excessive data be extracted?
- Can resources be intentionally exhausted?
- Can approvals be bypassed?
- Can financial processes be manipulated?

Examples include:

| Abuse Case | Example |
|------------|----------|
| Fraud | Manipulating reimbursement requests |
| Data Harvesting | Excessive customer exports |
| Workflow Abuse | Self-approval scenarios |
| Financial Abuse | Discount exploitation |
| Resource Abuse | Excessive AI consumption |

Document all abuse paths and associated control requirements.

---

# Step 8: Path Erasure Analysis

Path Erasure Analysis focuses on existing attack paths.

For every attack path ask:

> Can this path be removed?

Examples include:

- Permission removal
- Connectivity removal
- Service elimination
- Integration removal
- Trust reduction
- Identity simplification
- Data deletion
- Application retirement

The preferred outcome is removal rather than monitoring.

A control that eliminates a path should generally be preferred over a control that detects path traversal.

---

# Path Treatment Hierarchy

Attack paths should be addressed in the following order:

## Level 1: Prevent

The path is never created.

Examples:

- Architectural simplification
- Feature redesign
- Removal of unnecessary dependencies

---

## Level 2: Erase

The path exists and is removed.

Examples:

- Permission removal
- Trust removal
- Integration removal
- Service removal

---

## Level 3: Constrain

The path remains but becomes more difficult to traverse.

Examples:

- Segmentation
- Least privilege
- Just-in-time access
- Rate limiting
- Conditional access

---

## Level 4: Detect

Path traversal is identified.

Examples:

- Monitoring
- Logging
- SIEM
- EDR
- UEBA

---

## Level 5: Respond

Actions are taken after path traversal occurs.

Examples:

- Incident response
- Recovery procedures
- Containment processes

---

# Net Attack Path Change

All significant architectural changes should evaluate whether they increase or decrease attack-path availability.

Architectures that reduce total attack-path availability are preferable to architectures that increase it.

Projects that increase attack-path availability should provide documented business justification.

---

# Metrics

Traditional Metrics

- Vulnerabilities identified
- Findings closed
- Threats documented
- Scan coverage

Subtractive Metrics

- Attack paths prevented
- Attack paths erased
- Permissions removed
- Trust relationships removed
- Connectivity removed
- Attack Path Introduction Rate (APIR)
- Path Erasure Rate (PER)

The objective is continuous reduction of attack-path availability.

---

# Maturity Model

## Level 1: Vulnerability Management

Focus:

- Vulnerability discovery
- Vulnerability remediation

---

## Level 2: Threat Modeling

Focus:

- Threat identification
- Risk assessment
- Risk mitigation

---

## Level 3: Attack Path Modeling

Focus:

- Lateral movement
- Privilege escalation
- Trust boundaries
- Multi-stage attack chains

---

## Level 4: Path Erasure

Focus:

- Architectural simplification
- Trust reduction
- Attack-path elimination

---

## Level 5: Path Prevention

Focus:

- Prevention of attack-path creation
- Security-informed architecture decisions
- Continuous reduction of future attack-path introduction
- Security as a design optimization discipline

Note: This maturity model assesses an organization's architectural design process and pre-implementation threat analysis methodology. For measuring the operational execution, quantification, and continuous verification of path removal in deployed environments, refer to the companion PER-1.0 Operational Maturity Model.

---

# Relationship to Path Erasure Rate (PER)

Path Erasure Rate (PER) provides a quantitative mechanism for measuring attack-path reduction.

Subtractive Threat Modeling provides the decision-making framework used to:

- Identify attack paths
- Prevent attack-path introduction
- Prioritize path elimination
- Reduce attacker optionality

Threat Modeling answers:

> Which paths should be addressed?

PER answers:

> Which actions reduce attack paths most effectively?

Together they create a continuous system for attack-path reduction.


---

# Conclusion

Traditional threat modeling often ends with a list of risks and recommended controls.

Subtractive Threat Modeling continues beyond identification and asks:

- Which attack paths can be prevented?
- Which attack paths can be removed?
- Which attack paths should no longer exist?

The objective is not merely to document threats.

The objective is to design systems with fewer opportunities for compromise.

> The most effective attack path is not the one that is monitored.
>
> The most effective attack path is not the one that is detected.
>
> The most effective attack path is the one that was never created.
