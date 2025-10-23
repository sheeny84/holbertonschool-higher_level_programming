#!/usr/bin/python3
'''This is the Filter States Module'''
import MySQLdb
import sys


def filter_states(username, password, name):
    ''' This function lists all the states in the database '''
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
