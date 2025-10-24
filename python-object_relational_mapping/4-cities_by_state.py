#!/usr/bin/python3
'''This is the Cities By State Module'''
import MySQLdb
import sys


def cities_by_state(username, password, name):
    ''' This function lists all the cities and their state '''
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=name)
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name " \
            "FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            "ORDER BY cities.id"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])
