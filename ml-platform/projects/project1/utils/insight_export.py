from pathlib import Path

def export_insights(insights, project_root, filename="eda_insights.txt"):
    """
    Export a list of insights to a text file in the project's insights directory.
    """
    insight_dir = project_root / "insights"
    insight_dir.mkdir(parents=True, exist_ok=True)
    insight_file = insight_dir / filename
    with open(insight_file, "w", encoding="utf-8") as f:
        for line in insights:
            f.write(str(line) + "\n")
    print(f"✅ Key insights exported to {insight_file}")