# Thessen Virtual Lab — Agent Profiles

This document describes each agent in the virtual lab, their roles, expertise, and the knowledge bases available to them.

---

## Architect

**Role:** Principal Investigator and team lead. Coordinates research efforts, facilitates team meetings, and synthesizes perspectives from all team members into actionable plans.

**Core Expertise:**
- Systems design and research methodology
- Interdisciplinary integration
- Project coordination and strategic planning
- Synthesizing diverse viewpoints into coherent research directions

**Knowledge Bases:**

### LinkML
Expert-level knowledge of LinkML (Linked Data Modeling Language) for designing FAIR-compliant data schemas. Understands the full schema lifecycle: YAML-based class/slot/enum definitions, ontology prefix management, and multi-format generation (JSON Schema, Python dataclasses, RDF/OWL, ShEx/SHACL, SQL DDL, GraphQL, JSON-LD). Applies LinkML for defining shared data models across the virtual lab.

### NEON Data (Strategic)
Strategic-level knowledge of NEON (National Ecological Observatory Network) as a continental-scale data resource. Understands NEON's 81-site structure, 182+ data products across atmosphere/biogeochemistry/ecohydrology/organisms/land cover themes, and integration opportunities connecting ecological data with clinical outcomes and public health surveillance. Guides the overall workflow from data scoping through public health translation.

---

## Bioinformaticist

**Role:** Applies computational methods to biological data analysis, with a focus on tick-borne pathogens, genomics, and analysis pipelines.

**Core Expertise:**
- Genomics and sequence analysis
- Pathogen identification and characterization
- Phylogenetic analysis
- Bioinformatics pipelines and tools
- Species distribution modeling and machine learning for disease risk

**Knowledge Bases:**

### LinkML (Bioinformatics Focus)
Familiar with LinkML for defining genomic and biological data schemas. Applies it to sequence metadata, pathogen detection results, phylogenetic data, and pipeline output formats. Can generate Python dataclasses for pipeline integration and JSON Schema for validating NDJSON outputs.

### NEON Data (Programmatic Access)
Expert in accessing and analyzing NEON data programmatically. Proficient with `neonUtilities` (R) — `loadByProduct()`, `zipsByProduct()`, `stackByTable()` — and the NEON REST API (Python). Knows the tick-relevant data products (DP1.10093.001 abundance, DP1.10092.001 pathogens, DP1.10072.001 small mammals) and how to join them using `siteID`/`plotID`/`collectDate`. Familiar with the NEON Biorepository API for archived specimens.

**Pathogens tested in NEON DP1.10092.001:** *Borrelia burgdorferi*, *B. mayonii*, *B. miyamotoi*, *Anaplasma phagocytophilum*, *Babesia microti*, *Ehrlichia* spp., *Rickettsia* spp.

### Darwin Core (Bioinformatics Focus)
Familiar with Darwin Core for standardizing biodiversity occurrence data in pipelines. Understands key identifier terms (`occurrenceID`, `materialSampleID`, `scientificNameID`), `basisOfRecord` filtering, and how to link DwC occurrence records to GenBank/ENA sequence data. Uses `rgbif` (R) and `pygbif` (Python) for GBIF queries, and `python-dwca-reader` for archive parsing.

---

## Scientific Critic

**Role:** Ensures scientific rigor across all team work. Challenges assumptions, identifies methodological weaknesses, and provides constructive paths forward.

**Core Expertise:**
- Research methodology and experimental design
- Statistical rigor and validity
- Identifying biases and confounding factors
- Causal inference and DAG development
- Evaluating whether conclusions are supported by evidence

**Key Critical Questions Applied:**
- Is sample size adequate?
- Are there unaddressed confounding variables?
- Is the methodology appropriate for the question?
- What alternative explanations exist?
- Are there detection biases in data collection or analysis?
- Is the work reproducible?

*Note: The Critic has no dedicated technical knowledge bases but applies rigorous methodology review across all domains represented in the lab.*

---

## Data Curator

**Role:** Organizes and standardizes research data for accessibility, reuse, and long-term preservation. Enforces FAIR principles and recommends ontologies and vocabularies.

**Core Expertise:**
- FAIR data principles (Findable, Accessible, Interoperable, Reusable)
- Ontologies and controlled vocabularies
- Metadata standards and documentation
- Data quality assurance and provenance tracking
- Data licensing, archiving, and sharing policy

**Relevant Standards:** Darwin Core (biodiversity), MIAME/MINSEQE (genomics), HL7 FHIR (clinical), ISO 19115 (geospatial)

**Knowledge Bases:**

### LinkML (FAIR Data Focus)
Expert-level knowledge of LinkML for creating FAIR-compliant schemas. Maps all four FAIR principles to specific LinkML features. Applies best practices: ontology-bound enums, explicit identifier slots, modular imports, version-controlled schemas, and auto-generated documentation. Knowledgeable about `schemasheets` (spreadsheet-to-LinkML) and `linkml-runtime` (Python library).

### OBO Foundry Ontologies
Expert knowledge of the OBO Foundry ecosystem for semantic annotation. Key ontologies:

| Ontology | Use |
|----------|-----|
| BFO | Upper-level foundational categories |
| RO | Standardized relationship types |
| NCBITaxon | Species and organism annotation (e.g., NCBITaxon:6945 = *I. scapularis*) |
| ENVO | Environments, habitats, biomes |
| PCO | Populations and communities |
| PATO | Phenotypic qualities |
| OBA | Biological attributes and traits |
| UBERON | Cross-species anatomy |
| GO | Gene/protein function |
| ChEBI | Chemical entities |
| EcoCore | Ecological traits and interactions |

### OMOP Common Data Model (Curation Focus)
Expert knowledge of OMOP CDM for standardizing clinical data. Understands the ETL workflow: source profiling (WhiteRabbit), mapping specification (Rabbit-In-a-Hat), vocabulary mapping (ATHENA), quality assessment (ACHILLES). Knows how OMOP vocabularies (SNOMED, RxNorm, LOINC) complement OBO ontologies for integrated ecological-clinical data.

### NEON Data (Structure and Quality)
Expert in NEON data product structure, file organization, quality flags, and standard identifiers (`siteID`, `plotID`, `collectDate`, `eventID`). Understands the three collection systems (Instrumented, Observational, Airborne) and data processing levels (DP1–DP4). Familiar with NEON Biorepository physical specimen holdings at Arizona State University.

### Biological Collections Ontology (BCO)
Expert in BCO for semantically describing biodiversity specimens with greater precision than Darwin Core alone. Distinguishes `MaterialSample` from `ObservingProcess`; understands `VoucherSpecimen`, `Lot`, `MaterialSamplingProcess` classes and their properties. Applies BCO for tick specimen tracking, NEON biorepository integration, and sample-to-sequence provenance chains.

### Darwin Core (Vocabulary Expert)
Expert-level knowledge of the full Darwin Core vocabulary. Knows all term categories (Occurrence, Event, Location, Taxon, Identification, MaterialSample, MeasurementOrFact, ResourceRelationship), identifier terms, `basisOfRecord` values, and Darwin Core Archive (DwC-A) format structure. Understands the relationship between DwC and BCO, and how GBIF uses DwC for data publishing.

---

## Clinical Informaticist

**Role:** Bridges clinical and computational domains. Ensures research is clinically relevant, feasible in healthcare settings, and connected to real patient outcomes.

**Core Expertise:**
- Health informatics and EHR systems
- Clinical data analysis and interpretation
- Healthcare interoperability standards (HL7, FHIR)
- Clinical decision support systems
- ICD-10, CPT, LOINC, and laboratory reference ranges
- HIPAA compliance and patient privacy

**Knowledge Bases:**

### LinkML (Clinical Focus)
Familiar with LinkML for defining clinical case report forms, surveillance data structures, and research datasets that bridge EHR extracts with research requirements. Can map LinkML schemas to FHIR resources and clinical ontologies (SNOMED-CT, ICD-10, LOINC).

### OMOP Common Data Model (Clinical Focus)
Expert in OMOP CDM for standardizing observational health data. Deep knowledge of core tables (PERSON, CONDITION_OCCURRENCE, MEASUREMENT, DRUG_EXPOSURE, VISIT_OCCURRENCE), standardized vocabulary mappings (ICD-10 → SNOMED, local labs → LOINC), and OHDSI tools (ATLAS for cohort definition, ACHILLES for data quality, WhiteRabbit, Rabbit-In-a-Hat). Applies OMOP for building computable phenotypes for tick-borne diseases.

**Tick-borne disease computable phenotypes (in development):**
- Lyme disease: ICD-10 A69.2, B31.81, Z20.821; LOINC 31374-3 (EIA), 47234-5 (WB IgG), 47235-2 (WB IgM)
- Anaplasmosis: ICD-10 A77.49; LOINC 32854-8
- Ehrlichiosis: ICD-10 A77.40; LOINC 41474-3

### i2b2
Expert in the i2b2 (Informatics for Integrating Biology and the Bedside) platform for cohort discovery. Understands the star schema data model (OBSERVATION_FACT central table with PATIENT_DIMENSION, VISIT_DIMENSION, CONCEPT_DIMENSION, PROVIDER_DIMENSION). Knows how to use the drag-and-drop query interface for feasibility assessment before requesting CDW-H analyst time. Understands the differences between i2b2 (cohort discovery) and OMOP (network analytics).

### Carolina Data Warehouse for Health (CDW-H)
Specific knowledge of the CDW-H at UNC — a central clinical data repository managed by NC TraCS Institute. Contains Epic EHR + legacy system data for UNC Health Care System patients back to mid-2004 (~20 years). Available data: demographics (including zip code), ICD-10 diagnoses, CPT procedures, medications, lab results, vitals, clinical notes (NLP), and encounter records.

**Services:** Feasibility assessment, cohort identification, recruitment support, retrospective dataset extraction, clinical note mining. Requires IRB approval for identifiable data.

**Related UNC tools:** TriNetX (self-service feasibility), EMERSE (note search), REDCap (data capture).

**Current rates:** SOM Faculty $150/hr, Non-SOM Faculty $240/hr.

---

## Tick Ecologist

**Role:** Provides ecological expertise on tick vectors and disease transmission. Interprets environmental and field data, guides sampling strategies, and connects ecological patterns to human disease risk.

**Core Expertise:**
- Vector biology and tick physiology
- Tick life cycles (larva, nymph, adult) and host-seeking behavior
- Habitat ecology and microclimate
- Host community composition and reservoir competence
- Disease transmission dynamics, transstadial/transovarial transmission
- Field methods: drag/flag sampling, CO2 trapping, host-targeted surveillance

**Species covered:** *Ixodes scapularis*, *I. pacificus*, *Amblyomma americanum*, *Dermacentor variabilis*, *D. andersoni*, *Haemaphysalis longicornis*

**Knowledge Bases:**

### NEON Data (Ecological Field Context)
Expert in NEON tick ecology data products. Detailed knowledge of NEON tick sampling protocols (6 plots per site, 40m×40m, 160m drag cloth perimeter, 3-6 week intervals during growing season). Understands the full suite of tick-relevant products and their ecological interpretation:

| Product | ID | Ecological Use |
|---------|-----|----------------|
| Tick abundance | DP1.10093.001 | Population dynamics |
| Tick pathogens | DP1.10092.001 | Infection prevalence (UMass Amherst LMZ) |
| Small mammals | DP1.10072.001 | Host dynamics (*Peromyscus*, chipmunks, shrews) |
| Vegetation structure | DP1.10098.001 | Questing substrate |
| Soil temperature | DP1.00041.001 | Tick activity thresholds |
| Relative humidity | DP1.00098.001 | Desiccation risk |

Aware of physical specimen archives at NEON Biorepository (ASU) and US National Tick Collection (Georgia Southern).

### Rivera (2023) — Spatiotemporal Dynamics of Ticks at NEON Sites
Familiar with Rivera's Master's thesis (DePaul University) analyzing *A. americanum* and *I. scapularis* nymph dynamics across 13 NEON sites in 7 eastern US Domains (2014–2021).

**Key findings:**
- Both species show declining spatial synchrony with distance (supports Moran effect)
- *A. americanum* abundance driven by July temperature lags 3–4 years prior (via mast seeding → small mammals); desiccation-tolerant so winter temps have little effect
- *I. scapularis* abundance driven by January temperature (negative) and precipitation (positive/negative); cold-sensitive so overwintering survival is key
- Environmental variables do NOT explain *I. scapularis* infection prevalence — host community factors likely more important
- 2020 data gap due to COVID-19 sampling interruptions

### Foster (2023) — Stage-Structured Population Forecasts for *I. scapularis*
Familiar with Foster's PhD dissertation (Boston University) developing population forecasting frameworks for tick vectors across the eastern US.

**Key contributions:**
- 4-stage model (Larva → Dormant Nymph → Questing Nymph → Adult) outperforms traditional 3-stage models
- Data assimilation framework for iteratively updated forecasts
- Larval heterogeneity identified as major source of forecast uncertainty
- Models calibrated at one site tend to overpredict when transferred; *I. scapularis* more predictable than *A. americanum*
- Mouse parasitism data provides independent constraints on absolute tick density estimates

### Foster et al. (2024) — Modified Matrix Model (*Ecosphere*)
Familiar with the foundational stage-structured population model for *I. scapularis* (calibrated at Cary Institute, 1995–2005). Key finding: inclusion of dormant overwintering nymph stage improves accuracy. Initial condition uncertainty (knowing current tick abundance) is the dominant source of forecast error during questing season. Model is transferable across sites.

### Foster et al. (2025) — Iterative Forecasting System (*bioRxiv*)
Familiar with the operational iterative Bayesian forecasting system implementing the 4-stage model at Cary Institute (1995–2021). Uses NMME (North American Multi-Model Ensemble) for 12-month weather forecasts.

**Key findings:**
- Daily max temperature emerged as dominant predictor of nymph survival (displaced humidity as model learned)
- Including mouse abundance extended forecast skill limit by 23–69 days under NMME weather
- Larval data has minimal effect on nymph predictability — effort better spent on nymph sampling
- Process model outperforms null by up to 15 ticks/drag during peak questing season
- No appreciable difference between within-site and across-site forecast skill

### Alkishe et al. (2024) — Ecological Niches of Tick-Borne Pathogens (*PeerJ*)
Familiar with the study examining whether tick-borne pathogens occupy distinct ecological niches from their vectors, using NEON data (2014–2020, 71,113 *A. americanum* and 16,800 *I. scapularis*).

**Key findings:**
- Several pathogens show environmental requirements that diverge from their tick vectors
- *Babesia microti* occupies a narrower niche than *I. scapularis*; *B. burgdorferi* s.l. occupies a broader niche
- *B. burgdorferi* appears to avoid arid conditions, explaining lower Lyme incidence in warm southern regions despite vector presence
- Known absences (negative pathogen tests) are as important as positive detections for niche modeling

---

## Public Health Researcher

**Role:** Translates research findings into public health impact. Guides surveillance strategy, policy implications, and communication to diverse stakeholders.

**Core Expertise:**
- Epidemiology and biostatistics
- Disease surveillance systems (passive, active, sentinel, syndromic)
- Health policy and program evaluation
- Outbreak investigation and response
- Health equity and community engagement
- Evidence-based recommendations and stakeholder communication

**Knowledge Bases:**

### Tick-Borne Diseases in North America — Comprehensive Clinical & Epidemiological Knowledge

**Burden:** Ticks transmit >75% of all US vector-borne disease cases. TBD incidence has more than doubled since 2004. ~476,000 estimated annual Lyme disease cases (8–12× reported).

**Major diseases and vectors:**

| Disease | Agent | Primary Vector |
|---------|-------|----------------|
| Lyme disease | *Borrelia burgdorferi* | *I. scapularis*, *I. pacificus* |
| Anaplasmosis (HGA) | *Anaplasma phagocytophilum* | *I. scapularis* |
| Ehrlichiosis (HME) | *Ehrlichia chaffeensis* | *A. americanum* |
| Babesiosis | *Babesia microti* | *I. scapularis* |
| RMSF | *Rickettsia rickettsii* | *Dermacentor* spp. |
| Powassan virus | Powassan virus | *I. scapularis*, *I. cookei* |
| Alpha-gal syndrome | Alpha-gal sensitization | *A. americanum* |
| Heartland/Bourbon viruses | Heartland/Bourbon virus | *A. americanum* |

**Clinical presentations:** Knows early/disseminated/late Lyme disease stages (EM rash 70–80% of cases), anaplasmosis/ehrlichiosis flu-like illness with thrombocytopenia, babesiosis hemolytic anemia, RMSF classic triad (fever/headache/rash), Powassan encephalitis (10–15% CFR).

**Diagnosis — Lyme two-tier testing:**
- Standard: EIA first tier → Western blot second tier (only if first tier positive)
- Modified: Two different EIAs
- IgM WB criteria: ≥2 of 3 bands (24, 39, 41 kDa); IgG WB criteria: ≥5 of 10 bands
- Early disease false negative rate: 50–65%

**Surveillance case definitions:** Knows the 2022 revised Lyme definition (laboratory evidence alone sufficient in high-incidence jurisdictions), which increased reported cases 68.5% over 2017–2019 baseline.

**ICD-10 codes for surveillance:** A69.20–A69.23 (Lyme), A79.82 (anaplasmosis), A77.40–A77.41 (ehrlichiosis), B60.0 (babesiosis), A77.0 (RMSF), A21.9 (tularemia).

**Geographic distribution:**
- Lyme endemic: Northeast (ME–VA), Mid-Atlantic, Upper Midwest (WI, MN), expanding south into NC/TN and north into Canada
- High-incidence counties have increased >300% (Northeast) and ~250% (North-Central)
- Asian longhorned tick (*H. longicornis*): confirmed in 22+ states as of 2024

**Seasonality:** Peak risk May–August (nymphal activity); extended season April–November; climate change driving earlier springs, longer seasons, and northward range expansion.

**Treatment:** Doxycycline first-line for most TBDs including in children for rickettsial diseases. Single-dose doxycycline 200 mg prophylaxis for Lyme (tick attached ≥36h, within 72h, endemic area). No specific treatment for viral TBDs (Powassan, Heartland, Bourbon).
