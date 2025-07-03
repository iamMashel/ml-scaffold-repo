def save_plot(fig, name, path="reports/figures/"):
    fig.savefig(f"{path}{name}.png", bbox_inches='tight')

def export_to_excel(df, filename="cleaned.xlsx", sheet_name="Sheet1"):
    df.to_excel(f"client_deliverables/{filename}", index=False, sheet_name=sheet_name)
