#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Requires 4 command-line arguments: mysql username, mysql password,
database name, and the state name to search for.
"""

import MySQLdb
import sys


def main():
    """
    Fetches and prints states matching the provided name, sorted by states.id.
    """
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    query = ("SELECT * FROM states WHERE name = '{}'"
             " ORDER BY id ASC").format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        main()
