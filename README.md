# Hospital Data Analysis — Simple, beginner-friendly

Nawaf — here's a stripped-down, no-nonsense version you can commit. 
You're a Jupyter + Power BI person. This keeps it that way.

## What this package contains
- simple README with exact steps
- requirements.txt (only essentials)
- data/README.md (where to put your CSVs)
- .gitignore (keeps data out of the repo)
- export_clean_csvs.py — tiny script you can run to clean all CSVs in `data/raw/` and write cleaned CSVs to `data/processed/`. No refactor, no modules, no CI.

## How to use (3 steps)
1. Put your raw CSV files in `data/raw/` (create the folder).
2. Create a Python venv and install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # or .\.venv\Scripts\activate on Windows
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. Run the simple cleaner:
   ```bash
   python export_clean_csvs.py
   ```
   Cleaned CSVs will appear in `data/processed/`. Open your Jupyter notebook and point it to `data/processed/` or open the Power BI `.pbix` and update data sources to `data/processed/`.

## If you want me to do one thing next:
- I can edit your actual notebook to read/write from `data/raw/` and save outputs to `data/processed/`. I’ll do it directly (one notebook file change). Say "edit notebook".
