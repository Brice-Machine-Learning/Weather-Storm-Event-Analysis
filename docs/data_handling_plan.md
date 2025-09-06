# Data Handling Plan

## Step 0. Data Acquisition

*Notebook: `00_data_download.ipynb`* - Download NOAA Storm Events
dataset (all yearly files).\
- Save into `data/raw/` preserving folder/year structure.\
- Maintain a log of source URLs, versions, and SHA checksums for
reproducibility.\
- Draft an initial **data dictionary** (columns, dtypes, units).

------------------------------------------------------------------------

## Step 1. Data Profiling & Cutoff Decision

*Notebook: `01_data_quality_profiling.ipynb`* - Inspect missingness,
duplicates, odd encodings.\
- Compare pre-1996 vs post-1996 record quality.\
- **Decision**: Document final cutoff year (likely 1996).\
- Save a **cleaning rules plan** into `reports/`.

------------------------------------------------------------------------

## Step 2. Merge Per-Year Files

*Notebook: `01_data_quality_profiling.ipynb` → `src/io_utils.py`* - Join
`details`, `fatalities`, and `locations` by `EVENT_ID`.\
- Append all years into a single **master interim dataset** in
`data/interim/master_events.parquet`.\
- Keep raw → interim transformations scripted for reproducibility.

------------------------------------------------------------------------

## Step 3. Event-Type Filtering

*Notebook: `02_eda_overview.ipynb` / `03_geo_eda_mapping.ipynb`* -
Create three filtered subsets: - **Floods** (`floods.parquet`)\
- **Hurricanes** (`hurricanes.parquet`)\
- **Tornadoes** (`tornadoes.parquet`)\
- Save into `data/interim/` for later modeling.\
- Each subset should include event metadata + merged damage + fatality
data.

------------------------------------------------------------------------

## Step 4. Cost Normalization

*Notebook: `04_feature_engineering.ipynb`* - Source a CPI index (e.g.,
FRED, Bureau of Labor Statistics).\
- Adjust `property_damage` and `crop_damage` to **2025 USD**.\
- Example: `normalized_cost = raw_cost * (CPI_2025 / CPI_eventyear)`\
- Add normalized columns: `property_damage_usd`, `crop_damage_usd`.

------------------------------------------------------------------------

## Step 5. Feature Engineering

*Notebook: `04_feature_engineering.ipynb`* - Derive standardized
features across hazards: - **Temporal**: month, season, year offset.\
- **Spatial**: coastal flag, population density (if available),
state/region.\
- **Hazard-specific**: wind bins (for hurricanes/tornadoes), rainfall
bins (for floods).\
- Save per-hazard modeling tables into `data/processed/`.

------------------------------------------------------------------------

## Step 6. Modeling Per Hazard

*Notebooks: `05_baseline_models.ipynb` →
`06_model_tuning_and_selection.ipynb`* - Train regression/classification
models **separately for each hazard type**.\
- Evaluate performance (R², RMSE, Precision@k, etc.).\
- Serialize tuned models into `models/artifacts/`.

------------------------------------------------------------------------

## Step 7. Risk Scoring

*Notebook: `08_risk_scoring_and_thresholds.ipynb`* - Define **Low /
Medium / High** damage thresholds for each hazard.\
- Calibrate thresholds with business metrics (e.g., over-prediction cost
vs under-prediction cost).

------------------------------------------------------------------------

## Step 8. Reporting & Export

*Notebooks: `09_reporting_figures_and_tables.ipynb` →
`10_export_artifacts.ipynb`* - Generate: - Trend charts (event counts,
damages by year).\
- Geospatial plots (damage intensity per county/state).\
- Risk tables.\
- Save to `reports/figures/` and `reports/tables/`.\
- Export final datasets and models with a `model_card.md` summarizing
assumptions + caveats.

------------------------------------------------------------------------

### Deliverables from this pipeline

-   **Master interim dataset** (`master_events.parquet`).\
-   **Three hazard-specific subsets** (`floods.parquet`,
    `hurricanes.parquet`, `tornadoes.parquet`).\
-   **Normalized costs** (2025 USD).\
-   **Processed feature tables** in `data/processed/`.\
-   **Trained models** per hazard.\
-   **Reports + model card** for documentation.
