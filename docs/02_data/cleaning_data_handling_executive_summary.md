# Cleaning & Data Handling — Executive Summary

## Cleaning Rules (Highlights)

### General

* Drop duplicate `EVENT_ID`s.
* Handle missing values:

  * Drop if key identifiers (EVENT\_ID, date, state) missing.
  * Impute 0 for absent numerical damage/injury fields.
* Ensure correct data types (dates → datetime, damages → numeric).

### Event-Specific

* **Floods**: Normalize flood subtypes; validate rainfall/height values.
* **Hurricanes**: Standardize wind units (knots/mph), storm names, drop `UNNAMED`.
* **Tornadoes**: Validate EF scale (0–5), path length/width ranges.

### Damage & Casualties

* Parse multipliers (`K`, `M`, `B`) into numbers.
* Normalize to **2025 USD**.
* Fatalities/injuries: integers ≥ 0, consistent EVENT\_ID joins.

### Geographic

* Standardize state/county to FIPS codes.
* Drop invalid/missing geographies.
* Add coastal/inland flag.

### Outliers

* Damages > \$100B, fatalities > 1000 → manual review.
* Invalid lat/long → drop or correct.

### Temporal

* Exclude events before **1996**.
* Flag incomplete years.

### Documentation

* Save cleaning decisions in `reports/cleaning_rules.md`.
* Maintain a changelog for reproducibility.

---

## Data Handling Pipeline (Step-by-Step)

1. **Acquisition**  (`00_data_download.ipynb`)

   * Download all NOAA yearly files → `data/raw/`.
   * Log URLs, versions, checksums.
   * Draft initial data dictionary.

2. **Profiling & Cutoff Decision**  (`01_data_quality_profiling.ipynb`)

   * Compare pre-/post-1996 record quality.
   * Document cutoff (1996+).
   * Save cleaning plan to `reports/`.

3. **Merge Per-Year Files**  (`01_data_quality_profiling.ipynb`)

   * Join `details`, `fatalities`, `locations` by EVENT\_ID.
   * Append all years → `data/interim/master_events.parquet`.

4. **Event-Type Filtering**  (`02`–`03 notebooks`)

   * Create hazard-specific subsets:

     * `floods.parquet`
     * `hurricanes.parquet`
     * `tornadoes.parquet`
   * Save in `data/interim/`.

5. **Cost Normalization**  (`04_feature_engineering.ipynb`)

   * Apply CPI adjustment to 2025 USD.
   * Add normalized fields.

6. **Feature Engineering**  (`04_feature_engineering.ipynb`)

   * Temporal: month, season, year offset.
   * Spatial: coastal flag, population density, region.
   * Hazard-specific: wind bins (hurricanes/tornadoes), rainfall bins (floods).
   * Save processed tables → `data/processed/`.

7. **Modeling Per Hazard**  (`05`–`06 notebooks`)

   * Train/evaluate models separately for each hazard.
   * Serialize tuned models → `models/artifacts/`.

8. **Risk Scoring**  (`08 notebook`)

   * Define Low/Medium/High thresholds.
   * Calibrate with business metrics.

9. **Reporting & Export**  (`09`–`10 notebooks`)

   * Generate figures, tables, and risk summaries.
   * Export final datasets + `model_card.md`.

---

## Deliverables

* Master interim dataset (`master_events.parquet`).
* Hazard-specific subsets (floods, hurricanes, tornadoes).
* Normalized cost fields (2025 USD).
* Processed feature tables.
* Trained hazard models.
* Reports + `model_card.md` for transparency.