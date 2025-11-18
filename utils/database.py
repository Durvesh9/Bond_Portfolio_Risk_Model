# utils/database.py
import psycopg2
import pandas as pd
import config
import os

def get_db_connection():
    try:
        return psycopg2.connect(**config.DB_CONFIG)
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def initialize_db_from_csv():
    print("Checking database initialization...")
    conn = get_db_connection()
    if conn is None: return

    try:
        cur = conn.cursor()
        
        # Create Table
        cur.execute("""
        CREATE TABLE IF NOT EXISTS bond_portfolio (
            bond_id SERIAL PRIMARY KEY,
            bond_name VARCHAR(150),
            face_value DECIMAL(15, 2),
            coupon_rate DECIMAL(6, 5),
            maturity_years INT,
            current_yield DECIMAL(6, 5)
        );
        """)
        
        # Check if empty
        cur.execute("SELECT COUNT(*) FROM bond_portfolio")
        count = cur.fetchone()[0]
        
        if count == 0:
            print(f"Table is empty. Loading from {config.CSV_FILE_PATH}...")
            if os.path.exists(config.CSV_FILE_PATH):
                df = pd.read_csv(config.CSV_FILE_PATH)
                
                insert_query = """
                INSERT INTO bond_portfolio (bond_name, face_value, coupon_rate, maturity_years, current_yield)
                VALUES (%s, %s, %s, %s, %s)
                """
                data_tuples = [tuple(x) for x in df.to_numpy()]
                cur.executemany(insert_query, data_tuples)
                conn.commit()
                print(f"Successfully inserted {len(df)} records.")
            else:
                print(f"Error: CSV file not found at {config.CSV_FILE_PATH}")
        else:
            print(f"Database already contains {count} records.")
            
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error initializing database: {e}")
        if conn: conn.close()

def fetch_portfolio_data():
    conn = get_db_connection()
    if conn is None: return pd.DataFrame()
    try:
        df = pd.read_sql_query("SELECT * FROM bond_portfolio", conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Error executing query: {e}")
        conn.close()
        return pd.DataFrame()