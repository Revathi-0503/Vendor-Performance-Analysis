# Vendor Performance Analytics for Profit Optimization

An end-to-end **Data Analytics** project that analyzes vendor performance, inventory efficiency, and sales profitability using **Python, SQL (SQLite), and Power BI**. The project demonstrates the complete analytics workflow from data ingestion and preprocessing to business analysis, dashboard development, and actionable business recommendations.

---

## 📖 Project Overview

Retail and wholesale businesses work with multiple vendors, thousands of products, and large transactional datasets. This project transforms raw purchasing, inventory, sales, and vendor invoice data into meaningful business insights.

The objective is to optimize profitability by evaluating vendor performance, improving inventory turnover, identifying underperforming brands, and supporting data-driven business decisions.

---

## 🎯 Problem Statement

Analyze vendor purchasing and sales data to identify:

- High and low-performing vendors
- Underperforming brands
- Inventory turnover efficiency
- Purchase contribution by vendors
- Pricing inefficiencies
- Profitability gaps

Develop an interactive Power BI dashboard and generate business recommendations to improve vendor management and operational efficiency.

---

## 🛠️ Tech Stack

- **Python** – Data preprocessing and exploratory data analysis
- **Pandas** – Data manipulation
- **SQL (SQLite)** – Database management and business analysis
- **Power BI** – Interactive dashboard and visualization
- **Jupyter Notebook** – Data analysis
- **VS Code** – Development environment
- **Git & GitHub** – Version control and project hosting

---

## 📂 Dataset

The project uses multiple retail datasets including:

- Purchases
- Sales
- Purchase Prices
- Vendor Invoice
- Beginning Inventory
- Ending Inventory

These datasets are integrated to create a complete vendor performance analysis.

> **Note:** Due to GitHub's file size limitations, the complete raw datasets are hosted externally.

**Dataset Download:**  
https://1drv.ms/f/c/42e2b607b89d8560/IgCF3p7_CRK-QLeP0lF1Ol9IAS8qun9TC2IoMG67XjSnDLQ?e=r1XBUC

---

## ⚙️ Project Workflow

### 1️⃣ Data Ingestion

- Imported multiple CSV datasets
- Loaded data into SQLite database
- Automated ingestion using Python scripts

### 2️⃣ SQL Data Processing

- Created vendor summary tables
- Joined multiple business tables
- Cleaned missing values
- Aggregated purchase and sales information

### 3️⃣ Exploratory Data Analysis (Python)

Performed business analysis including:

- Vendor Sales Summary
- Purchase Contribution Analysis
- Brand Performance Analysis
- Low Inventory Turnover Analysis
- Gross Profit Calculation
- Profit Margin Analysis
- Inventory Turnover Analysis
- Sales vs Purchase Analysis

### 4️⃣ Power BI Dashboard

The dashboard includes:

- Total Sales
- Total Purchase
- Gross Profit
- Profit Margin
- Top Vendors
- Top Brands
- Purchase Contribution
- Brand Performance
- Low Turnover Products
- Interactive Filters & Slicers

---

## 📊 Key Insights

This project answers important business questions such as:

- Which vendors contribute the highest purchase value?
- Which brands generate the highest sales?
- Which vendors have poor inventory turnover?
- Which products require pricing improvements?
- How does vendor performance affect profitability?
- Which vendors should receive procurement priority?

---

## 💡 Business Recommendations

- Optimize pricing strategies for low-performing brands.
- Increase procurement from high-performing vendors.
- Improve inventory turnover for slow-moving products.
- Reduce dependence on underperforming vendors.
- Leverage bulk purchasing to reduce procurement costs.
- Continuously monitor vendor KPIs using Power BI dashboards.

---
## 📊 Dashboard Preview

### Dashboard Overview

[![Dashboard Overview](dashboard/Dashboard_Overview.png)](dashboard/Dashboard_Overview.png)

### Dashboard Insights

[![Dashboard Insights](dashboard/Dashboard_Insights.png)](dashboard/Dashboard_Insights.png)

---

## 📁 Project Structure

```text
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
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Revathi-0503/Vendor-Performance-Analysis.git
```

### 2. Download the Dataset

Download the datasets from the link below and place them inside the **data/** folder.

https://1drv.ms/f/c/42e2b607b89d8560/IgCF3p7_CRK-QLeP0lF1Ol9IAS8qun9TC2IoMG67XjSnDLQ?e=r1XBUC

### 3. Navigate to the Project Folder

```bash
cd Vendor-Performance-Analysis
```

### 4. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 5. Run Data Ingestion

```bash
python scripts/ingestion_db.py
```

### 6. Generate Vendor Summary

```bash
python scripts/get_vendor_summary.py
```

### 7. Run the Jupyter Notebooks

Execute the notebooks in the following order:

- Exploratory_Data_Analysis.ipynb
- Vendor_Performance_Analysis.ipynb

### 8. Open Power BI Dashboard

Open:

```
dashboard/Vendor_Performance_Analysis_Dashboard.pbix
```

Refresh the data source if required.

---

## 🔮 Future Enhancements

- Machine Learning-based Vendor Performance Prediction
- Sales Forecasting using Time-Series Models
- Automated ETL Pipeline with Apache Airflow
- Cloud Deployment using Power BI Service
- Real-Time Inventory Monitoring Dashboard

---

## 👩‍💻 Author

**Revathi A S**

**Data Analytics | Python | SQL | Power BI**

---

## 📄 License

This project is intended for educational and portfolio purposes.
