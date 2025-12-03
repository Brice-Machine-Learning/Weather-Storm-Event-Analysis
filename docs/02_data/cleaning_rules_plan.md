# Cleaning Rules Plan (Outline)

## 1. General Checks

-   **Duplicates**: Drop duplicate EVENT_ID rows.\
-   **Missing values**:
    -   Key identifiers (EVENT_ID, BEGIN_DATE, STATE) → if missing,
        drop.\
    -   Numerical fields (damage, injuries) → impute as 0 if truly
        absent.\
-   **Data types**: Ensure correct casting (dates → datetime, costs →
    numeric).

------------------------------------------------------------------------

## 2. Event-Specific Cleaning

### Floods

-   Normalize flood types (`FLASH FLOOD`, `RIVER FLOOD`, etc.) into
    canonical categories.\
-   Ensure rainfall/water height values are numeric and valid.

### Hurricanes

-   Standardize wind speed units (knots vs mph).\
-   Check storm names consistency across years.\
-   Remove placeholder names like `UNNAMED`.

### Tornadoes

-   Validate EF scale (0--5).\
-   Ensure path length/width are within realistic ranges.

------------------------------------------------------------------------

## 3. Damage & Casualty Data

-   **Property/Crop Damage**:
    -   Parse multiplier codes (`K`, `M`, `B`) into numeric values.\
    -   Apply CPI-based normalization to 2025 USD.\
-   **Fatalities/Injuries**:
    -   Ensure integers ≥ 0.\
    -   Merge carefully with event IDs (no double counting).

------------------------------------------------------------------------

## 4. Temporal Coverage

-   Exclude records **before cutoff year** (to be decided, likely
    1996).\
-   Flag incomplete years (if downloads are partial).

------------------------------------------------------------------------

## 5. Geographic Data

-   Standardize state/county names (align with FIPS codes).\
-   Drop events with invalid or missing county/state info.\
-   Create coastal/inland flag for relevant states.

------------------------------------------------------------------------

## 6. Outlier Handling

-   Extremely high damages (\>\$100B) → validate against NOAA notes
    (could be data entry errors).\
-   Fatalities \> 1000 → manually review.\
-   Out-of-range lat/long values → drop or correct.

------------------------------------------------------------------------

## 7. Documentation

-   Save final cleaning decisions into `reports/cleaning_rules.md`.\
-   Maintain a changelog for reproducibility.
