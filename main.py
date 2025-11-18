

import sys


from utils import database, reporting
from models import scenarios

def main():
    print("--- Starting Bond Portfolio Risk Model ---")


    # Step 1: Database Initialization & ETL
    
    database.initialize_db_from_csv()


    # Step 2: Fetch Data

    print("[1/3] Loading Portfolio from PostgreSQL...")
    portfolio_df = database.fetch_portfolio_data()
    
    if portfolio_df.empty:
        print("CRITICAL ERROR: No data found in database.")
        print("Please check if your PostgreSQL server is running and credentials in config.py are correct.")
        sys.exit(1)
    
    print(f" >> Successfully loaded {len(portfolio_df)} bonds.")

    
    # Step 3: Run Financial Models (Valuation & Scenarios)
    
    print("[2/3] Running Interest Rate Shock Scenarios...")
    
    # This calls the logic in models/scenarios.py
    results_df = scenarios.run_scenario_analysis(portfolio_df)

 
    # Step 4: Generate Report
   
    print("[3/3] Exporting Analysis to Excel...")
    
    # This calls the logic in utils/reporting.py
    reporting.generate_excel_report(results_df)

    print("\n--- Process Complete ---")
    print("Check 'portfolio_risk_report.xlsx' for results.")

if __name__ == "__main__":
    main()