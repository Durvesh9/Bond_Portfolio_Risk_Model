# models/valuation.py
import numpy as np

def calculate_bond_price(face_value, coupon_rate, maturity_years, yield_rate):
    t = np.arange(1, maturity_years + 1)
    coupon_payment = face_value * coupon_rate
    discounted_coupons = np.sum(coupon_payment / ((1 + yield_rate) ** t))
    discounted_principal = face_value / ((1 + yield_rate) ** maturity_years)
    return discounted_coupons + discounted_principal

def calculate_dv01(face_value, coupon_rate, maturity_years, current_yield):
    p_base = calculate_bond_price(face_value, coupon_rate, maturity_years, current_yield)
    shock_yield = current_yield - 0.0001 # 1bp shock
    p_shock = calculate_bond_price(face_value, coupon_rate, maturity_years, shock_yield)
    return p_shock - p_base