# Customer Data Cleaning & Preprocessing

## 📌 Project Overview
This project demonstrates **data cleaning and preprocessing** techniques on a simulated customer dataset (`customers-100.csv`).  
The goal is to transform raw, messy data into an **analysis-ready format** suitable for reporting, dashboards, and further analytics.

---

## 🛠 Steps Performed
1. **Data Ingestion**
   - Loaded dataset from CSV using Pandas.
   - Performed initial sanity checks (shape, column names, data types).

2. **Deduplication**
   - Identified and removed duplicate rows.
   - Ensured unique `Customer Id` values.

3. **Column Management**
   - Dropped irrelevant columns (`Index`).
   - Renamed `Phone 1` → `Phone` for clarity.

4. **Missing Value Handling**
   - Diagnosed missing values.
   - Applied strategies: deletion (critical IDs), imputation (numerical/categorical).

5. **Data Type Correction**
   - Converted phone numbers to string format.
   - Standardized categorical fields (City, Country).

6. **Format Standardization**
   - Normalized text (lowercase, strip whitespace).
   - Fixed inconsistent city/country capitalization.

7. **Validation**
   - Ensured no duplicates remain.
   - Verified no missing `Customer Id`.

---

## 📂 Files in Repository
- `customers-100.csv` → Raw dataset (input).
- `customer_cleaning.ipynb` → Jupyter Notebook with step-by-step cleaning workflow.
- `cleaned_customers.csv` → Final cleaned dataset (output).
- `README.md` → Project documentation.

---

## 🎯 Outcome
The final dataset is **clean, consistent, and analysis-ready**, enabling reliable insights for business use cases such as customer segmentation, churn analysis, and reporting.

---

## 🚀 Skills Demonstrated
- Pandas DataFrame operations
- Data quality assessment
- Handling missing values & duplicates
- Text normalization & categorical encoding
- Real-world problem solving with messy data
