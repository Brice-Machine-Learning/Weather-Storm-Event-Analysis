# Data Handling & Organization — Storm Events (Design Doc)

## Overview
This document describes how NOAA Storm Events data is organized and staged prior to profiling and cleaning. The approach emphasizes reproducibility, speed, and schema clarity while deferring joins and business rules to later notebooks.

---

## Summary
- **Raw layout:** `data/raw/<YEAR>/StormEvents_*.csv(.gz)` with three per-year file types: **details**, **locations**, and **fatal** (mapped to the **fatalities** table).
- **Staging (no cleaning):** `00_data_download.ipynb` reads raw files, standardizes minimal fields, appends metadata (`year`, `source_filename`), and writes **one staged file per type per year** to `data/interim/<type>/<type>_<year>.csv`.
- **No joins/merges in 00:** Combining and cleaning are handled in subsequent notebooks.

---

## Scope & Assumptions
- Source: NOAA Storm Events (multiple CSV/CSV.GZ per year).
- Coverage: **1996+** (earlier years exhibit inconsistent schema/coverage).
- Three per-year tables, linkable via **`EVENT_ID`**:
  - `details` (approximately one row per event)
  - `locations` (zero-to-many rows per event)
  - `fatalities` (zero-to-many rows per event; filenames contain “fatal”)
- Filenames typically begin with `StormEvents_…`; extensions may be `.csv` or `.csv.gz`.

---

## Directory Layout (Convention)
```
data/
  raw/
    1996/ StormEvents_details_1996.csv.gz
         StormEvents_locations_1996.csv.gz
         StormEvents_fatal_1996.csv.gz
    1997/ ...
  interim/
    details/    details_1996.csv, details_1997.csv, ...
    locations/  locations_1996.csv, ...
    fatalities/ fatalities_1996.csv, ...
    _logs/      ingest_summary.csv
  processed/
reports/
  figures/
  tables/
```
- **raw/** — untouched source files.  
- **interim/** — staged copies for consistent, fast reads by later notebooks.  
- **processed/** — modeling-ready feature tables (produced later).

---

## Ingestion Rules (Notebook 00)

**Per-file actions:**
1. **Year detection**
   - Primary: parent folder name `data/raw/<YYYY>/…`.
   - Fallbacks: `_dYYYY_` token in filename, else any 4-digit year in filename.
2. **Type detection**
   - Filename contains:
     - `detail` → **details**
     - `locat` / `location` → **locations**
     - `fatal` → **fatalities**
3. **Read** CSV/CSV.GZ (raw files remain unchanged).
4. **Column standardization (light-touch)**
   - Lowercase, trim whitespace.
   - Normalize `event_id`: rename variants (e.g., `event id`, `eventid`) to `event_id`.
   - Coerce `event_id` to nullable integer (`Int64`); non-numeric values become `<NA>`.
5. **Metadata**
   - Append `year` (int) and `source_filename` (string).
6. **Staging output**
   - Write to `data/interim/<type>/<type>_<year>.csv`.
   - Re-runs overwrite the same staged path for determinism.
7. **Logging**
   - Write per-file summary to `data/interim/_logs/ingest_summary.csv` (rows, saved path, type, year).

**Explicit non-goals in 00:**
- No deduplication, imputation, monetary parsing, or joins/merges.  
- These are addressed in profiling/cleaning notebooks to preserve auditability.

---

## Rationale for the Organization

1. **Performance & Reproducibility**  
   Staged **interim** files load quickly and consistently without repeated type inference. Including `year` and `source_filename` supports provenance and debugging.

2. **Normalized Tables Preserve Cardinality**  
   `details` (1:1), `locations` (1:n), and `fatalities` (1:n) differ in cardinality. Early joins cause row explosion and can obscure data-quality issues. Normalization defers joining until required by analysis and allows safe aggregation first.

3. **Manage Schema Drift Explicitly**  
   Year-to-year column additions/removals are isolated by staging per type/year. A stricter column contract can be enforced during cleaning after profiling the drift.

4. **1996+ Cutoff**  
   Post-mid-1990s records exhibit better standardization, reducing bespoke cleaning and improving model signal quality.

---

## Configuration (“Knobs”) in Notebook 00
- `MIN_YEAR` — ignore files older than this (default: 1996).
- `INCLUDE_YEARS` — optional whitelist (e.g., `{2018, 2019, 2020}`).
- `ACCEPT_EXTENSIONS` — default `("*.csv", "*.csv.gz")`.
- `DRY_RUN` — preview actions without writing to `interim/`.
- `SAVE_INTERIM_AS` — `"csv"` currently; can be switched to `"parquet"` later without architectural changes.

> **Note on Parquet:** Parquet is a typed, compressed, columnar format; beneficial for large datasets and selective loading. CSV remains acceptable for initial staging and simplicity.

---

## Edge Cases & Handling
- Filenames containing only **`fatal`** are mapped to the **fatalities** table type.
- Missing or non-numeric `event_id` values are coerced to `<NA>` and addressed in profiling/cleaning.
- Duplicate `EVENT_ID` in `details` is allowed to pass in staging and is evaluated in profiling for a deduplication policy.
- Orphan `locations`/`fatalities` referencing absent events are permitted at staging; counts are surfaced in profiling.
- `.csv.gz` files are read transparently and staged as `.csv` by default.
- Re-runs overwrite prior staged outputs; the summary log is regenerated for consistency.

---

## Execution Order (Notebook 00)
1. **Cell 1:** Defines globals and configuration (paths, patterns, options).  
2. **Cell 2:** Defines helper routines and executes the ingest runner that performs detection, standardization, metadata append, staging, and logging.  
3. **Optional dry-run cell:** Prints “would-save” paths without writing.

---

## Next Steps
- **01_data_quality_profiling.ipynb**
  - Produce row counts, missingness profiles, duplicate-key checks for `details`, and orphan checks for `locations`/`fatalities`.
  - Finalize cleaning rules (drop/keep conditions, date parsing, numeric coercions).
  - Create a “silver” layer:
    - Continue with normalized tables under a documented column contract, or
    - Build an event-level analysis view by left-joining `details` with aggregated `locations` and `fatalities` on `event_id`.
- **02–04 notebooks**
  - Separate by hazard (floods/hurricanes/tornadoes), normalize damage dollars to a common year, and construct features for modeling.

---

## Definition of Done (Notebook 00)
- All 1996+ raw files are scanned.  
- Staged copies exist at `data/interim/<type>/<type>_<year>.csv`.  
- `data/interim/_logs/ingest_summary.csv` contains per-file counts and paths.  
- No cleaning or joins have been applied at this stage.
