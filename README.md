***Seller Cohort Analysis with PySpark & SQL***

**📋 Project Overview**
This project ingests e-commerce order data, computes monthly seller cohorts and retention metrics via PySpark, exposes results through SQL, and visualizes key insights in an Excel dashboard.

🔧 Tech Stack
- Python 3.8+
- Apache Spark (PySpark)
- SQLite (or Spark SQL/Hive)
- Excel or Google Sheets
- pandas, sqlalchemy
- Git & GitHub

**📂 Repo Structure**

seller-cohort-analysis/
├── data/
│ ├── List of Orders.csv
│ ├── Order Details.csv
│ ├── Sales target.csv
│ ├── orders_cleaned.csv # output of etl.py
│ ├── metrics.parquet # output of cohort_analysis.py
│ └── metrics.csv # CSV for dashboard
├── spark_jobs/
│ ├── etl.py
│ └── cohort_analysis.py
├── sql/
│ └── cohort_queries.sql
├── dashboard/
│ └── seller_cohort_dashboard.xlsx
├── docs/
│ └── README.md
└── requirements.txt


🚀 Setup & Run

1. **Clone & install**  
   ```bash
   git clone <repo-url>
   cd seller-cohort-analysis
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

  2. **ETL**
   python spark_jobs/etl.py

  3. **Cohort Analysis**
   spark-submit spark_jobs/cohort_analysis.py

  4. **SQL Queries**
   Load data/metrics.parquet into your SQL engine (or convert to a SQLite table).
   Run sql/cohort_queries.sql to extract cohort sizes, retention rates, and revenue trends.

   5. **Dashboard**
      Open data/metrics.csv in Excel.
      Build charts as described in dashboard/ section.
      Save as dashboard/seller_cohort_dashboard.xlsx.

***🔍 Key Findings***
    Jan 2025 Cohort: 120 sellers, 60% retention in Month 2
    Revenue Trend: January cohort generated ₹75K in Month 1, rising to ₹90K by Month 3



