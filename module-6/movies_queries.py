#Blaise A. Johnson
#Assignment 6.2
#July 5, 2026

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
    
    #FIRST QUERY
    cursor = db.cursor()
    #Description
    print(f"--STUDIO TABLE--")

    #Selects everything from studio table 
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()

    #iterates through all rows in studio
    for studio in studios:
        print (f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}")
        print()

    print()
    #SECOND QUERY
    cursor = db.cursor()
    #Decription
    print(f"--GENRE TABLE--")

    #Selects everything from genre table 
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()    

    #itersates through genre table
    for genre in genres:
        print (f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}")
        print()       

    print()
    #THIRD QUERY
    cursor = db.cursor()
    # Description
    print(f"--RUNTIME--")

    # 2 hours is 120 minutes so 
    cursor.execute("SELECT * FROM film WHERE film_runtime < 120")
    films = cursor.fetchall()

    for film in films:
        print(f"Film Name: {film[1]}")
        print(f"Runtime: {film[3]}")
        print()

    print()
    #Fourth query
    cursor = db.cursor()
    print(f"--Directors--")

    #orders results by director
    cursor.execute ("SELECT * FROM film ORDER BY film_director")
    films = cursor.fetchall()

    for film in films:
        print(f"Film Name: {film[1]}")
        print(f"Director: {film[4]}")
        print()

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

    db.close()

