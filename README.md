
# data-science-tests

Starter repo do nauki narzędzi, testów i workflow dla projektów data-science.

Szybkie instrukcje (lokalnie)

1. Utwórz i aktywuj wirtualne środowisko:
   - Linux/macOS:
     python -m venv .venv
     source .venv/bin/activate
   - Windows (PowerShell):
     python -m venv .venv
     .\\.venv\\Scripts\\Activate.ps1

2. Zainstaluj zależności:
   pip install -r requirements.txt

3. Zainstaluj pre-commit hooks (jednorazowo):
   pre-commit install

4. Uruchamianie pre-commit lokalnie dla wszystkich plików:
   pre-commit run --all-files

5. Uruchamianie testów:
   pytest -q

6. Coverage:
   pytest --cov=src --cov-report=term-missing

Jak testować poprawnie:
- Testy powinny być deterministyczne (brak zależności od internetu/losowości).
- Testuj funkcje „czyste” (bez efektów ubocznych) — działaj na DataFrame w pamięci.
- Używaj małych, czytelnych przykładów danych w testach.
- W razie potrzeby użyj fixture’ów pytest do budowy wspólnych danych testowych.
- Do testów integracyjnych (np. czytanie z plików) stwórz katalog `tests/data/` i referencje do małych próbek — unikaj dużych danych.
