# 🌪 Storm Events Analysis (NOAA)

This project explores and models NOAA Storm Events data (hurricanes, floods, tornadoes, etc.).  
It combines **data science (EDA, visualization, trend analysis)** with **machine learning (damage prediction, risk modeling)**.

## 📂 Project Structure
- `data/` → raw, interim, and processed datasets
- `notebooks/` → numbered Jupyter notebooks for analysis pipeline
- `reports/` → saved figures, tables, and summary write-ups
- `models/` → trained model artifacts and experiment logs
- `src/` → reusable helper scripts (data cleaning, viz, feature engineering)
- `tests/` → unit tests for helper functions

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

## ⚙️ Environment Setup
```bash
conda env create -f environment.yml
conda activate storm-events
```
