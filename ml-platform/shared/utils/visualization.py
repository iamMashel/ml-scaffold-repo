import seaborn as sns
import matplotlib.pyplot as plt

def plot_top_n(df, col, value_col='total_sale', n=5):
    top = df.groupby(col)[value_col].sum().nlargest(n).reset_index()
    sns.barplot(x=value_col, y=col, data=top)
    plt.title(f"Top {n} by {value_col}")
    plt.tight_layout()
