#!/usr/bin/python3
'''This is the Cities By State Module'''
import MySQLdb
import sys


def list_all_cities(username, password, name):
    ''' This function lists all the cities in the database '''
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=name)
    cur = db.cursor()
    query = "SELECT * FROM cities ORDER BY cities.id"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_all_cities(sys.argv[1], sys.argv[2], sys.argv[3])
