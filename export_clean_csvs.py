"""Simple CSV cleaner.

- Reads all CSV files from data/raw/
- Drops duplicate rows
- Strips whitespace from string columns
- Writes cleaned files to data/processed/ with same filenames
"""
import os
import pandas as pd

SRC_DIR = os.path.join('data', 'raw')
DST_DIR = os.path.join('data', 'processed')

def process_file(src_path, dst_path):
    df = pd.read_csv(src_path)
    df = df.drop_duplicates()
    # strip whitespace from string columns
    obj_cols = df.select_dtypes(include=['object']).columns
    for c in obj_cols:
        df[c] = df[c].astype(str).str.strip()
    df.to_csv(dst_path, index=False)

def main():
    if not os.path.exists(SRC_DIR):
        print('Create data/raw/ and put your CSV files there. See data/README.md')
        return
    os.makedirs(DST_DIR, exist_ok=True)
    files = [f for f in os.listdir(SRC_DIR) if f.lower().endswith('.csv')]
    if not files:
        print('No CSV files found in data/raw/.')
        return
    for f in files:
        src = os.path.join(SRC_DIR, f)
        dst = os.path.join(DST_DIR, f)
        try:
            process_file(src, dst)
            print(f'Processed {f} -> data/processed/{f}')
        except Exception as e:
            print(f'Failed to process {f}: {e}')

if __name__ == '__main__':
    main()
