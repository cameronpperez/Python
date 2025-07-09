#!/usr/bin/env python3

# Assignment 3 - SQL Statements
# Author: Cameron Perez

import sqlite3
import os
import logging

def main():
    #logging setup
    logging.basicConfig(level=logging.DEBUG,format="[Movies]:%(asctime)s:%(levelname)s:%(message)s")  # DEBUG,INFO,ERROR,WARNING,CRITICAL

    if os.path.exists('movies_python.db') and os.path.getsize('movies_python.db') > 0:
        logging.debug("{a} found and not zero size".format(a='movies_python.db'))
    else:
        logging.error("{a} not found or zero size".format(a='movies_python.db'))

    info_1 = [
        (1, 'Adventure', 'Cars', 'John Lasseter'),
        (2,'Drama','Whiplash','Damien Chazelle'),
        (3, 'Romance', 'Fallen Angels', 'Wong Kar-wai')
    ]

    info_2 = [
        (1, 2006, 'Speed, I am speed'),
        (2, 2014, 'Talented young drummer begins to pursue perfection at any cost, even his humanity.'),
        (3, 1995, 'Assassin goes through obstacles as he attempts to escape his violent lifestyle despite the opposition of his partner, who is secretly attracted to him.')
    ]

    con = sqlite3.connect('movies_python.db')
    logging.debug("DB Connected".format())

    # get a cursor for the connection
    cur = con.cursor()

    # inserting info_1 data into movies_info_1 database
    cur.execute("DROP TABLE IF EXISTS movies_info_1")
    cur.execute("CREATE TABLE movies_info_1 (show_id, genre, title, director)")
    cur.executemany("INSERT INTO movies_info_1 VALUES(?, ?, ?, ?)", info_1)
    con.commit()

    # inserting info_2 data into movies_info_2 database
    cur.execute("DROP TABLE IF EXISTS movies_info_2")
    cur.execute("CREATE TABLE movies_info_2 (show_id, release_year, description)")
    cur.executemany("INSERT INTO movies_info_2 VALUES(?, ?, ?)", info_2)
    con.commit()

    print("My Movie Database\n")

    # join statement
    join_query = cur.execute("""
        SELECT m1.genre, m1.title, m1.director, m2.release_year, m2.description 
        FROM movies_info_1 m1
        JOIN movies_info_2 m2
        ON m1.show_id = m2.show_id
        """)

    # headers
    headers = ['Genre', 'Title', 'Director', 'Year', 'Description']
    print(f"{headers[0]:<15}{headers[1]:<15}{headers[2]:<20}{headers[3]:<8}{headers[4]:<30}")

    rows = join_query.fetchall()
    for genre, title, director, release_year, description in rows:
        print("{:<15}{:<15}{:<20}{:<8}{:<30}".format(
            genre, title, director, release_year, description
        ))

    logging.debug("DB Closed")

    # if connection is open (not False), then close it
    if con:
        con.close()

if __name__ == "__main__":
    main()

# try:
    # run the query
#    cur.execute(query1)
#    cur.execute(query2)
#    con.commit()
# except sqlite3.OperationalError as e:
#    print("An error occurred:", e)

# save the results in artists
# artists = cur.fetchall()

# loop through and print all the artists
# for artist in artists:
#    print(artist[1])  # [1] give us the second column in the table

# if connection is open (not False), then close it
# if con:
#     con.close()

# print("Table has been created")