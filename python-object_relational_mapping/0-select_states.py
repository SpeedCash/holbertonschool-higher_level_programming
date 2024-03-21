#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It requires 3 command-line arguments: mysql username, mysql password, and database name.
"""

import MySQLdb
import sys

def main():
    """
    Main function that fetches and prints all states from the database, sorted by states.id.
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        main()
