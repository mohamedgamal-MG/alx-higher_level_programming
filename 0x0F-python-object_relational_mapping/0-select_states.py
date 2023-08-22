#!/usr/bin/python3
import MySQLdb
import sys

def get_states(username, password, database):
    try:
        # Establishing a connection to the MySQL server
        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        
        # Creating a cursor object to execute queries
        cur = conn.cursor()
        
        # Executing the SELECT query to retrieve states
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        
        # Fetching all rows from the query result
        query_rows = cur.fetchall()
        
        # Displaying the results
        for row in query_rows:
            print(row)
        
        # Closing the cursor and the connection
        cur.close()
        conn.close()
    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    get_states(username, password, database)

