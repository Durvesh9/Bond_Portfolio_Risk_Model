-- data/schema.sql
CREATE TABLE IF NOT EXISTS bond_portfolio (
    bond_id SERIAL PRIMARY KEY,
    bond_name VARCHAR(150),
    face_value DECIMAL(15, 2),
    coupon_rate DECIMAL(6, 5),
    maturity_years INT,
    current_yield DECIMAL(6, 5)
);