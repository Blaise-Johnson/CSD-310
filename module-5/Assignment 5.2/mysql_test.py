""" import statements """
import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values


# using our .env file
secrets = dotenv_values("dotenv_values.env")

""" database config object """
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "port" : 3304,
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

""" MySQL: mysql_test.py Connection test code """
""" try/catch block for handling potential MySQL database errors """

try:

    # connect to the movies database
    db = mysql.connector.connect(**config)

    # output the connection status
    print("\nDatabase user {} connected to MySQL on host {} with database {}"
          .format(config["user"], config["host"], config["database"]))

    input("\n\nPress any key to continue...")

except mysql.connector.Error as err:

    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    pass
    """ close the connection to MySQL """

    #db.close()

