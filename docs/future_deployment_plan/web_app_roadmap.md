# Web App Roadmap (Flask or FastAPI)

## 0) Product Slice (what the demo shows)

**Public (no login):** - County/state heatmap (last N years) with
tooltips: event count, total normalized damage. - "Top 10 high-damage
counties this year." - One interactive "what-if": pick hazard + month →
see historical risk band (Low/Med/High).

**Behind login (full app):** - Filters: hazard, year range, region,
coastal/inland, wind/rain bins. - Tables: event list with links to NOAA
IDs, damages (2025 USD), fatalities/injuries. - Model outputs: predicted
damage band per county, threshold editor, export CSV. - Download center:
reports/tables, model card, API key management.

------------------------------------------------------------------------

## 1) Architecture (MVP → scalable)

-   **Backend**: FastAPI (recommended for clean schemas + speed) or
    Flask (if you prefer templates).
-   **DB**: Postgres for app state + curated aggregates;
    **DuckDB/Parquet** for large analytical scans (read-only).
-   **Cache**: Redis (hot tiles, top-N queries, rate limits).
-   **Tasks**: Simple cron/Invoke or Celery (optional) to refresh
    aggregates.
-   **Auth**: Email+password → JWT access/refresh, RBAC (`user`, `pro`,
    `admin`). CSRF only if using cookies.
-   **Frontend**:
    -   Flask: Jinja2 templates + HTMX/Alpine (fastest to ship), or
    -   FastAPI: serve a small React/Vite frontend (more polish, more
        work).
-   **Maps**: Leaflet (lightweight) or Mapbox GL (nicer, paid tier
    optional). Pre-generate vector/geojson tiles.

------------------------------------------------------------------------

## 2) Data Serving Strategy (it's a huge dataset)

-   **Don't query raw on every request.** Pre-compute and store:
    -   `agg_county_year_hazard.parquet` (counts, sums, medians; 1 row
        per county/year/hazard).
    -   `agg_state_year_hazard.parquet`.
    -   Optional quantiles for thresholds: `q20, q40, q60, q80` per
        hazard/region.
-   **Load path**:
    1)  Cold start: read aggregates into DuckDB or Polars; keep in
        memory if small enough.
    2)  For maps: serve **pre-sliced GeoJSON** per hazard/year (or
        vector tiles if you want max snappiness).
-   **Write path**: none for raw NOAA---treat as immutable; only
    regenerate aggregates offline.

**Files to generate from your pipeline** -
`data/tiles/geojson/{hazard}/{year}.geojson` -
`data/aggregates/agg_county_year_hazard.parquet` -
`data/aggregates/agg_state_year_hazard.parquet` -
`models/artifacts/{hazard}_model.pkl` (+ preprocessing pipeline)

------------------------------------------------------------------------

## 3) API Design (FastAPI example)

**Public (rate-limited)** -
`GET /api/v1/demo/heatmap?hazard=hurricane&year=2020` -
`GET /api/v1/demo/top-counties?hazard=flood&years=2015:2024&limit=10` -
`GET /api/v1/demo/risk-band?hazard=tornado&month=4&state=AL`

**Auth** - `POST /api/v1/auth/login` → access/refresh JWTs\
- `POST /api/v1/auth/refresh`\
- `POST /api/v1/auth/request-reset` → SendGrid\
- `POST /api/v1/auth/reset-password`

**Protected** - `GET /api/v1/agg/county` params:
`hazard, years, region, coastal_flag` - `GET /api/v1/model/predict`
body: `{hazard, features...}` (batch allowed) -
`POST /api/v1/model/thresholds` (admin) save chosen cutoffs -
`GET /api/v1/exports/predictions.csv` - `GET /api/v1/me` /
`GET /api/v1/api-keys`

------------------------------------------------------------------------

## 4) Security + "safe demo"

-   Public endpoints:
    -   Serve **only aggregated** data (no PII, no precise coordinates).
    -   Add **rate limit** (Redis counters) + CORS locked to your
        domain.
-   Private app:
    -   RS256 JWT (rotate keys later), password hashing **Argon2**.
    -   Strict input validation (Pydantic), 413 upload limits.
-   Observability:
    -   Request IDs, structured logs, error tracking (Sentry).

------------------------------------------------------------------------

## 5) Deployment (simple + low-maintenance)

-   **Option A (FastAPI)**:
    -   App Runner or Elastic Beanstalk (Python) with
        `gunicorn uvicorn.workers.UvicornWorker`.
    -   RDS Postgres, S3 for static & tiles, CloudFront CDN (optional),
        Secrets Manager.
-   **Option B (Flask)**: same infra; can start on Heroku if you want
    speed, then port to AWS.
-   **Static/tiles**: prebuild and push to S3; frontend/map fetches via
    CDN.

------------------------------------------------------------------------

## 6) Performance checklist

-   Use **columnar** storage (Parquet) and **predicate pushdown**
    (DuckDB/Polars).
-   Pre-generate **map layer files**; avoid per-request joins.
-   Cache hot combinations in Redis (`hazard+year+state` → JSON).
-   Paginate tables; lazy-load heavy charts.

------------------------------------------------------------------------

## 7) Project management (keep it shippable)

**Milestone 1 --- Demo Map (public)** - Precompute
`agg_state_year_hazard` and 1 geojson. - `GET /api/v1/demo/heatmap` +
one public page. - Basic rate limiting.

**Milestone 2 --- Auth + Private Views** - JWT auth, RBAC, `/me`. -
Private dashboard: filters + tables.

**Milestone 3 --- Model Integration** - Load `{hazard}_model.pkl`. -
`/model/predict` + thresholds UI. - Export CSV.

**Milestone 4 --- Polish & Docs** - Model card, About page, system
diagram. - Add API keys (programmatic access) if desired.

------------------------------------------------------------------------

## 8) Repo structure add-ons

    app/
      api/ (routers: auth, demo, agg, model, exports)
      core/ (config, security, deps)
      services/ (tiles, agg_loader, model_runner)
      web/ (templates, static)  # if Flask/Jinja
    infra/
      docker/compose.yml
      aws/ (terraform or docs)
    frontend/ (optional React/Vite)

`docs/` → architecture.md, api.md, threat_model.md, model_card.md\
`data/tiles` and `data/aggregates` → published to S3 in CI

------------------------------------------------------------------------

## 9) Next 7 days (light lift, future-proof)

-   Generate **one** `state-level` GeoJSON + an
    `agg_state_year_hazard.parquet`.
-   Add a **demo** FastAPI route + rate limit middleware.
-   One simple HTML page (or a small React page) embedding Leaflet
    fetching that endpoint.
-   Write `docs/architecture.md` (1-pager) so future steps are obvious.
