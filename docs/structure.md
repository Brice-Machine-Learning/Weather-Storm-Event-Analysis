# Project Structure

```mermaid
storm-events-analysis/
│
├── data/
│   ├── raw/               # untouched source files (NOAA CSV/TXT)
│   ├── interim/           # cleaned/merged but not modeled
│   └── processed/         # final feature tables ready for ML
│
├── notebooks/
│   ├── 00_data_download.ipynb
│   ├── 01_data_quality_profiling.ipynb
│   ├── 02_eda_overview.ipynb
│   ├── 03_geo_eda_mapping.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_baseline_models.ipynb
│   ├── 06_model_tuning_and_selection.ipynb
│   ├── 07_error_analysis_and_bias_checks.ipynb
│   ├── 08_risk_scoring_and_thresholds.ipynb
│   ├── 09_reporting_figures_and_tables.ipynb
│   └── 10_export_artifacts.ipynb
│
├── reports/
│   ├── figures/           # plots saved from 02/03/09
│   ├── tables/            # CSVs/LaTeX/markdown tables for report
│   └── summary.md         # human-readable findings
│
├── models/
│   ├── experiments/       # per-run metadata (params + metrics)
│   └── artifacts/         # serialized models, preprocessors
│
├── src/                   # optional helpers used by notebooks
│   ├── io_utils.py        # load/save helpers (paths central)
│   ├── clean_utils.py     # NOAA-specific cleaning functions
│   ├── fe_utils.py        # feature engineering utilities
│   └── viz_utils.py       # plotting helpers (maps, facets)
│
├── environment.yml
├── README.md
└── .gitignore
```
