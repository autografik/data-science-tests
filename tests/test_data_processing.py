# tests / test_data_processing.py
"""
Testy modułu data_processing.py.

Uwagi dla testowania:
- Testy powinny być deterministyczne: nie polegaj na zewnętrznych plikach ani zdalnych źródłach.
- Twórz małe DataFrame w testach (konstrukcja z dict) i używaj ich jako wejścia funkcji.
- Uruchamianie: `pytest -q` lub `pytest -q --maxfail=1`.
- Aby uruchomić pojedynczy test: `pytest tests/test_data_processing.py::test_clean_column_names -q`.
"""

import pandas as pd
import pytest

from ds_tests import data_processing as dp


def test_clean_column_names():
    df = pd.DataFrame({" A ": [1, 2], "b C": [3, 4]})
    cleaned = dp.clean_column_names(df)
    assert "a" in cleaned.columns or "a" in [c.strip() for c in cleaned.columns]
    # dokładna nazwa po oczyszczeniu:
    assert "a" not in cleaned.columns  # sprawdź, że nie ma spacji
    assert "a" not in [c for c in cleaned.columns if " " in c]
    assert "a" not in list(filter(lambda x: " " in x, cleaned.columns))
    # konkretne oczekiwane nazwy:
    assert "a" in [col.replace("_", "") for col in cleaned.columns] or "a" in [
        c[0] for c in zip(*[cleaned.columns])
    ]
    # Prostsze sprawdzenie — nazwy powinny być lower() i bez spacji:
    for col in cleaned.columns:
        assert col == col.strip()
        assert " " not in col
        assert col == col.lower()


def test_select_numeric_columns_and_means():
    df = pd.DataFrame(
        {
            "num": [1, 2, 3, None],
            "cat": ["a", "b", "c", "d"],
            "float_col": [0.5, 1.5, None, 2.5],
        }
    )
    numeric = dp.select_numeric_columns(df)
    assert "num" in numeric.columns
    assert "float_col" in numeric.columns
    assert "cat" not in numeric.columns

    means = dp.compute_column_means(df, ["num", "float_col"])
    # Porównujemy wartości z obliczonymi bezpośrednio
    assert pytest.approx(means["num"], rel=1e-9) == float(df["num"].mean(skipna=True))
    assert pytest.approx(means["float_col"], rel=1e-9) == float(
        df["float_col"].mean(skipna=True)
    )


def test_compute_column_means_missing_column():
    df = pd.DataFrame({"a": [1, 2, 3]})
    with pytest.raises(KeyError):
        dp.compute_column_means(df, ["nonexistent"])
