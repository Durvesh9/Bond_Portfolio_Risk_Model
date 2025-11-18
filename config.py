# config.py

# --- DATABASE SETTINGS ---
DB_CONFIG = {
    "dbname": "bond_project",  # Updated DB name
    "user": "postgres",
    "password": "password",     # Updated it with your actual password
    "host": "localhost",
    "port": "5432"
}

# --- FILE SETTINGS ---

CSV_FILE_PATH = "data/portfolio_data.csv"
OUTPUT_FILENAME = "portfolio_risk_report.xlsx"

# --- SIMULATION SETTINGS ---
SCENARIOS = {
    "Base": 0,
    "Bull_Flattening": -50,
    "Bear_Steepening": 50,
    "Shock_Up_100": 100,
    "Shock_Down_100": -100
}