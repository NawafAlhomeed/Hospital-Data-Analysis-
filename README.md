# Hospital Data Analysis (ETL with Python + Power BI)

This project demonstrates how a data engineer can use Python to prepare hospital data for analysis and visualization in **Power BI**.  
It focuses on the **ETL process** — Extract, Transform, Load — turning raw hospital data into business-ready insights.

⚠️ Note: The dataset is **not included** in this repository. Please download it directly from Kaggle (link below).

---

## Dataset
The hospital dataset is publicly available here:  
[Hospital Management Dataset – Kaggle](https://www.kaggle.com/datasets/kanakbaghel/hospital-management-dataset)

---

## Process Overview

### 1. Extract
- Load multiple CSV files (`patients`, `appointments`, `doctors`, `treatments`, `billing`) into **pandas**.

### 2. Transform
- Clean and standardize the data:
  - Rename columns for clarity.  
  - Convert text fields (e.g., dates) into proper types.  
  - Derive new features (age, age groups, late payments).  
  - Standardize values (e.g., gender codes → "Male"/"Female").  
  - Merge tables to show patient-doctor-appointment relationships.  
  - Generate summary insights (e.g., total bill per patient, top doctors).  

### 3. Load
- Save the transformed data as new CSV files.  
- These files can be imported into **Power BI** to create reports and dashboards.  

---

## How to Use
1. Download the dataset from Kaggle.  
2. Place the CSV files in a folder named `data/`.  
3. Open `analysis.ipynb` in Jupyter Notebook.  
4. Run the notebook step by step to see the ETL process.  
5. Use the transformed CSVs in **Power BI** for visualization.  

---

## Tools Used
- **Python (pandas)** → ETL / Data Cleaning  
- **Jupyter Notebook** → Workflow  
- **Power BI** → Visualization  
