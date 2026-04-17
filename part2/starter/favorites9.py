# favorites9.py
# Task: Count languages using SQL instead of a Python dictionary.
#
# Before running this file, import the CSV into SQLite:
#   sqlite3 favorites.db
#   .mode csv
#   .import ../week1/favorites.csv favorites
#   .quit
#
# The SQL query replaces the entire counting loop from favorites5–8.
# One query does what 10+ lines of Python did.
#
# Expected output:
#   Python 196
#   C 40
#   Scratch 28

from cs50 import SQL
from pathlib import Path

# Open the database relative to this script's folder
db_path = Path(__file__).parent.parent / "favorites.db"
db = SQL(f"sqlite:///{db_path}")

rows = db.execute(
    "SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC"
)

for row in rows:
    print(f"{row['language']} {row['n']}")
