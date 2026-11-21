"""
Titanic Data Explorer
A small data-analytics project that applies the core pandas functions
(head, tail, sample, shape, columns, dtypes, info, describe,
value_counts, unique, isna, duplicated) to the Titanic dataset.
"""

import pandas as pd


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def load_data(path):
    df = pd.read_csv(path)
    print(f"Loaded '{path}' successfully.")
    return df


def preview_data(df):
    section("1. DATA PREVIEW")
    print("First 3 rows:")
    print(df.head(3))
    print("\nLast 5 rows:")
    print(df.tail())
    print("\n5 random rows (random_state=42):")
    print(df.sample(5, random_state=42))


def inspect_structure(df):
    section("2. DATASET STRUCTURE")
    print("Shape (rows, columns):", df.shape)
    print("\nColumns:", list(df.columns))
    print("\nData types:")
    print(df.dtypes)
    print("\nInfo:")
    df.info()


def summarize_data(df):
    section("3. STATISTICAL SUMMARY")
    print("Numeric columns:")
    print(df.describe())
    print("\nAll columns (include='all'):")
    print(df.describe(include="all"))


def explore_categories(df):
    section("4. CATEGORICAL COLUMNS")
    for col in ["Sex", "Pclass", "Embarked", "Survived"]:
        print(f"\n{col} -> unique values: {df[col].unique()}")
        print(df[col].value_counts())


def check_quality(df):
    section("5. DATA QUALITY CHECK")
    print("Missing values per column:")
    print(df.isna().sum())
    print("\nDuplicate rows:", df.duplicated().sum())


def main():
    df = load_data("Titanic-Dataset.csv")
    preview_data(df)
    inspect_structure(df)
    summarize_data(df)
    explore_categories(df)
    check_quality(df)


if __name__ == "__main__":
    main()
