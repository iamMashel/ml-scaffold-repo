import pandas as pd

# Cleaning utilities for dataframes. Return copy to avoid modifying original dataframe.
def clean_column_names(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def convert_dates(df, date_cols):
    df = df.copy()
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df

#check if the column exists before calculating total sale
# handle errors gracefully.
def calculate_total_sale(df, qty_col='quantity', price_col='unit_price'):
    df = df.copy()
    if qty_col in df.columns and price_col in df.columns:
        df['total_sale'] = df[qty_col] * df[price_col]
    else:
        df['total_sale'] = pd.NA
    return df
