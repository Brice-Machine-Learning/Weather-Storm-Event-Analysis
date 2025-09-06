# Extreme Weather Events

- **Dataset**: NOAA Storm Events, 215 files (huge Kaggle dataset: hurricanes, tornadoes, floods).
- **Project**: Predict property damage or casualties from storm features (wind speed, duration, location).
- **Skills**: classification/regression, imbalanced datasets, risk modeling.
- **Bonus**: Tie into infrastructure resilience (water systems, power grids).

## How should this be organized?

- Needs to be separated by storm event, ie: Hurricanes have a different destructive power and different costs than a flood or tornadoes
  - **Solution**: Use 03_geo_eda_mapping.ipynb and 04_feature_engineering.ipynb to branch the data into three(3) sub-files(floods.csv, hurricanes.csv, tornadoes.csv under data/interim/)
- Run a separate model for floods, hurricanes, and tornadoes
  - Later notebooks (05 - 06) should train/tune a model per hazard class.  That makes interpretation cleaner and avoids blending very different distributions.
- Data should be filtered to a different file for each separating out each type of event.
- Costs need to be normalized.  The cost of a storm in 1970 does not equal dollars in current year of 2025.
  - Important for comparing across decades.  In 04_feature_engineering.ipynb, add a CPI or GDP deflator adjustment so that all damages are in real 2025 USD.
- How far back should the project be trained on data?  What year is the cutoff and why?
  - NOAA event reporting becomes more standardized around the 1990s. Earlier records (1950–1989) are sparse and inconsistent.
  - Practical Cutoff:
    - **Conservative**: 1996 onward (post-Event Database standardization).
    - **Broader**: 1970 onward (but requires heavier cleaning/normalization).
    - **Recommendation**: 1996+ for initial models (higher data quality), and document that decision in `01_data_quality_profiling.ipynb` and `reports/summary.md`

## How is the data set organized

- Each year has its own file.
- In addition to each year, the following files are how it is organized:
  - storm event details (floods, hurricanes, tornadoes)
  - storm event fatalities (linked by event ID)
  - storm event locations (county/state info)
- In `00_data_download.ipynb` logic will need to be incorporated across the three yearly files to produce a consolidated event table before moving on.

## Summary

### Main decisions to document early

1. Event separation (floods, hurricanes, tornadoes)
2. Cost normalization method.
3. Training cutoff year (1996+)
