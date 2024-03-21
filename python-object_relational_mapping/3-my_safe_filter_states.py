#!/usr/bin/python3
"""
This script is safe from SQL injections. It takes an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


def main():
    """
    Fetches and prints states matching the provided name, sorted by states.id,
    while being safe from SQL injections.
    """
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        main()
