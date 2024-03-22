#!/usr/bin/python3
"""
This module provides functionality to list states from\
    the database hbtn_0e_0_usa
where the name starts with 'N'. It demonstrates database\
    connection and querying
using MySQLdb.
"""

import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database, queries for states starting with 'N',
    and prints them. Requires command-line arguments for MySQL username,
    password, and database name.
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        main()
