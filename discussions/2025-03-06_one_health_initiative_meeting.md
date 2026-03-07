# Team Meeting: One Health Tick-Borne Disease Research Initiative

**Date:** March 6, 2025
**Participants:** Architect (Lead), Bioinformaticist, Scientific Critic, Data Curator, Clinical Informaticist, Tick Ecologist, Public Health Researcher

## Agenda

Develop a research plan for investigating the connections between ecosystem health, tick and pathogen abundance, and human health outcomes, based on the NEON Convergence Summit proposal framework.

---

## Discussion Summary

### Architect (Principal Investigator)

This research initiative presents an excellent opportunity to leverage NEON's continental-scale ecological data alongside clinical health records to understand tick-borne disease dynamics. Our approach should integrate:

1. **Ecological surveillance** using NEON tick abundance (DP1.10093.001) and pathogen (DP1.10092.001) data
2. **Clinical outcomes** from health systems like CDW-H
3. **Environmental drivers** including climate, vegetation, and host community data

The key innovation will be creating a unified data framework that bridges ecological and clinical domains.

### Tick Ecologist

From an ecological perspective, NEON provides exceptional resources:

- **Standardized sampling protocols** across 81 sites enable cross-site comparisons
- **Multi-trophic data** linking ticks, small mammals (DP1.10072.001), and vegetation structure
- **Temporal depth** for detecting long-term trends and seasonal patterns

Key ecological questions to address:
- How do host community composition and diversity affect pathogen prevalence?
- What environmental factors drive tick population dynamics across climate gradients?
- How do land use changes influence tick-borne disease risk?

### Bioinformaticist

For computational approaches, I recommend:

1. **Pathogen genomics pipeline** for strain typing and phylogeography
2. **Species distribution modeling** integrating NEON environmental data
3. **Machine learning models** predicting disease risk from ecological variables

Data integration strategy:
```
NEON Tick Data → Darwin Core standardization →
  ↓
Pathogen Sequences → NCBI/GenBank linkage →
  ↓
Integrated analysis pipeline
```

### Clinical Informaticist

To connect ecological findings to human health:

1. **OMOP CDM implementation** for standardizing clinical data across institutions
2. **Computable phenotypes** for tick-borne diseases (Lyme, anaplasmosis, ehrlichiosis)
3. **Spatio-temporal linkage** between NEON sites and patient residences

CDW-H at UNC can serve as a pilot site, with ~20 years of clinical data and established informatics infrastructure.

### Data Curator

For FAIR data management:

1. **LinkML schemas** defining shared data models across domains
2. **Ontology bindings** using:
   - NCBITaxon for pathogen taxonomy
   - ENVO for environmental contexts
   - UBERON for anatomical terms
   - Darwin Core for occurrence data
3. **BCO (Biological Collections Ontology)** for specimen provenance

Proposed data harmonization architecture:
```
Ecological Data (NEON) ──┐
                         ├── LinkML Schema ── Integrated Database
Clinical Data (OMOP) ────┘
```

### Public Health Researcher

Public health translation priorities:

1. **Risk prediction tools** for state/local health departments
2. **Surveillance enhancement** integrating ecological early warning signals
3. **Health equity analysis** examining disparities in tick-borne disease burden

Policy-relevant outputs:
- County-level risk maps updated with real-time ecological data
- Clinical decision support for endemic regions
- Public awareness campaigns timed to ecological risk periods

### Scientific Critic

Critical considerations for the research plan:

**Strengths:**
- Leverages unprecedented continental-scale standardized data
- Novel integration of ecological and clinical domains
- Strong interdisciplinary team coverage

**Potential Weaknesses:**
1. **Spatial mismatch** - NEON sites may not align with clinical catchment areas
2. **Temporal lag** - Ecological exposures precede clinical presentations by weeks to months
3. **Confounding factors** - Human behavior, healthcare access, diagnostic practices vary regionally

**Recommendations:**
- Develop explicit causal models before analysis
- Include validation cohorts from regions with different ecological/clinical contexts
- Address detection bias in both ecological and clinical data

---

## Synthesized Research Plan

### Phase 1: Data Infrastructure (Months 1-6)
- Develop LinkML schemas for tick-pathogen-health data integration
- Establish NEON data access pipelines using neonUtilities
- Define OMOP-based computable phenotypes for tick-borne diseases
- Create Darwin Core-compliant occurrence database

### Phase 2: Ecological Analysis (Months 4-12)
- Characterize tick abundance and pathogen prevalence across NEON sites
- Model environmental and host community drivers
- Develop predictive models for disease risk

### Phase 3: Clinical Integration (Months 8-18)
- Extract and standardize clinical data from partner institutions
- Link ecological risk indicators to clinical outcomes
- Validate predictive models against health records

### Phase 4: Translation (Months 15-24)
- Develop decision support tools for clinicians
- Create risk communication products for public health
- Publish findings and data products

### Key Deliverables
1. Integrated ecological-clinical data platform
2. Validated risk prediction models
3. Clinical decision support algorithms
4. Public health surveillance enhancement tools
5. Open-source data schemas and pipelines

---

## Action Items

| Task | Lead | Timeline |
|------|------|----------|
| Draft LinkML schema for tick-pathogen data | Curator + Bioinformaticist | 2 weeks |
| Identify pilot NEON sites near clinical partners | Tick Ecologist + Architect | 1 week |
| Define OMOP phenotypes for Lyme disease | Clinical Informaticist | 3 weeks |
| Develop causal framework diagram | Critic + Architect | 2 weeks |
| Outline public health stakeholder engagement | Public Health Researcher | 2 weeks |

---

## Next Meeting

Topic: Review draft data schemas and site selection
Proposed Date: TBD
