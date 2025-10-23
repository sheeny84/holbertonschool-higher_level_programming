#!/usr/bin/python3
'''This is the Filter States Module'''
import MySQLdb
import sys


def list_all_states(username, password, name, state_name_searched):
    ''' This function lists all the states in the database '''
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=name)
    cur = db.cursor()
    sql_str = "SELECT * FROM states WHERE name LIKE BINARY '" \
        + state_name_searched + "'"
    cur.execute(sql_str)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_all_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
