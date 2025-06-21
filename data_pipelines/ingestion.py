import pandas as pd
import logging

def ingest_from_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        logging.info(f"Loaded {len(df)} records from {filepath}")
        return df
    except Exception as e:
        logging.error(f"Failed to load CSV: {e}")
        return pd.DataFrame()

def ingest_from_api(api_func, *args, **kwargs):
    try:
        data = api_func(*args, **kwargs)
        return pd.DataFrame(data)
    except Exception as e:
        logging.error(f"API ingestion error: {e}")
        return pd.DataFrame()
