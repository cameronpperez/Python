#!/usr/bin/env python3

# Assignment 4
# Author: Cameron Perez

#imports at top of file
import sqlite3

def year_lookup(cur):
    # get user input
    year_str = input("Please enter the year to lookup: ").strip()  # .strip to get rid of whitespaces
    try:
        year = int(year_str)
    except ValueError:
        print(f"'{year_str}' is not a valid year.'")
        con.close()
        return

    # run a join query
    sql = """
          SELECT m.name AS title, m.year, m.minutes, c.name AS genre
          FROM movie m
                   JOIN category c
                        ON m.categoryID = c.categoryID
          WHERE m.year = ?
          ORDER BY title \
          """

    cur.execute(sql, (year,))
    rows = cur.fetchall()

    header = "{:40}{:<15}{:<15}{:<20}".format("Title", "Year", "Length", "Genre")
    print(header)
    print("-" * len(header))

    # show results
    if rows:
        for title, year, minutes, genre in rows:
            print("{:40}{:<15}{:<15}{:<20}".format(title, year, minutes, genre))
    else:
        print() #spacing
        print(f"Sorry, no movie in our database for {year}.")

def main():
    con = sqlite3.connect('dbmovies.sqlite')
    cur = con.cursor()

    # execute an update for Toy Story
    cur.execute("UPDATE movie SET year = 1995 WHERE name = 'Toy Story'")
    con.commit()

    # delete Lawrence of Arabia from database
    cur.execute("DELETE FROM movie WHERE name = 'Lawrence of Arabia'")
    con.commit()

    while True:
        year_lookup(cur)
        print() #spacing
        ask = input("Look up another year (y/n)? ").strip().lower()
        if ask not in ("y", "yes"):
            print()  # spacing
            print("Bye for now - see you at the movies!")
            break
        print() #spacing

    con.close()

    if con:
        con.close()

if __name__ == "__main__":
    main()