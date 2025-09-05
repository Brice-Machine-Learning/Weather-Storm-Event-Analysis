# Notebook Purposes (what each one does)

## 00_data_download.ipynb

- Download/extract NOAA Storm Events files; log source URLs + versions.
- Write to data/raw/ and produce a data dictionary draft (columns, types).

## 01_data_quality_profiling.ipynb

- Inspect missingness, duplicated events, outliers, odd codes.
- Create a profiling report (e.g., pandas-profiling/ydata-profiling).
- Output a cleaning plan (list of rules) saved to reports/.

## 02_eda_overview.ipynb

- Global trends: event counts by year/type; seasonality; basic correlations.
- Save key figures to reports/figures/.

## 03_geo_eda_mapping.ipynb

- State/county heatmaps for event frequency and total damages.
- Optional: storm path overlays if data supports tracks.
- Save geoplots.

## 04_feature_engineering.ipynb

- Build modeling table: engineered features (e.g., month, coastal flag, wind bins, prior-event rates by county).
- Output the training dataset to data/processed/.

## 05_baseline_models.ipynb

- Quick baselines:
- Regression target: property_damage_usd (log-transform).
- OR Classification target: high_damage (e.g., top 20% quantile).
- Train/test split; simple models (Linear/Logistic, RandomForest) + baseline metrics.

## 06_model_tuning_and_selection.ipynb

- Hyperparameter search (Grid/Random/Optuna).
- Compare models with cross-validation; pick winner; serialize model + preprocessor to models/artifacts/.

## 07_error_analysis_and_bias_checks.ipynb

- Residuals (regression) or confusion matrix by event type/region (classification).
- Check performance by geography/time to avoid hidden bias.
- Document risk/limitations.

## 08_risk_scoring_and_thresholds.ipynb

- Convert predictions into actionable risk categories (Low/Med/High).
- Choose thresholds via business-centric metrics (precision@k, cost curves).

## 09_reporting_figures_and_tables.ipynb

- Generate polished, reusable charts/tables for the write-up.
- Export to reports/figures/ and reports/tables/.

## 10_export_artifacts.ipynb

- Save final datasets, model, and model_card.md (short doc describing data, metrics, caveats).
- Optionally export a predictions_sample.csv for demo.
