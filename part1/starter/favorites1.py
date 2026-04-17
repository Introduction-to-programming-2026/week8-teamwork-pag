# favorites1.py
# Task: Same as favorites0, but store the language in a variable called 'favorite'
#       before printing it.
#
# Why? Naming values makes code self-documenting.
#      row[1] tells you nothing. favorite = row[1] tells you exactly what row[1] is.

import csv
from pathlib import Path

csv_path = Path(__file__).parent.parent / "favorites.csv"

with open(csv_path, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        favorite = row[1]
        print(favorite)