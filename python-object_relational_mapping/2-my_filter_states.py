#!/usr/bin/python3
'''This is the Filter States Module'''
import MySQLdb
import sys


def my_filter_states(username, password, name, state_name_searched):
    ''' This function lists all the states in the database '''
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY"
                " '{}'".format(state_name_searched))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    my_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
