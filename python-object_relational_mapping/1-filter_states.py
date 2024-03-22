#!/usr/bin/python3
"""
This module lists states from the database hbtn_0e_0_usa where the name starts
with 'N', using MySQLdb.
"""

import MySQLdb
import sys


def list_states():
    """
    Connects to the MySQL database, queries for states starting with 'N',
    and prints them. Requires MySQL username, password, and database name.
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states()
