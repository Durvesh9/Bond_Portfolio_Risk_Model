# models/scenarios.py
import pandas as pd
from models import valuation # Import from sibling in models package
import config

def run_scenario_analysis(portfolio_df):
    results = []
    print("Running scenario analysis...")

    for index, row in portfolio_df.iterrows():
        b_id = row['bond_id']
        name = row['bond_name']
        face = row['face_value']
        c_rate = row['coupon_rate']
        years = row['maturity_years']
        curr_yield = row['current_yield']

        base_price = valuation.calculate_bond_price(face, c_rate, years, curr_yield)
        dv01 = valuation.calculate_dv01(face, c_rate, years, curr_yield)

        for scenario_name, bps_shock in config.SCENARIOS.items():
            shock_decimal = bps_shock / 10000
            new_yield = curr_yield + shock_decimal
            new_price = valuation.calculate_bond_price(face, c_rate, years, new_yield)
            pnl = new_price - base_price

            results.append({
                "Bond ID": b_id,
                "Bond Name": name,
                "Scenario": scenario_name,
                "Shock (bps)": bps_shock,
                "Original Yield": f"{curr_yield:.2%}",
                "New Yield": f"{new_yield:.2%}",
                "Base Price": base_price,
                "New Price": new_price,
                "PnL": pnl,
                "DV01": dv01
            })

    return pd.DataFrame(results)