name = src / ds_tests / data_processing.py
"""
Prosty moduł z funkcjami pomocniczymi do pracy z danymi.
Kod jest napisany tak, by dało się go łatwo testować — funkcje przyjmują DataFrame
jako wejście i zwracają DataFrame/wynik bez efektów ubocznych.
"""

from typing import Iterable
import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalizuje nazwy kolumn: strip(), lower(), zamiana spacji na '_'.
    Przyjmuje DataFrame i zwraca nowy DataFrame z przekształconymi nazwami.
    """
    new_columns = {col: col.strip().lower().replace(" ", "_") for col in df.columns}
    return df.rename(columns=new_columns)


def select_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Zwraca tylko kolumny typu numerycznego.
    """
    return df.select_dtypes(include="number")


def compute_column_means(df: pd.DataFrame, columns: Iterable[str]) -> dict:
    """
    Oblicza średnie wartości dla podanych kolumn (ignoruje NaN).
    Zwraca dict {column: mean}.
    """
    result = {}
    for col in columns:
        if col not in df.columns:
            raise KeyError(f"Column {col} not found in DataFrame")
        result[col] = float(df[col].mean(skipna=True))
    return result
