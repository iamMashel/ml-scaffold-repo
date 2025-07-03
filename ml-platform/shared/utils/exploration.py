def summarize_dataframe(df):
    print("Shape:", df.shape)
    print("Missing values:\n", df.isna().sum())
    print("\nNumeric summary:\n", df.describe())
    print("\nCategorical counts:\n", df.select_dtypes(include='object').nunique())

def category_breakdown(df, col):
    return df[col].value_counts(normalize=True).round(3)
