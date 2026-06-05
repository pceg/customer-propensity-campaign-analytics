import pandas as pd
from pathlib import Path


RAW_PATH = Path("../data/raw/bank-full.csv")


def main():
    df = pd.read_csv(RAW_PATH, sep=";")

    print("=== Pierwsze 5 wierszy ===")
    print(df.head())

    print("\n=== Informacje o danych ===")
    print(df.info())

    print("\n=== Liczba braków danych ===")
    print(df.isna().sum())

    print("\n=== Rozkład zmiennej celu y ===")
    print(df["y"].value_counts())

    print("\n=== Rozkład zmiennej celu y w % ===")
    print(df["y"].value_counts(normalize=True).round(4))

    print("\n=== Lista kolumn ===")
    print(df.columns.tolist())

    print("\n=== Podstawowe statystyki liczbowe ===")
    print(df.describe())


if __name__ == "__main__":
    main()