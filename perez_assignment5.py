import sqlite3
import matplotlib.pyplot as plt

# Connecting to the database file
conn = sqlite3.connect("degrees2.db")
cur = conn.cursor()

# Look at the available tables
cur.execute("SELECT * FROM degrees")
rows = cur.fetchall()

# Retrieve the headers and adding them to a list
# cur.description grabs the headers in the table
col_names = [description[0] for description in cur.description]

# Convert to dictionary: year to values for each major
years = [row[0] for row in rows]
majors = ['HealthProfessions', 'Education', 'ComputerScience', 'Engineering']

data = {major: [] for major in majors}
for row in rows:
    for major in majors:
        col_index = col_names.index(major)
        data[major].append(row[col_index])

# Plotting each major
plt.figure(figsize=(10,6))
for major in majors:
    plt.plot(years, data[major], label=major)

# Add labels and title
plt.xlabel("Year")
plt.ylabel("Degrees")
plt.title("Percentage of Bachelor's Degrees Awarded to Women (1970–2011)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()