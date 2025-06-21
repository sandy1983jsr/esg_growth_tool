import pandas as pd
import logging

def save_to_csv(df: pd.DataFrame, path: str):
    try:
        df.to_csv(path, index=False)
        logging.info(f"Data saved to {path}")
    except Exception as e:
        logging.error(f"Failed to save CSV: {e}")

def save_to_sql(df: pd.DataFrame, conn, table_name: str):
    try:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        logging.info(f"Data saved to {table_name} in SQL DB")
    except Exception as e:
        logging.error(f"Failed to save to SQL: {e}")
