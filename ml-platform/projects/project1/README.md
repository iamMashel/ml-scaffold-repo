# 📊 Netflix Content Analysis – Project Overview

## 📁 Table of Contents
- [Project Overview](#project-overview)
- [Setup](#setup)
- [Usage](#usage)
- [Deliverables](#deliverables)
- [Links](#links)

---

## 📝 Project Overview

This project analyzes the evolution of Netflix’s catalog to uncover trends by content type, genre, region, and rating.  
It includes data cleaning, exploratory data analysis (EDA), and an interactive dashboard for stakeholders.

---

## ⚙️ Setup

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd ml-platform/projects/project1
   ```

2. **Create and activate a conda environment:**
   ```sh
   conda env create -f environment.yml
   conda activate scaffolds
   ```

3. **Install required packages (if not using conda):**
   ```sh
   pip install -r requirements.txt
   ```

4. **Ensure data is available:**
   - Place raw data in `../../data/raw/`
   - Cleaned data will be saved to `../../data/processed/your_data_clean.csv`

---

## 🚀 Usage

### 1. **Run EDA Notebook**
   - Open `notebooks/01-eda.ipynb` in Jupyter and run all cells to explore and clean the data.

### 2. **Run the Dashboard**
   - From the `ml-platform` root directory, launch Streamlit:
     ```sh
     cd ../../..
     streamlit run projects/project1/dashboard/app.py
     ```
   - The dashboard will open in your browser.

### 3. **View Reports**
   - Executive summary and insights are in `reports/executive_summary.md`.

---

## 📦 Deliverables

- 📊 **Streamlit Dashboard**: Interactive exploration of Netflix data.
- 📓 **Jupyter Notebook**: EDA, cleaning, and visualizations.
- 📄 **Executive Summary**: Key findings and recommendations.
- 💾 **Cleaned Dataset**: `data/processed/your_data_clean.csv`

---

## 🔗 Links

- [Executive Summary](reports/executive_summary.md)
- [Kaggle Netflix Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)

---

## 🚦 Next Steps

- Present findings to stakeholders.
- Prioritize recommendations for future Netflix content strategy.

---