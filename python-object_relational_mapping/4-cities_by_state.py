#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa along with their
state names, sorted in ascending order by cities.id.
"""

import MySQLdb
import sys


def main():
    """
    Fetches and prints all cities along with their\
        state names, sorted by cities.id.
    """
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        main()
