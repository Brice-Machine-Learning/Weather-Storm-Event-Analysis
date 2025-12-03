---
title: Continuous Integration Pipeline Guide
file: docs/ci_pipeline_readme.md
---

# Continuous Integration (CI) Pipeline Guide

## Purpose

This document explains how the **GitHub Actions CI pipeline** is structured and how to run, monitor, and modify it for the NOAA Storm Events project.  
The workflow automates environment setup, quality checks, and notebook validation to ensure reproducibility across contributors.

---

## Overview

### Workflow File
- **Location:** `.github/workflows/ci-conda-pipeline.yml`
- **Purpose:** Automate environment validation, code linting, test execution, and sample notebook runs.

### Key Objectives
1. Verify the Conda environment builds correctly.
2. Run **linting** on helper scripts (`src/`).
3. Execute **smoke tests** (`tests/` folder).
4. Perform **sample notebook runs** (00–02) to confirm pipeline stability.
5. Upload executed notebooks as **artifacts** for inspection.

---

## Workflow Summary

| Job | Description | Notes |
|-----|--------------|-------|
| `conda-ci` | Main CI workflow for validation | Uses `conda-incubator/setup-miniconda` |
| **Setup Conda** | Creates an environment from `environment.yml` | Uses `mamba` for faster dependency resolution |
| **Lint Source Code** | Checks Python style and errors | Uses `ruff` |
| **Run Smoke Tests** | Executes `pytest` suite | Fail-fast on first error |
| **Run Sample Notebooks** | Executes 00–02 notebooks via `papermill` | Uses small test dataset |
| **Upload Artifacts** | Saves executed notebooks to GitHub | Viewable under **Actions → Artifacts** |

---

## Lightweight Notebook Execution

Because the full NOAA dataset is very large, the CI pipeline runs only **notebooks 00–02** on **sample data**.

The notebooks are parameterized via **Papermill**, so they can detect when CI is running:

```python
# inside notebook cells
import os
CI_MODE = os.getenv("CI", "False") == "True"

if CI_MODE:
    # Limit data to first few rows or sample files
    df = df.head(500)
else:
    # Full run for local or scheduled execution
    df = pd.read_csv(full_path)
```

In GitHub Actions, this variable is passed automatically:
```yaml
env:
  CI: "True"
```

---

## Running the Workflow Manually

### Option 1 — On Push
The workflow runs automatically on:
- Any `push` or `pull_request` to `main` or `dev`.

### Option 2 — Manual Trigger
You can manually re-run from the **Actions** tab:
1. Open **Actions** → **Data Pipeline (Conda)**.
2. Click **Run workflow**.
3. Select the branch (e.g., `dev`).
4. Optionally pass custom parameters later (e.g., `FULL_RUN=True`).

---

## Reviewing Results

After a run:
1. Go to **Actions → Data Pipeline (Conda)**.
2. Select the latest run.
3. Review:
   - ✅ Job status (green check = passed).
   - 📄 Logs (click step to expand).
   - 📦 Artifacts (executed notebooks).
4. Download artifacts to verify figures, sample outputs, or error traces.

---

## Common Issues

| Symptom | Likely Cause | Fix |
|----------|---------------|-----|
| Environment build timeout | Large dependencies (e.g., `geopandas`, `gdal`) | Enable `cache: true` under `setup-miniconda` |
| Lint or test failures | Code issues in `src/` or `tests/` | Run `ruff check src` and `pytest` locally |
| Notebook timeout | Heavy processing | Add `CI` condition to skip large data loads |
| Missing artifacts | Workflow exited early | Ensure `if: always()` is used on artifact upload step |

---

## Extending the Pipeline

Future enhancements:
- Add **scheduled runs** for full dataset notebooks (e.g., nightly or weekly).
- Integrate **data versioning** (DVC or Git LFS).
- Add **automated model retraining** when upstream data updates.
- Add **code coverage** metrics and **documentation build** checks.

---

## Maintenance Notes

- Always test `environment.yml` locally before pushing updates.
- When adding notebooks, keep CI-friendly parameters (e.g., `SAMPLE_RUN` or `CI` flags).
- Keep this guide synchronized with updates to `.github/workflows/`.

---

### Author
Data Pipeline Documentation — *Storm Events Analysis Project*  
Maintained under: `docs/ci_pipeline_readme.md`
