#!/usr/bin/python3
'''This is the Filter Cities Module'''
import MySQLdb
import sys


def filter_cities(username, password, name, state_name):
    ''' This function lists all the cities for a given state name'''
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=name)
    cur = db.cursor()
    query = "SELECT cities.name " \
            "FROM cities " \
            "INNER JOIN states ON cities.state_id=states.id " \
            "WHERE states.name=%s"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
