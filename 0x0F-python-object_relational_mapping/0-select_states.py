#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <host> <user> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
        
    host = sys.argv[1]
    user = sys.argv[2]
    password = sys.argv[3]
    database = sys.argv[4]
    
    try:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                    passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()
        cur.execute("SELECT * FROM states")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
