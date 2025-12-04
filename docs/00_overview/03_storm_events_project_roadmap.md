# 📘 **Storm Events Analysis — Project Roadmap & Master Checklist**

*A hybrid roadmap combining a high-level overview and a technical, step-by-step execution plan.*

---

# 🧭 **1. Executive Summary**

The **Storm Events Analysis Project** is a large-scale, multi-phase pipeline built to transform decades of NOAA severe weather records into clean, hazard-specific predictive models. The project uses a structured set of Jupyter notebooks, a reproducible data/processing pipeline, and separate modeling tracks for **floods, hurricanes, and tornadoes**.

The final outputs include:  
- Hazard-specific, cost-normalized feature datasets  
- Tuned ML models for each hazard  
- Risk scoring thresholds  
- A polished model card and visual report package  
- A full `models/` directory of serialized artifacts  
- Reusable EDA, mapping, and feature engineering utilities

This roadmap provides both a **high-level narrative** and a **precise engineering checklist** to move confidently through the entire workflow.

---

# 🧩 **2. High-Level Phases**

**PHASE 0 – Project Setup**  
Repo structure, environment, helpers, early decisions.

**PHASE 1 – Raw Data Acquisition**  
Download 200+ NOAA files, log metadata, build data dictionary draft.

**PHASE 2 – Profiling & Cleaning Rules**  
Missingness, duplicates, pre-1996 assessment, cleaning rules plan.

**PHASE 3 – Master Dataset Merge**  
Join details + fatalities + locations into a single master parquet file.

**PHASE 4 – Hazard Splits & EDA**  
Create floods/hurricanes/tornadoes interim datasets; perform EDA & mapping.

**PHASE 5 – Feature Engineering**  
Normalize costs to 2025 USD, build temporal/spatial/hazard features.

**PHASE 6 – Modeling (Baseline → Tuned)**  
Train separate models per hazard; select tuned best model.

**PHASE 7 – Error Analysis**  
Residuals, bias checks, confusion matrices, limitations.

**PHASE 8 – Risk Scoring**  
Convert model outputs into Low / Medium / High hazard-specific tiers.

**PHASE 9 – Reporting & Exports**  
Produce figures, tables, summary notes, and model card.

---

# 📚 **3. Full Technical Roadmap & Checklist**

## **PHASE 0 — Project Setup**

### ✔ Repository & Environment
- [ ] Clone/create `storm-events-analysis/`
- [ ] Add conda environment & lock files (`environment.yml`)
- [ ] Set up project structure:
```
data/raw/
data/interim/
data/processed/
models/
reports/
src/
notebooks/
```
- [ ] Initialize README
- [ ] Add helper modules

### ✔ Early Decisions
- [ ] Cutoff year: **1996+**
- [ ] Hazards: Floods, Hurricanes, Tornadoes
- [ ] Cost normalization: CPI-based → 2025 USD

---

## **PHASE 1 — Data Acquisition**

*Notebook: `00_data_download.ipynb`*

- [ ] Download NOAA files
- [ ] Save into `data/raw`
- [ ] Log SHA checksums
- [ ] Draft data dictionary

---

## **PHASE 2 — Data Profiling & Cleaning Rules**

*Notebook: `01_data_quality_profiling.ipynb`*

- [ ] Missingness/duplicates
- [ ] Type normalization
- [ ] Outliers
- [ ] Pre-1996 assessment
- [ ] Build `cleaning_rules.md`

---

## **PHASE 3 — Merge Into Master Dataset**

- [ ] Merge details + fatalities + locations
- [ ] Validate EVENT_ID linking
- [ ] Save → `data/interim/master_events.parquet`

---

## **PHASE 4 — Hazard Splits & EDA**

- [ ] Split into:
  - floods.parquet
  - hurricanes.parquet
  - tornadoes.parquet
- [ ] Global EDA
- [ ] Geo heatmaps

---

## **PHASE 5 — Feature Engineering**

- [ ] Normalize costs to 2025 USD  
- [ ] Temporal / spatial features  
- [ ] Hazard-specific features  
- [ ] Save final feature tables

---

## **PHASE 6 — Modeling**

- [ ] Baseline models
- [ ] Tuning (Optuna/Grid/Random)
- [ ] Serialize best models

---

## **PHASE 7 — Error Analysis**

- [ ] Residuals/confusion matrices
- [ ] Bias checks (state/region/time)
- [ ] Document limitations

---

## **PHASE 8 — Risk Scoring**

- [ ] Define Low/Med/High thresholds  
- [ ] Precision@k or cost-based  
- [ ] Save thresholds JSON

---

## **PHASE 9 — Reporting & Export**

- [ ] Figures & tables
- [ ] model_card.md
- [ ] Export final datasets & samples

---

# 🏁 **4. Completion Criteria**

- Full reproducibility  
- Hazard models complete  
- Documentation + model card  
- Final artifacts exported  

