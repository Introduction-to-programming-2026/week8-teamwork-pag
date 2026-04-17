# favorites2.py
# Task: Print every language using csv.DictReader instead of csv.reader
#
# Key difference:
#   csv.reader  → row is a LIST  → access by index: row[1]
#   DictReader  → row is a DICT → access by name:  row["language"]
#
# Bonus: DictReader automatically uses the first row as keys — no need for next()

import csv
from pathlib import Path

csv_path = Path(__file__).parent.parent / "favorites.csv"

with open(csv_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row["language"]
        print(language)