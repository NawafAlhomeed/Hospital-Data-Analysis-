# Hospital Data Analysis — Portfolio-ready (Enhanced)

**Author:** Nawaf Alhomeed  
**Purpose:** Clean, transform and visualize hospital dataset; reproducible ETL and a Power BI/Streamlit demo.

## What I changed (direct, no BS)
- Converted notebook logic into a small `src/` package with a CLI.
- Added reproducible environment files (`requirements.txt`, `requirements-dev.txt`).
- Added unit test for core transformation logic.
- Added GitHub Actions CI for tests, a Dockerfile, and a clear README + data handling instructions.
- Added MIT license and a robust `.gitignore`.

## Quick start (run locally)
1. Put your raw dataset files in `data/raw/` (see `data/README.md`).
2. Create and activate a virtualenv:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Run the pipeline:
   ```bash
   python -m hospital_etl.cli data/raw data/processed
   ```
   This creates cleaned CSVs under `data/processed/`.

4. Run tests:
   ```bash
   pip install -r requirements-dev.txt
   pytest -q
   ```

## Project structure
```
Hospital-Data-Analysis-Enhanced/
├─ LICENSE
├─ README.md
├─ requirements.txt
├─ requirements-dev.txt
├─ .github/workflows/ci.yml
├─ src/hospital_etl/ (ETL package)
├─ tests/
├─ data/ (gitignored — put raw files in data/raw/)
└─ Dockerfile
```

## Notes / Security
- Do NOT commit raw patient data. Keep `data/` in `.gitignore`.
- Confirm the dataset license (Kaggle or other) before publishing.
- If dataset contains PHI, replace with synthetic/anonymized examples before sharing.

## Next steps I recommend (high ROI)
1. Add 2–3 dashboard screenshots to `docs/screenshots/` and embed in README.
2. Convert a notebook to a reproducible `papermill` job and automate PDF builds in CI.
3. Add a simple Streamlit demo and deploy to Streamlit Cloud for a live link.

---  
Done. Download the prepared repo zip from the link below and commit to your GitHub.
