Quick notebook checklist (do this inside your Jupyter notebook):

1. At top of notebook, set a clear data path variable:
   RAW = 'data/raw'
   PROCESSED = 'data/processed'

2. When you read files, prefer:
   import pandas as pd
   patients = pd.read_csv(f'{RAW}/patients.csv')

3. After transformations, save outputs explicitly:
   patients.to_csv(f'{PROCESSED}/patients.csv', index=False)

4. Keep one cell that runs all saves — this gives you reproducible outputs for Power BI.
