# 🌪 Storm Events Analysis (NOAA)

This project explores and models NOAA Storm Events data (hurricanes, floods, tornadoes, etc.).  
It combines **data science (EDA, visualization, trend analysis)** with **machine learning (damage prediction, risk modeling)**.

---

## 📌 Project Scope (High-Level)
- **Hazard separation**: Run **separate models** for floods, hurricanes, and tornadoes.  
- **Cost normalization**: Convert all damage values to **2025 USD** using CPI/GDP deflators.  
- **Training cutoff**: Use **1996 onward** for baseline models (higher data quality).  
- **Deliverables**: Hazard-specific datasets, normalized costs, trained models, and a `model_card.md`.

---

## 🧹 Cleaning & Pipeline Highlights
- **Cleaning rules**:  
  - Drop duplicates, fix missing values, standardize types.  
  - Event-specific checks (wind units, EF scale, rainfall bins).  
  - Normalize damage multipliers (`K/M/B`) and convert to USD.  
  - Standardize geographies (FIPS codes) and flag outliers.  

- **Data pipeline**:  
  1. Download & log raw NOAA files → `data/raw/`.  
  2. Merge yearly files → `data/interim/master_events.parquet`.  
  3. Split into hazard subsets (`floods`, `hurricanes`, `tornadoes`).  
  4. Apply cost normalization + feature engineering.  
  5. Train/tune models per hazard.  
  6. Export artifacts + reports + `model_card.md`.  

---

## 📂 Project Structure
- `data/` → raw, interim, and processed datasets  
- `notebooks/` → numbered Jupyter notebooks for analysis pipeline  
- `reports/` → saved figures, tables, and summary write-ups  
- `models/` → trained model artifacts and experiment logs  
- `src/` → reusable helper scripts (data cleaning, viz, feature engineering)  
- `tests/` → unit tests for helper functions  

---

## 🚀 Workflow
1. `00_data_download.ipynb` → Download/extract NOAA datasets  
2. `01_data_quality_profiling.ipynb` → Assess missingness, odd values  
3. `02_eda_overview.ipynb` → Global trends, correlations  
4. `03_geo_eda_mapping.ipynb` → Geographic mapping & heatmaps  
5. `04_feature_engineering.ipynb` → Build ML features  
6. `05_baseline_models.ipynb` → Quick baseline models  
7. `06_model_tuning_and_selection.ipynb` → Model optimization  
8. `07_error_analysis_and_bias_checks.ipynb` → Evaluate fairness & errors  
9. `08_risk_scoring_and_thresholds.ipynb` → Convert predictions into categories  
10. `09_reporting_figures_and_tables.ipynb` → Generate final plots/tables  
11. `10_export_artifacts.ipynb` → Save models, datasets, and docs  

---

## ⚙️ Environment Setup
```bash
conda env create -f environment.yml
conda activate storm-events