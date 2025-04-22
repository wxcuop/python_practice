import os

# Path to the corrupted database
db_path = "difference_of_squares.db"

# Delete the corrupted database file
if os.path.exists(db_path):
    os.remove(db_path)

# Create a fresh database
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE "difference-of-squares" (
    "number" INT,
    "property" TEXT,
    "result" INT
)
''')

connection.commit()
connection.close()
print("Fresh database created successfully!")

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("difference_of_squares.db")
cursor = connection.cursor()
# Step 1: Create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS "difference-of-squares" (
    "number" INT,
    "property" TEXT,
    "result" INT
)
''')

# Step 2: Clear existing data from the table
cursor.execute('DELETE FROM "difference-of-squares"')

# Step 3: Insert the provided data
data = [
    (1, "squareOfSum", None),
    (5, "squareOfSum", None),
    (100, "squareOfSum", None),
    (1, "sumOfSquares", None),
    (5, "sumOfSquares", None),
    (100, "sumOfSquares", None),
    (1, "differenceOfSquares", None),
    (5, "differenceOfSquares", None),
    (100, "differenceOfSquares", None),
]
cursor.executemany('INSERT INTO "difference-of-squares" ("number", "property", "result") VALUES (?, ?, ?)', data)

# Step 4: Update the result column based on the property
cursor.execute('''

-- Schema: CREATE TABLE "difference-of-squares" ("number" INT", property" TEXT, "result" INT);
-- Task: update the difference-of-squares table and set the result based on the number and property fields.

UPDATE "difference-of-squares"
SET "result" = CASE
    WHEN "property" = 'squareOfSum' THEN (
        ("number" * ("number" + 1)) / 2 * ("number" * ("number" + 1)) / 2
    )
    WHEN "property" = 'sumOfSquares' THEN (
        ("number" * ("number" + 1) * (2 * "number" + 1)) / 6
    )
    WHEN "property" = 'differenceOfSquares' THEN (
        (("number" * ("number" + 1)) / 2 * ("number" * ("number" + 1)) / 2) -
        (("number" * ("number" + 1) * (2 * "number" + 1)) / 6)
    )
    ELSE NULL
END
''')

# Commit the changes and close the connection
connection.commit()

# Step 5: Verify the results
cursor.execute('SELECT * FROM "difference-of-squares"')
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

connection.close()
