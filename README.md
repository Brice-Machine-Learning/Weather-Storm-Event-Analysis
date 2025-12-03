# 🌪️ Storm Events Analysis (NOAA)
_Advanced ML Pipeline for Extreme Weather Risk Modeling_

![Status: In Progress](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)
![Dataset Size: Massive](https://img.shields.io/badge/Dataset-215%20Files%20%7C%2025M%2B%20Rows-red?style=flat-square)
![Framework: Python](https://img.shields.io/badge/Framework-Python%203.12-blue?style=flat-square)
![Tools: Pandas | DuckDB | Scikit-Learn](https://img.shields.io/badge/Tools-Pandas%20%7C%20DuckDB%20%7C%20Scikit--Learn-green?style=flat-square)
![Hazards: Floods | Hurricanes | Tornadoes](https://img.shields.io/badge/Hazards-Floods%20%7C%20Hurricanes%20%7C%20Tornadoes-orange?style=flat-square)
![CI Status](https://github.com/Brice-Repo-Name/storm-events-analysis/actions/workflows/ci-data-pipeline.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)
![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)

---

## 🧭 Project Overview
This project analyzes and models the **NOAA Storm Events Database**, focusing on major U.S. hazards: **floods**, **hurricanes**, and **tornadoes**.  
The goal is to produce hazard-specific models that estimate property damage risk after normalizing all costs to **2025 USD**.

The pipeline follows a clear data lineage (raw → interim → processed), aligns with reproducible research standards, and uses modular notebooks and helper scripts to keep the workflow clean and maintainable.

---

## 🎯 High-Level Scope
- **Event separation** — Floods, hurricanes, and tornadoes processed independently  
- **Cost normalization** — CPI adjustment to 2025 USD  
- **Training cutoff (1996+)** — Focus on modern, higher-quality records  
- **Artifacts** — Clean datasets, feature tables, trained models, reports, model card

---

## 🧹 Cleaning & Quality Rules
### General Rules
- Remove duplicate EVENT_ID entries  
- Standardize data types  
- Handle missing identifiers  
- Validate FIPS, coordinates, and event codes  

### Hazard‑Specific Checks
- **Floods:** rainfall/depth consistency  
- **Hurricanes:** wind units + storm name validation  
- **Tornadoes:** EF-scale and path geometry  

### Damage Processing
- Parse K/M/B multipliers  
- Normalize to 2025 USD  
- Merge fatalities & injuries safely  

---

## 🔄 Pipeline Workflow
1. **00_data_download** — Download raw files  
2. **01_data_quality_profiling** — Missingness, duplicates, cutoff decision  
3. **Master merge** — Build `master_events.parquet`  
4. **Hazard filtering** — Floods, hurricanes, tornadoes subsets  
5. **Feature engineering** — Hazard bins + CPI normalization  
6. **Modeling** — Baselines → tuning → selection  
7. **Error & bias analysis**  
8. **Risk scoring**  
9. **Reporting + artifact export**  

---

## 📂 Repository Structure

For full structure, see `docs/01_architecture/01_project_structure.md`  
Summarized structure:

```plaintext
storm-events-analysis/
│
├── data/                 # raw, interim, processed
├── notebooks/            # 00–10 pipeline
├── reports/              # figs, tables, summaries
├── models/               # experiments + artifacts
├── src/                  # reusable utilities
└── tests/                # health checks
```

---

## 📘 Notebook Roles
- `00` → data acquisition  
- `01` → profiling  
- `02–03` → EDA + geospatial  
- `04` → hazard splits + FE  
- `05–06` → modeling  
- `07` → error/bias  
- `08` → risk scoring  
- `09–10` → reporting + export  

---

## ⚙️ Environment Setup
```bash
conda env create -f environment.yml
conda activate storm-events
```

---

## 📑 Documentation & Outputs
- Figures, tables, model artifacts  
- Model card  
- Processed feature datasets  
- Hazard-specific parquet files  

---

## 🏷 Version History

This project uses **Semantic Version History** (`MAJOR.MINOR.PATCH`).

Latest release: **`v0.1.0`**

Release notes are maintained in:
- `CHANGELOG.md`
- GitHub Releases (when publishing tagged versions)

---

## 📫 Contact

If you’d like to connect, collaborate, or discuss the project:

- **Email:** [brice@devbybrice.com](mailto:brice@devbybrice.com)
- **LinkedIn:** [linkedin.com/in/brice-a-nelson-p-e-mba-36b28b15](https://www.linkedin.com/in/brice-a-nelson-p-e-mba-36b28b15/)
- **Website:** [devbybrice.com](https://www.devbybrice.com)


