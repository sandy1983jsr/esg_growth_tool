import pandas as pd
import hashlib

def anonymize_column(df: pd.DataFrame, column: str):
    if column in df.columns:
        df[column] = df[column].apply(lambda x: hashlib.sha256(str(x).encode()).hexdigest())
    return df

def mask_email(df: pd.DataFrame, column: str):
    import re
    if column in df.columns:
        df[column] = df[column].str.replace(r'([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', r'***@***', regex=True)
    return df
