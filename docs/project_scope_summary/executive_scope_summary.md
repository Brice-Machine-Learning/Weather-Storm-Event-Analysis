# Extreme Weather Events Project — Scope Summary

## Dataset

* Source: **NOAA Storm Events** dataset (\~215 yearly files).
* Coverage: Hurricanes, tornadoes, floods (multi-decade, nationwide).

## Objectives

* Predict **property damage** (regression) or **casualty severity** (classification).
* Produce hazard-specific risk models to support **infrastructure resilience** planning.

## Key Scope Decisions

### 1. Hazard Separation

* Floods, hurricanes, and tornadoes differ significantly in impact.
* **Decision**: Split master dataset into three interim files:

  * `floods.parquet`
  * `hurricanes.parquet`
  * `tornadoes.parquet`
* Each hazard type will have its **own modeling pipeline**.

### 2. Cost Normalization

* Historical storm damages must be comparable.
* **Decision**: Normalize all property/crop damages to **2025 USD**.

  * Use CPI or GDP deflator index.
  * Example transformation: `cost_2025 = raw_cost * (CPI_2025 / CPI_eventyear)`.

### 3. Training Cutoff Year

* NOAA event records pre-1990 are inconsistent and incomplete.
* **Decision**:

  * **Primary**: Use **1996 onward** (post-standardization of event database).
  * **Optional**: Extend back to 1970 with heavier cleaning, documented separately.

### 4. Data Organization

* Each year contains multiple linked files: `details`, `fatalities`, `locations`.
* Merge into a consolidated **master interim dataset** before hazard splits.
* Ensure consistent EVENT\_ID joins across all files.

## Deliverables

* **Hazard-specific datasets** in `data/interim/`.
* **Normalized damage fields** (`property_damage_usd`, `crop_damage_usd`).
* **Processed feature tables** in `data/processed/`.
* **Trained models** per hazard (artifacts + metrics).
* **Documentation**: cleaning rules, cutoff rationale, and a final `model_card.md`.

---

**Summary:** This project will build **separate, cost-normalized models** for hurricanes, floods, and tornadoes using NOAA Storm Events data from **1996 onward**. All decisions (hazard split, cost normalization, cutoff year) are documented for transparency and reproducibility.
