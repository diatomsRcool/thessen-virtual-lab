# Team Meeting: Action Item Review — One Health Initiative
**Date:** March 25, 2026
**Participants:** Architect (Lead), Bioinformaticist, Scientific Critic, Data Curator, Clinical Informaticist, Tick Ecologist, Public Health Researcher

## Agenda
Review progress on action items from the March 6, 2025 meeting, identify blockers, and plan next steps.

---

## Architect's Opening

Welcome, everyone. It has been just under three weeks since our last meeting, where we laid the groundwork for the One Health Tick-Borne Disease Research Initiative. That session was productive - we aligned on a vision for integrating NEON ecological surveillance, pathogen genomics, and clinical health records into a coherent research program. Today we reconvene to take stock of where we stand.

As a reminder, we left that meeting with five concrete action items distributed across the team. The Curator and Bioinformaticist took on drafting a LinkML schema for tick-pathogen data. The Tick Ecologist and I committed to identifying pilot NEON sites near our clinical partners. The Clinical Informaticist was charged with defining OMOP phenotypes for Lyme disease. The Critic and I agreed to develop a causal framework diagram. And the Public Health Researcher took the lead on outlining a stakeholder engagement strategy.

The purpose of today's meeting is threefold: hear progress reports on each action item, surface blockers and dependencies, and plan concrete next steps.

---

## Status Reports

### Data Curator — LinkML Schema
**Progress:** Core schema skeleton is complete. `TickSpecimen` class fully drafted with Darwin Core-aligned slots (`occurrenceID`, `eventDate`, `decimalLatitude`, `decimalLongitude`, `geodeticDatum`, `samplingProtocol`). `SamplingEvent` class maps to NEON's event structure using `siteID`, `plotID`, and `collectDate`. Ontology prefix declarations in place (NCBITaxon, ENVO, UBERON, DwC). Enums for `TickSpeciesEnum` and `LifeStageEnum` drafted with NCBITaxon bindings for the four most common NEON surveillance species.

**Blocker:** `PathogenDetection` class not yet drafted. NEON's `tck_pathogen` and `tck_fielddata` tables use different primary key structures, requiring resolution before schema can be finalized.

**Questions for team:**
- Should `PathogenDetection` carry LOINC codes, or defer to OMOP mapping?
- Linked class or attribute on specimen record?
- Estimates one focused 2-hour sprint with Bioinformaticist gets to reviewable draft.

---

### Bioinformaticist — Schema + Pipeline
**Recommendation on PathogenDetection:** Should be a **separate linked class** (one-to-many from `TickSpecimen`), not a direct attribute. Rationale: single specimens can carry co-infections; each detection event has its own assay metadata, quality flags, and sequence accession.

**Identifier solution:** Use `sampleID` as the join key between `tck_pathogen` and `tck_fielddata`. Document the `uid` ↔ `sampleID` mapping in schema metadata.

**Required genomic fields for PathogenDetection:**
- `sequenceAccession` (GenBank/ENA)
- `targetGene` (locus amplified — 16S, *groEL*, *ospC*, etc.)
- `percentIdentity` and `queryCoverage` (floats)
- `detectionMethod` (enum: PCR, metagenomic, culture)
- `amplicon_length` (integer)
- `qualityFlag` (controlled vocabulary)
- `referenceSequenceID` (accession used for identity calculations)

**Decision requested:** Scope schema to NEON-only now, or design immediately for extensibility to GBIF occurrence records and clinical case data?

---

### Clinical Informaticist — OMOP Phenotypes
**Lyme disease phenotype drafted** — two-pathway structure:
- *Confirmed:* qualifying diagnosis code + laboratory confirmation
- *Probable:* clinical diagnosis alone with supporting exposure/tick-bite code

**ICD-10 codes:** A69.2 (Lyme disease), B31.81 (erythema migrans), Z20.821 (contact/exposure to Lyme disease)

**LOINC codes:** 31374-3 (Borrelia burgdorferi antibody, EIA), 47234-5 (Western blot IgG), 47235-2 (Western blot IgM)

**Logic:** Lab result must fall within 60-day window of condition start date.

**Unresolved:** Two-tier serology logic — require both EIA + Western blot, or allow EIA alone with qualifying diagnosis? (CDC standard requires both, but CDW-H data shows many clinicians document only EIA.)

**Answer on Curator's LOINC question:** YES — include LOINC codes directly in `PathogenDetection`. NCBITaxon captures *what* was detected; LOINC captures *how* (test method and specimen type). These are complementary, not redundant, and the distinction matters for sensitivity/specificity interpretation.

**Needs from team:**
- NEON site bounding boxes/county crosswalks from Tick Ecologist (for CDW-H geographic filter)
- Minimum viable pathogen confirmation record definition from Bioinformaticist (for OMOP linkage)

**Anaplasmosis/ehrlichiosis:** Outlined (A77.49, LOINC 32854-8; A77.40, LOINC 41474-3) but not fully drafted. On track within 2 weeks of finalizing Lyme phenotype.

---

### Tick Ecologist — NEON Site Selection
**Candidate sites identified:**

| Site | Location | County | Rationale |
|------|----------|--------|-----------|
| SCBI | Front Royal, VA | Warren County, VA | Top candidate — robust *I. scapularis* + *A. americanum* co-occurrence, continuous sampling since 2014 |
| SERC | Edgewater, MD | Anne Arundel County, MD | Strong pathogen prevalence data; farther from UNC patient population |
| ORNL | Oak Ridge, TN | Roane County, TN | ~400 km from Chapel Hill; *I. scapularis* + *A. americanum* data; Appalachian migration patterns |
| TALL | Talladega NF, AL | Clay/Cleburne Counties, AL | Strong *A. americanum* dataset; relevant for ehrlichiosis analyses |

**CRITICAL CHALLENGE:** No NEON sites in North Carolina. This is a fundamental spatial mismatch between ecological data and UNC/CDW-H clinical catchment area.

**Geographic boundaries for Clinical Informaticist:** County-level crosswalks available by end of week. Patient residence filtering should be defined at county level, not plot level.

**Decision needed from team:** Expand pilot to adjacent state sites as ecological proxies, OR filter CDW-H by patient travel/exposure zones near VA and TN sites?

**Needs from Curator:** Verify data completeness for DP1.10092.001 at candidate sites; document 2020 COVID-era sampling gap (flagged by Rivera 2023).

---

### Public Health Researcher — Stakeholder Engagement
**Four stakeholder tiers identified:**
1. State and county health departments (endemic and expanding-risk regions)
2. Clinical partners (primary care, ED, urgent care in high-incidence counties)
3. Community-based organizations (rural, agricultural, outdoor recreation communities)
4. School systems and public health nursing networks

**Engagement mechanisms:** State health department working group with shared dashboard access; clinical decision support pilot; localized spring campaign toolkit.

**Health equity concerns:** Migrant farmworkers, outdoor laborers, and uninsured rural populations carry disproportionate tick exposure burden but are underrepresented in surveillance data. Risk maps may systematically undercount burden in these communities. Prevention messaging framed around "seek healthcare promptly" has unequal feasibility across populations.

**URGENT BLOCKER:** State health departments need materials by early April for pre-season provider trainings. Research timeline may not align with public health calendar.

**Needs from team:**
- "Good enough for public communication" threshold from Tick Ecologist + Bioinformaticist (with uncertainty language)
- Clinical Informaticist input on EHR-implementable decision support
- Scientific Critic to stress-test equity framing

---

### Scientific Critic — Causal Framework
**DAG progress:** Draft exists tracing primary pathway: tick population density → human-tick contact probability → *Borrelia burgdorferi* exposure → seroconversion → clinical presentation → diagnosis.

**Three major unresolved confounders:**
1. Regional healthcare-seeking behavior (affects both exposure probability and detection)
2. Diagnostic practice variation (determines whether a case enters CDW-H at all)
3. Land-use patterns (drives both tick habitat and human recreational exposure simultaneously)

**Critical concern — serology logic:** The unresolved two-tier serology logic is not a schema detail — it is a source of **differential misclassification in the outcome variable**. If case definition sensitivity/specificity varies systematically by region (likely given lab and clinician heterogeneity), any ecological gradient in tick infection prevalence could be confounded by an artifactual gradient in case ascertainment. DAG outcome node is underspecified until this is resolved.

**Critical concern — schema extensibility:** Designing a NEON-only schema and extending later encodes spatial and methodological assumptions that will create silent misalignment with GBIF/clinical data. This is a **validity threat**, not merely technical debt.

**Needs from team:**
- GIS-precise NEON site footprints vs. CDW-H catchment boundary comparison
- Preliminary characterization of diagnostic practice variation across CDW-H institutions
- `PathogenDetection` class draft before finalizing causal framework measurement model

---

## Three Decisions Made

**Decision 1: Schema extensibility — design for it now.**
`PathogenDetection` carries LOINC codes and non-NEON-specific method/specimen vocabularies. GBIF and OMOP alignment are first-class constraints in the current sprint, not future aspirations. Rationale: extensibility cost at design time is low; refactoring cost after data is flowing is high; a NEON-only schema bakes in assumptions that undermine clinical integration — the entire purpose of this project.

**Decision 2: Two-tier serology — implement both pathways as distinct, queryable strata.**
Confirmed = EIA + Western blot. Probable = EIA alone + qualifying diagnosis. All analyses report results stratified by phenotype pathway until empirical concordance is validated. Rationale: analytically conservative; prevents differential misclassification; preserves equity signal since populations with less diagnostic follow-through will be systematically undercounted under a two-test requirement.

**Decision 3: Spatial mismatch — filter CDW-H by exposure-zone proximity.**
Primary strategy is patient residence filtering using county-level NEON crosswalks. Adjacent-state proxy expansion retained as secondary sensitivity analysis only. Rationale: filtering by exposure zone is methodologically stronger than administrative state boundaries; preserves human-tick contact geography as the linking variable.

---

## Revised Action Items — Next Two Weeks

| Priority | Task | Owner | Collaborators | Deadline |
|----------|------|-------|---------------|----------|
| CRITICAL | `PathogenDetection` class draft (LOINC, genomic fields, extensible method/specimen vocabularies) | Curator + Bioinformaticist | Clinical Informaticist (LOINC review) | April 1 |
| CRITICAL | Serology strata implementation in OMOP phenotype | Clinical Informaticist | Scientific Critic | April 1 |
| CRITICAL | County-level crosswalks for SCBI, SERC, ORNL, TALL + CDW-H filtering protocol | Tick Ecologist | Clinical Informaticist | March 28 |
| HIGH | Verify DP1.10092.001 data completeness at pilot sites; document 2020 COVID gap | Data Curator | Tick Ecologist | April 1 |
| HIGH | Update DAG with resolved outcome node; characterize diagnostic practice variation across pilot states | Scientific Critic | Clinical Informaticist | April 8 |
| HIGH | Minimum viable pathogen confirmation record definition for OMOP linkage | Bioinformaticist | Clinical Informaticist | April 4 |
| HIGH | Stakeholder materials package for state health departments (pilot scope, sites, timeline, limitations) | Public Health Researcher | Architect (review) | April 4 |
| MEDIUM | Anaplasmosis/ehrlichiosis phenotype drafts using resolved serology framework as template | Clinical Informaticist | Scientific Critic | April 11 |
| MEDIUM | GIS-precise NEON site footprints vs. CDW-H catchment boundary comparison | Tick Ecologist | Bioinformaticist | April 8 |
| MEDIUM | Schema documentation: `uid` ↔ `sampleID` mapping + GBIF/OMOP alignment notes | Data Curator | Bioinformaticist | April 8 |

---

## Acknowledged Risks

1. **Outcome variable integrity:** The Critic is correct — an unresolved outcome variable means the DAG is a diagram, not a causal framework. Resolving serology strata by April 1 is non-negotiable.

2. **Schema design validity:** NEON-only design is a validity threat embedded in data infrastructure. The extensibility decision made today closes this risk.

3. **Public health calendar:** State health department materials are due April 4. The research will not be complete by then. The Public Health Researcher will deliver a package that accurately represents pilot scope, data strength, and limitations. We do not overstate. We do not go silent.

4. **Health equity structural gap:** Migrant farmworkers and rural uninsured are systematically excluded from both CDW-H and NEON catchments. This must be explicitly characterized in all pilot outputs as a limitation we own, not one we obscure. The Critic will stress-test the equity framing during DAG revision.

---

## Next Meeting Agenda — April 8, 2026

1. `PathogenDetection` schema draft review — Curator leads, full team critique (15 min)
2. Serology phenotype strata review — Clinical Informaticist presents confirmed/probable implementation; Critic responds (15 min)
3. Spatial analysis update — Tick Ecologist presents crosswalks and CDW-H filtering protocol (15 min)
4. DAG revision — Critic presents updated causal framework with resolved outcome node and diagnostic practice variation characterization (15 min)
5. Stakeholder materials review — Public Health Researcher presents April health department package for team input (10 min)
6. Schema extensibility confirmation — verify GBIF and OMOP alignment are structurally present in draft (10 min)

**Total:** ~80 minutes. This meeting should produce a reviewable schema draft, a finalized phenotype logic decision, and a spatial analysis plan. Those three outputs clear the path for the analysis phase to begin.
