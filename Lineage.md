# Lineage of Subtractive Security

Subtractive Security developed through a documented progression from empirical security testing, to evidence-based measurement of defensive efficacy, to architectural elimination of unnecessary attack paths, and finally to quantitative measurement of path erasure.

This page records that progression. It is intended as a history of the engineering ideas and evidence that informed the OWASP Subtractive Security project, not as a claim that the later terminology or complete framework existed at every earlier stage.

## Lineage at a Glance

- **2015:** Empirical malware-propagation testing
- **2020:** Evidence-Based Security codified
- **2022:** Quantitative, threat-informed measurement
- **2022:** Architectural hardening beyond control deployment
- **2023:** *Evidence-Based Security* published by O'Reilly Media
- **2024:** Identification and removal of unnecessary capability
- **2024:** Control-resilient security architecture
- **2026:** Subtractive Security formally articulated
- **2026:** Path Erasure Rate (PER) and the PER 1.0 Engineering Specification
- **2026:** OWASP Subtractive Security Top 10 operationalizes the discipline

---

## 2015 | Empirical Security Measurement

The earliest stage of this lineage was empirical rather than terminological.

A hospital-based mass-malware simulation used a custom script and the EICAR test string to evaluate defensive-control efficacy against simulated lateral propagation. The exercise tested whether existing security architecture changed observable attack outcomes. Network segmentation constrained propagation, and the findings informed further segmentation and movement toward a Zero Trust architecture.

This established a foundational principle that continued through the later work:

> Security claims should be tested against observable attack behavior rather than inferred from the presence of controls.

### Supporting sources

- [Medical Device CyberSecurity: Don't WannaDie — Using a Zero Trust Approach to Secure Healthcare, NIST/NCCoE presentation](https://www.nccoe.nist.gov/sites/default/files/legacy-files/8_frenz_interfaith_distribution.pdf)

---

## 2020 | Evidence-Based Security Codified

Evidence-Based Security was first codified in the 2020 CHIME publication *The Need for Evidence-Based Security*.

The methodology called for security decisions to be grounded in empirical testing, defined metrics, measurement, analysis, remediation, and repeated evaluation. This provided the methodological foundation from which the later architectural and subtractive work developed.

The central question was no longer simply:

> Has a security control been deployed?

It became:

> Is there measurable evidence that the control changes attack outcomes?

### Primary source

- [The Need for Evidence-Based Security, CHIME](https://chimecentral.org/chime/resource-post/the-need-for-evidence-based-security)

### Related source

- [Taking an Evidence-Based Approach to Healthcare Security](https://www.healthtechmagazines.com/taking-an-evidence-based-approach-to-healthcare-security/)

---

## 2022 | Quantitative and Threat-Informed Measurement

The 2022 article *Achieving Evidence-Based Security with Threat-Informed Defense* further developed the methodology around measurable control efficacy against real-world tactics, techniques, and procedures.

The work emphasized that security programs should define relevant metrics, simulate representative threats, measure outcomes, analyze results, remediate weaknesses, and retest.

This made the quantitative objective increasingly explicit:

> Security improvement should be demonstrated through measured changes in attack outcomes.

### Primary source

- [Achieving Evidence-Based Security with Threat-Informed Defense](https://www.healthcareitnews.com/blog/achieving-evidence-based-security-threat-informed-defense)

---

## 2022 | From Control Deployment to Architectural Hardening

*Seeing Through the Security Illusion* extended the discussion beyond the acquisition and deployment of security products.

It argued that effective security also depends on hardened system configurations, secure network design, validation of actual control efficacy, and disabling functionality that is not operationally required.

This marked an important transition in the lineage:

1. Measure whether controls work.
2. Identify the architectural conditions that permit attack paths.
3. Remove or harden unnecessary capabilities where feasible.
4. Apply controls to the capabilities that must remain.

This work preceded the later Subtractive Security terminology. It is included because it documents the movement from measuring deployed controls toward changing the architecture itself.

### Primary source

- [Seeing Through the Security Illusion](https://www.healthcareitnews.com/blog/seeing-through-security-illusion)

---

## 2023 | Evidence-Based Security Expanded

The 2023 O'Reilly book *Evidence-Based Security*, by Christopher Frenz and Jonathan Reiber, expanded the methodology into a broader treatment of empirically grounded security evaluation.

The book consolidated principles including:

- threat-informed testing;
- measurable control efficacy;
- metrics tied to security outcomes;
- simulation and experimentation;
- analysis and remediation; and
- repeated testing to demonstrate improvement.

The book represents the maturation of the Evidence-Based Security methodology first codified in 2020. It does not represent the beginning of that methodology.

### Publication

Christopher Frenz and Jonathan Reiber. *Evidence-Based Security*. O'Reilly Media, 2023. ISBN 978-1-098-14891-1.

---

## 2024 | Measuring Necessary Behavior to Remove Unnecessary Capability

The 2024 article *Know Thyself: An Analytics-Based Approach to Combating Living off the Land Attacks* examined how observed legitimate behavior could be used to determine where system capabilities were required and where they could be blocked.

Examples included:

- blocking binaries where no legitimate use was observed;
- limiting the populations permitted to use particular executables;
- preventing productivity applications from spawning script interpreters; and
- restricting interpreters to approved execution locations.

This represented a further evolution in the engineering question.

Instead of asking only whether malicious use could be detected, the analysis asked:

> Where is this capability genuinely necessary, and where can it be removed or made non-traversable?

This principle later became central to Subtractive Security: unnecessary capabilities should not remain universally available merely because defensive tools can monitor them.

### Primary source

- [Know Thyself: An Analytics-Based Approach to Combating Living off the Land Attacks](https://www.healthcareitnews.com/blog/know-thyself-analytics-based-approach-combating-living-land-attacks)

---

## 2024 | Architectures That Remain Effective When Controls Fail

*Healthcare Needs Security Architectures That Provide Control Resiliency* developed the architectural dimension further.

The article addressed security architectures that remain protective when individual preventive or detective controls are bypassed, degraded, or fail. It emphasized hardened architectures, compensating controls, control-efficacy measurement, and the elimination of bypass opportunities.

This helped establish a distinction that later became explicit within Subtractive Security:

- **Control deployment** adds a defensive mechanism.
- **Control resilience** limits the consequences of control failure.
- **Architectural subtraction** removes an unnecessary transition capability or attack path.

### Primary source

- [Healthcare Needs Security Architectures That Provide Control Resiliency](https://www.healthcareitnews.com/blog/healthcare-needs-security-architectures-provide-control-resiliency)

### Related quantitative work

- [Measuring Control Efficacy: Time for Metrics and Not "Meh"-trics](https://cxotechmagazine.com/measuring-control-efficacy-time-for-metrics-and-not-meh-trics/)

---

## 2025 | Documentary Continuity

Public discussion continued to connect the original empirical security testing with the broader Evidence-Based Security methodology.

These retrospective discussions are useful to the historical record because they document continuity between early simulation work, measurement of control efficacy, and the later architectural approach. They are supporting sources rather than separate conceptual milestones.

### Supporting source

- [Nexus Podcast: Christopher Frenz on Evidence-Based Security](https://nexusconnect.io/podcasts/nexus-podcast-christopher-frenz-on-evidence-based-security)

---

## 2026 | Subtractive Security

Subtractive Security formalized the architectural principle that unnecessary adversary-usable capabilities should be removed where feasible rather than perpetually governed through additional controls.

The approach distinguishes three broad forms of treatment:

1. **Architectural deletion:** Remove an unnecessary transition capability or executable edge.
2. **Architectural constraint:** Narrow a capability that cannot be completely removed.
3. **Monitoring and runtime governance:** Observe and govern the residual capabilities required for legitimate operation.

These treatments are complementary, but they do not represent the same system state. A tightly monitored capability remains technically present. An erased capability does not participate in the reachable attack-path set within the evaluated state.

### Formal publication

Christopher Frenz. *The Science of Silence: Subtractive Security and the Physics of Defense*. Subtractive Security, LLC, 2026. ISBN 979-8-9955336-0-3.

---

## 2026 | Path Erasure Rate

Path Erasure Rate, or PER, supplied an explicit quantitative measure for structural attack-path elimination.

For a defined scope and evaluated system state:

`PER = |E_erased| / |E_scoped|`

Where:

- `E_scoped` is the set of transition capabilities included in the evaluation; and
- `E_erased` is the subset whose executable edges have been structurally removed.

PER measures a change in the set of traversable capabilities. It is not a count of deployed security controls.

A claim of erasure is state-conditioned and falsifiable. If testing demonstrates that the selected transition remains traversable in the evaluated state, the path has not been erased.

PER does not determine which paths an organization should remove. Selection of the scoped set remains an engineering and governance decision. PER measures whether the paths selected for structural treatment were rendered non-conductive.

### Public discussion

- [The Architecture of Subtraction: Why It's Time to Erase the Roads, Not Just Map the Traffic](https://www.helpnetsecurity.com/2026/06/09/subtractive-security-attack-path-erasure/)
- [Patching Can't Outpace Mythos: Here's What Comes Next](https://www.bankinfosecurity.net/patching-cant-outpace-mythos-heres-what-comes-next-a-31733)

### Engineering specification

- [Path Erasure Rate 1.0 Engineering Specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md)

---

## 2026 | OWASP Operationalization

The OWASP Subtractive Security Top 10 translates this body of work into practical, platform-oriented security engineering guidance.

The project identifies and documents opportunities to reduce cyber risk through attack-path elimination. Its focus is not solely on adding security controls. It asks engineers to identify unnecessary transitions, remove them where feasible, constrain those that must remain, and monitor the residual attack surface.

The OWASP project therefore represents an implementation-level expression of the preceding lineage:

1. Empirical testing
2. Evidence-based measurement
3. Quantitative control evaluation
4. Architectural hardening
5. Identification of unnecessary capability
6. Structural attack-path elimination
7. Quantification through PER
8. Platform-specific engineering guidance

---

## Conceptual Continuity

The lineage does not imply that Evidence-Based Security, Zero Trust, threat-informed defense, control resiliency, Subtractive Security, and PER are interchangeable.

Each addresses a distinct question:

| Discipline or concept | Principal question |
|---|---|
| Evidence-Based Security | What evidence demonstrates that a security measure changes attack outcomes? |
| Threat-informed defense | How do defenses perform against relevant adversary techniques and behaviors? |
| Zero Trust | Under what conditions should access be granted and continuously evaluated? |
| Control resilience | Does the architecture remain protective when a control is bypassed or fails? |
| Subtractive Security | Which unnecessary adversary-usable capabilities can be structurally removed? |
| Path Erasure Rate | What proportion of the scoped transition capabilities has been structurally erased? |

The continuity lies in the engineering method:

> Observe, test, measure, change the architecture, and retest.

Subtractive Security applies that method specifically to the structural elimination of attack paths.

---

## Scope and Limitations

This history documents the development of the engineering ideas that informed the OWASP Subtractive Security project.

It does not claim:

- that the complete Subtractive Security framework existed in 2015 or 2020;
- that the term "Subtractive Security" was used in the earlier Evidence-Based Security publications;
- that all security measurement originated with this body of work;
- that PER is the only valid attack-surface or attack-path metric;
- that every attack path can or should be removed; or
- that authentication, authorization, detection, monitoring, and response are unnecessary.

The narrower claim is that a documented progression connects:

1. empirical evaluation of defensive architecture;
2. codification of Evidence-Based Security;
3. quantitative measurement of control efficacy;
4. removal of unnecessary system capabilities;
5. design for architectural control resilience;
6. formalization of structural attack-path elimination; and
7. quantitative measurement through Path Erasure Rate.

---

## References

1. Frenz, Christopher. "The Need for Evidence-Based Security." CHIME, 2020. [Read the CHIME publication](https://chimecentral.org/chime/resource-post/the-need-for-evidence-based-security)
2. Frenz, Christopher. "Taking an Evidence-Based Approach to Healthcare Security." *HealthTech Magazines*. [Read the article](https://www.healthtechmagazines.com/taking-an-evidence-based-approach-to-healthcare-security/)
3. Frenz, Christopher. "Achieving Evidence-Based Security with Threat-Informed Defense." *Healthcare IT News*, 2022. [Read the article](https://www.healthcareitnews.com/blog/achieving-evidence-based-security-threat-informed-defense)
4. Frenz, Christopher. "Seeing Through the Security Illusion." *Healthcare IT News*, 2022. [Read the article](https://www.healthcareitnews.com/blog/seeing-through-security-illusion)
5. Frenz, Christopher, and Jonathan Reiber. *Evidence-Based Security*. O'Reilly Media, 2023. ISBN 978-1-098-14891-1.
6. Frenz, Christopher. "Know Thyself: An Analytics-Based Approach to Combating Living off the Land Attacks." *Healthcare IT News*, 2024. [Read the article](https://www.healthcareitnews.com/blog/know-thyself-analytics-based-approach-combating-living-land-attacks)
7. Frenz, Christopher. "Healthcare Needs Security Architectures That Provide Control Resiliency." *Healthcare IT News*, 2024. [Read the article](https://www.healthcareitnews.com/blog/healthcare-needs-security-architectures-provide-control-resiliency)
8. Frenz, Christopher. "Measuring Control Efficacy: Time for Metrics and Not 'Meh'-trics." *CXOTech Magazine*. [Read the article](https://cxotechmagazine.com/measuring-control-efficacy-time-for-metrics-and-not-meh-trics/)
9. Frenz, Christopher. "Medical Device CyberSecurity: Don't WannaDie — Using a Zero Trust Approach to Secure Healthcare." NIST/NCCoE presentation. [View the presentation](https://www.nccoe.nist.gov/sites/default/files/legacy-files/8_frenz_interfaith_distribution.pdf)
10. "Nexus Podcast: Christopher Frenz on Evidence-Based Security." *Nexus / Claroty*. [Listen to the interview](https://nexusconnect.io/podcasts/nexus-podcast-christopher-frenz-on-evidence-based-security)
11. Frenz, Christopher. *The Science of Silence: Subtractive Security and the Physics of Defense*. Subtractive Security, LLC, 2026. ISBN 979-8-9955336-0-3.
12. Frenz, Christopher. "The Architecture of Subtraction: Why It's Time to Erase the Roads, Not Just Map the Traffic." *Help Net Security*, June 9, 2026. [Read the article](https://www.helpnetsecurity.com/2026/06/09/subtractive-security-attack-path-erasure/)
13. Frenz, Christopher. "Patching Can't Outpace Mythos: Here's What Comes Next." *Information Security Media Group / BankInfoSecurity*, 2026. [View the interview](https://www.bankinfosecurity.net/patching-cant-outpace-mythos-heres-what-comes-next-a-31733)
14. Frenz, Christopher. "Path Erasure Rate 1.0 Engineering Specification." *Path Erasure Engine*. [View the specification](https://github.com/cfrenz/Path-Erasure-Engine/blob/main/PER-1.0_Engineering_Specification.md)
15. OWASP. "OWASP Subtractive Security Top 10." [View the OWASP project repository](https://github.com/OWASP/OWASP-Subtractive-Hardening-Top-10)

---

## Suggested Citation

OWASP Subtractive Security Top 10 Project. "Lineage of Subtractive Security." OWASP, 2026.
