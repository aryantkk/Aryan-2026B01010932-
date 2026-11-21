# 🚢 Titanic Data Cleaning & Exploration

A beginner-friendly data analytics project using **Python** and **pandas** to explore and clean the classic Titanic passenger dataset.

The repo has two scripts:

- **`titanic_data_explorer.py`** inspects the raw dataset using core pandas functions.
- **`cleaning.py`** cleans the raw data and saves a analysis-ready CSV.

---

## 📁 Project Structure

```
├── Titanic-Dataset.csv          # Raw dataset
├── cleaned_titanic.csv          # Output of cleaning.py
├── titanic_data_explorer.py     # Data exploration script
├── cleaning.py                  # Data cleaning script
└── README.md
```

---

## 🔍 Data Explorer (`titanic_data_explorer.py`)

Walks through the dataset in five sections and prints the results to the console:

| Section | What it does | pandas functions |
|---|---|---|
| 1. Data Preview | Shows first, last and random rows | `head()`, `tail()`, `sample()` |
| 2. Dataset Structure | Shape, column names, data types | `shape`, `columns`, `dtypes`, `info()` |
| 3. Statistical Summary | Numeric and full-column summaries | `describe()` |
| 4. Categorical Columns | Unique values and counts for `Sex`, `Pclass`, `Embarked`, `Survived` | `unique()`, `value_counts()` |
| 5. Data Quality Check | Missing values and duplicate rows | `isna()`, `duplicated()` |

---

## 🧹 Data Cleaning (`cleaning.py`)

Cleans `Titanic-Dataset.csv` and writes `cleaned_titanic.csv`. Steps:

1. **Drop the extra index column** (`Unnamed: 0`) if present
2. **Remove duplicate rows**
3. **Strip extra whitespace** from column names and text values
4. **Fill missing values** instead of deleting rows:
   - `Age` → filled with the median age
   - `Embarked` → filled with `"S"` (the most common port)
   - `Cabin` → filled with `"Unknown"`
5. **Keep only valid values:**
   - `Age > 0`
   - `Fare >= 0`
   - `Survived` is 0 or 1
   - `Pclass` is 1, 2 or 3
6. **Reset the index** and save the cleaned file

The script prints the shape and missing-value counts before and after cleaning so you can verify the result.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pandas

```bash
pip install pandas
```

### Run

```bash
# Clone the repo
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# Explore the raw data
python titanic_data_explorer.py

# Clean the data (creates cleaned_titanic.csv)
python cleaning.py
```

> Run the scripts from the folder that contains the CSV files, since they use relative paths.

---

## 📊 Dataset

The Titanic dataset contains information about passengers aboard the RMS Titanic, including:

| Column | Description |
|---|---|
| `PassengerId` | Unique passenger ID |
| `Survived` | 0 = No, 1 = Yes |
| `Pclass` | Ticket class (1st, 2nd, 3rd) |
| `Name` | Passenger name |
| `Sex` | Gender |
| `Age` | Age in years |
| `SibSp` | Number of siblings/spouses aboard |
| `Parch` | Number of parents/children aboard |
| `Ticket` | Ticket number |
| `Fare` | Ticket fare |
| `Cabin` | Cabin number |
| `Embarked` | Port of embarkation (C, Q, S) |

---

## 🛠️ Tech Stack

- Python
- pandas
