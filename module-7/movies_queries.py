# Lea Trueworthy
# November 25, 2024
# CSD 310 - Module 7.2 Assignment: Movies Table Queries
# Description: Write the code to connect to your MySQL movies database.
# Write four queries, in one Python file including descriptions of output and format.
    # The first and second query is to select all the fields for the studio and genre tables.
    # The third query is to select the movie names for those movies that have a run time of less than two hours.
    # The fourth query is to get a list of film names, and directors grouped by director.

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password was invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()