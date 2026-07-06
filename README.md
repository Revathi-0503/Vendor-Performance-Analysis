Vendor Performance Analysis for Profit Optimization:

An end-to-end Data Analytics project that analyzes vendor performance, inventory efficiency, and sales profitability using Python, SQL, and Power BI. The project demonstrates the complete analytics workflow from data ingestion and preprocessing to business analysis, dashboard development, and actionable business recommendations.

Project Overview:

Retail and wholesale businesses work with multiple vendors, thousands of products, and large transactional datasets. This project transforms raw purchasing, inventory, sales, and vendor invoice data into meaningful business insights.

The objective is to optimize profitability by evaluating vendor performance, improving inventory turnover, identifying underperforming brands, and supporting data-driven business decisions.

Problem Statement

Analyze vendor purchasing and sales data to identify:

High and low-performing vendors
Underperforming brands
Inventory turnover efficiency
Purchase contribution by vendors
Pricing inefficiencies
Profitability gaps

Develop an interactive Power BI dashboard and generate business recommendations to improve vendor management and operational efficiency.

Tech Stack
Python – Data preprocessing and exploratory data analysis
Pandas – Data manipulation
SQL (SQLite) – Database management and business analysis
Power BI – Interactive dashboard and visualization
Jupyter Notebook – Data analysis
VS Code – Development environment
Git & GitHub – Version control and project hosting
Dataset

The project uses multiple retail datasets including:

Purchases
Sales
Purchase Prices
Vendor Invoice
Inventory Beginning
Inventory Ending

These datasets are integrated to create a complete vendor performance analysis.

Project Workflow:
1. Data Ingestion

Imported multiple CSV datasets
Loaded data into SQLite database
Automated ingestion using Python scripts

2. SQL Data Processing

Created vendor summary tables
Joined multiple business tables
Cleaned missing values
Aggregated purchase and sales information

3. Exploratory Data Analysis (Python)

Performed business analysis including:

Vendor Sales Summary
Purchase Contribution Analysis
Brand Performance Analysis
Low Inventory Turnover Analysis
Gross Profit Calculation
Profit Margin Analysis
Inventory Turnover Analysis
Sales vs Purchase Analysis

4. Power BI Dashboard

Developed an interactive dashboard containing:

Total Sales
Total Purchase
Gross Profit
Profit Margin
Top Vendors
Top Brands
Vendor Purchase Contribution
Brand Performance
Low Turnover Products
Interactive Filters and Slicers

Key Insights:

Some important business questions answered include:

Which vendors contribute the highest purchase value?
Which brands generate the highest sales?
Which vendors have poor inventory turnover?
Which products require pricing improvements?
How does vendor performance affect profitability?
Which vendors should receive priority for procurement?
Business Recommendations

Based on the analysis:

Optimize pricing strategies for low-performing brands.
Increase procurement from high-performing vendors.
Improve inventory turnover for slow-moving products.
Reduce dependence on underperforming vendors.
Leverage bulk purchasing to reduce procurement costs.
Continuously monitor vendor KPIs using Power BI dashboards.
Dashboard Preview

The interactive Power BI dashboard includes:

KPI Cards (Total Sales, Gross Profit, Purchase Cost)
Vendor Sales Analysis
Brand Performance Analysis
Purchase Contribution Donut Chart
Low Inventory Turnover Analysis
Interactive Filters

Project Structure:

Vendor-Performance-Analysis/
│
├── dashboard/
│   ├── Vendor_Performance_Analysis_Dashboard.pbix
│   ├── Dashboard_Overview.png
│   └── Dashboard_Insights.png
│
├── data/
│   ├── begin_inventory.csv
│   ├── end_inventory.csv
│   ├── purchases.csv
│   ├── purchase_prices.csv
│   ├── sales.csv
│   ├── vendor_invoice.csv
│   ├── Vendor_Sales_Summary.csv
│   ├── Purchase_Contribution.csv
│   ├── Brand_Performance.csv
│   └── Low_Turnover.csv
│
├── logs/
│   ├── ingestion_db.log
│   └── get_vendor_summary.log
│
├── notebooks/
│   ├── Exploratory_Data_Analysis.ipynb
│   └── Vendor_Performance_Analysis.ipynb
│
├── scripts/
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
│
├── sqlite/
│   └── inventory.db
│
├── README.md
├── requirements.txt
└── .gitignore

How to Run the Project:

1. Clone the Repository
git clone https://github.com/Revathi-0503/Vendor-Performance-Analysis.git
get dataset :https://1drv.ms/f/c/42e2b607b89d8560/IgCF3p7_CRK-QLeP0lF1Ol9IAS8qun9TC2IoMG67XjSnDLQ?e=r1XBUC
2. Navigate to the Project Folder
cd Vendor-Performance-Analysis
3. Install Required Libraries
pip install -r requirements.txt
4. Run Data Ingestion
python ingestion_db.py
5. Generate Vendor Summary
python get_vendor_summary.py
6. Execute Jupyter Notebooks
Run the following notebooks sequentially:

Exploratory_Data_Analysis.ipynb
Vendor_Performance_Analysis.ipynb
7. Open Power BI Dashboard

Open:
(<dashboard/Vendor Performance Analysis Dashboard.pbix>)

Refresh the data source if required and explore the dashboard.

Future Enhancements:

Machine Learning-based vendor performance prediction
Sales forecasting using time-series models
Automated ETL pipeline with Apache Airflow
Cloud deployment using Power BI Service
Real-time inventory monitoring dashboard

Author:

Revathi A S
Data Analytics | Python | SQL | Power BI

License:

This project is intended for educational and portfolio purposes.endor Performance Analytics for Profit Optimization

