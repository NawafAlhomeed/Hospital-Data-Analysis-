"""Simple ETL script for small project.

Put CSVs under data/raw/ and run this script.
It will write cleaned CSVs to data/processed/.
"""
import os
import pandas as pd
from datetime import datetime

RAW_DIR = 'data/raw'
OUT_DIR = 'data/processed'

def calculate_age(dob, ref_date=None):
    if pd.isna(dob):
        return None
    dob = pd.to_datetime(dob, errors='coerce')
    if pd.isna(dob):
        return None
    if ref_date is None:
        ref = pd.Timestamp.today()
    else:
        ref = pd.to_datetime(ref_date)
    age = ref.year - dob.year - ((ref.month, ref.day) < (dob.month, dob.day))
    return int(age)

def clean_patients(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # strip whitespace from string columns
    for c in df.select_dtypes(include=['object']).columns:
        df[c] = df[c].astype(str).str.strip()
    # map gender
    if 'gender' in df.columns:
        df['gender'] = df['gender'].map({'M':'Male','F':'Female','m':'Male','f':'Female'}).where(df['gender'].notna())
    # calc age if dob present
    if 'dob' in df.columns:
        df['age'] = df['dob'].apply(calculate_age)
    # drop exact duplicates
    df = df.drop_duplicates()
    return df

def main():
    if not os.path.exists(RAW_DIR):
        print(f"Create {RAW_DIR} and add CSV files (e.g. patients.csv). Exiting.")
        return
    os.makedirs(OUT_DIR, exist_ok=True)
    files = [f for f in os.listdir(RAW_DIR) if f.lower().endswith('.csv')]
    if not files:
        print(f"No CSV files found in {RAW_DIR}. Put patients.csv and retry.")
        return
    for fname in files:
        path = os.path.join(RAW_DIR, fname)
        print(f"Processing {path}...")
        try:
            df = pd.read_csv(path)
        except Exception as e:
            print(f"Failed to read {fname}: {e}")
            continue
        name = os.path.splitext(fname)[0].lower()
        if name == 'patients':
            df_clean = clean_patients(df)
        else:
            # generic cleaning: strip whitespace & drop duplicates
            for c in df.select_dtypes(include=['object']).columns:
                df[c] = df[c].astype(str).str.strip()
            df_clean = df.drop_duplicates()
        out_path = os.path.join(OUT_DIR, fname)
        df_clean.to_csv(out_path, index=False)
        print(f"Wrote cleaned file to {out_path}")
    print("Done.")

if __name__ == '__main__':
    main()
