# Solar Irradiance Dashboard – Technical Documentation

## 1. Project Overview

This project is a **Streamlit-based interactive dashboard** for visualizing and analyzing solar irradiance data (GHI, DNI, DHI) across three countries: **Benin**, **Sierra Leone**, and **Togo**.

The dashboard enables:

- Interactive comparison of countries
- Statistical testing of solar metrics
- Summary tables of descriptive statistics
- Visualization for decision-making in solar energy planning

---

## 2. Architecture & Folder Structure
```plaintext
project-root/
├── app/
│ ├── init.py
│ ├── main.py # Streamlit app
│ └── utils.py # Data loading, cleaning, visualization functions
├── data/ # Raw CSV data files
│ ├── benin-malanville_clean.csv
│ ├── sierraleone-bumbuna_clean.csv
│ └── togo-dapaong_qc_clean.csv
└── scripts/
├── init.py
└── README.md

---

## 3. Technical Development

### Data Loading & Processing

- CSV files are loaded per country using `utils.py`.
- Missing values are handled and negative readings are removed.
- A `Country` column is added to each dataset for grouping.

### Dashboard Features

- Sidebar for country selection.
- Boxplots for GHI, DNI, DHI per country.
- Summary table showing mean, median, and standard deviation.
- Bar charts ranking countries by average metric.
- Statistical testing (ANOVA / Kruskal–Wallis).

### Warnings & Compatibility

- Seaborn FutureWarnings and minor Streamlit warnings are suppressed.
- Fixed relative import issues using `sys.path.append`.

---

## 4. Data Processing Pipeline

<img width="1317" height="668" alt="image" src="https://github.com/user-attachments/assets/f7289e1c-e775-4c81-8b71-2e5a53fa726e" />


## 5. Key Functions in `utils.py`

| Function                   | Description                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------- |
| `load_data()`              | Loads CSV datasets, merges them, adds `Country` column, handles missing values.          |
| `plot_boxplot(df, metric)` | Generates a Seaborn boxplot for a given metric grouped by country, suppressing warnings. |
| `summarize_metrics(df)`    | Returns a summary table of mean, median, and standard deviation per metric and country.  |

```


```

### 6. Installation & Setup

# Clone the repository

git clone <your-repo-url>
cd solar-challenge-week0

# Create and activate virtual environment

python -m venv .venv
.venv\Scripts\activate # Windows
source .venv/bin/activate # macOS/Linux

# Install dependencies

pip install -r requirements.txt

# Run the dashboard

streamlit run app/main.py
