#Blaise A. Johnson
#Assignment 7.2
#July 12, 2026




    

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


        
    cursor = db.cursor()

    #function to join tables
    def show_films(cursor, title):
        cursor.execute(
        "SELECT film_name AS Name, film_director AS Director, "
        "genre_name AS Genre, studio_name AS Studio "
        "FROM film INNER JOIN genre ON film.genre_id = genre.genre_id "
        "INNER JOIN studio ON film.studio_id = studio.studio_id"
        )

        films = cursor.fetchall()

        #prints title argument
        print(f"--{title}--")

        #iterates through film table
        for film in films:
            print(
            "Name: {}\n"
            
            "Director: {}\n"
            
            "Genre: {}\n"
            
            "Studio: {}\n".format(
                film[0],
                film[1],
                film[2],
                film[3]
            )
        )       
        #Calls function and displays title
    show_films(cursor, "INITAL FILMS")

       
    # Updates Gladiator to a horror film
    cursor.execute(
    "UPDATE film "
    "SET genre_id = 1 "
    "WHERE film_id = 1"
)
    show_films(cursor, "UPDATED FILM")

    #DELETE gladiator
    cursor.execute (
    "DELETE FROM film " \
    "WHERE film_id = 1"
)
    show_films(cursor,"DELETED FILM")

    #INSERTED film 
    cursor.execute(
    "INSERT INTO film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) "
    "VALUES (4, 'MA', 2019, 100, 'Tate Taylor', 2, 1)"
)
        #calls new function and inserts film 
    show_films(cursor, "INSERTED FILM")


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

