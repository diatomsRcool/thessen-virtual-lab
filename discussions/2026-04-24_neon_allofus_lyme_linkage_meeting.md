# Thessen Virtual Lab Team Meeting
**Date**: April 24, 2026
**Agenda**: Research plan to link NEON tick-borne disease prevalence (SCBI, SERC, BLAN) with human clinical outcomes from NIH All of Us (Maryland & Virginia participants)

---

## Opening — Architect

Thank you everyone for joining. This is a genuinely exciting and timely research question — one that sits at the intersection of ecological surveillance, clinical informatics, and public health. Let me frame what we're trying to do.

**The core question**: Does variation in *Borrelia burgdorferi* prevalence among tick populations at NEON sites in the Mid-Atlantic region predict or correlate with tick-borne disease diagnoses and phenotypic presentations in nearby human populations, as captured in NIH All of Us clinical data?

Our NEON sites of interest — **SCBI** (Smithsonian Conservation Biology Institute, Front Royal, VA), **SERC** (Smithsonian Environmental Research Center, Edgewater, MD), and **BLAN** (Blandy Experimental Farm, Boyce, VA) — are all within NEON Domain 02 (Mid-Atlantic). Rivera (2023) confirmed that both *Ixodes scapularis* and *Amblyomma americanum* are present at these sites. This is our ecological anchor.

**Our data bridge**: We have Lyme disease prevalence data from the tick population at these sites broken down by site and year (from the PDF provided). On the clinical side, the NIH All of Us Research Program provides OMOP-formatted EHR data for participants in Maryland and Virginia — the two states that encompass all three NEON sites.

**Key questions this meeting needs to answer**:
1. How do we operationalize "nearby human populations" given the geographic resolution constraints of All of Us data?
2. Which clinical phenotypes and diagnoses should we include beyond confirmed Lyme diagnosis codes?
3. What is the appropriate temporal alignment between ecological and clinical data?
4. What statistical approach handles the multi-site, multi-year, ecological-to-individual linkage?
5. What are the major threats to validity we need to address?

---

## Tick Ecologist

This proposal maps well onto existing NEON data infrastructure, and I want to highlight some important ecological nuances that will shape the analysis design.

**What we have from NEON at these three sites**:
- **Tick abundance** (DP1.10093.001): Drag cloth sampling every 3-6 weeks during the growing season, with counts by species, life stage, and sex. All three sites have multi-year records.
- **Tick pathogen status** (DP1.10092.001): PCR-based testing for *Borrelia burgdorferi*, *B. miyamotoi*, *Anaplasma phagocytophilum*, *Babesia microti*, *Ehrlichia* spp., and others. Testing is performed on **nymphs**, which is the life stage most relevant to human infection.

**Critical point on what the Lyme prevalence graph shows**: The prevalence data is the **proportion of infected nymphs (PIN)** — the percentage of *I. scapularis* nymphs that test positive for *B. burgdorferi*. This is a better proxy for human risk than tick abundance alone, because it integrates both vector density and pathogen carriage. The **entomological risk index** (ERI = nymph density x PIN) is the gold standard for ecological risk.

**What to extract from NEON**:
1. Annual PIN for *B. burgdorferi* at each site
2. Annual nymph density (nymphs per 1600m² drag, standardized)
3. Derived annual ERI per site
4. Ancillary: small mammal abundance (DP1.10072.001), which drives infection dynamics with a 1-2 year lag

**Temporal considerations**: For *I. scapularis* in the Mid-Atlantic:
- Peak nymph questing: May-July
- Disease incidence in humans: diagnosis typically 2-8 weeks after bite, so peaks June-August
- We should expect same-year or perhaps 0-1 year lag between high PIN and elevated human diagnoses

**Landscape note**: SERC is on the Chesapeake Bay (Anne Arundel/Prince George's County border area), with a very different landscape from SCBI and BLAN, which are in the Shenandoah Valley. This matters for the human catchment area: SERC draws on a suburban/peri-urban population, while SCBI and BLAN serve more rural/exurban areas.

---

## Clinical Informaticist

**NIH All of Us — what's available**:
The Researcher Workbench provides OMOP-formatted data. The relevant tables are:
- `CONDITION_OCCURRENCE` — diagnoses with ICD-10 codes (mapped to SNOMED)
- `DRUG_EXPOSURE` — prescriptions (doxycycline is a proxy for tick-borne disease treatment)
- `MEASUREMENT` — lab results (Lyme serologies, CBC for thrombocytopenia patterns)
- `PERSON` — demographics including state of residence
- `SURVEY` — participant-reported data including detailed home location and outdoor activity

**Geographic resolution**: All of Us suppresses exact addresses for privacy. Available at **state** or **3-digit zip code prefix**:
- SCBI/BLAN catchment: 3-digit zip prefixes 226 (Warren, Clarke, Shenandoah counties VA)
- SERC catchment: 3-digit zip prefixes 210, 211, 217 (Anne Arundel, Prince George's MD)

**Clinical phenotypes — recommended three-tier approach**:

| Signal | OMOP Table | Rationale |
|---|---|---|
| ICD-10 A69.20-A69.23 | CONDITION_OCCURRENCE | Confirmed Lyme diagnosis |
| A79.82, A77.40, B60.0 | CONDITION_OCCURRENCE | Other TBDs (anaplasmosis, ehrlichiosis, babesiosis) |
| Doxycycline prescription (21-day course) | DRUG_EXPOSURE | Empiric Lyme treatment proxy |
| Erythema migrans (skin exam codes) | CONDITION_OCCURRENCE | Pathognomonic rash |
| Bell's palsy + geographic risk | CONDITION_OCCURRENCE | Lyme-associated cranial neuropathy |
| Lyme arthritis (M13.80 + serology) | CONDITION_OCCURRENCE + MEASUREMENT | Late Lyme phenotype |
| Positive *B. burgdorferi* Ab two-tier test | MEASUREMENT | LOINC 33931-2 and related |
| Thrombocytopenia + summer fever visits | MEASUREMENT + VISIT | Anaplasmosis/ehrlichiosis phenotype |

**Access requirements**: Requires a registered Researcher Workbench account, institutional affiliation, and project-specific access approval. Controlled Tier (which includes EHR data) requires additional training and IRB documentation.

---

## Public Health Researcher

**Study design recommendation**: This is an **ecological correlation study with individual-level clinical data** — a multi-level or contextual design. We're measuring exposure at the site/area level (tick prevalence from NEON) and outcome at the individual level (All of Us clinical records), linked by geography and time.

**Outcome definitions — three tiers**:

- *Tier 1* (most specific): Confirmed tick-borne disease diagnosis (ICD-10 codes, any TBD)
- *Tier 2* (broader): Probable tick-borne disease — ICD-10 OR doxycycline course OR positive serology
- *Tier 3* (broadest, phenotype-based): Any clinical encounter with tick-borne disease phenotype (erythema migrans, unexplained summer fever with thrombocytopenia, Lyme arthritis)

**Temporal design**: Panel dataset — one observation per site-catchment-area-year combination — covering **2018-2024** (All of Us enrollment start through current data).

**Exposure variable construction**:
- Primary: Annual PIN at the nearest NEON site
- Secondary: Annual ERI (density x PIN)
- Test 0-year and 1-year lag

**Key confounders to address**:
1. Healthcare access and healthcare-seeking behavior
2. Outdoor occupational and recreational exposure (available from All of Us Basics survey)
3. Awareness and testing rates (less differential within high-incidence MD/VA, but still relevant)
4. Population density and demographics (suburban SERC vs. rural SCBI/BLAN)

**Covariates**: Age, sex, race/ethnicity, insurance status, rurality index, year (fixed effect for secular trends), site (random effect or fixed stratification).

---

## Bioinformaticist

**Data integration pipeline — four stages**:

**Stage 1 — NEON Data Extraction**
```r
library(neonUtilities)
pathogens <- loadByProduct(
  dpID = "DP1.10092.001",
  site = c("SCBI", "SERC", "BLAN"),
  startdate = "2016-01",
  enddate = "2024-12"
)
```
Compute annual PIN = positive tests / total tests per site per year. Also pull DP1.10093.001 for nymph density to compute ERI.

**Stage 2 — All of Us Clinical Data**
```sql
-- Example: Lyme disease cases in MD/VA participants
SELECT p.person_id, c.condition_start_date,
       p.state_of_residence_concept_id
FROM condition_occurrence c
JOIN person p ON c.person_id = p.person_id
WHERE c.condition_source_value IN ('A69.20','A69.21','A69.22','A69.23')
  AND p.state_of_residence_concept_id IN (
    -- Maryland concept ID, Virginia concept ID
  )
```

**Stage 3 — Temporal and Spatial Linkage**
- Assign each All of Us participant to a NEON site catchment based on 3-digit zip code
- Extract diagnosis year for each participant-event
- Match to NEON annual PIN for that site-year (and lagged PIN)

**Stage 4 — Statistical Analysis**
- Primary: **Negative binomial regression** of annual TBD case rate on annual PIN, with site and year as covariates
- Secondary: **Individual-level logistic regression** with site-level PIN as contextual predictor (mixed effects, random intercept for site-catchment)
- Phenotype analysis: **Latent class analysis** to identify phenotype clusters, test whether class prevalence rates correlate with site-level PIN

**Tools**: R (`neonUtilities`, `glmmTMB`, `lme4`), Python/SQL for All of Us BigQuery, All of Us cohort builder.

---

## Data Curator

**Geographic linkage schema — proposed catchment zones**:

| NEON Site | State | 3-digit ZIP Prefixes | Counties |
|---|---|---|---|
| SCBI | Virginia | 226 | Warren, Shenandoah |
| BLAN | Virginia | 226 | Clarke, Frederick VA |
| SERC | Maryland | 210, 211, 217 | Anne Arundel, PG County |

Note: SCBI and BLAN share zip prefix 226. They should be treated as separate sites with distinct NEON exposure values, or combined as a single Shenandoah Valley catchment — the statistical team should decide.

**Temporal linkage**: Aggregate NEON pathogen data to annual PIN per site. Exclude 2020 (COVID-19 gap in NEON sampling).

**Correct denominator**: Use **enrolled All of Us participants with at least one EHR observation in the analysis year** per catchment, not census population. This controls for enrollment bias.

**Provenance**:
- NEON data: access via specific RELEASE tag (e.g., RELEASE-2024)
- All of Us data: document CDR version
- Linkage table: version-controlled and deposited

**Recommended integrated data model**:
```yaml
classes:
  SiteCatchmentYear:
    attributes:
      neon_site_id:                    # SCBI, SERC, BLAN
      year:
      annual_pin:                      # proportion infected nymphs
      annual_eri:                      # entomological risk index
      zip_prefix_3:                    # list of 3-digit zip codes in catchment
      tbd_case_count:                  # from All of Us
      catchment_enrolled_participants: # All of Us denominator
      tbd_case_rate_per_100k_enrolled:
```

---

## Scientific Critic

**Threat 1 — Ecological fallacy (most serious)**
We cannot confirm that individuals who got sick were exposed to ticks near the NEON sites. Mitigation: restrict to All of Us participants who report predominantly local outdoor exposure or stable residential address. Use the survey data.

**Threat 2 — Geographic mismatch**
3-digit zip prefixes are large relative to the NEON sampling footprint. Conduct a sensitivity analysis with tighter geographic buffers if county-level data is available in the Controlled Tier. Validate against CDC county-level Lyme surveillance.

**Threat 3 — Diagnosis ascertainment bias**
Lyme is underdiagnosed by 8-12x. Diagnostic rates may correlate with tick awareness, which may correlate with local tick prevalence — creating a spurious ecological correlation. Phenotype-based outcomes (Tier 2/3) partially mitigate this.

**Threat 4 — Temporal confounding**
Both tick prevalence and Lyme incidence have been increasing in the Mid-Atlantic due to climate change and range expansion. This secular trend could create spurious correlation. Year fixed effects help but test for non-linear temporal trends.

**Threat 5 — All of Us enrollment bias**
All of Us over-represents healthcare-engaged populations and under-represents rural areas. SCBI/BLAN catchments are more rural than SERC. Check for systematic enrollment differences across catchments.

**Threat 6 — 2020 data gap**
COVID-19 disrupted both NEON tick sampling and healthcare-seeking behavior. Exclude 2020 from primary analysis; include as sensitivity test.

**What would make this study convincing**:
1. External validation: correlate NEON PIN with CDC county-level Lyme incidence
2. Dose-response: test for monotonic relationship between PIN and case rates
3. Negative control: show the correlation does NOT hold for non-tick-borne diseases in the same participants
4. Site-specific analysis given heterogeneity between suburban SERC and rural SCBI/BLAN

---

## Discussion — Key Exchanges

**On denominator**: The correct denominator is enrolled All of Us participants with at least one EHR observation in the analysis year per catchment-year — not census population. This trades generalizability for internal validity.

**On SERC landscape validity**: SERC's forested peninsula habitat captures tick prevalence in conditions suburban residents may not encounter. However, *I. scapularis* has colonized suburban yards and parks regionwide, so SERC PIN may still serve as a valid regional endemicity proxy.

**On statistical power**: Rough estimate — ~30,000-40,000 All of Us participants in MD/VA total. Within a specific 3-digit zip catchment: 500-3,000 participants. At 100-300 diagnosed Lyme cases per 100,000 per year, we expect 1-9 cases per catchment-year — very sparse. **Resolution**: pool all MD/VA participants and use nearest NEON site PIN as a continuous predictor for the primary analysis; use tight catchments for sensitivity analyses only. Tier 2/3 phenotype outcomes will substantially increase case counts.

---

## Research Plan — Proposed Phases

### Phase 1 — Data Preparation (Months 1-3)

**NEON side**:
- Download DP1.10092.001 and DP1.10093.001 for SCBI, SERC, BLAN (all years, exclude 2020)
- Compute annual PIN, nymph density, and ERI per site per year
- Extract small mammal data (DP1.10072.001) for lagged host effects

**All of Us side**:
- Confirm Controlled Tier Researcher Workbench access and geographic data availability
- Query participants in Maryland and Virginia
- Define three outcome tiers
- Obtain enrolled participant counts per catchment-year as denominators

**Linkage**:
- Define catchment zones by 3-digit zip prefix
- Assign All of Us participants to nearest NEON site
- Build the `SiteCatchmentYear` integrated dataset

### Phase 2 — Validation of Ecological Exposure Metric (Months 3-4)

- Correlate annual NEON PIN per site with CDC county-level reported Lyme incidence in overlapping counties
- Validates NEON PIN as a meaningful ecological risk proxy before linking to All of Us

### Phase 3 — Primary Ecological Analysis (Months 4-6)

- **Model 1**: Negative binomial regression of annual TBD case rate on NEON annual PIN; year fixed effects, site random effect; test 0- and 1-year lag
- **Model 2**: Same using ERI as exposure
- **Model 3**: Individual-level logistic regression (TBD diagnosis yes/no) with site-level PIN as contextual predictor, individual demographics as covariates (mixed-effects)

### Phase 4 — Clinical Phenotype Analysis (Months 5-7)

- Latent class analysis (LCA) or hierarchical clustering of All of Us participants in MD/VA to identify TBD phenotype classes (classic Lyme, atypical fever, late Lyme arthritis, treatment-exposed without confirmed diagnosis)
- Test whether class prevalence rates correlate with site-level PIN

### Phase 5 — Sensitivity Analyses & Validation (Months 7-9)

- Exclude 2020; re-run all models
- Tighter geographic restriction (county-level if available)
- Negative control outcome test (non-tick-borne disease in same participants)
- Replication using CDC state/county surveillance as independent outcome

### Deliverables

1. Integrated `SiteCatchmentYear` dataset (FAIR, versioned, NEON component publicly shareable)
2. Validated catchment zone definition for NEON-to-All of Us linkage
3. Manuscript: "Ecological tick-borne pathogen prevalence predicts human tick-borne disease burden in the Mid-Atlantic: A NEON-NIH All of Us linked analysis"

---

## Open Questions

1. What years of NEON pathogen data are available for all three sites? Are there gaps beyond 2020?
2. What is the geographic resolution available in the All of Us Controlled Tier — state only, or 3-digit zip?
3. Should SCBI and BLAN be treated as separate sites or combined as a single Shenandoah Valley catchment?
4. Should additional NEON sites outside MD/VA (e.g., HARV in MA) be included as comparison sites to test whether the correlation is regionally specific?
5. Are there existing All of Us publications on Lyme disease that establish methodological precedent?

---

*Note: The file `LymePrevalencebySiteYEar.pdf` could not be rendered during this meeting (poppler-utils not installed). Run `brew install poppler` to enable PDF reading. The Lyme prevalence-by-site-year data in that file should be incorporated into Phase 1 of the pipeline.*
