# utils/reporting.py
import pandas as pd
import config

def generate_excel_report(results_df):
    filename = config.OUTPUT_FILENAME
    print(f"Generating report: {filename}")

    try:
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            summary_df = results_df.groupby("Scenario")[["Base Price", "New Price", "PnL"]].sum().reset_index()
            summary_df.to_excel(writer, sheet_name="Summary", index=False)
            results_df.to_excel(writer, sheet_name="Details", index=False)
        print("Report generated successfully.")
    except Exception as e:
        print(f"Error saving Excel report: {e}")