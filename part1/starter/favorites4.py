# favorites4.py
# Task: Count how many students chose each language using separate counter variables.
#
# Expected output:
#   Scratch: 28
#   C: 40
#   Python: 196
#
# Note: This approach has a serious limitation — can you spot it?
#       (Think about what happens if a new language appears in the data)

import csv
from pathlib import Path

scratch = 0
c = 0
python = 0

csv_path = Path(__file__).parent.parent / "favorites.csv"

with open(csv_path, "r") as file:
    reader = csv.DictReader(file)

    

    for row in reader:
        favorite = row["language"]
        if favorite == "Scratch": # The limitation is that we have to hardcode the language names and we use an if else chain. If a new language appears, we have to add a new variable and a new branch to the if else chain.
            scratch += 1
        elif favorite == "C":
            c += 1
        elif favorite == "Python":
            python += 1

print(f"Scratch: {scratch}")
print(f"C: {c}")
print(f"Python: {python}")
