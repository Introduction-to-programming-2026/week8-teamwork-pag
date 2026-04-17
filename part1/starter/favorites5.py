# favorites5.py
# Task: Count languages using a single dictionary instead of separate variables.
#
# Why is this better than favorites4?
#   - Works for any number of languages — no hard-coding
#   - Adding a new language to the CSV requires zero code changes
#
# Expected output (order may vary):
#   Python: 196
#   C: 40
#   Scratch: 28

import csv
from pathlib import Path

csv_path = Path(__file__).parent.parent / "favorites.csv"

with open(csv_path, "r") as file:
    reader = csv.DictReader(file)

    counts = {}  # language -> count

    for row in reader:
        favorite = row["language"]
        match favorite in counts:
            case None:
                counts[favorite] = 1
            case _:
                counts[favorite] += 1

    for language, count in counts.items():
        print(f"{language}: {count}")

