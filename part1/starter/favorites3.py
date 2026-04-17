# favorites3.py
# Task: Same as favorites2 but print directly without a named variable.
#       One-liner inside the loop: print(row["language"])
#
# This version is more concise. favorites2 is more readable.
# Neither is "wrong" — it depends on the situation.

import csv
from pathlib import Path

csv_path = Path(__file__).parent.parent / "favorites.csv"

with open(csv_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["language"])