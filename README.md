# **Bond Portfolio Risk Model**

### **A Python-based Financial Risk Engine**

This project is a **quantitative finance tool** designed to simulate **Interest Rate Shocks** on a fixed-income portfolio. It connects to a local **PostgreSQL** database, loads raw bond data, performs **DCF-based valuation**, computes **DV01**, and generates a professional **Excel Risk Report** summarizing portfolio behavior under multiple yield curve scenarios.

---

## 📌 **Project Overview**

### 🎯 **Objective**

Quantify **PnL impact** of interest rate movements
(e.g., **+100 bps**, **–50 bps**)
on a portfolio of Indian Bonds:

* Government Securities (G-Secs)
* State Development Loans (SDLs)
* Corporate Bonds

---

### 📈 **Key Metrics**

* **Present Value (PV)** – DCF-based bond valuation
* **DV01** – Duration risk (Sensitivity to 1 bps move)
* **Scenario PnL** – Profit/Loss under simulated yield shocks

---

### 🧰 **Tech Stack**

* **Python 3.10+**
* **PostgreSQL** (via `psycopg2` or `sqlalchemy`)
* **Pandas**, **NumPy**
* Optional: `openpyxl`, `tabulate`

---

## 📂 **Project Structure**

```
bond_portfolio_project/
│
├── main.py                     # <--- ENTRY POINT (Run this file)
├── config.py                   # Configuration (DB credentials, Shock settings)
├── requirements.txt            # Python dependencies
│
├── data/                       # DATA LAYER
│   ├── portfolio_data.csv      # Raw dataset (200+ Indian government & corporate bonds)
│   └── schema.sql              # SQL reference schema (documentation only)
│
├── models/                     # LOGIC LAYER (Financial brain)
│   ├── valuation.py            # DCF logic, pricing functions, DV01
│   └── scenarios.py            # Yield curve simulation loops
│
└── utils/                      # INFRASTRUCTURE LAYER
    ├── database.py             # PostgreSQL connection + auto-loader
    └── reporting.py            # Excel generator for risk reports
```

---

## ⚙️ **Installation & Setup**

### **1. Prerequisites**

* Python installed and added to PATH
* PostgreSQL installed (with pgAdmin 4)

---

### **2. Install Python Dependencies**

Open terminal:

```bash
pip install -r requirements.txt
```

---

### **3. Database Setup (One-Time Process)**

1. Open **pgAdmin 4**
2. Right-click **Databases → Create → Database**
3. Name it:

```bash
bond_project
```

4. Click **Save**

⚠️ *No manual tables required.*
The Python ETL script creates tables automatically.

---

### **4. Configure Database Credentials**

Open `config.py` and edit:

```python
DB_CONFIG = {
    "dbname": "bond_project",
    "user": "postgres",
    "password": "YOUR_PASSWORD",   # <--- update this
    "host": "localhost",
    "port": "5432"
}
```

---

## 🚀 **How to Run**

### **Step 1 — Run the Main Engine**

This executes the full workflow:

```bash
python main.py
```

### **What the Script Does**

#### ✔ Auto-ETL

* Checks if the SQL table is empty
* If empty → loads `portfolio_data.csv` into PostgreSQL automatically

#### ✔ Valuation Engine

* Fetches data from the DB
* Computes base DCF price

#### ✔ Shock Simulation

Simulates multiple yield curve shifts:

* +100 bps parallel up
* –50 bps parallel down
* Bear Steepening
* Bull Flattening

#### ✔ Reporting

Creates:

```bash
portfolio_risk_report.xlsx
```

---

## 📊 **Financial Logic Explained**

### **1. Bond Price (DCF Valuation)**


### Price=t=1∑N​(1+r)tC​+(1+r)NF​


Where:

* **C** = Annual coupon
* **F** = Face value
* **r** = Yield to maturity (or shocked yield)
* **t** = Time period

---

### **2. DV01 — Dollar Value of a Basis Point**

### DV01=Pbase​−Pyield+1bp​

Interpretation:

* High DV01 = high rate sensitivity (higher risk)
* Used widely in trading desks and treasury risk teams

---

## 📑 **Output Report**

The generated `portfolio_risk_report.xlsx` includes:

### **📘 Sheet 1 — Summary**

* Total PnL per scenario
* Key risk indicators
* Answers questions like:
  **“How much do we lose if rates rise by 1%?”**

### **📗 Sheet 2 — Details**

Row-by-row information:

* Base Price
* Shocked Price
* Original Yield
* New Yield
* DV01
* Scenario PnL

Perfect for risk teams, traders, and portfolio managers.

---

Just tell me!
