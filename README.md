# OWASP Subtractive Security Top 10 Project

![OWASP Project Level](https://img.shields.io/badge/OWASP-Incubator%20Project-blue)
![Standard](https://img.shields.io/badge/Specification-PER--1.0-orange)

## Overview

The OWASP Subtractive Security Top 10 Project is an initiative to identify, document, and promote the highest-impact opportunities for reducing cyber risk through the elimination of attack paths.

Unlike traditional security guidance that focuses primarily on adding controls, the Subtractive Security Top 10 emphasizes the removal of unnecessary attack surface, trust relationships, protocols, privileges, services, and communication paths that enable adversary progression.

The project is founded on the principle that the most effective security control is often the complete removal of an attack path rather than attempting to monitor or manage it.

The long-term vision of the project is to establish attack-path elimination as a foundational security engineering discipline supported by measurable outcomes through the Path Erasure Rate (PER) standard.

## Guiding Principle

Attackers can only traverse paths that exist.

The objective of Subtractive Security is to systematically eliminate or constrain those paths until adversary activity can no longer compose into material business impact.

## Purpose

The purpose of this project is to provide practical, evidence-based guidance for identifying and eliminating common attacker paths across operating systems, cloud platforms, identity systems, and enterprise environments.

Each Top 10 focuses on attack paths whose removal produces disproportionate reductions in risk while minimizing operational impact.

The project seeks to answer a simple question:

> What can be removed to make an attack materially more difficult or impossible?

## Relationship to the Path Erasure Rate Standard (PER 1.0)

The Subtractive Security Top 10 Project is aligned with the Path Erasure Rate (PER) Engineering Standard (https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md) 

PER provides a methodology for measuring the effectiveness of security improvements by quantifying the reduction of adversary-accessible attack paths.

$$\text{PER} = \frac{|P_{\text{erased}}|}{|P_{\text{eligible}}|}$$

Where **$P_{\text{eligible}}$** represents valid, actionable attack paths identified within scope, and **$P_{\text{erased}}$** represents the subset where executable edges have been structurally removed.

PER serves as the quantitative measurement framework for Subtractive Security.

The Subtractive Security Top 10 identifies high-value attack paths whose elimination is expected to produce meaningful reductions in adversary capability, while PER provides the mechanism for validating and measuring those reductions.

Together they establish a repeatable engineering process for attack-path discovery, prioritization, elimination, and measurement.

- Identify attack paths
- Measure attack-path exposure
- Remove or constrain attack paths
- Measure resulting reduction
- Continuously improve security architecture

## Hierarchy of Efficacy

The project is based upon the principle that security controls do not provide equal levels of risk reduction.

The hierarchy reflects a simple principle:

Architectural Deletion > Architectural Constraint > Monitoring

Whenever an attack path can be eliminated, elimination is preferred. If elimination is not feasible, the path should be constrained. Monitoring is reserved for residual paths that cannot be removed or sufficiently constrained.

Subtractive Security prioritizes:

### 1. Architectural Deletion
Remove attack paths entirely.

Examples:
- Remove legacy protocols
- Remove unnecessary privileges
- Remove public exposure
- Remove dormant identities
- Remove unnecessary trust relationships

### 2. Architectural Constraint
Constrain attack paths that cannot be eliminated.

Examples:
- Segmentation
- Permission boundaries
- Conditional access
- Private endpoints
- Privilege restrictions

### 3. Monitoring and Detection
Monitor the residual risk that cannot be deleted or constrained.

Examples:
- Logging
- Alerting
- SIEM
- IDS/IPS
- Endpoint detection

This hierarchy reflects the project's belief that the elimination of an attack path is generally more effective than detecting its use.

# Project Structure

The OWASP Subtractive Hardening Top 10 is a family of platform-specific security engineering standards operating under a common set of universal architectural laws.

At the foundation of the framework is the OWASP Universal Subtractive Security Laws Top 10, which defines platform-agnostic attack-path reduction principles applicable across operating systems, cloud platforms, identity systems, SaaS environments, networks, embedded devices, and future technology domains.

Environment-specific standards provide reference implementations of these universal laws within particular technology stacks.

## Universal Foundation

- Universal Subtractive Security Laws Top 10

## Published Platform Standards

- Windows Subtractive Hardening Top 10
- Linux Subtractive Hardening Top 10
- Active Directory Subtractive Hardening Top 10
- AWS Subtractive Hardening Top 10
- Microsoft 365 Subtractive Hardening Top 10
- Network Subtractive Hardening Top 10
- IoT Subtractive Hardening Top 10
- macOS Subtractive Hardening Top 10

## Planned and Future Standards

- Identity & Access Management (IAM) Subtractive Hardening Top 10
- Azure Subtractive Hardening Top 10
- Google Cloud Platform (GCP) Subtractive Hardening Top 10
- Container & Kubernetes Subtractive Hardening Top 10
- CI/CD & Software Supply Chain Subtractive Hardening Top 10
- AI & LLM Infrastructure Subtractive Hardening Top 10
- Medical Device Subtractive Hardening Top 10
- Additional standards as new architectural domains emerge

## Architectural Relationship

```text
Universal Security Laws
        ↓
Path Erasure Rate (PER)
        ↓
Platform Standards
        ↓
Implementation Controls
```

Each platform standard applies the same underlying architectural principles:

- Reduce unnecessary reachability.
- Reduce unnecessary trust relationships.
- Reduce credential exposure.
- Reduce privilege propagation.
- Reduce executable attack paths.
- Reduce control-plane exposure.
- Reduce attack-surface area.
- Enforce deterministic communications.
- Constrain residual attack paths.
- Measure structural improvement through PER.

The implementation details vary by platform, but the underlying architectural laws remain consistent.

These standards are designed for parallel adoption and layered deployment. When composed together, they provide enterprise-wide attack-path reduction across endpoint, server, identity, cloud, SaaS, network, and embedded-system environments.

## Stack Composition & Parallel Adoption

The OWASP Subtractive Hardening Top 10 family is designed for composable, parallel execution.

Individual Top 10 publications are not intended to be implemented in isolation. Modern enterprise systems are composed of multiple technology layers, each contributing unique attack paths, trust relationships, and opportunities for adversary progression.

Securing an enterprise asset requires applying platform-specific subtractive controls concurrently across all relevant layers.

Examples include:

- AWS Subtractive Hardening + Linux Subtractive Hardening
- Active Directory Subtractive Hardening + Windows Subtractive Hardening
- Kubernetes Subtractive Hardening + Linux Subtractive Hardening
- SaaS Subtractive Hardening + Identity and Access Management Subtractive Hardening
- Azure Subtractive Hardening + Active Directory Subtractive Hardening

Attack paths do not respect architectural boundaries.

A compromised cloud workload may leverage operating system attack paths. A compromised workstation may leverage identity attack paths. A compromised identity may leverage cloud control-plane attack paths.

Subtractive Security therefore promotes parallel attack-path reduction across all applicable layers of the technology stack.

### Defense in Depth Through Layered Path Erasure

Subtractive Security recognizes that all controls, including subtractive controls, may fail due to misconfiguration, operational drift, incomplete implementation, or changing business requirements. Subtractive Security, therefore, extends the traditional concept of defense in depth by emphasizing attack-path removal across multiple architectural layers.

Rather than relying solely on independent monitoring or prevention technologies, organizations should seek to eliminate, reduce, or constrain the same attack path wherever it appears within the stack.

Examples include:

- Reducing administrative trust within Linux while simultaneously segmenting lateral movement at the network layer.
- Restricting cloud identity trust relationships while eliminating operating-system-level privilege escalation paths.
- Enforcing egress determinism at the endpoint, network, and cloud-control-plane layers.

This approach creates multiple independently non-conductive boundaries that attackers must overcome. The result is defense in depth through layered path erasure rather than layered detection.

The objective is not merely to harden individual components.

The objective is to reduce the total attack-path conductivity of the system as a whole.

## Project Goals

- Promote attack-path elimination as a primary security strategy.
- Encourage measurable security improvement through PER.
- Provide actionable guidance for reducing architectural exposure.
- Establish a common vocabulary for subtractive security engineering.
- Improve security outcomes through evidence-based decision making.
- Advance security as an engineering discipline grounded in measurable risk reduction.

## Scope

This project focuses on architectural improvements that reduce adversary reachability, privilege, mobility, and persistence opportunities.

From a graph-theoretic perspective, the project focuses on reducing adversary reachability by eliminating or constraining executable edges within attack graphs.

The objective is to reduce the number of paths capable of composing into material business impact. Recommendations are selected based on their potential to eliminate or materially constrain attacker paths rather than their popularity, compliance value, or operational visibility.


## Contributing

The OWASP Subtractive Security Top 10 Project welcomes contributions from security practitioners, researchers, architects, cloud engineers, platform engineers, and defenders interested in advancing attack-path reduction methodologies.

Community feedback, empirical research, implementation experiences, and proposed attack-path removal techniques are encouraged.

## Learn More

- Path Erasure Rate (PER) Engineering Standard (https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md)
- Evidence-Based Security (https://subtractivesecurity.substack.com/p/the-cyber-falsifiability-crisis-and)
- Subtractive Security Engineering Framework (https://subtractivesecurity.substack.com/p/the-law-of-subtractive-risk-moving)

---

*"Security effectiveness is maximized when attack paths are removed, not merely observed."*

## Licensing

This project is open-source and released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). All documentation, specifications, and code are free to use, modify, and distribute for commercial and non-commercial purposes under the terms of the license.

## Project Leaders

- **Christopher Frenz** — Project Founder & Primary Author
